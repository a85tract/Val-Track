# Acceptance record — qe-numpy unreleased-783ef4bb

| | |
|---|---|
| Artifact | `https://github.com/a85tract/RecastEngine-Pro` @ `783ef4bb` |
| Reference | Quantum ESPRESSO (XClib, dft-d3), 61569eb480231b649c47f631df9c5c83537df461 |
| Val-Track | unreleased-53515314 (`53515314`) |
| Machine | Alpine (CU Boulder Research Computing), Linux el8_10 x86_64 |
| Compiler | gfortran 14.2.0 (/curc/sw/install/gcc/14.2.0) |
| Cases | 1 |
| Result | **PASS** |
| Security gate | NOT_RUN |
| Evidence class | reconstructed |
| Validated | 2026-10-05T05:01:39Z |

## Cases

### qe — PASS

Criteria: `qe-numpy/benchmarks/qe.yaml` (output-verdict)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `run_set_equal` | yes | yes | 4 runs, as the benchmark names them |
| `runs_identical` | yes | yes | 4 of 4 runs identical (9 output files compared) |
