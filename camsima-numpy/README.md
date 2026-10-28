# camsima-numpy — 3 output-verdict benchmarks

Backfilled from the wave24 application validation of RecastEngine-Pro `783ef4b` (`tools/backfill_wave24.py`). The case kit compared the native program with the same driver running the translated NumPy, in situ; only its verifier's per-run verdicts survive, so every record here is `reconstructed`.

| id | what it covers | runs | reference |
|---|---|---|---|
| `kessler` | CAM-SIMA with Kessler physics, outfrq test | 1 (primary 1) | CAM-SIMA (Kessler) `47e1e63` |
| `held-suarez` | CAM-SIMA with Held-Suarez forcing, outfrq test | 1 (primary 1) | CAM-SIMA (Held-Suarez) `47e1e63` |
| `tj2016` | CAM-SIMA with TJ2016 physics, before and after the coupler | 2 (primary 2) | CAM-SIMA (TJ2016) `47e1e63` |
