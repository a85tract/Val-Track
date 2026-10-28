# Acceptance record — camsima-numpy unreleased-783ef4bb

| | |
|---|---|
| Artifact | `https://github.com/a85tract/RecastEngine-Pro` @ `783ef4bb` |
| Reference | CAM-SIMA (Kessler), 47e1e6303951d999f6939bdffff829f682a2e081 |
| Val-Track | unreleased-53515314 (`53515314`) |
| Machine | Derecho (NCAR) |
| Compiler | _not captured_ |
| Cases | 3 |
| Result | **PASS** |
| Security gate | NOT_RUN |
| Evidence class | reconstructed |
| Validated | 2026-10-05T05:05:05Z |

## Cases

### kessler — PASS

Criteria: `camsima-numpy/benchmarks/kessler.yaml` (output-verdict)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `run_set_equal` | yes | yes | 1 runs, as the benchmark names them |
| `runs_identical` | yes | yes | 1 of 1 runs identical (3 output files compared) |

### held-suarez — PASS

Criteria: `camsima-numpy/benchmarks/held-suarez.yaml` (output-verdict)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `run_set_equal` | yes | yes | 1 runs, as the benchmark names them |
| `runs_identical` | yes | yes | 1 of 1 runs identical (3 output files compared) |

### tj2016 — PASS

Criteria: `camsima-numpy/benchmarks/tj2016.yaml` (output-verdict)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `run_set_equal` | yes | yes | 2 runs, as the benchmark names them |
| `runs_identical` | yes | yes | 2 of 2 runs identical (6 output files compared) |
