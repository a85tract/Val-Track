# cvmix-numpy — 1 output-verdict benchmark

Backfilled from the wave24 application validation of RecastEngine-Pro `783ef4b` (`tools/backfill_wave24.py`). The case kit compared the native program with the same driver running the translated NumPy, in situ; only its verifier's per-run verdicts survive, so every record here is `reconstructed`.

| id | what it covers | runs | reference |
|---|---|---|---|
| `cvmix` | four CVMix drivers, outermost plan | 4 (primary 4) | CVMix `fce4221` |
