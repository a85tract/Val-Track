# cosp2-numpy

COSP2: the computational Fortran that the project's own benchmark reaches, translated to NumPy by RecastEngine-Pro `783ef4bb` (tag `wave24-accepted`, branch `oopsla2027-wave24`). The translated program is the benchmark's own Fortran main program, with every benchmark-reached computational subprogram running as its NumPy translation through f2py; input, output and the driver stay Fortran.

Reference: COSPv2.0 (CFMIP, https://github.com/CFMIP/COSPv2.0), the CFMIP Observation Simulator Package offline driver at `5eb05e51187dd2d0e448b78c4e6b28e1d6f65493`, compiled and run as the original program in the same environment.

Records: `evidence/unreleased-783ef4bb/` (1 case, `bitwise` run pairs).

## Cases

| Case | Benchmark | Output files compared | How each file is compared | Result |
|---|---|---:|---|---|
| `ukmo` | COSPv2.0 offline driver, UKMO case (cosp_input_um.nc) | 3 | raw bytes; text after the kit's masks | PASS |

Each case's benchmark file (`benchmarks/<case>.yaml`) gives the benchmark, the build and run commands, the environment, the translation plan (delegated, inside-NumPy and kept-Fortran subprograms) and the accepted runs; `evidence/.../report.txt` gives every compared file's digests for both programs.

## What a PASS claims

In the stated environment, the translated program run on this benchmark case produces the same set of output files as the original Fortran program, and every compared file has the same digest: of its bytes, or of its text after the stated masks (dates, timers, host names), or of a fixed-format dump of its numeric values. Wall times are reported and never gate.

It does not claim anything about other inputs or cases, other compilers or machines, code the benchmark does not reach, or the project's shipped reference outputs (the reference is the original program in the same environment).
