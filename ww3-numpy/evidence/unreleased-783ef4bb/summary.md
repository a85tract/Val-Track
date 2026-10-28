# Acceptance record — ww3-numpy unreleased-783ef4bb

| | |
|---|---|
| Artifact | `https://github.com/a85tract/RecastEngine-Pro` @ `783ef4bb` |
| Reference | WAVEWATCH III, a0eaffebde6246e096f240509c9acf159fe09003 |
| Val-Track | unreleased-53515314 (`53515314`) |
| Machine | Alpine (CU Boulder Research Computing), Linux el8_10 x86_64 |
| Compiler | _not captured_ |
| Cases | 1 |
| Result | **PASS** |
| Security gate | NOT_RUN |
| Evidence class | reconstructed |
| Validated | 2026-10-05T06:26:32Z |

## Cases

### ww3 — PASS

Criteria: `ww3-numpy/benchmarks/ww3.yaml` (output-verdict)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `run_set_equal` | yes | yes | 3 runs, as the benchmark names them |
| `runs_identical` | yes | yes | 3 of 3 runs identical (16 output files compared) |
