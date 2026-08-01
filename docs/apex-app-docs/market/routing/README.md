---
metadata_schema_version: 1.0
document_id: DOC-0415
title: Market Routing README
plane: Product Specification
domain: Market
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/market/routing/routing-engine.md
related_concepts:
  - CONCEPT-0304
dependencies:
  - DOC-0304
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Market Routing

## Purpose and scope

Routing engine, route optimization, scoring, liquidity, slippage, gas, and MEV protection documentation.

## What belongs here

Route selection, route optimization, scoring, liquidity, slippage, gas, and MEV market behavior.

## What does not belong here

Execution submission, wallet management, or chain metadata registry ownership.

## Expected document classes

- Index
- Specification
- Reference
- Registry where this subdomain owns domain records

## Canonical boundaries

This folder indexes market documents in this subdomain and defers behavior to canonical owner documents identified by metadata and registry entries.

## Documents

| Document | Class |
| --- | --- |
| [Gas Optimisation](gas-optimisation.md) | Reference |
| [Liquidity Analysis](liquidity-analysis.md) | Reference |
| [MEV Protection Detail](mev-protection-detail.md) | Reference |
| [MEV Protection](mev-protection.md) | Reference |
| [Route Optimization](route-optimization.md) | Reference |
| [Route Scoring Model](route-scoring-model.md) | Reference |
| [Routing Engine](routing-engine.md) | Specification |
| [Slippage Model](slippage-model.md) | Reference |

## Adjacent domains

Adjacent domains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
