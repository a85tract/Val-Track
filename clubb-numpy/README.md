# clubb-numpy — 2 output-verdict benchmarks

Backfilled from the wave24 application validation of RecastEngine-Pro `783ef4b` (`tools/backfill_wave24.py`). The case kit compared the native program with the same driver running the translated NumPy, in situ; only its verifier's per-run verdicts survive, so every record here is `reconstructed`.

| id | what it covers | runs | reference |
|---|---|---|---|
| `replay` | independent replay of 150 recorded calls over eight trajectories | 8 (primary 8) | CLUBB_core, larson-group/clubb_release `8ab3902` |
| `feedback` | recorded-driver-input state feedback over seven configurations, 8,730 steps | 7 (primary 7) | CLUBB_core, larson-group/clubb_release `8ab3902` |
