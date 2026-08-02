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
canonical_source: docs/apex-app-docs/market/registries/token-registry.md
related_concepts:
  - CONCEPT-0309
dependencies: []
consumers:
  - DOC-0416
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Market
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

## Registry rules
- A token is identified by its chain id and contract address; the pair is unique.
- Decimals and asset type are validated before a token is promoted into the registry.
- Wrapped/native relationships are explicit and chain-aware.
- Stablecoin flags follow the stablecoin classification rules.
- A token's status and version are explicit; deprecated tokens are flagged, not removed.

## Registry boundary
This is a pure data registry. All runtime behaviour, routing decisions, and validation rules are defined by the market/data/routing authority.

## Interface Contract
Defines token metadata, chain association, address validation, status, and versioned token records.

## Lifecycle
- Tokens transition through candidate, active, and deprecated states.
- Discovery promotes candidates after validation; a candidate is never served as active.
- Deprecated tokens remain for history and are flagged, not removed.
- Registry updates emit change events to consumers.

## Cross-references
- `../core/market-data.md`
- `../../execution/wallet-portfolio/asset-management.md`
- `../../execution/wallet-portfolio/portfolio-management.md`
- `../../execution/wallet-portfolio/wallet-management.md`
- `../../data/persistence/database-schema.md`

## Example
A token entry stores symbol, decimals, chain id, and active status.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Trading Team |
