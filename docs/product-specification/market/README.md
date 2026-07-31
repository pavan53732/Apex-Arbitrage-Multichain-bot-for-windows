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
canonical_source: docs/product-specification/market/market-data.md
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

Market data, chain/DEX/token/oracle registries, routing, liquidity, gas, MEV, opportunities.

## Document classes expected

- Index
- Guide
- Reference
- Specification where this folder owns a canonical boundary
- Registry only in registry folders
- Historical only in historical folders
- Generated only in generated folders

## Canonical boundaries

Market, chain, DEX, token, routing, and discovery specifications.

## What does not belong here

Trade execution state machines.

## Documents

| Document ID | Title | Class | Authority | Status |
| --- | --- | --- | --- | --- |
| DOC-0302 | [Chain Integration](./chain-integration.md) | Specification | Canonical | Active |
| DOC-0303 | [DEX Integration](./dex-integration.md) | Specification | Canonical | Active |
| DOC-0304 | [Routing Engine](./routing-engine.md) | Specification | Canonical | Active |
| DOC-0305 | [RPC Manager](./rpc-manager.md) | Specification | Canonical | Active |
| DOC-0306 | [Chain Registry](./chain-registry.md) | Registry | Canonical | Active |
| DOC-0307 | [DEX Registry](./dex-registry.md) | Registry | Canonical | Active |
| DOC-0308 | [Oracle Registry](./oracle-registry.md) | Registry | Canonical | Active |
| DOC-0309 | [Token Registry](./token-registry.md) | Registry | Canonical | Active |
| DOC-0311 | [Chain Command Center](./chain-command-center.md) | Reference | Canonical | Active |
| DOC-0312 | [Chain Intelligence](./chain-intelligence.md) | Reference | Canonical | Active |
| DOC-0313 | [Chain Rotation](./chain-rotation.md) | Reference | Canonical | Active |
| DOC-0314 | [DEX Intelligence](./dex-intelligence.md) | Reference | Canonical | Active |
| DOC-0315 | [Gas Optimisation](./gas-optimisation.md) | Reference | Canonical | Active |
| DOC-0316 | [Liquidity Analysis](./liquidity-analysis.md) | Reference | Canonical | Active |
| DOC-0317 | [Market Data](./market-data.md) | Reference | Canonical | Active |
| DOC-0318 | [Market Intelligence](./market-intelligence.md) | Reference | Canonical | Active |
| DOC-0319 | [Market Regime Detection](./market-regime-detection.md) | Reference | Canonical | Active |
| DOC-0320 | [Market Session](./market-session.md) | Reference | Canonical | Active |
| DOC-0321 | [MEV Protection Detail](./mev-protection-detail.md) | Reference | Canonical | Active |
| DOC-0322 | [MEV Protection](./mev-protection.md) | Reference | Canonical | Active |
| DOC-0323 | [Opportunity Detection](./opportunity-detection.md) | Reference | Canonical | Active |
| DOC-0324 | [Opportunity Lifecycle](./opportunity-lifecycle.md) | Reference | Canonical | Active |
| DOC-0325 | [Opportunity Ranking](./opportunity-ranking.md) | Reference | Canonical | Active |
| DOC-0326 | [Pair Discovery](./pair-discovery.md) | Reference | Canonical | Active |
| DOC-0327 | [Price Discovery](./price-discovery.md) | Reference | Canonical | Active |
| DOC-0328 | [Route Optimization](./route-optimization.md) | Reference | Canonical | Active |
| DOC-0329 | [Route Scoring Model](./route-scoring-model.md) | Reference | Canonical | Active |
| DOC-0330 | [Slippage Model](./slippage-model.md) | Reference | Canonical | Active |
| DOC-0331 | [Token Discovery](./token-discovery.md) | Reference | Canonical | Active |
| DOC-0332 | [Token Intelligence](./token-intelligence.md) | Reference | Canonical | Active |
