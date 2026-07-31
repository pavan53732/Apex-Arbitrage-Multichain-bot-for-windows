---
metadata_schema_version: 1.0
document_id: DOC-0307
title: DEX Registry
plane: Product Specification
domain: Market
class: Registry
authority: Canonical
status: Active
owner: Trading Team
version: 1.0.0
canonical_source: docs/product-specification/market/dex/dex-registry.md
related_concepts:
  - CONCEPT-0307
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
purpose: Defines DEX registry.
scope: DEX listing and metadata.
---

# Dex Registry

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-29 | **Owner:** Trading Team

## Purpose
Defines the authoritative registry of supported DEXs and their capabilities.

## Scope
This registry is descriptive and feeds routing, liquidity, execution, and market data decisions.

## Fields
- DEX name.
- Chain id.
- Router address.
- Factory address.
- Pool types.
- Fee tiers.
- Version.
- Capability flags.

## Cross-references
- `./dex-integration.md`
- `../routing/routing-engine.md`
- `../routing/liquidity-analysis.md`
- `../core/market-data.md`
- `../../data/database-schema.md`

## Registry boundary
This is a pure data registry. All runtime behaviour, routing decisions, and validation rules are defined by the market/data/routing authority.

## Interface Contract
Defines DEX identity, pool coverage, supported routes, status, and versioned metadata.

## Example
A DEX entry includes router address, supported features, and chain associations.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Trading Team |
