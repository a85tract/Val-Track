# Acceptance record — mfc-numpy unreleased-783ef4bb

| | |
|---|---|
| Artifact | `https://github.com/a85tract/RecastEngine-Pro` @ `783ef4bb` |
| Reference | MFC, 1ececa3456a5ee57807327a4deebacdd723d0fa6 |
| Val-Track | unreleased-53515314 (`53515314`) |
| Machine | Alpine (CU Boulder Research Computing), Linux el8_10 x86_64 |
| Compiler | gfortran 14.2.0 (/curc/sw/install/gcc/14.2.0) |
| Cases | 1 |
| Result | **PASS** |
| Security gate | NOT_RUN |
| Evidence class | reconstructed |
| Validated | 2026-10-05T05:01:39Z |

## Cases

### mfc — PASS

Criteria: `mfc-numpy/benchmarks/mfc.yaml` (output-verdict)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `run_set_equal` | yes | yes | 9 runs, as the benchmark names them |
| `runs_identical` | yes | yes | 9 of 9 runs identical (270 output files compared) |
