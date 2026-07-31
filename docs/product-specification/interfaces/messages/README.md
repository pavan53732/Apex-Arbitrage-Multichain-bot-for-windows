---
metadata_schema_version: 1.0
document_id: DOC-0428
title: Interface Messages README
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

# Interface Messages

## Purpose and scope

Interface message, tool-call, notification-channel, and interface catalog documentation.

## What belongs here

Message/interface catalogs and typed message boundary documents.

## What does not belong here

API transport, IPC runtime, or event bus behavior unless message contract ownership is explicit.

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
| [Interface Agent Message](./interface-agent-message.md) | Reference |
| [Interface Catalog](./interface-catalog.md) | Index |
| [Interface Notification Channel](./interface-notification-channel.md) | Reference |
| [Interface Tool Call](./interface-tool-call.md) | Reference |

## Adjacent domains

Adjacent domains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
