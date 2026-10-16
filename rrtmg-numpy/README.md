# rrtmg-numpy

RRTMG (LW and SW): the computational Fortran that the project's own benchmark reaches, translated to NumPy by RecastEngine-Pro `783ef4bb` (tag `wave24-accepted`, branch `oopsla2027-wave24`). The translated program is the benchmark's own Fortran main program, with every benchmark-reached computational subprogram running as its NumPy translation through f2py; input, output and the driver stay Fortran.

Reference: AER RRTMG_LW column model (rrtmg_lw.1col), https://github.com/AER-RC/RRTMG_LW (revision committed 2025-04-07T12:52:41-04:00; the wave24 source-revision manifest) at `958edb1ad1618d76d0fcc5a9dc2e3c2f791a54dd`, compiled and run as the original program in the same environment.

Records: `evidence/unreleased-783ef4bb/` (30 cases, `bitwise` run pairs).

## Cases

| Case | Benchmark | Output files compared | How each file is compared | Result |
|---|---|---:|---|---|
| `lw-icrccm-sonde` | RRTMG_LW column model, run_examples_std_atm case ICRCCM_sonde | 2 | raw bytes | PASS |
| `lw-mls-cld5-imca0-icld2` | RRTMG_LW column model, run_examples_std_atm case MLS-cld5-imca0-icld2 | 2 | raw bytes | PASS |
| `lw-mls-cld5-imca1-icld2` | RRTMG_LW column model, run_examples_std_atm case MLS-cld5-imca1-icld2 | 2 | raw bytes | PASS |
| `lw-mls-cld7-imca1-icld2` | RRTMG_LW column model, run_examples_std_atm case MLS-cld7-imca1-icld2 | 2 | raw bytes | PASS |
| `lw-mls-cld7-imca1-icld4-idcor0` | RRTMG_LW column model, run_examples_std_atm case MLS-cld7-imca1-icld4-idcor0 | 2 | raw bytes | PASS |
| `lw-mls-cld7-imca1-icld5-idcor0` | RRTMG_LW column model, run_examples_std_atm case MLS-cld7-imca1-icld5-idcor0 | 2 | raw bytes | PASS |
| `lw-mls-cld7-imca1-icld5-idcor1` | RRTMG_LW column model, run_examples_std_atm case MLS-cld7-imca1-icld5-idcor1 | 2 | raw bytes | PASS |
| `lw-mls-clr` | RRTMG_LW column model, run_examples_std_atm case MLS-clr | 2 | raw bytes | PASS |
| `lw-mls-clr-aer12` | RRTMG_LW column model, run_examples_std_atm case MLS-clr-aer12 | 2 | raw bytes | PASS |
| `lw-mls-clr-idrv1` | RRTMG_LW column model, run_examples_std_atm case MLS-clr-idrv1 | 2 | raw bytes | PASS |
| `lw-mls-clr-xsec` | RRTMG_LW column model, run_examples_std_atm case MLS-clr-xsec | 2 | raw bytes | PASS |
| `lw-mlw-clr` | RRTMG_LW column model, run_examples_std_atm case MLW-clr | 2 | raw bytes | PASS |
| `lw-saw-clr` | RRTMG_LW column model, run_examples_std_atm case SAW-clr | 2 | raw bytes | PASS |
| `lw-trop-clr` | RRTMG_LW column model, run_examples_std_atm case TROP-clr | 2 | raw bytes | PASS |
| `sw-mls-cld5-imca1-icld2` | RRTMG_SW column model, run_examples_std_atm case MLS-cld5-imca1-icld2 | 2 | raw bytes | PASS |
| `sw-mls-cld6-imca0-icld2` | RRTMG_SW column model, run_examples_std_atm case MLS-cld6-imca0-icld2 | 2 | raw bytes | PASS |
| `sw-mls-cld7-imca1-icld2` | RRTMG_SW column model, run_examples_std_atm case MLS-cld7-imca1-icld2 | 2 | raw bytes | PASS |
| `sw-mls-cld7-imca1-icld5-idcor0` | RRTMG_SW column model, run_examples_std_atm case MLS-cld7-imca1-icld5-idcor0 | 2 | raw bytes | PASS |
| `sw-mls-cld7-imca1-icld5-idcor1` | RRTMG_SW column model, run_examples_std_atm case MLS-cld7-imca1-icld5-idcor1 | 2 | raw bytes | PASS |
| `sw-mls-clr` | RRTMG_SW column model, run_examples_std_atm case MLS-clr | 2 | raw bytes | PASS |
| `sw-mls-clr-aer12` | RRTMG_SW column model, run_examples_std_atm case MLS-clr-aer12 | 2 | raw bytes | PASS |
| `sw-mls-clr-sza45-isolvar0-tsi-avg` | RRTMG_SW column model, run_examples_std_atm case MLS-clr-sza45-isolvar0_tsi_avg | 2 | raw bytes | PASS |
| `sw-mls-clr-sza45-isolvar1-tsi-max` | RRTMG_SW column model, run_examples_std_atm case MLS-clr-sza45-isolvar1_tsi_max | 2 | raw bytes | PASS |
| `sw-mls-clr-sza45-isolvar1-tsi-min` | RRTMG_SW column model, run_examples_std_atm case MLS-clr-sza45-isolvar1_tsi_min | 2 | raw bytes | PASS |
| `sw-mls-clr-sza45-isolvar2-01jan1950` | RRTMG_SW column model, run_examples_std_atm case MLS-clr-sza45-isolvar2_01Jan1950 | 2 | raw bytes | PASS |
| `sw-mls-clr-sza45-isolvar3-bndscl-tsi-max` | RRTMG_SW column model, run_examples_std_atm case MLS-clr-sza45-isolvar3_bndscl_tsi_max | 2 | raw bytes | PASS |
| `sw-mls-clr-sza65` | RRTMG_SW column model, run_examples_std_atm case MLS-clr-sza65 | 2 | raw bytes | PASS |
| `sw-mlw-clr` | RRTMG_SW column model, run_examples_std_atm case MLW-clr | 2 | raw bytes | PASS |
| `sw-saw-clr` | RRTMG_SW column model, run_examples_std_atm case SAW-clr | 2 | raw bytes | PASS |
| `sw-trop-clr` | RRTMG_SW column model, run_examples_std_atm case TROP-clr | 2 | raw bytes | PASS |

Each case's benchmark file (`benchmarks/<case>.yaml`) gives the benchmark, the build and run commands, the environment, the translation plan (delegated, inside-NumPy and kept-Fortran subprograms) and the accepted runs; `evidence/.../report.txt` gives every compared file's digests for both programs.

## What a PASS claims

In the stated environment, the translated program run on this benchmark case produces the same set of output files as the original Fortran program, and every compared file has the same digest: of its bytes, or of its text after the stated masks (dates, timers, host names), or of a fixed-format dump of its numeric values. Wall times are reported and never gate.

It does not claim anything about other inputs or cases, other compilers or machines, code the benchmark does not reach, or the project's shipped reference outputs (the reference is the original program in the same environment).

## Uninitialised heap reads

The original Fortran program reads heap memory it never assigned in `lw-mls-cld5-imca0-icld2`, so its own output depends on the heap's contents. These cases are run with the heap zero-filled on both sides (`MALLOC_PERTURB_=255 GLIBC_TUNABLES=glibc.malloc.tcache_count=0`), which defines the values read as zero, as the translation does; the setting is part of each case's environment.
