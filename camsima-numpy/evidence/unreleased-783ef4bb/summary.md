# Acceptance record — camsima-numpy unreleased-783ef4bb

| | |
|---|---|
| Artifact | `https://github.com/a85tract/RecastEngine-Pro` @ `783ef4bb` |
| Reference | CAM-SIMA (ESCOMP/CAM-SIMA, CIME FPHYStest) with ESCOMP/atmospheric_physics and NCAR/ccpp-framework, CAM-SIMA 47e1e6303951d999f6939bdffff829f682a2e081 (development, + bin/git-fleximod update); atmospheric_physics 3fd57dde51ea63f35f3e3655012ad074a06ad051; ccpp-framework 766261cf0433692037eec258ba87dcdbea552692 |
| Val-Track | unreleased-0ad9f1a1 (`0ad9f1a1`) |
| Machine | NCAR Derecho CPU nodes, PBS, CIME machine derecho |
| Compiler | GNU Fortran 14.3.0 (CIME derecho_gnu, module gcc/14.3.0), the case's flags plus -ffp-contract=off |
| Cases | 4 |
| Result | **PASS** |
| Security gate | NOT_RUN |
| Evidence class | complete |
| Validated | 2026-10-05T06:48:14Z |

## Cases

### held-suarez — PASS

Criteria: `camsima-numpy/benchmarks/held-suarez.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (1 files) |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (1 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### kessler — PASS

Criteria: `camsima-numpy/benchmarks/kessler.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (1 files) |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (1 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### tj2016-after-coupler — PASS

Criteria: `camsima-numpy/benchmarks/tj2016-after-coupler.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (1 files) |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (1 files) |
| `timing_delta_pct` | no | — | reported without a bound |

### tj2016-before-coupler — PASS

Criteria: `camsima-numpy/benchmarks/tj2016-before-coupler.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (1 files) |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (1 files) |
| `timing_delta_pct` | no | — | reported without a bound |
