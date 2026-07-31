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
version: 1.0.0
canonical_source: docs/product-specification/data/data-flow.md
related_concepts:
  - CONCEPT-0271
dependencies:
  - DOC-0254
  - DOC-0257
  - DOC-0258
  - DOC-0267
  - DOC-0338
consumers:
  - DOC-0049
  - DOC-0059
  - DOC-0258
  - DOC-0269
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: Data Flow documentation.
scope: Reference documentation.
---

# Data Flow

## Document type
This document is an overview, reference, or index as noted below.

# Data Flow

## Purpose
Defines how data moves across market, trading, AI, risk, execution, persistence, and UI layers.

## Ownership
- Describes end-to-end flow only; message contracts stay in `../interfaces/ipc-protocol.md` and `../interfaces/api-reference.md`.

## Cross-references
- `../interfaces/event-flow.md`
- `./state-management.md`
- `../operations/runtime-operations.md`

## Operational Contract
Defines the pipeline from raw RPC data through normalization, validation, caching, analytics, AI, and decision support.

## Example
Raw pool data is normalized before reaching opportunity ranking.

## Windows data flow
- Must define AppData, ProgramData, IPC, and persistence paths.
- Must define how UI and backend share data under Windows.

## Required details
- Define desktop/backend data paths, IPC flow, and persistence boundaries.

## Desktop flow
- Must define data flow from RPC and backend workers to UI components and cache.
