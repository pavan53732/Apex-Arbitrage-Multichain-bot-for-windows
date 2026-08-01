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
canonical_source: docs/apex-app-docs/interfaces/messages/interface-catalog.md
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

Product interface specifications, protocols, adapters, events, and typed message contracts.

## What does not belong here

Runtime internals, UI behavior, market logic, or execution policy unless the document defines an interface boundary.

## Canonical owner map

| Subdomain | Concept ID | Canonical owner | README |
| --- | --- | --- | --- |
| adapters | CONCEPT-0262 | [Interface Provider Adapter](adapters/interface-provider-adapter.md) | [Interface Adapters README](adapters/README.md) |
| api | CONCEPT-0251 | [API Contracts](api/api-contracts.md) | [Interface API README](api/README.md) |
| events | CONCEPT-0253 | [Event Bus](events/event-bus.md) | [Events README](events/README.md) |
| ipc | CONCEPT-0254 | [IPC Protocol](ipc/ipc-protocol.md) | [Interface IPC README](ipc/README.md) |
| messages | CONCEPT-0255 | [Interface Catalog](messages/interface-catalog.md) | [Interface Messages README](messages/README.md) |

## Document classes expected

- Index
- Specification
- Reference
- Registry where an interface catalog is owned

## Relationship to adjacent domains

Interfaces documents define contracts consumed by Runtime, AI, Dashboard, Operations, Execution, and Plugins without owning those domains’ internal behavior.

## Subdomain navigation

### adapters

- Concept: `CONCEPT-0262`
- Canonical owner: [Interface Provider Adapter](adapters/interface-provider-adapter.md)
- Folder README: [Interface Adapters README](adapters/README.md)

Documents:

- [Interface Provider Adapter](adapters/interface-provider-adapter.md) — Reference

### api

- Concept: `CONCEPT-0251`
- Canonical owner: [API Contracts](api/api-contracts.md)
- Folder README: [Interface API README](api/README.md)

Documents:

- [API Contracts](api/api-contracts.md) — Specification
- [API Reference](api/api-reference.md) — Reference
- [Domain Model](api/domain-model.md) — Specification

### events

- Concept: `CONCEPT-0253`
- Canonical owner: [Event Bus](events/event-bus.md)
- Folder README: [Events README](events/README.md)

Documents:

- [Event Bus](events/event-bus.md) — Specification
- [Event Catalog](events/event-catalog.md) — Reference
- [Event Flow](events/event-flow.md) — Reference
- [Event Ownership Matrix](events/event-ownership-matrix.md) — Reference

### ipc

- Concept: `CONCEPT-0254`
- Canonical owner: [IPC Protocol](ipc/ipc-protocol.md)
- Folder README: [Interface IPC README](ipc/README.md)

Documents:

- [IPC Message Catalog](ipc/ipc-message-catalog.md) — Reference
- [IPC Protocol](ipc/ipc-protocol.md) — Specification

### messages

- Concept: `CONCEPT-0255`
- Canonical owner: [Interface Catalog](messages/interface-catalog.md)
- Folder README: [Interface Messages README](messages/README.md)

Documents:

- [Interface Agent Message](messages/interface-agent-message.md) — Reference
- [Interface Catalog](messages/interface-catalog.md) — Index
- [Interface Notification Channel](messages/interface-notification-channel.md) — Reference
- [Interface Tool Call](messages/interface-tool-call.md) — Reference

## Before adding a document here

- Identify the active Concept ID in the Concept Registry before creating a new document.
- Update an existing canonical owner instead of creating a duplicate specification when the concept already exists.
- Place the document in the narrowest matching subdomain folder.
- Assign a stable Document ID only if the document is new permanent repository knowledge.
- Add or update metadata, registries, README navigation, and cross-references in the same change.
- Run local metadata, registry, traceability, link, stale-path, empty-folder, and repository hygiene validation before committing.
- Do not add generated documentation, CI/CD files, GitHub Actions, temporary reports, or repository automation.
