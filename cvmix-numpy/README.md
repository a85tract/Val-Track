# cvmix-numpy

CVMix: the computational Fortran that the project's own benchmark reaches, translated to NumPy by RecastEngine-Pro `783ef4bb` (tag `wave24-accepted`, branch `oopsla2027-wave24`). The translated program is the benchmark's own Fortran main program, with every benchmark-reached computational subprogram running as its NumPy translation through f2py; input, output and the driver stay Fortran.

Reference: CVMix (Community ocean Vertical Mixing, CVMix-src): src/shared kernels driven by the standalone driver at `fce422195a0c58f15a55946b5ed517ba4365e232`, compiled and run as the original program in the same environment.

Records: `evidence/unreleased-783ef4bb/` (4 cases, `bitwise` run pairs).

## Cases

| Case | Benchmark | Output files compared | How each file is compared | Result |
|---|---|---:|---|---|
| `bryan-lewis` | CVMix reg_tests Bryan-Lewis | 4 | raw bytes | PASS |
| `double-diff` | CVMix reg_tests double_diff | 3 | raw bytes | PASS |
| `kpp` | CVMix reg_tests kpp | 10 | raw bytes | PASS |
| `shear` | CVMix reg_tests shear | 5 | raw bytes | PASS |

Each case's benchmark file (`benchmarks/<case>.yaml`) gives the benchmark, the build and run commands, the environment, the translation plan (delegated, inside-NumPy and kept-Fortran subprograms) and the accepted runs; `evidence/.../report.txt` gives every compared file's digests for both programs.

## What a PASS claims

In the stated environment, the translated program run on this benchmark case produces the same set of output files as the original Fortran program, and every compared file has the same digest: of its bytes, or of its text after the stated masks (dates, timers, host names), or of a fixed-format dump of its numeric values. Wall times are reported and never gate.

It does not claim anything about other inputs or cases, other compilers or machines, code the benchmark does not reach, or the project's shipped reference outputs (the reference is the original program in the same environment).
