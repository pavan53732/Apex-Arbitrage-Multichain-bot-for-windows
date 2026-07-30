---
type: REFERENCE
owner: Governance Platform
status: Canonical
version: 1.0.0
purpose: Formal, standalone certification decision for Programme 2.5 (Governance Platform Hardening, WS1-WS9), distinct from any chat-message report or descriptive execution_plan.json status string.
scope: Certification decision only. This document does not modify architecture; it records and evidences a decision about the state of already-completed work.
last_updated: 2026-07-30
canonical_source: .governance/programme_2.5/PROGRAMME-2.5-CERTIFICATION-DECISION.md
---

# Programme 2.5 Certification Decision

## Decision

**PROGRAMME 2.5 IS CERTIFIED.**

All 9 workstreams (WS1-WS9) are IMPLEMENTED. All 103 of 103 readiness-checklist
items pass. `apex-gov integrity` returns an unconditional 14/14 PASS. The full
governance test suite (238 tests) and all 5 legacy `architecture-tests/*.py`
scripts pass. Every figure in this document was reproduced independently in a
**genuinely fresh `git clone`** of the pushed remote (not the working copy
that authored the changes), in a fresh Python virtual environment, on
2026-07-30, immediately before this decision was written.

This certification supersedes the "IMPLEMENTED_PENDING_FINAL_CERTIFICATION"
status previously recorded in `execution_plan.json` and previously reported
only via chat. `execution_plan.json` is updated alongside this document to
read `"CERTIFIED"`.

## Certified Commit

| Field | Value |
|---|---|
| Certified commit | `7571a145a61a769e6fcb2448303b8a9f3d588144` |
| Branch | `main` |
| Immediately preceding substantive commit | `311a0b702f97a430a8b82acc87dcf6d6c4ecd972` (governance(WS4): wire 8 user-approved event-matrix subsystem name mappings) |
| Repository tree hash (freeze record) | `a153ec63535bb6eb2740d76bfe4bb7ffe7de6cf5` |
| Method | Independent fresh `git clone` of `https://github.com/pavan53732/Apex-Arbitrage-Multichain-bot-for-windows` at this commit, into a scratch directory with no relationship to the working copy that produced the commits, with a freshly created Python venv (`pip install -e tools/governance`), confirmed via `python -c "import governance; print(governance.__file__)"` resolving inside the fresh clone before any check was trusted. |

## 1. Workstream Status (fresh-clone reproduced)

| Workstream | Status | Passing | Total |
|---|---|---|---|
| WS1 — Root Detection Engine | IMPLEMENTED | 8 | 8 |
| WS2 — Closure Artefacts | IMPLEMENTED | 10 | 10 |
| WS3 — Category Validators | IMPLEMENTED | 17 | 17 |
| WS4 — Knowledge Graph | IMPLEMENTED | 16 | 16 |
| WS5 — Database Schema | IMPLEMENTED | 9 | 9 |
| WS6 — Freeze / Tamper-Evidence | IMPLEMENTED | 9 | 9 |
| WS7 — Evidence Store | IMPLEMENTED | 13 | 13 |
| WS8 — Metrics | IMPLEMENTED | 7 | 7 |
| WS9 — Integrity Engine | IMPLEMENTED | 14 | 14 |
| **Total** | **ALL 9 IMPLEMENTED** | **103** | **103** |

Source: `.governance/programme_2.5/WORKSTREAM-STATUS-ROLLUP.json`, regenerated
by `.governance/programme_2.5/_reconciliation/generate_manifests.py` inside
the fresh clone at commit `7571a145a`, identical to the working-copy result.

## 2. Canonical Pipeline Output (`apex-gov run`, fresh clone)

| Field | Value |
|---|---|
| `documents_indexed` | 277 |
| `behavioural_roots` | 35 |
| `validation_findings` | 22 |
| `closures_computed` | 35 |
| `avg_completeness` | 0.2234985231375123 |
| `graph_nodes` | 281 |
| `graph_edges` | 878 |
| `database_schema_version` | 1 |
| `closure_artefacts_written` | 175 (35 roots x 5 artefacts each) |
| `category_validators_executed` | 14 |
| `category_validator_findings` | 72 |
| `event_graph_edges_resolved` | 102 |
| `event_graph_names_unresolved` | 13 |
| `schema_graph_references_resolved` | 18 |

These numbers were produced twice independently (working copy and fresh
clone) and matched byte-for-byte on every numeric field, confirming the
pipeline is deterministic across environments, not just across repeated runs
in the same checkout.

## 3. Integrity Check (`apex-gov integrity`, fresh clone)

| Check | Result |
|---|---|
| configuration | PASS |
| database | PASS |
| graphs | PASS |
| runtime | PASS |
| roots | PASS |
| closures | PASS |
| validators | PASS |
| ownership | PASS |
| cross_references | PASS |
| freeze | PASS |
| evidence | PASS |
| metrics | PASS |
| repository | PASS |
| work_queue | PASS |

**14/14 PASS, `failed_checks: []`.** This is the full set of integrity checks
defined by WS9 (grew from 13 to 14 during this programme with the addition
of `work_queue`).

## 4. Test Suite (fresh clone)

| Suite | Result |
|---|---|
| `tools/governance/tests/` (pytest) | **238/238 PASS** |
| `architecture-tests/audit_duplicates.py` | PASS — no duplicates or conflicts detected |
| `architecture-tests/validate_contracts.py` | PASS — all `[CONTRACT]` documents pass 7/7 structural compliance |
| `architecture-tests/validate_cross_references.py` | PASS — all 240 docs checked, 0 broken references |
| `architecture-tests/validate_ownership.py` | PASS — no ownership conflicts, all key documents registered |
| `architecture-tests/validate_traceability.py` | PASS |

