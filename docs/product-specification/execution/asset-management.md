---
metadata_schema_version: 1.0
document_id: DOC-0286
title: Asset Management
plane: Product Specification
domain: Execution
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/execution/asset-management.md
related_concepts:
  - CONCEPT-0286
dependencies:
  - DOC-0293
  - DOC-0295
  - DOC-0301
  - DOC-0309
  - DOC-0317
consumers:
  - DOC-0049
  - DOC-0059
  - DOC-0285
  - DOC-0309
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: Asset Management documentation.
scope: Reference documentation.
---

# Asset Management

## Document type
This document is an overview, reference, or index as noted below.

# Asset Management

## Purpose
Owns canonical asset metadata, identifiers, decimals, display symbols, and chain-specific asset normalization.

## Responsibilities
- Maintain canonical asset registry across chains.
- Resolve symbol collisions and wrapped asset aliases.
- Validate asset metadata before it is used in execution or display.
- Emit change events when asset metadata is updated.

## Data model
- Asset id.
- Chain id.
- Contract address or native marker.
- Symbol.
- Name.
- Decimals.
- Display precision.
- Alias set.
- Verification status.

## Validation rules
- Duplicate canonical ids are rejected.
- Conflicting symbols must be resolved with chain-aware aliases.
- Unknown decimals block execution until verified.

## Cross-references
- `../market/market-data.md`
- `./portfolio-management.md`
- `./wallet-management.md`
- `./strategies.md`
- `../market/token-registry.md`

## Operational Contract
Defines asset tracking, balances, custody, approvals, and transfer governance.

## Example
A supported asset cannot be transferred until approval and balance checks pass.
