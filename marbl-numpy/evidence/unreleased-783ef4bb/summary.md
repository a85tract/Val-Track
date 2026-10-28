# Acceptance record — marbl-numpy unreleased-783ef4bb

| | |
|---|---|
| Artifact | `https://github.com/a85tract/RecastEngine-Pro` @ `783ef4bb` |
| Reference | MARBL, 6b2a5e41dc5b0faaf9b600c96432e2487515e878 |
| Val-Track | unreleased-53515314 (`53515314`) |
| Machine | Alpine (CU Boulder Research Computing), Linux el8_10 x86_64 |
| Compiler | _not captured_ |
| Cases | 1 |
| Result | **PASS** |
| Security gate | NOT_RUN |
| Evidence class | reconstructed |
| Validated | 2026-10-05T05:25:48Z |

## Cases

### marbl — PASS

Criteria: `marbl-numpy/benchmarks/marbl.yaml` (output-verdict)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `run_set_equal` | yes | yes | 2 runs, as the benchmark names them |
| `runs_identical` | yes | yes | 2 of 2 runs identical (3 output files compared) |
