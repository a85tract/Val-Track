# Acceptance record — cism-numpy unreleased-783ef4bb

| | |
|---|---|
| Artifact | `https://github.com/a85tract/RecastEngine-Pro` @ `783ef4bb` |
| Reference | CISM, 46e27de479f061ce7c0e96a148d3e7af7f65e461 |
| Val-Track | unreleased-53515314 (`53515314`) |
| Machine | Alpine (CU Boulder Research Computing), Linux el8_10 x86_64 |
| Compiler | _not captured_ |
| Cases | 1 |
| Result | **PASS** |
| Security gate | NOT_RUN |
| Evidence class | reconstructed |
| Validated | 2026-10-05T05:50:48Z |

## Cases

### cism — PASS

Criteria: `cism-numpy/benchmarks/cism.yaml` (output-verdict)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `run_set_equal` | yes | yes | 4 runs, as the benchmark names them |
| `runs_identical` | yes | yes | 2 of 2 runs identical (4 output files compared) |
| `runs_identical` | no | yes | 2 of 2 runs identical (6 output files compared) |
