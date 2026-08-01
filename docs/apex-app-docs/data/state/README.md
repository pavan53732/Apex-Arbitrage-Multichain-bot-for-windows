---
metadata_schema_version: 1.0
document_id: DOC-0435
title: Data State README
plane: Product Specification
domain: Data
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/data/state/state-management.md
related_concepts:
  - CONCEPT-0267
dependencies:
  - DOC-0267
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Data State

## Purpose and scope

State management, cache manager, runtime knowledge, and decision ledger documentation.

## What belongs here

Runtime state, cache, decision ledger, and runtime knowledge documents.

## What does not belong here

Database schema, file storage, or configuration profiles unless data state owns the concern.

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
| [Cache Manager](cache-manager.md) | Specification |
| [Decision Ledger](decision-ledger.md) | Reference |
| [Runtime Knowledge](runtime-knowledge.md) | Reference |
| [State Management](state-management.md) | Specification |

## Adjacent domains

Adjacent domains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
