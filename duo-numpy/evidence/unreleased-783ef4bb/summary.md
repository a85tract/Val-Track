# Acceptance record — duo-numpy unreleased-783ef4bb

| | |
|---|---|
| Artifact | `https://github.com/a85tract/RecastEngine-Pro` @ `783ef4bb` |
| Reference | Duo, 04b4718955fedf3eb551fb36019beabac225a3af |
| Val-Track | unreleased-53515314 (`53515314`) |
| Machine | Alpine (CU Boulder Research Computing), Linux el8_10 x86_64 |
| Compiler | gfortran 14.2.0 (/curc/sw/install/gcc/14.2.0) |
| Cases | 1 |
| Result | **PASS** |
| Security gate | NOT_RUN |
| Evidence class | reconstructed |
| Validated | 2026-10-05T05:01:39Z |

## Cases

### duo — PASS

Criteria: `duo-numpy/benchmarks/duo.yaml` (output-verdict)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `run_set_equal` | yes | yes | 2 runs, as the benchmark names them |
| `runs_identical` | yes | yes | 2 of 2 runs identical (4 output files compared) |
