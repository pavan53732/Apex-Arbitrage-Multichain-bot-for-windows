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
canonical_source: docs/repository-operating-model/registries/DOCUMENT-REGISTRY.md
related_concepts:
  - CONCEPT-0007
dependencies:
  - DOC-0007
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

## Document classes expected

- Registry
- Index
- Reference only when it explains registry usage

## Canonical boundaries

The registries define identity and relationships. They do not redefine product behavior or replace canonical product specifications.

## What does not belong here

Generated reports, temporary audit files, caches, or product-domain data registries.

## Registry versioning

| Registry | Version | Schema | Model |
| --- | --- | --- | --- |
| [Concept Registry](./CONCEPT-REGISTRY.md) | 1.1.0 | 1.1 | Concept-centric with stable aliases |
| [Document Registry](./DOCUMENT-REGISTRY.md) | 1.1.0 | 1.1 | Document identity with concept roles |
| [Traceability Registry](./TRACEABILITY-REGISTRY.md) | 1.1.0 | 1.1 | Semantic relationships only |

## Documents

| Document ID | Title | Class | Authority | Status |
| --- | --- | --- | --- | --- |
| DOC-0006 | [Concept Registry](./CONCEPT-REGISTRY.md) | Registry | Canonical | Active |
| DOC-0007 | [Document Registry](./DOCUMENT-REGISTRY.md) | Registry | Canonical | Active |
| DOC-0008 | [Traceability Registry](./TRACEABILITY-REGISTRY.md) | Registry | Canonical | Active |
