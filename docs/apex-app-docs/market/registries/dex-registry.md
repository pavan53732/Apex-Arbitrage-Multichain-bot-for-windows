---
metadata_schema_version: 1.0
document_id: DOC-0307
title: DEX Registry
plane: Repository Operating Model
domain: Registries
class: Registry
authority: Canonical
status: Active
owner: Trading Team
version: 2.0.0
canonical_source: docs/apex-app-docs/market/registries/dex-registry.md
related_concepts:
  - CONCEPT-0307
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-01
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

## 0. Provider Trust Boundaries

### DEX Authority Classification
**Trust Level:** HIGH | **Authority:** EXECUTION_AUTHORITY

**DEX Role:**
- ✅ Provide executable quotes for trades
- ✅ Determine actual trade pricing and slippage
- ✅ Authority for PNL calculation
- ✅ Source of truth for execution outcomes
- ❌ NOT validation authority (oracles validate DEX quotes)
- ❌ NOT analysis authority (AI analyzes but doesn't override)

### Critical Invariants
- **DEX quotes are execution authority** — actual trade prices come from DEX only
- **Oracle validation required** — DEX quotes must be within 2% of oracle reference
- **No single DEX monopoly** — use multiple DEXes for validation and redundancy

### DEX Trust Tiers
**Tier 1 (HIGH TRUST):**
- Uniswap V3 (Ethereum, Arbitrum, Optimism, Polygon)
- PancakeSwap V3 (BSC, Ethereum)
- SushiSwap (multi-chain)
- Curve Finance (stablecoin pools)

**Tier 2 (MEDIUM TRUST):**
-Balancer V2
- 1inch (aggregator, not direct DEX)
- Kyber Network

**Tier 3 (LOW TRUST - Use with Caution):**
- Newer DEXes (< 6 months track record)
- Low liquidity DEXes (< $1M TVL)
- DEXes with known exploits or vulnerabilities

---

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
- `../../data/persistence/database-schema.md`

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
