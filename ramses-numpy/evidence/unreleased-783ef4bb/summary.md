# Acceptance record — ramses-numpy unreleased-783ef4bb

| | |
|---|---|
| Artifact | `https://github.com/a85tract/RecastEngine-Pro` @ `783ef4bb` |
| Reference | RAMSES, 5f0ed46289f8eed71b2abd0e482f953bcaa02934 |
| Val-Track | unreleased-53515314 (`53515314`) |
| Machine | Alpine (CU Boulder Research Computing), Linux el8_10 x86_64 |
| Compiler | gfortran 14.2.0 (/curc/sw/install/gcc/14.2.0) |
| Cases | 1 |
| Result | **PASS** |
| Security gate | NOT_RUN |
| Evidence class | reconstructed |
| Validated | 2026-10-05T05:01:39Z |

## Cases

### ramses — PASS

Criteria: `ramses-numpy/benchmarks/ramses.yaml` (output-verdict)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `run_set_equal` | yes | yes | 3 runs, as the benchmark names them |
| `runs_identical` | yes | yes | 3 of 3 runs identical (63 output files compared) |
