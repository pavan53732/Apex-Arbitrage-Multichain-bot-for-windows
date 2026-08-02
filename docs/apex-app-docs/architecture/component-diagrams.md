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
Document type: [REFERENCE]

## Purpose
Provides structural diagrams of major runtime components and their boundaries for the APEX desktop application.

## Scope
Diagrammatic representations only: the Windows shell, the renderer, the IPC bridge, main-process services, and the domain packages. This document does not define behavior or contracts.

## Ownership
- Owns diagrammatic representations only.
- Does not define behavior or contracts; behavioral authority stays with the component owners.

## Desktop Runtime
```text
Renderer UI -> Preload API -> IPC Contracts -> Main Process Services -> Packages (AI, Risk, Strategy, DB, Adapters)
```

## Boundaries
- **Windows shell**: window management, tray, notifications, and OS integration; owned by the Windows documentation.
- **Renderer UI**: dashboard panels and widgets; owned by the dashboard and UI documentation.
- **Preload API / IPC**: typed message contracts; owned by the IPC protocol documentation.
- **Main process services**: orchestrator, workers, resource manager, and registries; owned by the runtime documentation.
- **Domain packages**: AI, risk, strategy, execution, market data, and persistence; owned by their respective canonical owners.
- **Data**: the persistence layer and caches; owned by the data documentation.

## Conventions
- Diagrams are ASCII or Mermaid and must stay aligned with `./architecture.md` and `./module-dependency.md`.
- Component boxes map to canonical owners; an unowned box is a documentation gap.
- Diagram updates require updating the ownership mapping in the same change.

## Diagram update rules
- A diagram update requires the corresponding ownership mapping update in the same change.
- Diagrams use the canonical component names from `./architecture.md`.
- An unowned box in any diagram is a documentation gap and must be resolved before merge.
- ASCII and Mermaid diagrams must agree with the module dependency rules.
- A component rename updates every diagram that references it in the same change.
- Diagrams render at the level of detail their reader needs; box internals belong to the component owner.

## Cross-references
- `./architecture.md`
- `./project-structure.md`
- `./module-dependency.md`
- `../operations/reliability/runtime-operations.md`
- `../windows/windows-desktop.md`

## Operational Contract

This document owns the structural diagram view of the system. It must remain consistent with the architecture reference and the module dependency rules; when a component's boundaries change, this document is updated with the change. It does not own component behavior.

## Example
The desktop runtime diagram shows the renderer reaching main-process services only through the typed preload/IPC bridge, matching the IPC contract.
