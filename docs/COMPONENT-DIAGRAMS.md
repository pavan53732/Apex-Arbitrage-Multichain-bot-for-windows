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
- `RUNTIME-OPERATIONS.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Required details
- Define Windows shell and backend boundaries.

## Boundaries
- Define the Windows shell, backend, worker, and data boundaries.
- Define the main IPC and service connections.
