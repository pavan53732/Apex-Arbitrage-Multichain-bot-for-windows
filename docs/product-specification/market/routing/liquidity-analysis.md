---
metadata_schema_version: 1.0
document_id: DOC-0316
title: Liquidity Analysis
plane: Product Specification
domain: Market
class: Reference
authority: Canonical
status: Active
owner: UI Team
version: 1.0.0
canonical_source: docs/product-specification/market/routing/liquidity-analysis.md
related_concepts:
  - CONCEPT-0316
dependencies: []
consumers:
  - DOC-0330
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Market
type: REFERENCE
purpose: Liquidity Analysis documentation.
scope: Reference documentation.
---

# Liquidity Analysis

## Document type
This document is an overview, reference, or index as noted below.

# Liquidity Analysis

## Purpose
Defines liquidity depth, route viability, execution impact, and pool health analysis.

## Ownership
- Owns liquidity depth estimation, pool health scoring, route viability gating, and executable size calculations.
- Feeds routing, market intelligence, strategy sizing, and execution validation.

## Responsibilities
- Estimate executable size under slippage and impact constraints.
- Detect shallow, fragmented, or unstable liquidity.
- Provide pool health and route viability scores.
- Surface liquidity rejection reasons for strategy, route, and execution owners.

## Analysis contract
Every liquidity analysis must define inputs, outputs, thresholds, scoring criteria, freshness requirements, and failure handling.

## Inputs
- Market data snapshots.
- Pool depth and reserve state.
- Route path and DEX topology.
- Volatility and recent impact history.
- Fee tier and expected trade size.
- Chain state and confirmation context.

## Outputs
- Liquidity depth score.
- Executable size estimate.
- Pool health class.
- Route viability score.
- Slippage impact estimate.
- Reject reason.

## Algorithmic rules
- Depth must be evaluated against target notional and route path length.
- Fragmented liquidity must be penalized relative to consolidated depth.
- Volatility and fee pressure increase effective impact.
- Stale pool data must fail closed.
- Low-confidence inputs must reduce route viability or reject the analysis.

## Thresholds
- Minimum depth threshold.
- Maximum expected impact threshold.
- Maximum fragmentation threshold.
- Maximum staleness threshold.
- Maximum venue concentration threshold.

## Validation
- Reject stale or incomplete pool data.
- Reject if executable size cannot be estimated within tolerance.
- Reject if route viability falls below policy threshold.

## Persistence
- Persist analysis id, route fingerprint, pool ids, depth values, impact values, thresholds, reject reason, and input snapshot hash.

## Monitoring
- Depth estimation latency.
- Rejection rate.
- Stale input rate.
- Route viability drift.
- Impact model error.

## Failure and recovery
- On incomplete inputs, fail closed and surface a rejection reason.
- On analysis failure, route and execution owners must not consume the result.
- On recovered market state, recompute before any route is admitted.

## Cross-references
- `./routing-engine.md`
- `../core/market-intelligence.md`
- `./slippage-model.md`
- `../../execution/transactions/execution-engine.md`

## Operational Contract
Defines liquidity inputs, thresholds, aggregation, scoring, and report generation.

## Example
A pool is flagged when depth falls below minimum trade size.
