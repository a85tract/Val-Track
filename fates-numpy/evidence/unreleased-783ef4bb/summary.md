# Acceptance record — fates-numpy unreleased-783ef4bb

| | |
|---|---|
| Artifact | `https://github.com/a85tract/RecastEngine-Pro` @ `783ef4bb` |
| Reference | FATES (NGEET/fates), functional_unit_testing/leaf_biophys with biogeophys/LeafBiophysicsMod.F90 and main/FatesUtilsMod.F90, 5a3c441ceeb141c35e87a33eeb2c168cc367b6f1 |
| Val-Track | unreleased-01b0f3a7 (`01b0f3a7`) |
| Machine | CURC Alpine, acpu partition, milan nodes (AMD EPYC 7713), Slurm |
| Compiler | GNU Fortran 14.2.0 (module gcc/14.2.0), each project's own flags plus -ffp-contract=off |
| Cases | 1 |
| Result | **PASS** |
| Security gate | NOT_RUN |
| Evidence class | complete |
| Validated | 2026-10-05T06:48:14Z |

## Cases

### smoke — PASS

Criteria: `fates-numpy/benchmarks/smoke.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (2 files) |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (1 files) |
| `timing_delta_pct` | no | — | reported without a bound |
