---
metadata_schema_version: 1.0
document_id: DOC-0256
title: Interfaces README
plane: Product Specification
domain: Interfaces
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/interfaces/messages/interface-catalog.md
related_concepts:
  - CONCEPT-0255
dependencies:
  - DOC-0255
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Interfaces

## Purpose and scope

APIs, IPC, events, adapters, message catalogs, and interface contracts for product boundaries.

## What belongs here

Product interface specifications and references. Runtime behavior, UI behavior, and market/execution logic belong in their owning product domains.

## What does not belong here

Implementation internals that do not define an interface boundary.

## Subdomains

| Subdomain | README | Canonical owner |
| --- | --- | --- |
| adapters | [Interface Adapters README](adapters/README.md) | [Interface Provider Adapter](./adapters/interface-provider-adapter.md) |
| api | [Interface API README](api/README.md) | [Api Contracts](./api/api-contracts.md) |
| events | [Events README](events/README.md) | [Event Bus](./events/event-bus.md) |
| ipc | [Interface IPC README](ipc/README.md) | [Ipc Protocol](./ipc/ipc-protocol.md) |
| messages | [Interface Messages README](messages/README.md) | [Interface Catalog](./messages/interface-catalog.md) |

## Document creation rule

Before adding an interface document, identify the active interface concept owner and place the document in the matching subdomain. Do not create duplicate interface ownership documents.
