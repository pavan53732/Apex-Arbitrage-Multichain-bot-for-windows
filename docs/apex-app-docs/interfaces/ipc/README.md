---
metadata_schema_version: 1.0
document_id: DOC-0427
title: Interface IPC README
plane: Product Specification
domain: Interfaces
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/interfaces/ipc/ipc-protocol.md
related_concepts:
  - CONCEPT-0254
dependencies:
  - DOC-0254
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Interface IPC

## Purpose and scope

IPC protocol and IPC message catalog documentation.

## What belongs here

IPC transport, protocol, envelopes, delivery semantics, and IPC message catalog documents.

## What does not belong here

API contracts, events, adapters, or product UI behavior unless IPC-owned.

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
| [IPC Message Catalog](ipc-message-catalog.md) | Reference |
| [IPC Protocol](ipc-protocol.md) | Specification |

## Adjacent domains

Adjacent domains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
