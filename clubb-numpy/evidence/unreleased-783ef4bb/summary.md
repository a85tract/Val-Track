# Acceptance record — clubb-numpy unreleased-783ef4bb

| | |
|---|---|
| Artifact | `https://github.com/a85tract/RecastEngine-Pro` @ `783ef4bb` |
| Reference | CLUBB_core, larson-group/clubb_release, 8ab3902e812c2883976b4f1f57c085d682666d92 |
| Val-Track | unreleased-53515314 (`53515314`) |
| Machine | Linux workstation (host not recorded) |
| Compiler | _not captured_ |
| Cases | 2 |
| Result | **PASS** |
| Security gate | NOT_RUN |
| Evidence class | reconstructed |
| Validated | 2026-10-07T23:55:48Z |

## Cases

### replay — PASS

Criteria: `clubb-numpy/benchmarks/replay.yaml` (output-verdict)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `run_set_equal` | yes | yes | 8 runs, as the benchmark names them |
| `runs_identical` | yes | yes | 8 of 8 runs identical |

### feedback — PASS

Criteria: `clubb-numpy/benchmarks/feedback.yaml` (output-verdict)

| Check | Gating | Passed | Detail |
|---|---|---|---|
| `run_set_equal` | yes | yes | 7 runs, as the benchmark names them |
| `runs_identical` | yes | yes | 7 of 7 runs identical |
