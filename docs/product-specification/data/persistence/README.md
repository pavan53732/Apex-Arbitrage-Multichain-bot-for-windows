---
metadata_schema_version: 1.0
document_id: DOC-0433
title: Data Persistence README
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

# Data Persistence

## Purpose and scope

Database schema and file storage documentation.

## What belongs here

Persistence schema, storage, database, and durable file-storage documents.

## What does not belong here

Runtime state transitions or knowledge graph behavior unless persistence owns the concern.

## Expected document classes

- Index
- Specification
- Reference
- Policy or Registry where this subdomain owns the concern

## Canonical boundaries

This folder indexes Data documents in this subdomain and defers behavior to canonical owner documents identified by metadata and registry entries.

## Documents

| Document | Class |
| --- | --- |
| [Database Schema](./database-schema.md) | Specification |
| [File Storage](./file-storage.md) | Reference |

## Adjacent domains

Adjacent domains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
