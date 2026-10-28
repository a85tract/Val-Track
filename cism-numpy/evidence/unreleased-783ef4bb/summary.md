# Acceptance record — cism-numpy unreleased-783ef4bb

| | |
|---|---|
| Artifact | `https://github.com/a85tract/RecastEngine-Pro` @ `783ef4bb` |
| Reference | CISM (Community Ice Sheet Model), cism_driver with the Glissade dycore (libglide, libglissade, libglimmer), 46e27de479f061ce7c0e96a148d3e7af7f65e461 |
| Val-Track | unreleased-01b0f3a7 (`01b0f3a7`) |
| Machine | CURC Alpine, acpu partition, milan nodes (AMD EPYC 7713), Slurm |
| Compiler | GNU Fortran 14.2.0 (module gcc/14.2.0), each project's own flags plus -ffp-contract=off |
| Cases | 1 |
| Result | **PASS** |
| Security gate | NOT_RUN |
| Evidence class | complete |
| Validated | 2026-10-05T06:48:14Z |

## Cases

### halfar-ho-t5 — PASS

Criteria: `cism-numpy/benchmarks/halfar-ho-t5.yaml` (bitwise)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `file_set_equal` | yes | yes | file sets match |
| `numeric_md5_equal` | yes | yes | overall_numeric_equal=True (3 files) |
| `timing_delta_pct` | no | — | reported without a bound |
