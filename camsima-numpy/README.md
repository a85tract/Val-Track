# camsima-numpy

CAM-SIMA (idealized physics test suites): the computational Fortran that the project's own benchmark reaches, translated to NumPy by RecastEngine-Pro `783ef4bb` (tag `wave24-accepted`, branch `oopsla2027-wave24`). The translated program is the benchmark's own Fortran main program, with every benchmark-reached computational subprogram running as its NumPy translation through f2py; input, output and the driver stay Fortran.

Reference: CAM-SIMA (ESCOMP/CAM-SIMA, CIME FPHYStest) with ESCOMP/atmospheric_physics and NCAR/ccpp-framework at `CAM-SIMA 47e1e6303951d999f6939bdffff829f682a2e081 (development, + bin/git-fleximod update); atmospheric_physics 3fd57dde51ea63f35f3e3655012ad074a06ad051; ccpp-framework 766261cf0433692037eec258ba87dcdbea552692`, compiled and run as the original program in the same environment.

Records: `evidence/unreleased-783ef4bb/` (4 cases, `bitwise` run pairs).

## Cases

| Case | Benchmark | Output files compared | How each file is compared | Result |
|---|---|---:|---|---|
| `held-suarez` | CAM-SIMA Held-Suarez (SMS_Ln2.ne3pg3_ne3pg3_mg37.FPHYStest.derecho_gnu.cam-outfrq_held_suarez_derecho) | 4 | text after the kit's masks; numpy %+.17g: every numeric netCDF variable (byte/short/int/float/double) in sorted name order: a line with the name, then one line per value '%+.17g' (C order, all records); md5 of the text | PASS |
| `kessler` | CAM-SIMA Kessler (SMS_Ln2.ne3pg3_ne3pg3_mg37.FPHYStest.derecho_gnu.cam-outfrq_kessler_derecho) | 4 | text after the kit's masks; numpy %+.17g: every numeric netCDF variable (byte/short/int/float/double) in sorted name order: a line with the name, then one line per value '%+.17g' (C order, all records); md5 of the text | PASS |
| `tj2016-after-coupler` | CAM-SIMA TJ2016 (after coupler) (SMS_Ln2.ne3pg3_ne3pg3_mg37.FPHYStest.derecho_gnu.cam-outfrq_tj2016_after_coupler_derecho) | 4 | text after the kit's masks; numpy %+.17g: every numeric netCDF variable (byte/short/int/float/double) in sorted name order: a line with the name, then one line per value '%+.17g' (C order, all records); md5 of the text | PASS |
| `tj2016-before-coupler` | CAM-SIMA TJ2016 (before coupler) (SMS_Ln2.ne3pg3_ne3pg3_mg37.FPHYStest.derecho_gnu.cam-outfrq_tj2016_before_coupler_derecho) | 4 | text after the kit's masks; numpy %+.17g: every numeric netCDF variable (byte/short/int/float/double) in sorted name order: a line with the name, then one line per value '%+.17g' (C order, all records); md5 of the text | PASS |

Each case's benchmark file (`benchmarks/<case>.yaml`) gives the benchmark, the build and run commands, the environment, the translation plan (delegated, inside-NumPy and kept-Fortran subprograms) and the accepted runs; `evidence/.../report.txt` gives every compared file's digests for both programs.

## What a PASS claims

In the stated environment, the translated program run on this benchmark case produces the same set of output files as the original Fortran program, and every compared file has the same digest: of its bytes, or of its text after the stated masks (dates, timers, host names), or of a fixed-format dump of its numeric values. Wall times are reported and never gate.

It does not claim anything about other inputs or cases, other compilers or machines, code the benchmark does not reach, or the project's shipped reference outputs (the reference is the original program in the same environment).
