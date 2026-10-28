# carma-numpy — 1 output-verdict benchmark

Backfilled from the wave24 application validation of RecastEngine-Pro `783ef4b` (`tools/backfill_wave24.py`). The case kit compared the native program with the same driver running the translated NumPy, in situ; only its verifier's per-run verdicts survive, so every record here is `reconstructed`.

| id | what it covers | runs | reference |
|---|---|---|---|
| `carma` | the CARMA test programs | 33 (ordinary_overlap_diagnostic 6, primary 27) | CARMA `26b30b2` |

**Which run gates.** For GROWCLRTEST, GROWINTEST, GROWSUBTEST, GROWTEST, NUCTEST and PHEATTEST the gated run is the zero-heap one (malloc zero-filled in both processes), as the table selects it. The default-allocator runs of those tests are the ordinary_overlap_diagnostic rows, and GROWTEST and PHEATTEST differ there - the same undefined-storage reading that keeps RRTMG's MLS-cld5-imca0-icld2 failing, where the table selected the default-allocator run instead.
