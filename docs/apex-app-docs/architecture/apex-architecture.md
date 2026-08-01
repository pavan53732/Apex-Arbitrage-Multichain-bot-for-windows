---
metadata_schema_version: 1.0
document_id: DOC-0069
title: APEX Architecture
plane: Product Specification
domain: Architecture
class: Guide
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/architecture/architecture.md
related_concepts:
  - CONCEPT-0079
dependencies:
  - DOC-0079
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Reference
owned_domains: []
type: OVERVIEW
purpose: Apex architecture overview.
scope: Architecture reference.
---

# APEX Architecture


## AI Guard
Before creating or modifying ANY markdown file, verify it complies with the 5 Prime Directives.
- Lifecycle docs must explicitly define initial state, terminal state, allowed transitions, forbidden transitions, recovery transitions, and failure transitions.
- Interface docs must explicitly define producer, consumer, payload, schema, validation, versioning, and failure behavior.
- Owner docs must explicitly state what they own and do not own.
- Cross-cutting docs must defer to canonical owners.
- Short docs must explicitly declare whether they are an [INDEX], [OVERVIEW], or [REFERENCE].
If a file fails any directive, abort and fix it before proceeding.

## Purpose
Top-level index for the implementation specification set.

## Ownership
- `../../apex-repository-docs/documentation-lifecycle/documentation-map.md` owns documentation authority rules.
- `./architecture.md` owns system architecture and subsystem boundaries.
- `./project-structure.md` owns repository layout and package boundaries.

## Authority Boundary

**This document is a derived architecture guide.**

- **Owns:** Architecture overview, project structure, documentation map navigation.
- **Does NOT own:** System architecture (owned by `architecture.md`), subsystem implementation, runtime coordination, state management.
- **Authority level:** Derived — defers to `architecture.md` for canonical system architecture.
- **Superordinate document:**
  - `architecture.md` — Whole-system canonical architecture reference
- **Related documents:**
  - `apex-os.md` — Platform constitution
  - `apex-kernel.md` — Kernel specification
  - `orchestrator.md` — Runtime sequencing

**This document defers to `architecture.md` for system architecture and subsystem boundaries.** It is a derived guide, not a canonical specification.

## Before creating or modifying ANY markdown file, verify it complies with the 5 Prime Directives.
- `./architecture.md` owns system architecture and subsystem boundaries.
- `./project-structure.md` owns repository layout and package boundaries.

## Cross-references
- `../../apex-repository-docs/documentation-lifecycle/documentation-map.md`
- `./architecture.md`
- `./project-structure.md`
- `../execution/trading/trading-engine.md`
- `../execution/transactions/execution-engine.md`


## Cross-references
- `../runtime/orchestrator.md`


## System Contracts
- `../interfaces/api/domain-model.md` — authoritative system contract.
