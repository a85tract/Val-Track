# Acceptance record — marbl-numpy unreleased-783ef4bb

| | |
|---|---|
| Artifact | `https://github.com/a85tract/RecastEngine-Pro` @ `783ef4bb` |
| Reference | MARBL (Marine Biogeochemistry Library), stand-alone test driver tests/driver_src, 6b2a5e41dc5b0faaf9b600c96432e2487515e878 |
| Val-Track | unreleased-01b0f3a7 (`01b0f3a7`) |
| Machine | CURC Alpine, acpu partition, milan nodes (AMD EPYC 7713), Slurm |
| Compiler | GNU Fortran 14.2.0 (module gcc/14.2.0), each project's own flags plus -ffp-contract=off |
| Cases | 2 |
| Result | **PASS** |
| Security gate | NOT_RUN |
| Evidence class | complete |
| Validated | 2026-10-05T06:48:14Z |

## Cases

### call-compute-subroutines — PASS

Criteria: `marbl-numpy/benchmarks/call-compute-subroutines.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (1 files) |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (1 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### init — PASS

Criteria: `marbl-numpy/benchmarks/init.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (1 files) |
| `timing_delta_pct` | no | — | reported without a bound |
