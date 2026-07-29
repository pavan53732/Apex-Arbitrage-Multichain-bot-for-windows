---
type: NOTICE
owner: Governance Platform
status: Active
version: 1.0.0
purpose: Disambiguate historical vs. current WS0 evidence after ADR-0011.
---

# Historical Evidence Notice

ADR-0011 (`.governance/programme_2.5/phase_0.75/adr_0011_ws0_verification_layer.md`)
removed WS0's independent test-harness runtime (`test_harness.py`,
`loader/fixture_loader.py`, `generator/golden_generator.py`,
`comparator/golden_comparator.py`, `dashboard/test_dashboard.py`). That
runtime no longer exists anywhere in this repository.

The following files in this directory were produced by that **removed**
runtime, before ADR-0011, and are **not reproducible today** because the
code that generated them has been deleted:

| File | Status |
|---|---|
| `determinism_report.json` | Historical (pre-refactor WS0 harness, 100 runs) |
| `corruption_report.json` | Historical (pre-refactor WS0 harness, 10 injected-corruption cases) |
| `evidence_report.json` | Historical (pre-refactor WS0 harness, single evidence record) |
| `dashboard.json` | Historical (pre-refactor WS0 harness dashboard render) |

They are retained for historical/audit-trail purposes only. **They must
never be cited as current evidence of platform correctness**, and they
must never be used to support a certification decision about the
present state of the repository (current HEAD or later).

Three additional files that were also produced by the pre-refactor
harness -- `fuzz_report.json`, `stress_report.json`,
`fresh_clone_report.json` -- were found during the Programme 2.5 Final
Certification Audit (commit `3b1240164`) to contain suspiciously
formulaic/idealized figures with no corresponding executable code
capable of reproducing them (e.g. `fuzz_report.json` claimed
`"mutations": 10000, "crashes": 0, "deterministic_failures": 10000,
"status": "PASS"` with zero fuzzing code anywhere in the repository).
Those three have been moved to
`.governance/archive/pre-consolidation-2026-07-29/ws0-stale-2026-07-29/`
rather than left in this directory, since -- unlike the four files
above -- there is no confidence they reflect real historical
measurements at all, as opposed to plausible-looking placeholder data.

`determinism_report_post_refactor.json` and `baseline_output.json` in
this directory ARE current: they are produced by the live
`WS0VerificationLayer`, which invokes the canonical
`tools/governance/` runtime exclusively (per ADR-0011), and are
refreshed by re-running that layer.

## What "current" evidence looks like

For a certification claim to be trustworthy today, it must be traceable
to one of:
- A live `apex-gov <command>` execution against the commit being
  certified (see `tools/governance/cli/main.py`).
- `tools/governance/evidence/evidence_engine.py`'s `EvidenceEngine`.
- `tools/governance/freeze/freeze_engine.py`'s `FreezeEngine`.
- `tools/governance/tests/` (pytest) or `architecture-tests/*.py`,
  executed directly.

Anything else -- including everything in this directory dated before
this notice -- should be treated as historical record only.
