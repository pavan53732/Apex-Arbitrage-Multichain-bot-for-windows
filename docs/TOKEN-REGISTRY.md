---
last_updated: 2026-07-29
type: CONTRACT
owner: Trading Team
status: Canonical
version: 1.0.0
purpose: Defines token registry.
scope: Token listing and metadata.
canonical_source: docs/TOKEN-REGISTRY.md
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
- `MARKET-DATA.md`
- `ASSET-MANAGEMENT.md`
- `PORTFOLIO-MANAGEMENT.md`
- `WALLET-MANAGEMENT.md`
- `DATABASE-SCHEMA.md`

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
