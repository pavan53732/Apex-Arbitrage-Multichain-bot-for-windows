---
metadata_schema_version: 1.0
document_id: DOC-0255
title: Interface Catalog
plane: Product Specification
domain: Interfaces
class: Index
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/interfaces/messages/interface-catalog.md
related_concepts:
  - CONCEPT-0255
dependencies: []
consumers:
  - DOC-0256
  - DOC-0428
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Interfaces
type: INDEX
purpose: Interface Catalog documentation.
scope: Reference documentation.
---

# Interface Catalog

## Document type
Document type: [INDEX]

## Purpose
Index of interface contracts and canonical owners.

## Catalog
- Interface, owner, producer, consumer, schema, version, reference.

## How to use this catalog
- Each row names an interface, its canonical owner, its producer and consumer, its schema source, its version, and the reference document.
- Behavior and schema details are owned by the referenced contract documents; this catalog is navigation only.
- A new interface is added here in the same change that introduces its contract document.

## Interface families
- Messages: agent messages, tool calls, and notification channels.
- Events: the event catalog and event flow.
- IPC: the IPC protocol and message catalog.
- API: the public API reference and domain model.

## Update rules
- This index must reflect the current contract set; a renamed or retired interface updates its row in the same change.
- The catalog never duplicates a contract's schema; it points to the owner.

## Catalog entries
- Every interface row lists: interface, owner, producer, consumer, schema, version, and reference.

## Maintenance
- The catalog is updated in the same change as the contract it references.
- A retired interface is marked retired, never deleted from the catalog.

## Conventions
- Interface names are stable identifiers.
- The catalog points to owners; it never duplicates a contract's schema.
- Version bumps are reflected in the catalog row in the same change.
- A contract that gains a producer or consumer updates the row in the same change.
- The catalog lists retired interfaces with their retirement marker, never deleting them.
- Every catalog row resolves to a real contract document; a dangling row is a defect.
- Interface families partition the catalog for navigation and ownership clarity.
- New interfaces are added to the catalog in the same change as their contract.

## Cross-references
- `./interface-agent-message.md`
- `./interface-tool-call.md`
- `./interface-notification-channel.md`
- `../events/event-catalog.md`
- `../ipc/ipc-message-catalog.md`
- `../api/api-reference.md`

## Operational Contract

This index owns the navigation surface for interface contracts. Each contract's schema, validation, versioning, and failure behavior are owned by its contract document and referenced from this catalog.

## Example
A developer looking up the tool-call contract finds the owner, schema, and version in this catalog, then follows the reference to the contract document.
