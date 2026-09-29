# Correctness Track

Reproducible correctness tracking for the **CESM / CAM modernization effort** —
the port of legacy Fortran components to NumPy, JAX, and Numba through
RecastEngine, and the evidence that each port computes what the Fortran it
replaces computed.

This is the **correctness counterpart of [`CESM-Sec-Track`](https://github.com/a85tract/CESM-Sec-Track)**:
where the security track keeps every finding as a CWE-labelled bug + fix, this
track keeps every accepted version as an **append-only acceptance record** whose
verdict a third party can re-check from the manifest alone. The two tracks meet
in one place — a single acceptance record carries both a correctness and a
`security` verdict for the same commit.

> The Cyber half of CC-Test (secret scan, SBOM→CVE→VEX, AI audit, sanitizer) now
> lives as RecastEngine's `audit` recipe and the domain extension's scanners;
> what remains here is the **correctness** half plus the evidence index.

---

## At a glance (as of 2026-09-29)

| Product | Version | Criterion | Cases | Result | Security | Validated |
|---|---|---|---|---|---|---|
| clubb-jax | `unreleased-99c8b22f` | unit-differential | 15 / 15 | **PASS** | NOT_RUN | 2026-09-21 |
| clm-ml-jax | — | unit-differential | 2 defined | *targeted* | — | — |
| PyCAM5 | — | bitwise | — | *targeted* | — | — |
| freeCAM | — | bitwise | — | *targeted* | — | — |
| jax-kernels | — | statistical\* | — | *targeted* | — | — |
| numba-kernels | — | statistical\* | — | *targeted* | — | — |

\* the `statistical` family is **provisional**: the verifier refuses evidence
filed against it until its vocabulary is finalized (decision D4), so no
statistical record can be filed yet.

**Honest status:** exactly **one** acceptance record is filed today (clubb-jax,
15/15 PASS). Every other row above is a *declared target* — the criterion is
chosen and, for most, reference evidence exists to backfill, but no record has
been verified into `evidence/` yet. This file states that plainly so the track
is never mistaken for more than it is.

---

## Where to start

- [`README.md`](./README.md) — the two halves (Correctness + Cyber) and the repo layout.
- [`docs/VALIDATION-ARCHITECTURE.md`](./docs/VALIDATION-ARCHITECTURE.md) — the two-layer design (produce on HPC, verify in CI), the schema, and the open decisions.
- [`evidence/MASTER-REGISTER.md`](./evidence/MASTER-REGISTER.md) — **every acceptance record, with its full provenance and the meaning of its verdict.**
- [`evidence/INDEX.md`](./evidence/INDEX.md) — the machine-generated one-line-per-record index (`index.json` beside it for machines).
- [`schemas/`](./schemas) — `acceptance.v1.json` (criterion vocabulary) and `evidence-manifest.v1.json` (what a record is).
- [`correctness/verify_evidence.py`](./correctness/verify_evidence.py) — the CI checker; its docstring lists every invariant it enforces.

---

## What makes a record trustworthy

A record is not a green checkmark to be trusted; it is a document to be
re-checked. Two properties make that possible, and both are enforced
mechanically:

1. **The verdict follows from the gates.** `verify_evidence.py` re-derives each
   case's status from its recorded gating checks and rejects any record whose
   claimed result its own checks do not support. A PASS is never an assertion.
2. **"Not compared" is never a pass.** The comparator distinguishes *identical*
   (PASS), *different* (FAIL), and *nothing compared* (ERROR — mismatched file
   sets, an unreadable input, a scan that could not run); the verifier's exit
   codes carry the same three-way distinction (`0` / `1` / `2`). Silence cannot
   masquerade as success.

Reproducibility rests on the manifest's per-output fingerprints (md5 + byte
count), not on retaining terabytes of model output: a purged run is still
verifiable against its recorded fingerprint.
