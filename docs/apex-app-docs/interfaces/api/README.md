---
metadata_schema_version: 1.0
document_id: DOC-0426
title: Interface API README
plane: Product Specification
domain: Interfaces
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/interfaces/api/api-contracts.md
related_concepts:
  - CONCEPT-0251
dependencies:
  - DOC-0251
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Interface API

## Purpose and scope

API contracts, API references, and product domain model interface documentation.

## What belongs here

API contracts, API references, and domain model documents.

## What does not belong here

IPC transport, event bus behavior, adapter boundaries, or message catalogs unless API-owned.

## Expected document classes

- Index
- Specification
- Reference
- Registry where this subdomain owns an interface catalog

## Canonical boundaries

This folder indexes interface documents in this subdomain and defers behavior to canonical owner documents identified by metadata and registry entries.

## Documents

| Document | Class |
| --- | --- |
| [API Contracts](api-contracts.md) | Specification |
| [API Reference](api-reference.md) | Reference |
| [Domain Model](domain-model.md) | Specification |

## Adjacent domains

Adjacent domains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
