---
last_updated: 2026-07-29
type: REFERENCE
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Component Diagrams documentation.
scope: Reference documentation.
canonical_source: docs/COMPONENT-DIAGRAMS.md
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
- `ARCHITECTURE.md`
- `PROJECT-STRUCTURE.md`
- `MODULE-DEPENDENCY.md`
- `operations/RUNTIME-OPERATIONS.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Required details
- Define Windows shell and backend boundaries.

## Boundaries
- Define the Windows shell, backend, worker, and data boundaries.
- Define the main IPC and service connections.
