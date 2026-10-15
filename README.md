# Val-Track — Validation Track

Acceptance records for modernized scientific code. When a component is ported to a
new language or framework — a CAM physics package to Python, a CLUBB or CLM kernel to
JAX — this repository records what one version was checked against and what the check
found, so anyone can verify the claim instead of taking it on trust. Each record
answers two questions about the same commit:

- **Correctness** — does the port compute the same answer as the code it replaces?
- **Cyber** — was that commit scanned for secrets, known vulnerabilities, and defects?

Val-Track is a results repository. It runs no comparison and no scanner: comparisons
run in RecastEngine and recast-cesm, scans in the engine's Cyber gate. What lands here
is the verdict, the criteria it was judged by, and the tools that assemble, verify and
index records. `evidence/index.json` lists every record for the SciRecast site.

## What is here

```
benchmarks/<product>/<case>.yaml        acceptance criteria, one file per case; edited as criteria change
evidence/<product>/<version>/           acceptance records, one per validated version; append-only
  manifest.json                           the record, validated by schemas/evidence-manifest.v1.json
  summary.md, report.txt                  one-page summary, comparator text output
evidence/INDEX.md, index.json           generated from the records by correctness/index_evidence.py
schemas/                                record and criteria schemas, with a self-test
correctness/                            make_manifest, verify_evidence, index_evidence, check_validation
docs/                                   architecture, ownership, migration history, decisions
```

| Product | Benchmarks | Records |
|---|---|---|
| clubb-jax | 15 | `unreleased-99c8b22f`: 15 cases, PASS, security `NOT_RUN` |
| clm-ml-jax | 2 | none yet: the case does not commit the engine's schema-1 summary (`benchmarks/clm-ml-jax/README.md`) |
| pycam5, freecam | 0 | none yet |

## How a record is made and checked

A real validation run needs the machine the model lives on — for CESM, a build and a
long integration on Derecho, which no GitHub runner can do. So the work splits in two:

```
Layer 1 — produce (HPC or the case repository)
  run reference + candidate
    → a comparator: recast-cesm scripts/compare/compare_runpair.py --json (whole model),
      or the summary a RecastEngine case commits (unit-differential)
    → recast run audit <product> --gate-summary summary.json      (the Cyber verdict)
    → correctness/make_manifest.py --case ID=RESULT ... --security-summary summary.json
    → evidence/<product>/<version>/ + index_evidence.py, in a pull request here

Layer 2 — verify (GitHub Actions, every pull request, seconds)
  verify_evidence.py  schema, the commits it names, results that follow from the
                      criteria, and no existing record altered
  index_evidence.py --check
```

A product carries a `VALIDATION.md` rendered from its record
(`check_validation.py render`) and calls `.github/workflows/validation-callable.yml`,
which fails when the file no longer agrees with the record and reports how far HEAD
has moved past the validated commit. `correctness/README.md` has every tool's flags.

To run the checks locally (no model output needed):

```bash
python3 -m venv .venv && .venv/bin/pip install jsonschema pyyaml pytest
.venv/bin/python schemas/test_schemas.py
.venv/bin/python -m pytest tests/test_correctness.py
.venv/bin/python correctness/verify_evidence.py
```

## What a record guarantees

- **Every rule says whether it gates.** A criteria block in which nothing gates is
  rejected, so a reader can tell exactly what a PASS covered.
- **`ERROR` is not `FAIL`.** A comparison that could not be carried out — mismatched
  file sets, an unreadable file, a gating rule with no measurement — is `ERROR` and
  exit 2, never a pass. Every tool exits `0` PASS, `1` FAIL, `2` ERROR.
- **A digest records how it was taken** (`dump_format`, `dump_tool`), because it is only
  comparable with one taken the same way.
- **Provenance is not invented.** A record missing any provenance field is
  `reconstructed`, not `complete`.
- **The Cyber verdict is always stated.** With no gate summary the record says
  `NOT_RUN`; a gate `PASS` with a plane that did not run is recorded as `INCOMPLETE`.
  Findings never enter this repository (`SECURITY.md`).
- **Records are immutable.** A re-run files a new version; CI rejects a pull request
  that edits or deletes an existing record.

## Ownership and open decisions

| Area | Owner |
|---|---|
| Schemas, structure, contracts | lewisychen |
| Manifest builder, verifier, benchmarks; the comparators in recast-cesm | Qinrun |
| Cyber gate — RecastEngine `audit`, recast-cesm `audit-cesm`, product-repo config | Chien-Wei |

One decision is open: **D4**, the statistical (ensemble-spread) criteria for Pipeline 2.
Until it is settled the schema marks that family `provisional` and the verifier rejects
evidence filed against it; bitwise and unit-differential records are unaffected. The
decisions, the migration that made Val-Track results-only, and what moved where are in
`docs/VALIDATION-ARCHITECTURE.md` and `docs/CORRECTNESS-ORGANIZATION.md`. Former
`hpc-devsecops` users: the engine's `docs/cyber-gate.md` maps every old command to its
replacement.
