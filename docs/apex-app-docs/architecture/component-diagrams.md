---
metadata_schema_version: 1.0
document_id: DOC-0080
title: Component Diagrams
plane: Product Specification
domain: Architecture
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/architecture/component-diagrams.md
related_concepts:
  - CONCEPT-0080
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Architecture
type: REFERENCE
purpose: Component Diagrams documentation.
scope: Reference documentation.
---

# Component Diagrams

## Document type
This document is an overview, reference, or index as noted below.

# Component Diagrams

## Purpose
Provides structural diagrams of major runtime components and their boundaries.

## Ownership
- Owns diagrammatic representations only.
- Does not define behavior or contracts.

## Desktop Runtime
```text
Renderer UI -> Preload API -> IPC Contracts -> Main Process Services -> Packages (AI, Risk, Strategy, DB, Adapters)
```

## Cross-references
- `./architecture.md`
- `./project-structure.md`
- `./module-dependency.md`
- `../operations/reliability/runtime-operations.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Required details
- Define Windows shell and backend boundaries.

## Boundaries
- Define the Windows shell, backend, worker, and data boundaries.
- Define the main IPC and service connections.
