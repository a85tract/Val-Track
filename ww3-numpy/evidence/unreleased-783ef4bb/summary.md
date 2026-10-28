# Acceptance record — ww3-numpy unreleased-783ef4bb

| | |
|---|---|
| Artifact | `https://github.com/a85tract/RecastEngine-Pro` @ `783ef4bb` |
| Reference | WAVEWATCH III (NOAA-EMC/WW3), ww3_shel built with switch_PR3_UQ, a0eaffebde6246e096f240509c9acf159fe09003 |
| Val-Track | unreleased-01b0f3a7 (`01b0f3a7`) |
| Machine | CURC Alpine, acpu partition, milan nodes (AMD EPYC 7713), Slurm |
| Compiler | GNU Fortran 14.2.0 (module gcc/14.2.0), each project's own flags plus -ffp-contract=off |
| Cases | 2 |
| Result | **PASS** |
| Security gate | NOT_RUN |
| Evidence class | complete |
| Validated | 2026-10-05T08:31:00Z |

## Cases

### tp1-1 — PASS

Criteria: `ww3-numpy/benchmarks/tp1-1.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (6 files) |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (3 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### ts1 — PASS

Criteria: `ww3-numpy/benchmarks/ts1.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (7 files) |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (3 files) |
| `timing_delta_pct` | no | — | reported without a bound |
