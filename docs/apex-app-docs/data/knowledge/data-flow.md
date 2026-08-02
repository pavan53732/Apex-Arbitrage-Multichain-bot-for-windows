---
metadata_schema_version: 1.0
document_id: DOC-0271
title: Data Flow
plane: Product Specification
domain: Data
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.1.0
canonical_source: docs/apex-app-docs/data/knowledge/data-flow.md
related_concepts:
  - CONCEPT-0271
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - Data
type: REFERENCE
purpose: Data Flow documentation.
scope: Reference documentation.
---

# Data Flow

## Document type
Document type: [REFERENCE]

## Purpose
Defines how data moves across market, trading, AI, risk, execution, persistence, and UI layers.

## Ownership
- Describes end-to-end flow only; message contracts stay in `../../interfaces/ipc/ipc-protocol.md` and `../../interfaces/api/api-reference.md`.

## End-to-end flow
- Raw RPC data is ingested and normalized into canonical records.
- Normalized records are validated and cached before reaching analytics.
- Analytics and AI layers consume the validated records and produce decision support.
- Decisions flow to the execution path and are persisted with full lineage.
- UI components consume the domain model via the typed IPC and API contracts.

## Windows data flow
- User-scoped data lives in `%APPDATA%`; system-scoped service data lives in `%PROGRAMDATA%`.
- UI and backend share data through the typed IPC bridge, never by direct file access from the renderer.
- Persistence boundaries follow the data ownership map; caches are acceleration only.

## Desktop flow
- RPC and backend workers publish normalized data to the cache and event bus; UI components subscribe via the domain model.

## Data stages
- Ingest: raw RPC data is captured from chain and DEX sources.
- Normalize: records are canonicalized to the domain model.
- Validate: provenance and schema checks run before acceptance.
- Cache: validated records are cached by domain.
- Analyze: analytics and AI consume validated records.
- Persist: lineage and history are stored durably.
- Present: UI consumes the domain model via contracts.

## Flow guarantees
- A consumer reads validated records only; raw records never bypass normalization.
- Lineage is preserved from ingest to persist; a record without lineage is not served.
- Caches accelerate reads and never change the meaning of a record.
- Flow changes update this document and the affected owner contracts in the same change.
- A stage that cannot complete fails closed and is surfaced to the operator rather than silently skipped.
- Event-driven updates flow through the event bus per the event flow contract.

## Cross-references
- `../../interfaces/events/event-flow.md`
- `../state/state-management.md`
- `./data-ownership.md`
- `../../operations/reliability/runtime-operations.md`

## Operational Contract

Defines the pipeline from raw RPC data through normalization, validation, caching, analytics, AI, and decision support. This document describes the flow; the contracts and stores it traverses are owned by their canonical owners.

## Example
Raw pool data is normalized before reaching opportunity ranking, and the normalized record is what downstream consumers read.
