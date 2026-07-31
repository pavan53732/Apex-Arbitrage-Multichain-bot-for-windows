---
metadata_schema_version: 1.0
document_id: DOC-0308
title: Oracle Registry
plane: Product Specification
domain: Market
class: Registry
authority: Canonical
status: Active
owner: Trading Team
version: 1.0.0
canonical_source: docs/product-specification/market/tokens/oracle-registry.md
related_concepts:
  - CONCEPT-0308
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Market
type: CONTRACT
purpose: Defines oracle registry.
scope: Oracle listing and metadata.
---

# Oracle Registry

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-29 | **Owner:** Trading Team

## Purpose
Defines the authoritative registry of supported oracle sources and fallback order.

## Scope
This registry is descriptive and feeds market data, routing, slippage, and risk decisions.

## Fields
- Oracle name.
- Chain id.
- Feed identifiers.
- Supported assets.
- Update cadence.
- Confidence policy.
- Fallback priority.
- Health status.

## Cross-references
- `../core/market-data.md`
- `../routing/liquidity-analysis.md`
- `../routing/slippage-model.md`
- `../../execution/risk-engine.md`
- `../../data/database-schema.md`

## Registry boundary
This is a pure data registry. All runtime behaviour, routing decisions, and validation rules are defined by the market/data/routing authority.

## Interface Contract
Defines oracle identity, feed metadata, heartbeat expectations, and versioned feed configuration.

## Example
A price oracle entry includes chain, feed id, heartbeat, and status.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Trading Team |
