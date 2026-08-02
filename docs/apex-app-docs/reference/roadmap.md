---
metadata_schema_version: 1.0
document_id: DOC-0373
title: Roadmap
plane: Product Specification
domain: Reference
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/reference/roadmap.md
related_concepts:
  - CONCEPT-0373
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
purpose: Roadmap documentation.
scope: Reference documentation.
---

# Roadmap

## Document type
Document type: [REFERENCE]

## Purpose
Defines near-term priorities, deprecations, and acceptance criteria for the APEX platform.

## Near-term priorities
- Complete the validator suite coverage and reduce warning noise.
- Finalize the Windows desktop shell and service-mode contracts.
- Implement the simulation pipeline end to end (Phase 1).
- Prepare Polygon-first live integration planning (Phase 2).

## Deprecations
- Legacy agent rules and archived documentation remain historical and are not revived.
- A feature scheduled for deprecation is listed here with its removal target.

## Acceptance criteria
- A roadmap item is accepted only with a canonical owner and defined scope.
- An item is rejected if it duplicates an owned concept or lacks a canonical owner.
- Items are sequenced by dependency order per the implementation roadmap.

## Near-term details
- Validator coverage: complete the remaining VAL-018 coverage metadata and reduce warning noise.
- Windows shell: land tray, service mode, notifications, and signed packaging with the desktop contracts.
- Simulation: ship the end-to-end pipeline with backtesting and the decision ledger.
- Polygon-first: prepare live integration planning after simulation and the desktop shell land.

## Status semantics
- Each roadmap item records a status and an owning document.
- A status change updates the roadmap and the feature matrix together.
- Deferred items are reviewed on a defined cadence before re-scheduling.

## Governance
- The roadmap is reviewed with the enhancement and implementation roadmaps.
- Deprecations are listed here before execution begins.
- Roadmap changes are validated and committed with the docs they affect.
- The roadmap never overrides a canonical owner; it sequences them.
- Items without owners are not scheduled.
- Scope is fixed at acceptance; additions re-open the item.
- The roadmap is the near-term planning surface; the feature matrix is the status surface.
- Roadmap priorities are reviewed on the roadmap cadence.

## Cross-references
- `./implementation-roadmap.md`
- `./enhancement-roadmap.md`
- `./feature-matrix.md`

## Operational Contract

This document owns the roadmap overview: near-term priorities, deprecations, and acceptance criteria. Detailed sequencing is owned by the implementation roadmap.

## Example
A proposed feature without a canonical owner is rejected until ownership is established.
