# Acceptance record — cosp2-numpy unreleased-783ef4bb

| | |
|---|---|
| Artifact | `https://github.com/a85tract/RecastEngine-Pro` @ `783ef4bb` |
| Reference | COSPv2.0 (CFMIP, https://github.com/CFMIP/COSPv2.0), the CFMIP Observation Simulator Package offline driver, 5eb05e51187dd2d0e448b78c4e6b28e1d6f65493 |
| Val-Track | unreleased-01b0f3a7 (`01b0f3a7`) |
| Machine | CURC Alpine, acpu partition, milan nodes (AMD EPYC 7713), Slurm |
| Compiler | GNU Fortran 14.2.0 (module gcc/14.2.0), each project's own flags plus -ffp-contract=off |
| Cases | 1 |
| Result | **PASS** |
| Security gate | NOT_RUN |
| Evidence class | complete |
| Validated | 2026-10-05T06:48:14Z |

## Cases

### ukmo — PASS

Criteria: `cosp2-numpy/benchmarks/ukmo.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (1 files) |
| `timing_delta_pct` | no | — | reported without a bound |
