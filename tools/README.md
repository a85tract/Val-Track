# Record tools

These tools turn a comparator's result into an acceptance record that
`schemas/evidence-manifest.v1.json` accepts, check the records filed, and index them.
None of them compares anything: the comparators live where the run and its output format
are understood.

```
recast-cesm  scripts/compare/compare_runpair.py --json  (bitwise, Pipeline 1)  ─┐
recast-cesm  scripts/compare/compare_stats.py --json    (statistical, Pipeline 2) ├─► make_manifest.py ─► <product>/evidence/<version>/
RecastEngine recast run ... --summary                   (unit-differential)    ─┤                       manifest.json, summary.md
backfill_wave24.py (a case kit's verdicts, backfilled)   (output-verdict)       ─┘
                                                                                          │
                                                                                          ├─► verify_evidence.py  (CI)
                                                                                          ├─► index_evidence.py ─► INDEX.md, index.json
                                                                                          └─► check_validation.py render ─► <product>/VALIDATION.md
                                                                                              check_validation.py check   (product CI, via
                                                                                                .github/workflows/validation-callable.yml)
```

The comparators run on HPC where the output lives. `verify_evidence.py` runs in CI, on the
committed manifest, in seconds. Nothing in this directory ever executes a model run or reads
model output — see `../docs/VALIDATION-ARCHITECTURE.md` §4 for why that split exists.

`dataio.py` is the one file here that is not a tool: loading a benchmark, listing candidate
outputs to fingerprint, and `rule_key`, which must match what recast-cesm's
`compare_stats.py` writes.

## Status

| Module | Migration step | State |
|---|---|---|
| `make_manifest.py` | 3 | **implemented** |
| `verify_evidence.py` | 3 | **implemented** — all 11 error invariants and 6 warnings from `../schemas/README.md` |
| `index_evidence.py` | 4 | **implemented** — regenerates `../INDEX.md` and `index.json` from the manifests; `--check` exits 1 if it is stale |
| `backfill_wave24.py` | — | **one-off** — turns the wave24 application validations of RecastEngine-Pro `783ef4b` (the verdict table in a85tract/OOPSLA2027_evidence) into six `<system>-numpy` products' output-verdict benchmarks (`benchmarks`) and `reconstructed` records (`records`), in two commits so the records name the commit holding their criteria. It filed fifteen at `5351531`; nine were since replaced by `complete` bitwise records |
| `check_validation.py` | 8 | **implemented** — `render` prints a product's `VALIDATION.md` from a record; `check` (run in the product repository, by `../.github/workflows/validation-callable.yml`) verifies the file names a record that exists and says the same, and reports how far HEAD has moved on; `--strict` makes a stale drift line a finding, `--refresh` rewrites it |

The comparators (`compare_runpair.py`, `compare_stats.py`, and the CAM readers in their
`dataio.py`) moved to recast-cesm's `scripts/compare/` with their tests (step 5 of
`../docs/CORRECTNESS-ORGANIZATION.md`).

Benchmarks exist under `../clubb-jax/benchmarks/` (15, all evaluating PASS) and
`../clm-ml-jax/benchmarks/` (2, not evaluable until the case commits the engine's schema-1
summary). The first acceptance record, step 4 of `../docs/CORRECTNESS-ORGANIZATION.md`, is
filed as `../clubb-jax/evidence/unreleased-99c8b22f/` (15 cases, PASS, security `NOT_RUN`;
`verify_evidence.py` reports 0 errors and 1 warning). Its `cc_test.commit` (`86a46e8c`) is the
commit that holds the tooling and benchmarks that produced it; see `../README.md`.
`.github/workflows/verify-evidence.yml` checks it: on every pull request and push to `main` it runs
`../schemas/test_schemas.py`, `pytest tools/test_tools.py`, `verify_evidence.py` (with
`--base-ref origin/<base>` on a pull request, so the append-only check runs) and
`index_evidence.py --check`.
The format examples under `schemas/examples/` name
benchmarks that do not exist, on purpose, which is why the verifier reports
`example-bitwise.manifest.json` as naming a missing benchmark.

## Running them

