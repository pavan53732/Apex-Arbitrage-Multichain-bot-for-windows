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
canonical_source: docs/product-specification/interfaces/event-bus.md
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

# Events

## Purpose and scope

Event interface references, event catalogs, event flow descriptions, and event ownership indexes.

## What belongs here

Event Bus references, event catalogs, event flow references, and event ownership material.

## What does not belong here

Generic API, IPC, provider adapter, or product behavior documents that are not event-interface references.

## Expected document classes

- Index
- Reference
- Specification when this folder owns a product behavior boundary
- Guide when the document explains operational usage

## Canonical boundaries

This folder indexes documents in its subdomain and defers behavioral authority to the canonical owner documents listed below.

## Documents

| Document | Purpose |
| --- | --- |
| [Event Bus](../event-bus.md) | Canonical event bus behavior. |
| [Event Catalog](./event-catalog.md) | Event catalog reference that defers to Event Bus. |

## Adjacent domains

Adjacent domains may reference this folder, but they must not redefine the canonical behavior owned here.
