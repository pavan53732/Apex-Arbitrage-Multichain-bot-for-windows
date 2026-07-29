---
type: ADR
owner: Governance Platform
status: Proposed
version: 0.1.0
purpose: Propose formal revision of five Phase-0-frozen specifications that have diverged from the implemented governance platform.
canonical_source: .governance/programme_2.5/phase_0.75/adr_0012_phase0_specification_revision_PROPOSED.md
---

# ADR-0012 (PROPOSED, NOT RATIFIED): Phase-0 Specification Revision

**Status: PROPOSED.** This ADR has not been accepted. Per
`execution_plan.json`'s own `specification_drift_policy` ("If
implementation reveals incorrect specification, implementation must
stop. Change must be proposed through new ADR and specification
update. Only after specification update may implementation continue."),
this document is the required proposal step. It requires explicit
human ratification (status -> Accepted) before:
(a) any of the frozen `phase_0/*.json` files are edited, or
(b) Programme 2.5 is certified against the revised scope instead of
the original one.

Until ratified, the frozen `phase_0/` specifications remain the
system of record, and the gaps documented in
`.governance/programme_2.5/WORKSTREAM-STATUS-ROLLUP.json` remain
uncertified gaps -- not accepted scope reductions.

## Context

The Programme 2.5 Final Certification Audit (commit `3b1240164`) found
five Phase-0-frozen specifications that the live implementation does
not, and per current evidence will not soon, fully satisfy:

1. `root_taxonomy.json` -- freezes 6 tiers (Platform/Kernel/Runtime/
   Subsystem/Integration/UI Root) + Registry/Reference/Guide/ADR.
   `BehaviouralRootDetector` implements a flat boolean
   (root / not-root), with no tier concept whatsoever.
2. `validator_catalogue.json` -- freezes 14 validator IDs in a
   `<CATEGORY>-<NNN>` naming scheme (`OWNERSHIP-001`, `EVENT-002`, ...)
   organized into `validator/<category>/` subdirectories.
   The implemented `validator/registry.py` catalogues 9 IDs in a
   `<module>.<function>` naming scheme, as flat files with no category
   subdirectories.
3. `graph_specification.json` -- freezes 14 graphs including
   `service_graph`, `plugin_graph`, `runtime_graph`, `security_graph`,
   `recovery_graph`, `validation_graph`, `algorithm_graph`.
   The implemented `GraphBuilder` produces 8 graphs; the additional 6
   have no corresponding parseable document metadata fields anywhere
   in the 277-document corpus.
4. `metrics_specification.json` -- freezes 10 named ratio metrics.
   The implemented `CompletenessEngine` computes exactly 1
   (`avg_completeness`); `MetricsDashboard` is an unimplemented stub.
5. `readiness_checklist.json` CHECK-WS6/CHECK-WS7 -- freeze 6
   `Freeze*` classes and 10 structured evidence subdirectories.
   The implementation has 1 live `Freeze*` class (`FreezeRecord`) and
   a single flat, overwritten-in-place evidence file.

These are not implementation bugs (the code that exists is
deterministic, tested, and correctly executes what it claims to do).
They are a genuine divergence between an early, aspirational
architecture freeze and what nine iterative remediation rounds
actually built and validated against a real 277-document,
zero-trading-code repository.

## Options considered

