---
type: REPORT
owner: Governance Platform
status: Active
version: 1.0.0
purpose: Record the governance-reconciliation work performed in response to the Programme 2.5 Final Certification Audit (commit 3b1240164), and the resulting, still-NOT-CERTIFIED state.
canonical_source: .governance/programme_2.5/_reconciliation/RECONCILIATION-REPORT.md
---

# Programme 2.5 Governance Reconciliation Report

**Base commit audited and reconciled against: `3b1240164b08e17037f765034409450247b2c314`.**
**This work was performed from a fresh clone, with all figures live-executed, not asserted.**

## Why this exists

The Programme 2.5 Final Certification Audit delivered **NOT CERTIFIED**
against commit `3b1240164`, citing (among other things) that the
governance platform's own self-description was inconsistent with its
actual implementation state: every WS1-WS9 manifest still read
`PENDING` despite real, tested engineering work having occurred; the
WS0 certification report was 10 commits stale and referenced a foreign
sandbox path; three WS0 evidence files were confirmed fabricated
(no code capable of producing them exists). The reviewer's assessment
was that the remaining work is governance reconciliation, not more
engineering, plus a decision on whether Programme 2.5's frozen Phase-0
specification should be implemented as written or formally revised.

This report records what reconciliation work was actually done, with
evidence, and states plainly that **Programme 2.5 remains NOT
CERTIFIED** afterward -- reconciling the paperwork does not by itself
close the specification-vs-implementation gap.

## What was done (all live-executed against a fresh clone)

### 1. WS1-WS9 manifests regenerated from live evidence

Built `.governance/programme_2.5/_reconciliation/verify_workstreams.py`
-- a script that checks every individual item in
`readiness_checklist.json`'s WS1-WS9 checklists against real, executed
code (imports, `hasattr` checks, live CLI invocations, grep of source,
file-existence checks) and reports PASS/FAIL per item with a factual
detail string, never an assertion without a corresponding check.

Built `.governance/programme_2.5/_reconciliation/generate_manifests.py`
to turn that evidence into each `ws{1-9}/manifest.json`, classified as:
- `NOT_STARTED` (0 passing items)
- `PARTIALLY_IMPLEMENTED` (some but not all items passing)
- `IMPLEMENTED` (all items passing)

**Result: every one of WS1-WS9 is `PARTIALLY_IMPLEMENTED`. None is
`IMPLEMENTED`, none is `NOT_STARTED`.**

| Workstream | Passing | Status |
|---|---|---|
| WS1 Root Detection Engine | 4/8 | PARTIALLY_IMPLEMENTED |
| WS2 Closure Engine | 3/10 | PARTIALLY_IMPLEMENTED |
| WS3 Validator Framework | 2/4 | PARTIALLY_IMPLEMENTED |
| WS4 Knowledge Graph | 1/4 | PARTIALLY_IMPLEMENTED |
| WS5 Database Consolidation | 3/6 | PARTIALLY_IMPLEMENTED |
| WS6 Freeze Framework | 1/4 | PARTIALLY_IMPLEMENTED |
| WS7 Evidence System | 1/4 | PARTIALLY_IMPLEMENTED |
| WS8 Metrics Engine | 3/5 | PARTIALLY_IMPLEMENTED |
| WS9 Integrity Engine | 4/5 | PARTIALLY_IMPLEMENTED |

Full itemized evidence is in each `ws{N}/manifest.json`'s
`checklist_evidence` array, and rolled up in
`.governance/programme_2.5/WORKSTREAM-STATUS-ROLLUP.json`.
`readiness_checklist.json` was updated to reference the same evidence
rather than its own frozen-at-inception `PENDING` values.

