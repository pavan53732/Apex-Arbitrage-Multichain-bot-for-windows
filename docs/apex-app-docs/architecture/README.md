---
metadata_schema_version: 1.0
document_id: DOC-0068
title: Architecture README
plane: Product Specification
domain: Architecture
class: Index
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
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Architecture

## Purpose and scope

System boundaries, kernel, structure, and cross-system architecture.

## Document classes expected

- Index
- Guide
- Reference
- Specification where this folder owns a canonical boundary
- Registry only in registry folders
- Historical only in historical folders
- Generated only in generated folders

## Canonical boundaries

Architecture specifications and structural references.

## What does not belong here

Repository governance.

## Documents

| Document ID | Title | Class | Authority | Status |
| --- | --- | --- | --- | --- |
| DOC-0065 | [APEX Kernel](apex-kernel.md) | Specification | Canonical | Active |
| DOC-0066 | [End To End Wiring Contract](end-to-end-wiring-contract.md) | Specification | Canonical | Active |
| DOC-0069 | [APEX Architecture](apex-architecture.md) | Guide | Derived | Active |
| DOC-0078 | [APEX OS](apex-os.md) | Reference | Canonical | Active |
| DOC-0079 | [Architecture](architecture.md) | Reference | Canonical | Active |
| DOC-0080 | [Component Diagrams](component-diagrams.md) | Reference | Canonical | Active |
| DOC-0081 | [Dependency Graph](dependency-graph.md) | Reference | Canonical | Active |
| DOC-0082 | [Live Architecture Viewer](live-architecture-viewer.md) | Reference | Canonical | Active |
| DOC-0083 | [Module Dependency](module-dependency.md) | Reference | Canonical | Active |
| DOC-0084 | [Non Functional Requirements](non-functional-requirements.md) | Reference | Canonical | Active |
| DOC-0085 | [Project Structure](project-structure.md) | Reference | Canonical | Active |

## Architecture Ownership Boundaries

- APEX Kernel owns kernel lifecycle, service registration, events, and plugin loading.
- APEX Architecture is the derived orientation guide; it does not redefine kernel behavior.
- APEX OS owns the platform-level conceptual model.
- Architecture is the cross-system reference model; detailed contracts remain in domain specifications.
- decisions/ records rationale and does not create competing runtime specifications.
