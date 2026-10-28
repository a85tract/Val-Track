#!/usr/bin/env python3
"""Backfill the wave24 application validations as output-verdict acceptance records.

RecastEngine-Pro `783ef4b` (tag wave24-accepted) translated fifteen Fortran
systems to NumPy and each was checked in situ: the case kit ran the native
program and the same driver with the translated procedures delegated to the
generated NumPy, and its verifier compared the outputs. Those runs are gone;
what survives is the verdict table in a85tract/OOPSLA2027_evidence
(`auditing/paper_evidence/bitexact_scale/rule_run_detail.tsv`) plus CLUBB's
replay and feedback aggregates. This turns that into one product per system,
`<system>-numpy`, with output-verdict benchmarks and `reconstructed` records.

Two steps, so that the records name the commit that holds their criteria
(docs/PRODUCTS.md, "file a record the way clubb-jax's was"):

    backfill_wave24.py benchmarks --evidence ~/agent/OOPSLA2027_evidence
    git add ... && git commit                       # criteria and this tool
    backfill_wave24.py records --evidence ~/agent/OOPSLA2027_evidence
    python tools/index_evidence.py && git commit     # the records

Nothing is rerun and nothing is inferred beyond the table: a verdict string is
mapped to identical/different and kept verbatim beside the mapping, and a value
the table does not hold is left out.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional

import yaml

import make_manifest

REPO_ROOT = Path(__file__).resolve().parent.parent

ENGINE_REPO = "https://github.com/a85tract/RecastEngine-Pro"
ENGINE_COMMIT = "783ef4bbb334d8fa39572a13a6f04a9042ab43d2"
VERSION = "unreleased-%s" % ENGINE_COMMIT[:8]

RUN_TABLE = "auditing/paper_evidence/bitexact_scale/rule_run_detail.tsv"
REVISIONS = "wave24/scope/source_revisions.json"
CLUBB_AGGREGATE = "wave24/scope/clubb_wave24/aggregate.json"
CLUBB_REPLAY = "wave24/scope/clubb_wave24_replay150_stdout.txt"

INSITU = "candidates in-situ verifier (alpine/verify_insitu.sh)"
CPRNC = "candidates in-situ verifier with cprnc (Derecho)"
CLUBB_HARNESS = ("clubb boundary harness, sha256 "
                 "edeb666b4e8cc5004b3b1c95a59dcbfa08e6e3bd7cdd8ac5179c4baed152fc41")

KIT_NORMALIZATION = ("output files compared after the time fields and undefined padding "
                     "each kit records are normalized; not a claim that the raw files are "
                     "byte-identical")

ALPINE = {"machine": "Alpine (CU Boulder Research Computing), Linux el8_10 x86_64",
          "python": "CPython 3.12.14", "numpy": "2.5.3"}
GFORTRAN = "gfortran 14.2.0 (/curc/sw/install/gcc/14.2.0)"

# Verifier campaigns: when each finished (workers.tsv of the wave24 cost
# accounting) or, for the guard, when its prep finished (job 33422506's header
# in source_revisions.json). CLUBB's replay left no time; the bound is when the
# bitexact_scale inventory read its aggregate.
CAMPAIGNS = {
    "guard": ("2026-10-05T05:01:39Z", "the guard_o5f run on Alpine; the time is when its "
              "prep (job 33422506) finished, as the job header records"),
    "alpine-a": ("2026-10-05T05:25:48Z", "verifier job cand-o5w/o5w-alpine-a; the time is "
                 "when the job finished"),
    "alpine-b": ("2026-10-05T06:26:32Z", "verifier job cand-o5w/o5w-alpine-b; the time is "
                 "when the job finished"),
    "derecho": ("2026-10-05T05:05:05Z", "verifier job cand-o5w/o5w-derecho; the time is "
                "when the job finished"),
    "cism": ("2026-10-05T05:50:48Z", "verifier job cand-o5v-cism-783ef4bb; the time is "
             "when the job finished"),
    "clubb": ("2026-10-07T23:55:48Z", "no run time was recorded; the time is when the "
              "bitexact_scale inventory read the aggregate, so the runs are no later"),
}

# One entry per benchmark: target in the run table, product, case id, the
# systems' upstream component(s), the campaign, and how the case is described.
CASES = [
    # target, product, case, model, components, campaign, verifier, compiler, description
    ("qe", "qe-numpy", "qe", "Quantum ESPRESSO (XClib, dft-d3)", ["main"], "guard",
     INSITU, GFORTRAN, "XClib all_terms and derivative drivers, dft-d3 graphite"),
    ("mfc", "mfc-numpy", "mfc", "MFC", ["main"], "guard", INSITU, GFORTRAN,
     "nine MFC regression tests"),
    ("njoy", "njoy-numpy", "njoy", "NJOY2016", ["main"], "guard", INSITU, GFORTRAN,
     "four NJOY2016 tests and their additional tapes"),
    ("ramses", "ramses-numpy", "ramses", "RAMSES", ["main"], "guard", INSITU, GFORTRAN,
     "three RAMSES test problems"),
    ("duo", "duo-numpy", "duo", "Duo", ["main"], "guard", INSITU, GFORTRAN,
     "two Duo inputs"),
    ("cvmix", "cvmix-numpy", "cvmix", "CVMix", ["main"], "alpine-a", INSITU, GFORTRAN,
     "four CVMix drivers, outermost plan"),
    ("marbl", "marbl-numpy", "marbl", "MARBL", ["main"], "alpine-a", INSITU, None,
     "two MARBL drivers, outermost plan"),
    ("rrtmg", "rrtmg-numpy", "rrtmg", "RRTMG (LW, SW)", ["LW", "SW"], "alpine-a", INSITU,
     None, "the RRTMG LW and SW benchmark configurations, outermost plan"),
    ("cosp2", "cosp2-numpy", "cosp2", "COSP2", ["main"], "alpine-a", INSITU, None,
     "the COSP2 UKMO driver, outermost plan"),
    ("carma", "carma-numpy", "carma", "CARMA", ["wrapper", "base"], "alpine-b", INSITU, None,
     "the CARMA test programs"),
    ("fates", "fates-numpy", "fates", "FATES", ["main"], "alpine-b", INSITU, None,
     "the FATES leaf-biophysics smoke test"),
    ("ww3", "ww3-numpy", "ww3", "WAVEWATCH III", ["main"], "alpine-b", INSITU, None,
     "two WW3 test cases and the tp1.1 postprocessing"),
    ("cism", "cism-numpy", "cism", "CISM", ["main"], "cism", INSITU, None,
     "halfar-HO t5 with the merged plan, its restart, and the t0/t1 short runs"),
    ("cam_kessler", "camsima-numpy", "kessler", "CAM-SIMA (Kessler)",
     ["CAM-SIMA", "atmospheric_physics", "ccpp-framework"], "derecho", CPRNC, None,
     "CAM-SIMA with Kessler physics, outfrq test"),
    ("cam_held_suarez", "camsima-numpy", "held-suarez", "CAM-SIMA (Held-Suarez)",
     ["CAM-SIMA", "atmospheric_physics", "ccpp-framework"], "derecho", CPRNC, None,
     "CAM-SIMA with Held-Suarez forcing, outfrq test"),
    ("cam_tj2016", "camsima-numpy", "tj2016", "CAM-SIMA (TJ2016)",
     ["CAM-SIMA", "atmospheric_physics", "ccpp-framework"], "derecho", CPRNC, None,
     "CAM-SIMA with TJ2016 physics, before and after the coupler"),
    ("clubb:replay", "clubb-numpy", "replay", "CLUBB_core, larson-group/clubb_release",
     ["fortran"], "clubb", CLUBB_HARNESS, None,
     "independent replay of 150 recorded calls over eight trajectories"),
    ("clubb:feedback", "clubb-numpy", "feedback", "CLUBB_core, larson-group/clubb_release",
     ["fortran"], "clubb", CLUBB_HARNESS, None,
     "recorded-driver-input state feedback over seven configurations, 8,730 steps"),
]

# Roles that gate: the benchmark's tests, and outputs of those same runs the
# verifier reported separately. Diagnostic roles are control runs beside them.
GATING_ROLES = ("primary", "tape_outputs", "restart_output", "postprocess")

RRTMG_NOTE = (
    "LW MLS-cld5-imca0-icld2 differs by one value (max abs 1.0e-07) under the default "
    "allocator: the native program reads undefined heap storage. Under zero-filled malloc "
    "all 14 LW configurations are byte-identical (the zero_heap_diagnostic runs; "
    "OOPSLA2027_evidence wave24/rrtmg_initialization). The run stays gated: ungating it is "
    "a maintainer's decision, not something a backfill does.")

CARMA_NOTE = (
    "For GROWCLRTEST, GROWINTEST, GROWSUBTEST, GROWTEST, NUCTEST and PHEATTEST the gated "
    "run is the zero-heap one (malloc zero-filled in both processes), as the table selects "
    "it. The default-allocator runs of those tests are the ordinary_overlap_diagnostic "
    "rows, and GROWTEST and PHEATTEST differ there - the same undefined-storage reading "
    "that keeps RRTMG's MLS-cld5-imca0-icld2 failing, where the table selected the "
    "default-allocator run instead.")

CLUBB_NORMALIZATION = ("none: binary64 bit patterns and exact int32 values of every "
                       "argument at the routine boundary")


def read_table(evidence: Path) -> List[dict]:
    with (evidence / RUN_TABLE).open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def number(text: str) -> Optional[int]:
    text = (text or "").strip().replace(",", "")
    return int(text) if text.isdigit() else None


def verdict_entry(row: dict) -> dict:
    """One run of the table, verdict mapped and kept verbatim."""
    reported = row["verdict"].strip()
    counted = re.match(r"^(IDENTICAL|DIFFERENT) (\d+)/(\d+)$", reported)
    files = number(row["output_files"])
    if counted:
        verdict = counted.group(1).lower()
        compared = int(counted.group(3))
        matched = int(counted.group(2)) if verdict == "identical" else None
    elif reported in ("identical", "True", "normalized/cprnc identical"):
        verdict, compared, matched = "identical", files, files
    elif reported == "False":
        verdict, compared, matched = "different", files, None
    else:
        raise SystemExit("%s %s: verdict %r has no mapping" % (row["target"], row["case"], reported))
    entry = {"run": row["case"], "role": row["role"], "verdict": verdict, "reported": reported,
             "outputs_compared": compared, "outputs_identical": matched}
    for key, column in (("delegated_calls", "delegated_calls"),
                        ("values_compared", "compared_values")):
        if number(row[column]) is not None:
            entry[key] = number(row[column])
    entry["source"] = row["source"]
    entry["note"] = row["notes"]
    return entry


def clubb_runs(evidence: Path, layer: str) -> List[dict]:
    aggregate = json.loads((evidence / CLUBB_AGGREGATE).read_text())
    runs: List[dict] = []
    if layer == "replay":
        final: Dict[str, str] = {}
        for line in (evidence / CLUBB_REPLAY).read_text().splitlines():
            match = re.match(r"^(\S+) (\d+)/(\d+): (\d+)/(\d+) bit-identical", line)
            if match:
                final[match.group(1)] = line.strip()
        for name, line in final.items():
            match = re.match(r"^\S+ (\d+)/(\d+): (\d+)/(\d+)", line)
            calls, total, equal, values = (int(match.group(i)) for i in range(1, 5))
            identical = calls == total and equal == values
            runs.append({"run": name, "role": "primary",
                         "verdict": "identical" if identical else "different",
                         "reported": line, "outputs_compared": None, "outputs_identical": None,
                         "delegated_calls": total, "values_compared": values,
                         "source": CLUBB_REPLAY})
        if not aggregate["independent_replay"]["all_values_bit_identical"]:
            raise SystemExit("CLUBB aggregate says the replay is not bit-identical")
    else:
        for case in aggregate["state_feedback"]["cases"]:
            identical = (case["status"] == "bit_identical"
                         and case["bit_identical_steps"] == case["completed_steps"]
                         == case["expected_steps"])
            runs.append({"run": case["case"], "role": "primary",
                         "verdict": "identical" if identical else "different",
                         "reported": "%s: %d/%d steps bit-identical, %d/%d values" % (
                             case["status"], case["bit_identical_steps"], case["expected_steps"],
                             case["bit_equal_values"], case["compared_values"]),
                         "outputs_compared": None, "outputs_identical": None,
                         "delegated_calls": case["completed_steps"],
                         "values_compared": case["compared_values"],
                         "source": CLUBB_AGGREGATE})
    return runs


def runs_for(evidence: Path, rows: List[dict], target: str) -> List[dict]:
    if target.startswith("clubb:"):
        return clubb_runs(evidence, target.split(":", 1)[1])
    runs = [verdict_entry(r) for r in rows if r["target"] == target]
    # CARMA lists six tests twice, a zero-heap run as the test and the ordinary run
    # as a diagnostic; the diagnostic keeps its role in its name.
    primary = {r["run"] for r in runs if r["role"] == "primary"}
    for run in runs:
        if run["role"] != "primary" and run["run"] in primary:
            run["run"] = "%s [%s]" % (run["run"], run["role"])
    names = [r["run"] for r in runs]
    if not runs or len(set(names)) != len(names):
        raise SystemExit("%s: no runs, or a run name repeats: %s" % (target, names))
    return runs


def revisions(evidence: Path, target: str, components: List[str]) -> List[dict]:
    key = "clubb" if target.startswith("clubb:") else (
        "camsima_t1" if target.startswith("cam_") else target)
    sources = json.loads((evidence / REVISIONS).read_text())["sources"]
    found = [s for s in sources if s["target"] == key and s["component"] in components]
    if len(found) != len(components):
        raise SystemExit("%s: upstream revisions for %s not all found" % (target, components))
    return found


def benchmark_document(evidence: Path, rows: List[dict], spec) -> dict:
    target, product, case_id, model, components, campaign, verifier, _, description = spec
    runs = runs_for(evidence, rows, target)
    sources = revisions(evidence, target, components)
    roles = sorted({r["role"] for r in runs})
    gating = [r for r in roles if r in GATING_ROLES]
    diagnostic = [r for r in roles if r not in GATING_ROLES]
    clubb = target.startswith("clubb:")
    normalization = CLUBB_NORMALIZATION if clubb else (
        "cprnc compares the history files' numeric fields; the atmosphere log is normalized"
        if verifier == CPRNC else KIT_NORMALIZATION)

    rules: List[dict] = [{"check": "run_set_equal", "runs": [r["run"] for r in runs],
                          "gating": True}]
    rule = {"check": "runs_identical", "verifier": verifier, "roles": gating,
            "normalization": normalization, "gating": True}
    if target in ("rrtmg", "carma"):
        rule["note"] = RRTMG_NOTE if target == "rrtmg" else CARMA_NOTE
    rules.append(rule)
    if diagnostic:
        rules.append({"check": "runs_identical", "verifier": verifier, "roles": diagnostic,
                      "normalization": normalization, "gating": False,
                      "note": "control and overlap runs reported beside the tests; "
                              "they do not gate"})

    main = sources[0]
    provenance = (
        "dump-replay recordings of clubb_standalone (clubb-jax bench/out/fortran), built "
        "from %s; the candidate replays them through the generated NumPy" % main["revision"][:7]
        if clubb else
        "the case kit's native build of the same staged source tree; the candidate is that "
        "driver with the translated procedures delegated to the generated NumPy")
    if len(sources) > 1:
        provenance += "; components: " + ", ".join(
            "%s %s" % (s["component"], s["revision"][:12]) for s in sources)
    case: Dict[str, object] = {"engine": ENGINE_COMMIT[:7] + " (wave24-accepted)",
                               "campaign": CAMPAIGNS[campaign][1],
                               "runs": "%d (%s)" % (len(runs), ", ".join(
                                   "%s %d" % (role, sum(r["role"] == role for r in runs))
                                   for role in roles))}
    if clubb:
        case["extension"] = "recast-clubb cbca7b6"
    case["notes"] = "backfilled from a85tract/OOPSLA2027_evidence %s" % (
        CLUBB_AGGREGATE if clubb else RUN_TABLE)
    return {
        "id": case_id,
        "product": product,
        "description": description,
        "case": case,
        "reference": {"model": model, "commit_or_tag": main["revision"],
                      "provenance": provenance},
        "acceptance": {"kind": "output-verdict", "verdict_schema": 1, "rules": rules},
    }


def products() -> Dict[str, List[tuple]]:
    grouped: Dict[str, List[tuple]] = {}
    for spec in CASES:
        grouped.setdefault(spec[1], []).append(spec)
    return grouped


def write_benchmarks(evidence: Path) -> None:
    rows = read_table(evidence)
    for product, specs in products().items():
        directory = REPO_ROOT / product / "benchmarks"
        directory.mkdir(parents=True, exist_ok=True)
        lines = ["# %s — %d output-verdict benchmark%s" % (
                     product, len(specs), "" if len(specs) == 1 else "s"), "",
                 "Backfilled from the wave24 application validation of RecastEngine-Pro "
                 "`%s` (`tools/backfill_wave24.py`). The case kit compared the native "
                 "program with the same driver running the translated NumPy, in situ; only "
                 "its verifier's per-run verdicts survive, so every record here is "
                 "`reconstructed`." % ENGINE_COMMIT[:7], "",
                 "| id | what it covers | runs | reference |", "|---|---|---|---|"]
        for spec in specs:
            document = benchmark_document(evidence, rows, spec)
            header = ("# %s: %s.\n# Criterion for the verdict table backfilled from "
                      "OOPSLA2027_evidence; written by tools/backfill_wave24.py.\n\n"
                      % (document["id"], document["description"]))
            (directory / (document["id"] + ".yaml")).write_text(
                header + yaml.safe_dump(document, sort_keys=False, allow_unicode=True,
                                        width=100))
            lines.append("| `%s` | %s | %s | %s `%s` |" % (
                document["id"], document["description"], document["case"]["runs"],
                document["reference"]["model"], document["reference"]["commit_or_tag"][:7]))
            if spec[0] == "rrtmg":
                lines += ["", "**One gated run differs.** " + RRTMG_NOTE]
            if spec[0] == "carma":
                lines += ["", "**Which run gates.** " + CARMA_NOTE]
        (REPO_ROOT / product / "README.md").write_text("\n".join(lines) + "\n")
        print("wrote %s/benchmarks (%d)" % (product, len(specs)))


def write_records(evidence: Path) -> int:
    rows = read_table(evidence)
    evidence_commit = subprocess.check_output(
        ["git", "-C", str(evidence), "rev-parse", "HEAD"], text=True).strip()
    worst = 0
    for product, specs in products().items():
        record = REPO_ROOT / product / "evidence" / VERSION
        record.mkdir(parents=True, exist_ok=True)
        argv: List[str] = []
        report: List[str] = []
        for spec in specs:
            target, _, case_id = spec[0], spec[1], spec[2]
            runs = runs_for(evidence, rows, target)
            table = record / ("%s.verdicts.json" % case_id)
            table.write_text(json.dumps({"schema": 1, "verifier": spec[6], "runs": runs},
                                        indent=2, ensure_ascii=False) + "\n")
            argv += ["--case", "%s=%s" % (case_id, table)]
            if target.startswith("clubb:"):
                report += [line for line in (evidence / (
                    CLUBB_REPLAY if target == "clubb:replay" else CLUBB_AGGREGATE)
                ).read_text().splitlines()]
            else:
                with (evidence / RUN_TABLE).open() as handle:
                    head, *body = handle.read().splitlines()
                report += [head] if not report else []
                report += [line for line in body if line.split("\t")[0] == target]
        (record / "report.txt").write_text("\n".join(report) + "\n")

        campaign = specs[0][5]
        timestamp, how = CAMPAIGNS[campaign]
        environment = dict(ALPINE) if campaign in ("guard", "alpine-a", "alpine-b", "cism") else {
            "machine": "Derecho (NCAR)" if campaign == "derecho"
            else "Linux workstation (host not recorded)"}
        argv += ["--benchmark-dir", str(REPO_ROOT / product / "benchmarks"),
                 "--artifact-name", product, "--artifact-repo-url", ENGINE_REPO,
                 "--artifact-commit", ENGINE_COMMIT, "--artifact-version", VERSION,
                 "--machine", environment.pop("machine"), "--no-probe",
                 "--outputs-location", "a85tract/OOPSLA2027_evidence@%s: %s" % (
                     evidence_commit[:9],
                     CLUBB_AGGREGATE if product == "clubb-numpy" else RUN_TABLE),
                 "--outputs-retention", "not retained: the runs' outputs and verifier logs "
                                        "were not archived; the verdict table is what survives",
                 "--evidence-class", "reconstructed", "--timestamp", timestamp,
                 "--notes", "Backfilled by tools/backfill_wave24.py from "
                            "a85tract/OOPSLA2027_evidence@%s. Timestamp: %s. The generated "
                            "NumPy is not committed anywhere; artifact.commit is the engine "
                            "that generated it." % (evidence_commit[:9], how),
                 "--summary", str(record / "summary.md"),
                 "--out", str(record / "manifest.json")]
        for key, value in environment.items():
            argv += ["--env", "%s=%s" % (key, value)]
        compilers = {spec[7] for spec in specs}
        if len(compilers) == 1 and None not in compilers:
            argv += ["--env", "compiler=%s" % compilers.pop()]
        code = make_manifest.main(argv)
        worst = max(worst, code if code != 1 else 0)
    return worst


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("step", choices=("benchmarks", "records"))
    parser.add_argument("--evidence", type=Path, required=True,
                        help="a checkout of a85tract/OOPSLA2027_evidence")
    args = parser.parse_args(argv)
    if args.step == "benchmarks":
        write_benchmarks(args.evidence)
        return 0
    return write_records(args.evidence)


if __name__ == "__main__":
    sys.exit(main())
