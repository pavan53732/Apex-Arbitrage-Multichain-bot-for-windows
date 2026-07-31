---
metadata_schema_version: 1.0
document_id: DOC-0269
title: Data README
plane: Product Specification
domain: Data
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/data/persistence/database-schema.md
related_concepts:
  - CONCEPT-0266
dependencies:
  - DOC-0266
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Data

## Purpose and scope

Data persistence, state, registries, knowledge, governance, ownership, and flow documentation.

## What belongs here

Product data specifications and references for persistence, state management, registry systems, and knowledge structures.

## What does not belong here

Configuration profiles, market data behavior, repository registries, or runtime worker behavior unless the data domain owns it.

## Canonical owner map

| Subdomain | Concept ID | Canonical owner | README |
| --- | --- | --- | --- |
| knowledge | CONCEPT-0275 | [Knowledge Graph](./knowledge/knowledge-graph.md) | [Data Knowledge README](./knowledge/README.md) |
| persistence | CONCEPT-0266 | [Database Schema](./persistence/database-schema.md) | [Data Persistence README](./persistence/README.md) |
| registries | CONCEPT-0276 | [Registry System](./registries/registry-system.md) | [Data Registries README](./registries/README.md) |
| state | CONCEPT-0267 | [State Management](./state/state-management.md) | [Data State README](./state/README.md) |

## Document classes expected

- Index
- Specification
- Reference
- Policy where data ownership/governance is defined

## Relationship to adjacent domains

Data documents are consumed by Runtime, AI, Execution, Operations, and Configuration but must not redefine their domain behavior.

## Subdomain navigation

### knowledge

- Concept: `CONCEPT-0275`
- Canonical owner: [Knowledge Graph](./knowledge/knowledge-graph.md)
- Folder README: [Data Knowledge README](./knowledge/README.md)

Documents:

- [Context Builder](./knowledge/context-builder.md) — Reference
- [Data Flow](./knowledge/data-flow.md) — Reference
- [Data Governance](./knowledge/data-governance.md) — Reference
- [Data Ownership](./knowledge/data-ownership.md) — Policy
- [Knowledge Graph](./knowledge/knowledge-graph.md) — Reference

### persistence

- Concept: `CONCEPT-0266`
- Canonical owner: [Database Schema](./persistence/database-schema.md)
- Folder README: [Data Persistence README](./persistence/README.md)

Documents:

- [Database Schema](./persistence/database-schema.md) — Specification
- [File Storage](./persistence/file-storage.md) — Reference

### registries

- Concept: `CONCEPT-0276`
- Canonical owner: [Registry System](./registries/registry-system.md)
- Folder README: [Data Registries README](./registries/README.md)

Documents:

- [Registry System](./registries/registry-system.md) — Specification

### state

- Concept: `CONCEPT-0267`
- Canonical owner: [State Management](./state/state-management.md)
- Folder README: [Data State README](./state/README.md)

Documents:

- [Cache Manager](./state/cache-manager.md) — Specification
- [Decision Ledger](./state/decision-ledger.md) — Reference
- [Runtime Knowledge](./state/runtime-knowledge.md) — Reference
- [State Management](./state/state-management.md) — Specification

## Before adding a document here

- Identify the active Concept ID in the Concept Registry before creating a new document.
- Update an existing canonical owner instead of creating a duplicate specification when the concept already exists.
- Place the document in the narrowest matching subdomain folder.
- Assign a stable Document ID only if the document is new permanent repository knowledge.
- Add or update metadata, registries, README navigation, and cross-references in the same change.
- Run local metadata, registry, traceability, link, stale-path, empty-folder, and repository hygiene validation before committing.
- Do not add generated documentation, CI/CD files, GitHub Actions, temporary reports, or repository automation.
