# rrtmg-numpy — 1 output-verdict benchmark

Backfilled from the wave24 application validation of RecastEngine-Pro `783ef4b` (`tools/backfill_wave24.py`). The case kit compared the native program with the same driver running the translated NumPy, in situ; only its verifier's per-run verdicts survive, so every record here is `reconstructed`.

| id | what it covers | runs | reference |
|---|---|---|---|
| `rrtmg` | the RRTMG LW and SW benchmark configurations, outermost plan | 44 (primary 30, zero_heap_diagnostic 14) | RRTMG (LW, SW) `958edb1` |

**One gated run differs.** LW MLS-cld5-imca0-icld2 differs by one value (max abs 1.0e-07) under the default allocator: the native program reads undefined heap storage. Under zero-filled malloc all 14 LW configurations are byte-identical (the zero_heap_diagnostic runs; OOPSLA2027_evidence wave24/rrtmg_initialization). The run stays gated: ungating it is a maintainer's decision, not something a backfill does.
