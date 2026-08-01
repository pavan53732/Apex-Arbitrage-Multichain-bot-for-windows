---
metadata_schema_version: 1.0
document_id: DOC-0397
title: Events README
plane: Product Specification
domain: Interfaces
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/interfaces/events/event-bus.md
related_concepts:
  - CONCEPT-0253
dependencies:
  - DOC-0253
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Interface Events

## Purpose and scope

Event bus, event flow, event ownership, and event catalog documentation.

## What belongs here

Event interface references, event catalogs, event flow descriptions, and event ownership material.

## What does not belong here

Generic API, IPC, provider adapter, or product behavior documents that are not event-interface references.

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
| [Event Bus](event-bus.md) | Specification |
| [Event Catalog](event-catalog.md) | Reference |
| [Event Flow](event-flow.md) | Reference |
| [Event Ownership Matrix](event-ownership-matrix.md) | Reference |

## Adjacent domains

Adjacent domains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
