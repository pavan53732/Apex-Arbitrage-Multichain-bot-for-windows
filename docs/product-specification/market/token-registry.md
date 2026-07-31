---
metadata_schema_version: 1.0
document_id: DOC-0309
title: Token Registry
plane: Product Specification
domain: Market
class: Registry
authority: Canonical
status: Active
owner: Trading Team
version: 1.0.0
canonical_source: docs/product-specification/market/token-registry.md
related_concepts:
  - CONCEPT-0309
dependencies:
  - DOC-0266
  - DOC-0286
  - DOC-0293
  - DOC-0301
  - DOC-0317
consumers:
  - DOC-0049
  - DOC-0079
  - DOC-0286
  - DOC-0301
  - DOC-0310
  - DOC-0317
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: CONTRACT
purpose: Defines token registry.
scope: Token listing and metadata.
---

# Token Registry

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-29 | **Owner:** Trading Team

## Purpose
Defines the authoritative registry of tracked tokens and token metadata.

## Scope
This registry is descriptive and feeds market data, routing, wallet, portfolio, and risk workflows.

## Fields
- Token symbol.
- Contract address.
- Chain id.
- Decimals.
- Asset type.
- Wrapped/native relationship.
- Stablecoin flag.
- Display name.

## Cross-references
- `./market-data.md`
- `../execution/asset-management.md`
- `../execution/portfolio-management.md`
- `../execution/wallet-management.md`
- `../data/database-schema.md`

## Registry boundary
This is a pure data registry. All runtime behaviour, routing decisions, and validation rules are defined by the market/data/routing authority.

## Interface Contract
Defines token metadata, chain association, address validation, status, and versioned token records.

## Example
A token entry stores symbol, decimals, chain id, and active status.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Trading Team |
