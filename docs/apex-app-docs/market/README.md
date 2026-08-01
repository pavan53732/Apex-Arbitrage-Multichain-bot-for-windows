---
metadata_schema_version: 1.0
document_id: DOC-0310
title: Market README
plane: Product Specification
domain: Market
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/market/core/market-data.md
related_concepts:
  - CONCEPT-0317
dependencies:
  - DOC-0317
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Market

## Purpose and scope

Market data, intelligence, chain/DEX/token/oracle registries, routing, liquidity, gas, MEV, connectivity, and opportunity documentation.

## What belongs here

Product market specifications and references for discovering, scoring, and routing opportunities before execution.

## What does not belong here

Execution, wallet management, transaction lifecycle, UI, and product AI orchestration behavior unless explicitly market-owned.

## Canonical owner map

| Subdomain | Concept ID | Canonical owner | README |
| --- | --- | --- | --- |
| chains | CONCEPT-0302 | [Chain Integration](chains/chain-integration.md) | [Market Chains README](chains/README.md) |
| connectivity | CONCEPT-0305 | [RPC Manager](connectivity/rpc-manager.md) | [Market Connectivity README](connectivity/README.md) |
| core | CONCEPT-0317 | [Market Data](core/market-data.md) | [Market Core README](core/README.md) |
| dex | CONCEPT-0303 | [DEX Integration](dex/dex-integration.md) | [Market DEX README](dex/README.md) |
| opportunities | CONCEPT-0323 | [Opportunity Detection](opportunities/opportunity-detection.md) | [Market Opportunities README](opportunities/README.md) |
| routing | CONCEPT-0304 | [Routing Engine](routing/routing-engine.md) | [Market Routing README](routing/README.md) |
| tokens | CONCEPT-0309 | [Token Registry](./tokens/token-registry.md) | [Market Tokens README](tokens/README.md) |

## Document classes expected

- Index
- Specification
- Reference
- Registry where the market domain owns records

## Relationship to adjacent domains

Market documents feed execution and AI planning but do not own transaction submission, wallet policy, or AI model orchestration.

## Subdomain navigation

### chains

- Concept: `CONCEPT-0302`
- Canonical owner: [Chain Integration](chains/chain-integration.md)
- Folder README: [Market Chains README](chains/README.md)

Documents:

- [Chain Command Center](chains/chain-command-center.md) — Reference
- [Chain Integration](chains/chain-integration.md) — Specification
- [Chain Intelligence](chains/chain-intelligence.md) — Reference
- [Chain Registry](./chains/chain-registry.md) — Registry
- [Chain Rotation](chains/chain-rotation.md) — Reference

### connectivity

- Concept: `CONCEPT-0305`
- Canonical owner: [RPC Manager](connectivity/rpc-manager.md)
- Folder README: [Market Connectivity README](connectivity/README.md)

Documents:

- [RPC Manager](connectivity/rpc-manager.md) — Specification

### core

- Concept: `CONCEPT-0317`
- Canonical owner: [Market Data](core/market-data.md)
- Folder README: [Market Core README](core/README.md)

Documents:

- [Market Data](core/market-data.md) — Reference
- [Market Intelligence](core/market-intelligence.md) — Reference
- [Market Regime Detection](core/market-regime-detection.md) — Reference
- [Market Session](core/market-session.md) — Reference

### dex

- Concept: `CONCEPT-0303`
- Canonical owner: [DEX Integration](dex/dex-integration.md)
- Folder README: [Market DEX README](dex/README.md)

Documents:

- [DEX Integration](dex/dex-integration.md) — Specification
- [DEX Intelligence](dex/dex-intelligence.md) — Reference
- [DEX Registry](./dex/dex-registry.md) — Registry

### opportunities

- Concept: `CONCEPT-0323`
- Canonical owner: [Opportunity Detection](opportunities/opportunity-detection.md)
- Folder README: [Market Opportunities README](opportunities/README.md)

Documents:

- [Opportunity Detection](opportunities/opportunity-detection.md) — Reference
- [Opportunity Lifecycle](opportunities/opportunity-lifecycle.md) — Reference
- [Opportunity Ranking](opportunities/opportunity-ranking.md) — Reference

### routing

- Concept: `CONCEPT-0304`
- Canonical owner: [Routing Engine](routing/routing-engine.md)
- Folder README: [Market Routing README](routing/README.md)

Documents:

- [Gas Optimisation](routing/gas-optimisation.md) — Reference
- [Liquidity Analysis](routing/liquidity-analysis.md) — Reference
- [MEV Protection Detail](routing/mev-protection-detail.md) — Reference
- [MEV Protection](routing/mev-protection.md) — Reference
- [Route Optimization](routing/route-optimization.md) — Reference
- [Route Scoring Model](routing/route-scoring-model.md) — Reference
- [Routing Engine](routing/routing-engine.md) — Specification
- [Slippage Model](routing/slippage-model.md) — Reference

### tokens

- Concept: `CONCEPT-0309`
- Canonical owner: [Token Registry](./tokens/token-registry.md)
- Folder README: [Market Tokens README](tokens/README.md)

Documents:

- [Oracle Registry](./tokens/oracle-registry.md) — Registry
- [Pair Discovery](tokens/pair-discovery.md) — Reference
- [Price Discovery](tokens/price-discovery.md) — Reference
- [Token Discovery](tokens/token-discovery.md) — Reference
- [Token Intelligence](tokens/token-intelligence.md) — Reference
- [Token Registry](./tokens/token-registry.md) — Registry

## Before adding a document here

- Identify the active Concept ID in the Concept Registry before creating a new document.
- Update an existing canonical owner instead of creating a duplicate specification when the concept already exists.
- Place the document in the narrowest matching subdomain folder.
- Assign a stable Document ID only if the document is new permanent repository knowledge.
- Add or update metadata, registries, README navigation, and cross-references in the same change.
- Run local metadata, registry, traceability, link, stale-path, empty-folder, and repository hygiene validation before committing.
- Do not add generated documentation, CI/CD files, GitHub Actions, temporary reports, or repository automation.
