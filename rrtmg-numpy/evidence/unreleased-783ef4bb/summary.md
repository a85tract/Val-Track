# Acceptance record — rrtmg-numpy unreleased-783ef4bb

| | |
|---|---|
| Artifact | `https://github.com/a85tract/RecastEngine-Pro` @ `783ef4bb` |
| Reference | RRTMG (LW, SW), 958edb1ad1618d76d0fcc5a9dc2e3c2f791a54dd |
| Val-Track | unreleased-53515314 (`53515314`) |
| Machine | Alpine (CU Boulder Research Computing), Linux el8_10 x86_64 |
| Compiler | _not captured_ |
| Cases | 1 |
| Result | **FAIL** |
| Security gate | NOT_RUN |
| Evidence class | reconstructed |
| Validated | 2026-10-05T05:25:48Z |

## Cases

### rrtmg — FAIL

Criteria: `rrtmg-numpy/benchmarks/rrtmg.yaml` (output-verdict)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `run_set_equal` | yes | yes | 44 runs, as the benchmark names them |
| `runs_identical` | yes | no | 29 of 30 runs identical (60 output files compared); differ: LW MLS-cld5-imca0-icld2 outermost (DIFFERENT 1/2) |
| `runs_identical` | no | yes | 14 of 14 runs identical (28 output files compared) |
