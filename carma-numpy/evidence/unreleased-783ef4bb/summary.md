# Acceptance record — carma-numpy unreleased-783ef4bb

| | |
|---|---|
| Artifact | `https://github.com/a85tract/RecastEngine-Pro` @ `783ef4bb` |
| Reference | CARMA, 26b30b2738566de5d3979c1b2ccf191dd78c1207 |
| Val-Track | unreleased-53515314 (`53515314`) |
| Machine | Alpine (CU Boulder Research Computing), Linux el8_10 x86_64 |
| Compiler | _not captured_ |
| Cases | 1 |
| Result | **PASS** |
| Security gate | NOT_RUN |
| Evidence class | reconstructed |
| Validated | 2026-10-05T06:26:32Z |

## Cases

### carma — PASS

Criteria: `carma-numpy/benchmarks/carma.yaml` (output-verdict)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `run_set_equal` | yes | yes | 33 runs, as the benchmark names them |
| `runs_identical` | yes | yes | 27 of 27 runs identical (56 output files compared) |
| `runs_identical` | no | no | 4 of 6 runs identical (12 output files compared); differ: GROWTEST [ordinary_overlap_diagnostic] (False), PHEATTEST [ordinary_overlap_diagnostic] (False) |