This directly resolves CRITICAL-1 from the audit ("governance layer
cannot accurately describe itself") -- it can now, and will continue
to as long as `verify_workstreams.py` + `generate_manifests.py` are
re-run after future changes. **It does not mean the workstreams are
complete.**

### 2. WS0 certification artefacts regenerated against current HEAD

The stale `ws0_certification_report.json` (certified against
`d31492021`, 10 commits behind) and `ws0_certification_package.json`
(referencing `/home/user/apex_repo/...`, a foreign sandbox path) were
archived to
`.governance/archive/pre-consolidation-2026-07-29/ws0-stale-2026-07-29/`
and replaced with versions freshly computed live against
`3b1240164` (same commit as this reconciliation), including:
- Live `apex-gov run` output
- Live `python -m pytest tools/governance/tests/` result (46 passed)
- Live execution of all 5 `architecture-tests/*.py` scripts (all PASS)
- Live `apex-gov integrity` result
- The WS1-WS9 rollup from item 1

A genuine defect was found and fixed while doing this: WS0's stored
regression baseline (`reports/baseline_output.json`) predated the
identifier-normalization fix from a prior remediation round, so
`WS0VerificationLayer.run_regression_check()` was reporting **FAIL**
for what were actually correctness improvements (`validation_findings`
2065 -> 22, a bug-fix, not a regression). The stale baseline was
archived with an explanation
(`.governance/archive/.../baseline_output_pre_identifier_normalization_fix.json`)
and replaced with a freshly computed one, after which the regression
check correctly reports PASS with zero diffs.

**Important scope boundary, made explicit in the new report:** this
WS0-layer "PASS" means only that the canonical governance runtime
executes correctly, deterministically, and without regressing its own
baseline -- exactly what the original audit demanded be disambiguated
("Determine whether PASS means 'validator executed' or 'repository
passed validation'"). It is **not** a Programme 2.5 certification.
The new `ws0_certification_report.json`'s top-level
`certification_decision` field is literally named
`WS0_LAYER_PASS_PROGRAMME_NOT_CERTIFIED` to make this unambiguous in
the artifact itself, not just in prose around it.

This resolves CRITICAL-2 and part of CRITICAL-3.

### 3. Fabricated evidence retracted, not silently left in place

`fuzz_report.json`, `stress_report.json`, `fresh_clone_report.json`
(confirmed fabricated -- no code exists capable of producing their
suspiciously round figures) were moved to the same archive directory
with `_fabricated_fd784cf58` suffixes identifying the commit that
introduced them.

The four files that ARE real historical evidence from the
now-deleted pre-ADR-0011 WS0 test harness (`determinism_report.json`,
`corruption_report.json`, `evidence_report.json`, `dashboard.json`)
were left in place but a new
`ws0/reports/HISTORICAL-EVIDENCE-NOTICE.md` was added explicitly
labeling them as non-reproducible historical record, never to be
cited as current evidence -- this satisfies the audit's requirement
("Historical evidence should either be archived, clearly marked as
historical, or regenerated") without destroying an audit trail.

This resolves CRITICAL-3.

### 4. Specification-vs-implementation fork: proposed, not resolved unilaterally

Per the user's own framing -- "If the implementation intentionally
evolved away from the original frozen specification, the correct
governance action is to update the specification through the
project's change-control process, not to silently certify against a
specification that no longer matches reality" -- this agent did
**not** unilaterally edit any frozen `phase_0/*.json` file. Instead,
`.governance/programme_2.5/phase_0.75/adr_0012_phase0_specification_revision_PROPOSED.md`
was authored with `status: Proposed`, itemizing all 5 diverged
specifications (root taxonomy, validator catalogue, graph
specification, metrics specification, freeze/evidence structure),
their as-implemented alternative, and an explicit recommendation
(Option B: revise) with reasoning -- but it requires human
ratification (`status: Proposed` -> `Accepted`) before it takes
effect. Until ratified, the original frozen specifications remain
system-of-record and the gaps remain uncertified gaps, not accepted
scope reductions.

This directly addresses HIGH-severity findings 1-6 from the audit by
giving them a concrete, actionable governance path, without
overstepping into a decision that is the user's to make.

## What was explicitly NOT done (and why)

- **No implementation of the missing Phase-0 spec items** (6-tier
  roots, 5 more validator categories, 6 more graphs, 9 more metrics,
  5 more Freeze* classes, 10-directory evidence layout). Per the
  user's own instruction, this would be "more engineering," not
  reconciliation, and its scope depends on the ADR-0012 ratification
  decision.
- **CORE_ROOTS/EXCLUDED_PATTERNS contradictions (3), 8 false-negative
  roots, PROGRAMME-3-CLOSURE-ORCHESTRATOR.md's anomalous root
  classification, test coverage gaps (58%), no CI/CD** -- all
  confirmed still present via this session's independent
  `apex-gov run` + `pytest --cov` execution. These are genuine
  implementation bugs (not spec-vs-implementation forks) and are
  explicitly flagged in ADR-0012 as NOT proposed for descope --
  they remain open defects requiring a future remediation round.
- **Programme 2.5 has not been marked CERTIFIED.** Reconciling
  governance paperwork to be honest is a precondition for
  certification, not a substitute for it.

## Current, honestly-stated certification status

**Programme 2.5: NOT CERTIFIED.**
**WS1 approval: NOT GRANTED.**

Reasons unchanged from the original audit except where explicitly
resolved above:
- Governance self-description: **RESOLVED** (manifests now accurate).
- WS0 certification staleness: **RESOLVED** (regenerated at current HEAD, scope disambiguated).
- Fabricated/stale evidence: **RESOLVED** (retracted/archived/labeled).
- Specification-vs-implementation gap: **PROPOSED PATH, NOT RATIFIED** -- still blocks certification either way (whether resolved via full implementation or via ADR-0012 ratification, neither has happened yet).
- Known implementation bugs (CORE_ROOTS contradictions, false-negative roots, anomalous root classification, 58% coverage, no CI): **UNCHANGED, UNFIXED.**

## Reproducing this work

```
git clone <repo> && cd <repo>
python3 -m venv venv && source venv/bin/activate
pip install -e tools/governance && pip install pytest pytest-cov
python .governance/programme_2.5/_reconciliation/verify_workstreams.py .
python .governance/programme_2.5/_reconciliation/generate_manifests.py
```
