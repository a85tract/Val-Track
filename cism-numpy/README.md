# cism-numpy — 1 output-verdict benchmark

Backfilled from the wave24 application validation of RecastEngine-Pro `783ef4b` (`tools/backfill_wave24.py`). The case kit compared the native program with the same driver running the translated NumPy, in situ; only its verifier's per-run verdicts survive, so every record here is `reconstructed`.

| id | what it covers | runs | reference |
|---|---|---|---|
| `cism` | halfar-HO t5 with the merged plan, its restart, and the t0/t1 short runs | 4 (primary 1, restart_output 1, short_run_diagnostic 2) | CISM `46e27de` |
