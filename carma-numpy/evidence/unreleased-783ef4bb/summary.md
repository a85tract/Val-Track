# Acceptance record — carma-numpy unreleased-783ef4bb

| | |
|---|---|
| Artifact | `https://github.com/a85tract/RecastEngine-Pro` @ `783ef4bb` |
| Reference | CARMA (Community Aerosol and Radiation Model for Atmospheres): the CARMA wrapper's regression test programs, CARMA wrapper (ESCOMP/CARMA) 26b30b2738566de5d3979c1b2ccf191dd78c1207 with CARMA_base 7b12e0cce0f83de0c55682d20c64222cc339dfce in source/base |
| Val-Track | unreleased-01b0f3a7 (`01b0f3a7`) |
| Machine | CURC Alpine, acpu partition, milan nodes (AMD EPYC 7713), Slurm |
| Compiler | GNU Fortran 14.2.0 (module gcc/14.2.0), each project's own flags plus -ffp-contract=off |
| Cases | 27 |
| Result | **PASS** |
| Security gate | NOT_RUN |
| Evidence class | complete |
| Validated | 2026-10-05T06:48:14Z |

## Cases

### bc2gtest — PASS

Criteria: `carma-numpy/benchmarks/bc2gtest.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### bcoctest — PASS

Criteria: `carma-numpy/benchmarks/bcoctest.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### cetest — PASS

Criteria: `carma-numpy/benchmarks/cetest.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### coagtest — PASS

Criteria: `carma-numpy/benchmarks/coagtest.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### drydeptest — PASS

Criteria: `carma-numpy/benchmarks/drydeptest.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (3 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### falltest — PASS

Criteria: `carma-numpy/benchmarks/falltest.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### fractalmicrotest — PASS

Criteria: `carma-numpy/benchmarks/fractalmicrotest.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### fractalopticstest — PASS

Criteria: `carma-numpy/benchmarks/fractalopticstest.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### growclrtest — PASS

Criteria: `carma-numpy/benchmarks/growclrtest.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### growintest — PASS

Criteria: `carma-numpy/benchmarks/growintest.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### growsubtest — PASS

Criteria: `carma-numpy/benchmarks/growsubtest.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### growtest — PASS

Criteria: `carma-numpy/benchmarks/growtest.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### kappawetrtest — PASS

Criteria: `carma-numpy/benchmarks/kappawetrtest.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### mietest — PASS

Criteria: `carma-numpy/benchmarks/mietest.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### nuc2test — PASS

Criteria: `carma-numpy/benchmarks/nuc2test.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### nuctest — PASS

Criteria: `carma-numpy/benchmarks/nuctest.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### pheattest — PASS

Criteria: `carma-numpy/benchmarks/pheattest.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### scfalltest — PASS

Criteria: `carma-numpy/benchmarks/scfalltest.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### sigmadrydeptest — PASS

Criteria: `carma-numpy/benchmarks/sigmadrydeptest.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (3 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### sigmafalltest — PASS

Criteria: `carma-numpy/benchmarks/sigmafalltest.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### sulfate-ccdon-test — PASS

Criteria: `carma-numpy/benchmarks/sulfate-ccdon-test.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### sulfate-vehkamaki-test — PASS

Criteria: `carma-numpy/benchmarks/sulfate-vehkamaki-test.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### sulfatetest — PASS

Criteria: `carma-numpy/benchmarks/sulfatetest.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### sulfhet-vehkamaki-test — PASS

Criteria: `carma-numpy/benchmarks/sulfhet-vehkamaki-test.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### sulfhettest — PASS

Criteria: `carma-numpy/benchmarks/sulfhettest.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### swelltest — PASS

Criteria: `carma-numpy/benchmarks/swelltest.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### vdiftest — PASS

Criteria: `carma-numpy/benchmarks/vdiftest.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `timing_delta_pct` | no | — | reported without a bound |
