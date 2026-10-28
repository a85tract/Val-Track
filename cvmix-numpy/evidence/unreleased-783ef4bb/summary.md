# Acceptance record — cvmix-numpy unreleased-783ef4bb

| | |
|---|---|
| Artifact | `https://github.com/a85tract/RecastEngine-Pro` @ `783ef4bb` |
| Reference | CVMix (Community ocean Vertical Mixing, CVMix-src): src/shared kernels driven by the standalone driver, fce422195a0c58f15a55946b5ed517ba4365e232 |
| Val-Track | unreleased-01b0f3a7 (`01b0f3a7`) |
| Machine | CURC Alpine, acpu partition, milan nodes (AMD EPYC 7713), Slurm |
| Compiler | GNU Fortran 14.2.0 (module gcc/14.2.0), each project's own flags plus -ffp-contract=off |
| Cases | 4 |
| Result | **PASS** |
| Security gate | NOT_RUN |
| Evidence class | complete |
| Validated | 2026-10-05T06:48:14Z |

## Cases

### bryan-lewis — PASS

Criteria: `cvmix-numpy/benchmarks/bryan-lewis.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (4 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### double-diff — PASS

Criteria: `cvmix-numpy/benchmarks/double-diff.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (3 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### kpp — PASS

Criteria: `cvmix-numpy/benchmarks/kpp.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (10 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### shear — PASS

Criteria: `cvmix-numpy/benchmarks/shear.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (5 files) |
| `timing_delta_pct` | no | — | reported without a bound |
