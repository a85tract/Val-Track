# Acceptance record — njoy-numpy unreleased-783ef4bb

| | |
|---|---|
| Artifact | `https://github.com/a85tract/RecastEngine-Pro` @ `783ef4bb` |
| Reference | NJOY2016, ac5adf5f33d893e42f2eed7fb286b0d51c7580da |
| Val-Track | unreleased-53515314 (`53515314`) |
| Machine | Alpine (CU Boulder Research Computing), Linux el8_10 x86_64 |
| Compiler | gfortran 14.2.0 (/curc/sw/install/gcc/14.2.0) |
| Cases | 1 |
| Result | **PASS** |
| Security gate | NOT_RUN |
| Evidence class | reconstructed |
| Validated | 2026-10-05T05:01:39Z |

## Cases

### njoy — PASS

Criteria: `njoy-numpy/benchmarks/njoy.yaml` (output-verdict)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `run_set_equal` | yes | yes | 8 runs, as the benchmark names them |
| `runs_identical` | yes | yes | 8 of 8 runs identical (41 output files compared) |
