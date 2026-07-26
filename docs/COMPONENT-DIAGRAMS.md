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
