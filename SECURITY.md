# Security

Val-Track holds acceptance records, not security tooling. The Cyber gate that
produces each record's `security` block is RecastEngine's `audit` recipe (and
recast-cesm's `audit-cesm`, which adds the LLM audit and sanitizer planes); its
security model, trust boundaries and fail-closed contract are the engine's
`SECURITY.md` and `docs/cyber-gate.md`. The scripts that used to live here were
deleted in step 9e of `docs/CORRECTNESS-ORGANIZATION.md`.

## What this repository holds

A record's `security` block carries the gate's states and counts for one
commit, never a finding. Findings stay in the engine's store
(`RECAST_FINDINGS_HOME`) and reach Sec-Track only after adjudication and a
human's disclosure decision; none of that passes through here. Do not add a
finding, a scanner report, or anything that identifies an undisclosed
vulnerability to an acceptance record, a benchmark, or a pull request.

## Disclosure

Report a defect in this repository's tools (`correctness/`, `schemas/`, the
workflows under `.github/`) privately to the repository owner. Report a defect
in the gate itself the same way, to the engine's owner. Do not include live
credentials or undisclosed exploit material in an issue.
