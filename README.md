# Val-Track — Validation Track

A ledger of acceptance records for modernized scientific code. When a component
is ported to a new language or framework — a CAM physics package to Python, a
CLUBB or CLM kernel to JAX — this repository holds what it was checked against
and what the check found, so somebody else can verify the claim instead of
taking it on trust. It answers two questions about each version:

- **Correctness** — does the port compute the same answer as the code it replaces?
- **Cyber** — has the code been scanned for secrets, known vulnerabilities, and defects?

Val-Track is a results repository: it holds the records and the criteria they
were judged by, and the small tools that assemble, verify and index them. It runs
no comparison and no scanner. The comparisons run in RecastEngine and recast-cesm,
the scans in the engine's Cyber gate; both verdicts meet in one record, so a
reviewer opens a single acceptance record and sees both for the same commit,
rather than trusting two separate green checkmarks.

Nothing here is tied to one model. A product gets a directory under `benchmarks/`
with its criteria, and its records land under `evidence/<product>/`; today those
are CESM components (PyCAM5, freeCAM, clubb-jax, clm-ml-jax), and the format does
not assume they will stay that way. `evidence/index.json` lists every record in
machine-readable form, for the SciRecast site to read.

| Half | What it does | Status |
|---|---|---|
| [Correctness](#correctness--does-the-port-compute-the-right-answer) | Files a comparator's verdict on a candidate run against a reference as evidence | **Tools in place.** Schema, manifest builder, verifier and index implemented (the comparators moved to recast-cesm, step 5); benchmarks written for clubb-jax (15) and clm-ml-jax (2); first acceptance record filed (clubb-jax, 15 cases, PASS, security NOT_RUN); `verify-evidence.yml` verifies every record and the index on each pull request and push to main |
| [Cyber](#cyber--the-security-block) | Records the Cyber gate's verdict (secret scan, SBOM + CVE + VEX, AI code audit, AddressSanitizer) in each acceptance record | **Recorded here, run elsewhere.** The gate is RecastEngine's `audit` recipe and recast-cesm's `audit-cesm`; Val-Track's own copies were deleted in step 9e (2026-10-15) |

## Repository layout

```
schemas/       what an acceptance record is — JSON Schema + self-test
correctness/   the four tools that assemble, verify, index and render one
benchmarks/    per-product case definitions and acceptance criteria — clubb-jax (15), clm-ml-jax (2)
evidence/      acceptance records, one per validated version, append-only — one so far (clubb-jax)
tests/         test_correctness.py (pytest)
docs/          VALIDATION-ARCHITECTURE.md — the plan, ownership, open decisions
               CORRECTNESS-ORGANIZATION.md — which repository owns which part (D7, D8)
SECURITY.md    what this repository holds of the Cyber half, and its disclosure policy
```

---

# Correctness — does the port compute the right answer?

## The constraint that shapes everything

A real validation run usually needs the machine the model lives on. For a CESM
component it is a CESM build plus a multi-year integration on Derecho: the ifx
toolchain, input data, hours of compute, and `/glade` storage. **A GitHub runner
cannot do any of that.** So the work splits in two, and the split is the
reason the rest of the design looks the way it does:

```
Layer 1 — produce evidence          (HPC, offline, PBS or by hand)
  Derecho: run reference + candidate
        → recast-cesm scripts/compare/compare_runpair.py --json
        → make_manifest.py
        → evidence/<product>/<version>/manifest.json
        → pull request into this repository

Layer 2 — verify evidence           (GitHub Actions, every PR, seconds)
  verify_evidence.py: does the manifest validate? does the commit it names
  exist? do the claimed results follow from the declared criteria? has an
  existing record been altered?
```

Layer 2 is everything CI can honestly check, and it is worth checking: it
catches the case where a `VALIDATION.md` says PASS but points at a commit that
stopped being the current code months ago.

## What the evidence has to say

`schemas/evidence-manifest.v1.json` and `schemas/acceptance.v1.json` define the
record. Three things they make impossible to leave implicit:

**Every acceptance rule states whether it gates.** The existing comparator
measures character-variable differences and GPTL timing, but neither affects its
exit code — the real criterion is numeric bit-for-bit only. That was true and
unwritten, so a reader could not tell what a PASS covered. The schema requires a
`gating` flag on every rule and rejects a criteria block in which nothing gates.

**`ERROR` is not `FAIL`.** When the two run directories hold different file sets,
nothing was compared. That is an absent comparison, not a failed one, and the
comparator already exits `2` for it. The schema keeps them distinct.

**A digest records how it was taken.** The numeric md5 is one digest per output
file, over a fixed-format dump of all numeric variables in it — not one per
variable. It is only comparable against a digest taken with the same format
string, so the rule carries `dump_format` and `dump_tool` rather than assuming
them.

Two more, for the cases that come up in practice: `evidence_class` marks a
record as `complete` or `reconstructed`, so a historical run whose compiler
version can no longer be established is recorded honestly instead of having a
plausible value invented for it; and the statistical criteria for Pipeline 2 are
present but marked `provisional`, and the verifier rejects any evidence filed
against them until the tolerance, norm, variable set, and spread test are agreed
(decision D4).

## Status and where to start

The four tools under `correctness/` are implemented; the comparators that feed them are recast-cesm's `scripts/compare/`. What is still missing is
data, not code: benchmarks exist for clubb-jax (15) and clm-ml-jax (2), and the
first acceptance record is filed as `evidence/clubb-jax/unreleased-99c8b22f/` (15 cases,
all PASS, security `NOT_RUN` because the Cyber gate has not run against that commit).
`.github/workflows/verify-evidence.yml` verifies every record and the index on each pull
request and push to main (migration step 6 of `docs/VALIDATION-ARCHITECTURE.md`, the
`verify-evidence.yml` half). clubb-jax carries the `VALIDATION.md` rendered from that
record and a `validation.yml` that calls `.github/workflows/validation-callable.yml` here
(step 8 of `docs/CORRECTNESS-ORGANIZATION.md`, first product; `correctness/check_validation.py`
renders and checks the file).

| Module | Step | State |
|---|---|---|
| `make_manifest.py` | 3 | done — comparator JSON + benchmark + environment probe + the Cyber gate's `summary.json` → a manifest |
| `verify_evidence.py` | 3 | done — schema plus all 11 error invariants and 6 warnings from `schemas/README.md` |
| `index_evidence.py` | 4 | done — regenerates `evidence/INDEX.md` and `evidence/index.json` from the manifests; `--check` exits 1 if either is stale or missing |
| benchmarks, first acceptance record | 5, 4 | **both done for clubb-jax.** clubb-jax has 15 benchmarks, all PASS in the acceptance record filed 2026-09-24 (`verify_evidence.py`: 0 errors, 1 warning for `NOT_RUN`); clm-ml-jax has 2, blocked until the case commits the engine's schema-1 summary (`benchmarks/clm-ml-jax/README.md`). `verify-evidence.yml` verifies the record on every pull request and push to main (step 6) |

Each tool exits `0` PASS, `1` FAIL, `2` ERROR, and `2` genuinely means *nothing
was compared*: a missing file, a mismatched file set, an unreadable format, an
acceptance rule with no measurement behind it. That distinction is the point —
a stub that returned an empty result, or a tool that reported an absent
comparison as a clean one, would let a caller file a *passing* acceptance record
for a comparison that never ran, which is the failure mode the explicit gating
flags and `ERROR` status exist to prevent.

Read `correctness/README.md` for how the four compose, what they depend on, and
the conventions they share, then `docs/VALIDATION-ARCHITECTURE.md` for the
migration order, the open decisions, and who owns what. Both test suites run
in a bare checkout; neither reads model output:

```bash
python3 -m venv .venv && .venv/bin/pip install jsonschema pyyaml pytest
.venv/bin/python schemas/test_schemas.py          # schema self-test
.venv/bin/python -m pytest tests/test_correctness.py
```

---

# Cyber — the security block

Val-Track runs no scanner. Each acceptance record carries a `security` block: the
Cyber gate's verdict for the same commit the correctness verdict covers, so a
reviewer reads one record and sees both. The gate is
[RecastEngine](https://github.com/a85tract/RecastEngine)'s `audit` recipe (secret
scan, SBOM + CVE + VEX), or recast-cesm's `audit-cesm`, which adds the LLM code audit
and the AddressSanitizer plane. Run it against the validated commit and hand its
summary to `make_manifest.py`:

```bash
recast run audit <product-checkout> --gate-summary summary.json
correctness/make_manifest.py ... --security-summary summary.json
```

`make_manifest.py` reads only that file (`"schema": 1`); with no summary the record says
`NOT_RUN`. The gate calls itself `PASS` when nothing blocking was found among the planes
that ran; the schema's `PASS` means every plane ran, so a gate `PASS` with an unrun plane
is recorded as `INCOMPLETE`, with a warning. Findings never enter Val-Track.

The local pre-push gate, the config templates and the sanitizer job that used to live
here (`tools/`, `hooks/`, `hpc/`, `templates/`, under the name `hpc-devsecops`) were
deleted in step 9e of `docs/CORRECTNESS-ORGANIZATION.md`. The engine's
`docs/cyber-gate.md` maps every old command to its replacement. If you installed the old
pre-push hook, its symlink now points at nothing and Git skips it silently: reinstall
with the engine's `tools/install-hooks.sh <repo>`, and set `RECAST_AUDIT_RECIPE=audit-cesm`
where you want the LLM audit (the old wrapper chose it for repositories carrying
`.github/scripts/ai_audit.py`; the engine's hook defaults to `audit`).

---

# Who owns what

| Area | Owner |
|---|---|
| Correctness framework — schema, structure, contracts | lewisychen |
| Correctness implementation — manifest builder, verifier, benchmarks (the comparators, now in recast-cesm) | Qinrun |
| Cyber gate — RecastEngine's `audit` recipe, recast-cesm's `audit-cesm`, the product-repo config | Chien-Wei |

`docs/VALIDATION-ARCHITECTURE.md` §8 tracks the open decisions. One still needs a
person, not more code:

- **D4** — the Pipeline 2 acceptance vocabulary. The ULP family is settled
  (2026-09-24) as the `unit-differential` kind, read from a RecastEngine
  summary. The ensemble-spread family is not: recast-cesm's `compare_stats.py` is written, but
  it did not settle it: it states the reading it takes for each
  undecided point (`docs/VALIDATION-ARCHITECTURE.md` §8.1) and those readings
  need confirming or overturning by a person. Until then the schema keeps its
  `provisional` marker and no Pipeline 2 evidence is accepted. The bitwise path
  is unaffected.

**D6** — whether an acceptance record also carries the Cyber gate's verdict for the
same commit — is **resolved: yes.** The manifest carries a required `security`
block; when the gate has not run for that commit its `status` is `NOT_RUN`, so a
record is never silently missing the Cyber half rather than honestly marking it
absent. See `docs/VALIDATION-ARCHITECTURE.md` §11.

**D7** and **D8** — where the whole-model comparator lives, and what Val-Track is —
were settled on 2026-09-24: the whole-model comparison is the engine's `fullmodel.bitwise`,
and Val-Track narrows to its acceptance records and the criteria. Both moves are done:
the comparators went to recast-cesm's `scripts/compare/` (step 5, 2026-10-15), the Cyber
tooling to the engine (step 9e).
