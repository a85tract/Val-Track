# carma-numpy

CARMA: the computational Fortran that the project's own benchmark reaches, translated to NumPy by RecastEngine-Pro `783ef4bb` (tag `wave24-accepted`, branch `oopsla2027-wave24`). The translated program is the benchmark's own Fortran main program, with every benchmark-reached computational subprogram running as its NumPy translation through f2py; input, output and the driver stay Fortran.

Reference: CARMA (Community Aerosol and Radiation Model for Atmospheres): the CARMA wrapper's regression test programs at `CARMA wrapper (ESCOMP/CARMA) 26b30b2738566de5d3979c1b2ccf191dd78c1207 with CARMA_base 7b12e0cce0f83de0c55682d20c64222cc339dfce in source/base`, compiled and run as the original program in the same environment.

Records: `evidence/unreleased-783ef4bb/` (27 cases, `bitwise` run pairs).

## Cases

| Case | Benchmark | Output files compared | How each file is compared | Result |
|---|---|---:|---|---|
| `bc2gtest` | CARMA BC2GTEST | 2 | raw bytes | PASS |
| `bcoctest` | CARMA BCOCTEST | 2 | raw bytes | PASS |
| `cetest` | CARMA CETEST | 2 | raw bytes | PASS |
| `coagtest` | CARMA COAGTEST | 2 | raw bytes | PASS |
| `drydeptest` | CARMA DRYDEPTEST | 3 | raw bytes | PASS |
| `falltest` | CARMA FALLTEST | 2 | raw bytes | PASS |
| `fractalmicrotest` | CARMA FRACTALMICROTEST | 2 | raw bytes | PASS |
| `fractalopticstest` | CARMA FRACTALOPTICSTEST | 2 | raw bytes | PASS |
| `growclrtest` | CARMA GROWCLRTEST | 2 | raw bytes | PASS |
| `growintest` | CARMA GROWINTEST | 2 | raw bytes | PASS |
| `growsubtest` | CARMA GROWSUBTEST | 2 | raw bytes | PASS |
| `growtest` | CARMA GROWTEST | 2 | raw bytes | PASS |
| `kappawetrtest` | CARMA KAPPAWETRTEST | 2 | raw bytes | PASS |
| `mietest` | CARMA MIETEST | 2 | raw bytes | PASS |
| `nuc2test` | CARMA NUC2TEST | 2 | raw bytes | PASS |
| `nuctest` | CARMA NUCTEST | 2 | raw bytes | PASS |
| `pheattest` | CARMA PHEATTEST | 2 | raw bytes | PASS |
| `scfalltest` | CARMA SCFALLTEST | 2 | raw bytes | PASS |
| `sigmadrydeptest` | CARMA SIGMADRYDEPTEST | 3 | raw bytes | PASS |
| `sigmafalltest` | CARMA SIGMAFALLTEST | 2 | raw bytes | PASS |
| `sulfate-ccdon-test` | CARMA SULFATE_CCDON_TEST | 2 | raw bytes | PASS |
| `sulfate-vehkamaki-test` | CARMA SULFATE_VEHKAMAKI_TEST | 2 | raw bytes | PASS |
| `sulfatetest` | CARMA SULFATETEST | 2 | raw bytes | PASS |
| `sulfhet-vehkamaki-test` | CARMA SULFHET_VEHKAMAKI_TEST | 2 | raw bytes | PASS |
| `sulfhettest` | CARMA SULFHETTEST | 2 | raw bytes | PASS |
| `swelltest` | CARMA SWELLTEST | 2 | raw bytes | PASS |
| `vdiftest` | CARMA VDIFTEST | 2 | raw bytes | PASS |

Each case's benchmark file (`benchmarks/<case>.yaml`) gives the benchmark, the build and run commands, the environment, the translation plan (delegated, inside-NumPy and kept-Fortran subprograms) and the accepted runs; `evidence/.../report.txt` gives every compared file's digests for both programs.

## What a PASS claims

In the stated environment, the translated program run on this benchmark case produces the same set of output files as the original Fortran program, and every compared file has the same digest: of its bytes, or of its text after the stated masks (dates, timers, host names), or of a fixed-format dump of its numeric values. Wall times are reported and never gate.

It does not claim anything about other inputs or cases, other compilers or machines, code the benchmark does not reach, or the project's shipped reference outputs (the reference is the original program in the same environment).

## Uninitialised heap reads

The original Fortran program reads heap memory it never assigned in `growclrtest`, `growintest`, `growsubtest`, `growtest`, `nuctest`, `pheattest`, so its own output depends on the heap's contents. These cases are run with the heap zero-filled on both sides (`MALLOC_PERTURB_=255 GLIBC_TUNABLES=glibc.malloc.tcache_count=0`), which defines the values read as zero, as the translation does; the setting is part of each case's environment. Gating the zero-heap runs here is a maintainer's decision (2026-10-28); RRTMG's one heap-reading case is gated on the default allocator instead and fails (`rrtmg-numpy/README.md`).