## 5. Tamper-Evidence Verification (Ed25519, fresh clone, independently re-verified)

The freeze record's Ed25519 signature was independently re-verified in the
fresh clone using **only the committed public key**
(`.governance/freeze/signing_public_key.pem`); the private key
(`.governance/freeze/.signing_key`, git-ignored by design) is genuinely absent
from this clone, confirming the signature does not depend on any
clone-specific secret:

```
signature valid (fresh clone, public key only, no private key present): True
private key exists in this fresh clone: False
```

Additionally, running the full test suite and `apex-gov run`/`integrity`/
manifest-regeneration inside the fresh clone did **not** alter the committed
public key file (`md5sum` identical before and after: `fc35a046374317f76bdc59d34fb24166`),
confirming the earlier-discovered key-corruption defect (see WS6 fix #2 in
commit `1cd232fb7`) remains fixed under this fresh-clone re-verification.

## 6. Determinism

`apex-gov run` was executed independently in both the working copy and a
fresh clone of the identical commit; every field of `canonical_output` in
section 2 above matched exactly. This is consistent with prior determinism
fixes made earlier in the programme (closure work-queue tie-breaking,
`nx.DiGraph.subgraph()` non-determinism, unsorted DB upserts, wall-clock
timestamps in content-hashed rows) continuing to hold.

## 7. WS4 Event-Matrix Ambiguous-Mapping Decision (closed 2026-07-30)

Per explicit prior instruction, ambiguous event-matrix subsystem-name
mappings were never auto-wired; a full reviewable mapping table was produced
instead (`.governance/programme_2.5/_reconciliation/EVENT-MATRIX-UNRESOLVED-NAMES-REVIEW.md`).
Of 39 distinct subsystem names:

- **27 of 39 now resolve** to real documents: 13 by deterministic filename
  transform, 14 by hand-reviewed manual override (6 original + 8 explicitly
  approved by the user on 2026-07-30: Chain Adapter, Config Manager, DEX
  Adapter, Health Checker, Monitoring, Notification, Secret Manager, Widget
  Manager).
- **13 of 39 remain permanently unresolved** — disclosed as limitations, not
  pending work — because they have zero plausible single-document candidate,
  are deliberately generic broadcast terms ("All Subsystems", "Any
  Subsystem"), or are genuinely multi-way ambiguous with no way to
  disambiguate without either authoring new documents or editing the source
  event table itself (Dashboard: 4 candidates; Portfolio: 2; Runtime: 3;
  Wallet: 2; plus AI Cost Manager, Audit, Error Handler, Memory, Plugin
  Executor, Security Enforcer, Self-Healer with zero candidates each).

This item is fully closed: every name has either a traceable, approved
resolution or a documented, permanent, non-guessed non-resolution. No
mapping was ever wired without an explicit human decision.

## 8. What This Certification Does NOT Cover

- This certifies **Programme 2.5 only** — the governance tooling that audits
  and tracks the specification corpus for the future Windows multichain
  arbitrage bot. It does **not** certify, imply, or authorize any claim about
  the correctness, completeness, or safety of the bot itself, which has not
  been built.
- The Phase-0 specification was never revised, weakened, or reinterpreted to
  make certification easier at any point in this programme — every gap
  identified during zero-trust audits was closed by writing real
  implementation code and regression tests, never by redefining a
  requirement downward. The single pre-existing ADR proposal in this
  repository (`phase_0.75/adr_0012_phase0_specification_revision_PROPOSED.md`)
  remains unratified and was not used to satisfy any requirement in this
  certification.
- 22 `validation_findings` and 72 `category_validator_findings` remain
  present in the live pipeline output (section 2) — these are the governance
  platform correctly *detecting* real gaps in the underlying specification
  corpus (e.g. thin stubs, missing sections in some documents). Programme 2.5
  certifies that the platform correctly detects and reports these; it does
  not certify that the underlying specification corpus itself has zero
  gaps. Fixing the corpus's own findings is separate, future work (would
  fall under Programme 3's Closure Orchestrator / Repair Planner engines,
  per `docs/PROGRAMME-3-CLOSURE-ORCHESTRATOR.md` and
  `docs/PROGRAMME-3-REPAIR-PLANNER.md`).

## 9. Authorization

Per the Phase-0 execution order (`.governance/programme_2.5/execution_plan.json`,
`phase_0.accepted_order`: `PHASE_0, WS1, WS5, WS3, WS4, WS2, WS6, WS7, WS8,
WS9, RESUME_PROGRAMME_3`), Programme 2.5's certification is the explicit
precondition for resuming Programme 3. **This certification authorizes
Programme 3 (the actual bot implementation) to begin**, per the user's
explicit instruction on 2026-07-30 to proceed with Programme 3 once
Programme 2.5 is genuinely certified.

## Traceability

- Full workstream-by-workstream evidence: `.governance/programme_2.5/ws1/manifest.json`
  through `ws9/manifest.json`, each independently regenerated via live
  execution against the fresh clone (`verification_method` field in each
  manifest names the exact script used, never a hand-asserted claim).
- Readiness checklist: `.governance/programme_2.5/readiness_checklist.json`.
- Rollup: `.governance/programme_2.5/WORKSTREAM-STATUS-ROLLUP.json`.
- Freeze record: `.governance/freeze/freeze_WS0.json`, Ed25519-signed,
  public key `.governance/freeze/signing_public_key.pem`.
- Prior certification report (Repository Canonicality Repair, a narrower and
  earlier milestone that this document supersedes for Programme 2.5 as a
  whole): `.governance/programme_2.5/GOVERNANCE-CERTIFICATION-REPORT.md`.