**Option A -- Implement Phase-0 as written.** Build the missing 6
root tiers, 5 additional validator categories + directory
restructure, 6 additional graphs (3 of which -- security, recovery,
validation -- may be able to source from existing front-matter
fields; 3 -- service, plugin, runtime -- likely require new document
metadata fields that don't exist in the corpus today), 9 additional
metrics, 5 additional Freeze* classes, and a 10-directory evidence
layout. This is substantial net-new engineering (estimated: comparable
in scope to the 9 remediation rounds already completed this session),
much of it against document metadata that doesn't exist yet in the
277-document corpus (e.g. no document has `security_contracts`,
`interfaces` used consistently enough to justify a `security_graph`
today).

**Option B -- Revise the specification via this ADR.** Formally
descope each of the 5 items to match what has been built and
validated, explicitly re-baselining Programme 2.5's acceptance
criteria, while recording the descoped items as backlog for a future
Programme (not silently dropped).

## Recommendation (non-binding until ratified)

Option B, for the reasons the user asking for this ADR already
identified: "If the implementation intentionally evolved away from the
original frozen specification, the correct governance action is to
update the specification through the project's change-control process,
not to silently certify against a specification that no longer matches
reality." Attempting Option A now, against a repository that still has
**zero lines of actual trading/bot code**, risks over-investing in
governance-platform completeness for a system that doesn't exist yet
to be governed.

### Proposed revised scope, item by item

1. **Root taxonomy**: Revise to a single flat `BehaviouralRoot` concept
   (as implemented) for Programme 2.5. Tiering deferred to Programme 3+
   when there are enough real subsystems to make tiers meaningful
   (currently 28 roots against 0 lines of implementation code -- tier
   boundaries would be speculative).
2. **Validator catalogue**: Revise to the 9-ID `registry.py` catalogue
   (as implemented) as the Programme 2.5 baseline. The 14-ID
   `<CATEGORY>-<NNN>` catalogue is deferred to when Programme 3
   introduces actual runtime code needing category-specific validators
   (event/schema/interface validators are meaningless against docs
   that don't yet have real event/schema/interface implementations to
   validate).
3. **Graph specification**: Revise to the 8 graphs with genuine data
   support (as implemented). `event_graph`/`schema_graph` are kept in
   the frozen 8 but explicitly flagged NOT FUNCTIONALLY MET (0
   nodes/edges) until documents carry real `events_produced` /
   `schemas` data -- this is a data-completeness gap, not a spec
   gap, and is NOT proposed for descope. `service_graph`,
   `plugin_graph`, `runtime_graph`, `security_graph`, `recovery_graph`,
   `validation_graph`, `algorithm_graph` are deferred to Programme 3+.
4. **Metrics specification**: Revise to `avg_completeness` as the sole
   Programme 2.5 metric. The other 9 require the deferred graphs/
   validator categories above as inputs and cannot be honestly
   computed before those exist.
5. **Freeze/Evidence structure**: Revise to the single live
   `FreezeRecord`/`FreezeEngine` and single evidence-file model (as
   implemented) for Programme 2.5. Multi-class freeze history,
   tamper-evidence (signatures), and the 10-directory evidence
   taxonomy are deferred, explicitly flagged as needed BEFORE any
   Programme 2.5 evidence is treated as tamper-proof for compliance
   purposes (today it is not).

### What is explicitly NOT proposed for descope

- Determinism, single-canonical-runtime, single-canonical-database
  requirements: fully met, keep as-is.
- The 3 CORE_ROOTS/EXCLUDED_PATTERNS contradictions
  (SIMULATION-ENGINE.md, WORKER-POOL.md, SERVICE-REGISTRY.md): these
  are implementation bugs, not spec gaps -- must be fixed, not
  descoped.
- The 8 false-negative behavioural roots: same -- implementation bugs.
- `apex-gov validate` exit-code correctness: fully met, keep as-is.
- Reverse closure: fully met, keep as-is.

## Consequences if ratified

- `phase_0/root_taxonomy.json`, `validator_catalogue.json`,
  `graph_specification.json`, `metrics_specification.json`,
  `readiness_checklist.json` CHECK-WS6/WS7 would be edited to reflect
  the revised scope, with a `superseded_by: ADR-0012` marker added to
  each, preserving the original frozen text for audit trail (not
  deleted).
- `WORKSTREAM-STATUS-ROLLUP.json` and each `ws{1-9}/manifest.json`
  would be re-run against the revised checklist, likely producing
  materially higher completion percentages -- but this must be an
  honest re-baseline, not a way to manufacture a passing grade: the
  implementation bugs listed above still block certification either
  way.
- A new Programme (3.x or a Programme 2.5 continuation) would need to
  be scoped for the deferred items, to be picked up once actual
  trading-bot implementation work creates real subsystems to govern.

## Consequences if NOT ratified (rejected)

- Programme 2.5 remains NOT CERTIFIED until Phase-0 is implemented as
  originally written (Option A), which is a substantially larger
  undertaking than the remediation already completed.

## Acceptance criteria (for ratification, not yet met)

- [ ] A human with authority over Programme 2.5 changes `status:
  Proposed` to `status: Accepted` in this file's front matter.
- [ ] Each of the 5 `phase_0/*.json` files is updated to reference this
  ADR and reflect the revised scope.
- [ ] `readiness_checklist.json` is regenerated against the revised
  scope.
- [ ] `WORKSTREAM-STATUS-ROLLUP.json` is regenerated and shows accurate
  completion against the *revised* checklist (not silently reused from
  before ratification).
