---
metadata_schema_version: 1.0
document_id: DOC-0326
title: Pair Discovery
plane: Product Specification
domain: Market
class: Reference
authority: Canonical
status: Active
owner: AI Team
version: 1.0.0
canonical_source: docs/apex-app-docs/market/tokens/pair-discovery.md
related_concepts:
  - CONCEPT-0326
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Market
type: REFERENCE
purpose: Pair Discovery documentation.
scope: Reference documentation.
---

# Pair Discovery

## Document type
Document type: [CONTRACT]

## Purpose
Defines how trading pairs are discovered, validated, and promoted for the platform.

## Discovery sources
- DEX pool listings.
- Token registry additions.
- Chain registry scans.
- Strategy requirements.

## Discovery rules
- A pair is defined by its base and quote assets on a specific chain and DEX.
- A discovered pair is validated against token metadata before promotion.
- Pairs with stale or invalid metadata are rejected, not silently kept.
- Discovery runs on a defined cadence and on registry change events.
- Promoted pairs are recorded in the pair store and published to market data consumers.

## Pair validation
- A pair passes only when both assets resolve in the token registry for the same chain.
- Liquidity and freshness gates are evaluated before promotion.
- A rejected pair is recorded with its reason code for tuning.
- Pair records are versioned and chain-scoped.

## Sources and refresh
- Discovery sources are DEX pool listings, registry additions, chain scans, and strategy requirements.
- Discovery runs on a defined cadence and on registry change events.
- A source outage degrades discovery to the remaining sources and is flagged.

## Output
- Promoted pairs are published to market data consumers through the domain model.
- Pair output is deterministic for the same inputs.
- Pair records include the discovery source and timestamp for traceability.
- Duplicate pairs are collapsed; the registry entry is the identity.
- A pair that fails revalidation is withdrawn from market data surfaces.
- Pair discovery feeds opportunity detection with validated pairs only.
- Discovery configuration changes are validated before activation.

## Cross-references
- `../core/market-data.md`
- `../core/market-intelligence.md`
- `./token-discovery.md`
- `../../execution/trading/strategies.md`

## Operational Contract

This document owns pair discovery and validation. Token metadata is owned by the token registry; DEX pool data by the DEX integration. This document composes them into validated pairs.

## Example
A new pool on a supported DEX is discovered, its tokens are validated, and the pair is promoted to market data consumers.
