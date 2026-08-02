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
version: 1.1.0
canonical_source: docs/apex-app-docs/execution/wallet-portfolio/asset-management.md
related_concepts:
  - CONCEPT-0286
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - Execution
type: REFERENCE
purpose: Asset Management documentation.
scope: Reference documentation.
---

# Asset Management

## Document type
Document type: [CONTRACT]

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
- An asset with an unverified contract address is not eligible for execution.
- Metadata updates emit change events so caches and UI refresh consistently.

## Governance rules
- The canonical asset registry is the single source for asset identity across chains.
- Wrapped assets declare their native relationship and are normalized per chain.
- Display precision is chain-aware; a value is never displayed with more precision than its asset supports.

## Cross-references
- `../../market/core/market-data.md`
- `./portfolio-management.md`
- `./wallet-management.md`
- `../trading/strategies.md`
- `../../market/tokens/token-registry.md`

## Operational Contract

Defines asset tracking, balances, custody, approvals, and transfer governance. Asset identity is canonical here; balances and custody are owned by wallet management.

## Example
A supported asset cannot be transferred until approval and balance checks pass; an asset with unknown decimals blocks execution until verified.
