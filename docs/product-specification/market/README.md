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
canonical_source: docs/product-specification/market/core/market-data.md
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

Product market specifications and references. Trade execution and transaction submission belong under Execution.

## What does not belong here

Trading execution state machines, wallet management, and order submission behavior.

## Subdomains

| Subdomain | README | Canonical owner |
| --- | --- | --- |
| chains | [Market Chains README](chains/README.md) | [Chain Integration](./chains/chain-integration.md) |
| connectivity | [Market Connectivity README](connectivity/README.md) | [Rpc Manager](./connectivity/rpc-manager.md) |
| core | [Market Core README](core/README.md) | [Market Data](./core/market-data.md) |
| dex | [Market DEX README](dex/README.md) | [Dex Integration](./dex/dex-integration.md) |
| opportunities | [Market Opportunities README](opportunities/README.md) | [Opportunity Detection](./opportunities/opportunity-detection.md) |
| routing | [Market Routing README](routing/README.md) | [Routing Engine](./routing/routing-engine.md) |
| tokens | [Market Tokens README](tokens/README.md) | [Token Registry](./tokens/token-registry.md) |

## Document creation rule

Before adding a market document, identify the active market concept owner and place the document in the matching subdomain. Do not create duplicate market ownership documents.
