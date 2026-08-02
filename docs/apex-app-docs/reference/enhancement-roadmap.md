---
metadata_schema_version: 1.0
document_id: DOC-0367
title: Enhancement Roadmap
plane: Product Specification
domain: Reference
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/reference/enhancement-roadmap.md
related_concepts:
  - CONCEPT-0367
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Reference
type: REFERENCE
purpose: Enhancement Roadmap documentation.
scope: Reference documentation.
---

# Enhancement Roadmap

## Document type
Document type: [REFERENCE]

## Purpose
Defines enhancement milestones and delivery sequencing for the APEX platform.

## Milestones
- **M1 — Governance and validation**: validator suite complete, warning noise reduced, documentation stable.
- **M2 — Simulation**: end-to-end simulation pipeline with backtesting and decision ledger.
- **M3 — Windows desktop**: shell, tray, service mode, notifications, and signed packaging.
- **M4 — Polygon-first live**: operator-approved execution on Polygon with full safety controls.
- **M5 — Multi-chain expansion**: additional chains with the same provider-trust and risk controls.

## Roadmap rules
- Milestones are sequenced by dependency order; a milestone's prerequisites must land first.
- Every enhancement ties to an authoritative owner document and a feature-matrix status.
- A milestone is complete when its acceptance criteria are met and validated.

## Tracking
- Each enhancement records its status: proposed, in progress, complete, deferred, or dropped.
- A deferred or dropped enhancement is recorded with its reason.
- Milestone progress is visible in the roadmap and feature-matrix surfaces.

## Change management
- A milestone change updates this roadmap, the feature matrix, and the implementation roadmap together.
- An enhancement without a canonical owner is not scheduled.
- Scope additions re-validate the milestone's acceptance criteria.

## Acceptance
- Acceptance criteria are concrete, testable, and owned.
- A milestone is accepted when its criteria pass the validator suite.
- Acceptance is recorded with the release version.
- Post-acceptance changes are tracked as new enhancements.

## Governance
- The roadmap is reviewed on a defined cadence with the implementation roadmap.
- Priority is derived from dependency order and platform value.
- Deprecations and removals are tracked in the roadmap before execution.
- Every roadmap item is traceable to an owner document.
- Roadmap changes are validated and committed with the docs they affect.
- Milestone dependencies are explicit and checked before scheduling.

## Cross-references
- `./feature-matrix.md`
- `./implementation-roadmap.md`
- `./roadmap.md`

## Operational Contract

This document owns the enhancement roadmap: milestones, dependencies, and delivery sequencing. The implementation roadmap owns build sequencing; this roadmap owns the capability milestones.

## Example
M4 cannot start until M2 and M3 land because live execution depends on simulation and the desktop shell.