```bash
# Layer 1, on HPC, from a recast-cesm checkout. Text report to stderr, JSON to a file.
scripts/compare/compare_runpair.py \
    --reference-run-dir /glade/derecho/scratch/$USER/pi-native/run \
    --candidate-run-dir /glade/derecho/scratch/$USER/pi-codon/run \
    --timer physpkg_st1 --timer bc_physics --timer CPL:RUN_LOOP \
    --json pi.json 2> report.txt

# Then, from this checkout:
tools/make_manifest.py \
    --case pi-6month-allcodon=pi.json \
    --benchmark-dir pycam5/benchmarks \
    --artifact-repo ~/PyCAM5 \
    --reference-commit <baseline-sha> \
    --outputs-location /glade/derecho/scratch/$USER/pi-codon/run \
    --outputs-retention "scratch, purged ~2026-12-01" \
    --case-outputs pi-6month-allcodon=/glade/derecho/scratch/$USER/pi-codon/run \
    --security-summary ~/audits/recast/PyCAM5/<ts>/summary.json \
    --summary  pycam5/evidence/unreleased-e8d68996/summary.md \
    --out      pycam5/evidence/unreleased-e8d68996/manifest.json

# Layer 2, in CI or before opening the pull request.
tools/verify_evidence.py                       # every manifest under <product>/evidence/
tools/verify_evidence.py --base-ref origin/main --strict

# The product's VALIDATION.md: render it here after filing a record, check it over there.
tools/check_validation.py render --manifest clubb-jax/evidence/unreleased-99c8b22f/manifest.json > <clubb-jax>/VALIDATION.md
tools/check_validation.py check --validation VALIDATION.md --product-repo . \
    --val-track <val-track> [--strict] [--refresh]     # from the product checkout
```

`--security-summary` takes the Cyber gate's summary, written by `recast run audit <root>
--gate-summary PATH` (or `audit-cesm` for the LLM audit plane); a file without `"schema": 1`
is refused. The gate says `PASS` when nothing blocking was found among the planes that ran; the schema's `PASS` means every plane ran, so a `PASS` with a plane in
`not_configured`, `skipped` or `unavailable` is recorded as `INCOMPLETE` and a warning says so.

For a `unit-differential` case the comparator is RecastEngine, and the "comparator JSON" is the
summary the case repository commits. `make_manifest.py` reads its verdicts, decides which gate
by the benchmark, and fingerprints the summary file into `outputs.files`:

```bash
tools/make_manifest.py \
    --case tier0-translate=~/agent/cesm/clubb-jax/summaries/tier0.json \
    --benchmark-dir clubb-jax/benchmarks \
    --artifact-repo ~/agent/cesm/clubb-jax \
    --outputs-location https://github.com/a85tract/clubb-jax/tree/main/summaries \
    --outputs-retention "committed; kept" \
    --machine laptop --env compiler="gfortran 16.1.0 (Homebrew)" \
    --out clubb-jax/evidence/unreleased-<commit>/manifest.json
```

recast-cesm's `compare_stats.py` additionally needs the criteria, because a statistical
comparison has no criterion of its own; pass it the benchmark file from here. No statistical
benchmark has been written yet; that family of the acceptance schema is still `provisional`
(decision D4).

## Dependencies

Standard library, plus:

| Need | Used by | Absent means |
|---|---|---|
| `jsonschema` + `referencing` | `verify_evidence.py`, and `make_manifest.py` for its pre-write check | the verifier exits **2** and says so; `make_manifest.py` warns that it wrote unvalidated |
| `PyYAML` | reading `<product>/benchmarks/*.yaml` | a clear error naming the alternative (`.json`), never a guessed criterion |

```bash
python3 -m venv .venv && .venv/bin/pip install jsonschema pyyaml pytest
.venv/bin/python -m pytest tools/test_tools.py
.venv/bin/python schemas/test_schemas.py
```

`test_tools.py` reads committed comparator results under
`fixtures/comparator/` and never touches model output, so the suite runs in a bare
checkout.

## Conventions these tools share

- **Human-readable text goes to stderr**, so a caller never parses prose.
- **The comparator JSON matches the schema's shape directly.** `compare_runpair.py --json`
  emits `files[]` and `timing` that drop into `cases[].result` with no transformation, so
  `make_manifest.py` never has to reshape anything. That shape is the contract between
  recast-cesm and this repository; the fixtures under `fixtures/comparator/` pin it.
- **Exit codes are three-valued, matching the schema's `status`:** `0` PASS, `1` FAIL,
  `2` ERROR (the comparison could not be carried out — a missing file, a mismatched file
  set, an unreadable format, no overlapping variables). A failed comparison and an absent
  comparison are not the same result. `verify_evidence.py` reads the same way: `0` clean,
  `1` findings, `2` nothing could be verified.
- **Silence is not an available answer.** A rule with no measurement behind it is never a
  pass. If it gates, the case is ERROR and the check is written `passed: false` with the
  reason in `detail` — the schema forbids `null` on a gating check, and the ERROR status is
  what distinguishes this from a comparison that ran and failed. If it does not gate, the
  check is `passed: null` with the reason, which is what null is for.
- **The benchmark owns the criteria.** A comparator reports what it measured;
  `<product>/benchmarks/<case>.yaml` decides which of those measurements gate, and
  `make_manifest.py` copies that block into the manifest verbatim. Changing a criterion
  means editing a benchmark, never editing an acceptance record.
