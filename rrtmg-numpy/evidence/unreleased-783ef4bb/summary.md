# Acceptance record — rrtmg-numpy unreleased-783ef4bb

| | |
|---|---|
| Artifact | `https://github.com/a85tract/RecastEngine-Pro` @ `783ef4bb` |
| Reference | AER RRTMG_LW column model (rrtmg_lw.1col), https://github.com/AER-RC/RRTMG_LW (revision committed 2025-04-07T12:52:41-04:00; the wave24 source-revision manifest), 958edb1ad1618d76d0fcc5a9dc2e3c2f791a54dd |
| Val-Track | unreleased-01b0f3a7 (`01b0f3a7`) |
| Machine | CURC Alpine, acpu partition, milan nodes (AMD EPYC 7713), Slurm |
| Compiler | GNU Fortran 14.2.0 (module gcc/14.2.0), each project's own flags plus -ffp-contract=off |
| Cases | 30 |
| Result | **FAIL** |
| Security gate | NOT_RUN |
| Evidence class | complete |
| Validated | 2026-10-05T06:48:14Z |

## Cases

### lw-icrccm-sonde — PASS

Criteria: `rrtmg-numpy/benchmarks/lw-icrccm-sonde.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### lw-mls-cld5-imca0-icld2 — FAIL

Criteria: `rrtmg-numpy/benchmarks/lw-mls-cld5-imca0-icld2.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | no | overall_numeric_equal=False (2 files; differ: OUTPUT_RRTM) |
| `timing_delta_pct` | no | — | reported without a bound |

### lw-mls-cld5-imca1-icld2 — PASS

Criteria: `rrtmg-numpy/benchmarks/lw-mls-cld5-imca1-icld2.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### lw-mls-cld7-imca1-icld2 — PASS

Criteria: `rrtmg-numpy/benchmarks/lw-mls-cld7-imca1-icld2.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### lw-mls-cld7-imca1-icld4-idcor0 — PASS

Criteria: `rrtmg-numpy/benchmarks/lw-mls-cld7-imca1-icld4-idcor0.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### lw-mls-cld7-imca1-icld5-idcor0 — PASS

Criteria: `rrtmg-numpy/benchmarks/lw-mls-cld7-imca1-icld5-idcor0.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### lw-mls-cld7-imca1-icld5-idcor1 — PASS

Criteria: `rrtmg-numpy/benchmarks/lw-mls-cld7-imca1-icld5-idcor1.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### lw-mls-clr — PASS

Criteria: `rrtmg-numpy/benchmarks/lw-mls-clr.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### lw-mls-clr-aer12 — PASS

Criteria: `rrtmg-numpy/benchmarks/lw-mls-clr-aer12.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### lw-mls-clr-idrv1 — PASS

Criteria: `rrtmg-numpy/benchmarks/lw-mls-clr-idrv1.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### lw-mls-clr-xsec — PASS

Criteria: `rrtmg-numpy/benchmarks/lw-mls-clr-xsec.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### lw-mlw-clr — PASS

Criteria: `rrtmg-numpy/benchmarks/lw-mlw-clr.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### lw-saw-clr — PASS

Criteria: `rrtmg-numpy/benchmarks/lw-saw-clr.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### lw-trop-clr — PASS

Criteria: `rrtmg-numpy/benchmarks/lw-trop-clr.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### sw-mls-cld5-imca1-icld2 — PASS

Criteria: `rrtmg-numpy/benchmarks/sw-mls-cld5-imca1-icld2.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### sw-mls-cld6-imca0-icld2 — PASS

Criteria: `rrtmg-numpy/benchmarks/sw-mls-cld6-imca0-icld2.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### sw-mls-cld7-imca1-icld2 — PASS

Criteria: `rrtmg-numpy/benchmarks/sw-mls-cld7-imca1-icld2.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### sw-mls-cld7-imca1-icld5-idcor0 — PASS

Criteria: `rrtmg-numpy/benchmarks/sw-mls-cld7-imca1-icld5-idcor0.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### sw-mls-cld7-imca1-icld5-idcor1 — PASS

Criteria: `rrtmg-numpy/benchmarks/sw-mls-cld7-imca1-icld5-idcor1.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### sw-mls-clr — PASS

Criteria: `rrtmg-numpy/benchmarks/sw-mls-clr.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### sw-mls-clr-aer12 — PASS

Criteria: `rrtmg-numpy/benchmarks/sw-mls-clr-aer12.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### sw-mls-clr-sza45-isolvar0-tsi-avg — PASS

Criteria: `rrtmg-numpy/benchmarks/sw-mls-clr-sza45-isolvar0-tsi-avg.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### sw-mls-clr-sza45-isolvar1-tsi-max — PASS

Criteria: `rrtmg-numpy/benchmarks/sw-mls-clr-sza45-isolvar1-tsi-max.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### sw-mls-clr-sza45-isolvar1-tsi-min — PASS

Criteria: `rrtmg-numpy/benchmarks/sw-mls-clr-sza45-isolvar1-tsi-min.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### sw-mls-clr-sza45-isolvar2-01jan1950 — PASS

Criteria: `rrtmg-numpy/benchmarks/sw-mls-clr-sza45-isolvar2-01jan1950.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### sw-mls-clr-sza45-isolvar3-bndscl-tsi-max — PASS

Criteria: `rrtmg-numpy/benchmarks/sw-mls-clr-sza45-isolvar3-bndscl-tsi-max.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### sw-mls-clr-sza65 — PASS

Criteria: `rrtmg-numpy/benchmarks/sw-mls-clr-sza65.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### sw-mlw-clr — PASS

Criteria: `rrtmg-numpy/benchmarks/sw-mlw-clr.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### sw-saw-clr — PASS

Criteria: `rrtmg-numpy/benchmarks/sw-saw-clr.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### sw-trop-clr — PASS

Criteria: `rrtmg-numpy/benchmarks/sw-trop-clr.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |
