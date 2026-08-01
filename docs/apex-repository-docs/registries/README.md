---
metadata_schema_version: 1.0
document_id: DOC-0063
title: Registries README
plane: Repository Operating Model
domain: Registries
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-repository-docs/registries/DOCUMENT-REGISTRY.md
related_concepts:
  - CONCEPT-0007
  - CONCEPT-0006
  - CONCEPT-0008
  - CONCEPT-0067
  - CONCEPT-0069
dependencies:
  - DOC-0007
  - DOC-0006
  - DOC-0008
  - DOC-0067
  - DOC-0069
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Registries

## Purpose and scope

Canonical repository knowledge registries for concepts, documents, and semantic traceability.

## What belongs here

Registry definitions, registry versioning, registry usage references, and registry governance policies.

## What does not belong here

Generated reports, temporary audit files, caches, or product-domain data registries.

## Canonical owner map

| Subdomain | Concept ID | Canonical Owner | README |
| --- | --- | --- | --- |
| registries | CONCEPT-0007 | [Document Registry](DOCUMENT-REGISTRY.md) | (self) |

## Document classes expected

- Registry
- Index
- Reference
- Policy

## Relationship to adjacent domains

Registries define identity and relationships for the entire repository. All domains consume registry data. Registries must not redefine product behavior or replace canonical product specifications.

## Subdomain navigation

### registries

- Concept: `CONCEPT-0007`
- Canonical Owner: [Document Registry](DOCUMENT-REGISTRY.md)
- Folder README: (self)

Documents:
- [Concept Registry](CONCEPT-REGISTRY.md) — Registry
- [Document Registry](DOCUMENT-REGISTRY.md) — Registry
- [Traceability Registry](TRACEABILITY-REGISTRY.md) — Registry
- [Registry Governance Standard](registry-governance-standard.md) — Policy
- [Concept Lifecycle Policy](concept-lifecycle-policy.md) — Policy

## Registry versioning

| Registry | Version | Schema | Model |
| --- | --- | --- | --- |
| [Concept Registry](CONCEPT-REGISTRY.md) | 1.1.1 | 1.1 | Concept-centric with stable aliases |
| [Document Registry](DOCUMENT-REGISTRY.md) | 1.1.1 | 1.1 | Document identity with concept roles |
| [Traceability Registry](TRACEABILITY-REGISTRY.md) | 1.1.1 | 1.1 | Semantic relationships only |

## Before adding a document here

- Identify the active Concept ID in the Concept Registry before creating a new document.
- Update an existing canonical owner instead of creating a duplicate specification when the concept already exists.
- Place the document in the narrowest matching subdomain folder.
- Assign a stable Document ID only if the document is new permanent repository knowledge.
- Add or update metadata, registries, README navigation, and cross-references in the same change.
- Run local metadata, registry, traceability, link, stale-path, empty-folder, and repository hygiene validation before committing.
- Do not add generated documentation, CI/CD files, GitHub Actions, temporary reports, or repository automation.
