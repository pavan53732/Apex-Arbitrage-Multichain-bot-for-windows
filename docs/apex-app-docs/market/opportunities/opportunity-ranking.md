---
metadata_schema_version: 1.0
document_id: DOC-0325
title: Opportunity Ranking
plane: Product Specification
domain: Market
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/market/opportunities/opportunity-ranking.md
related_concepts:
  - CONCEPT-0325
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
purpose: Opportunity Ranking documentation.
scope: Reference documentation.
---

# Opportunity Ranking

## Document type
This document is an overview, reference, or index as noted below.

# Opportunity Ranking

## Purpose
Ranks detected opportunities for execution or human review.

## Responsibilities
- Score expected edge, confidence, risk, liquidity, gas, and MEV exposure.
- Return deterministic ordering for downstream consumers.

## Inputs
Opportunity candidates, market data, risk profile, AI confidence, chain conditions.

## Outputs
Ranked opportunities, score breakdowns, and reject reasons.

## Algorithms
Weighted scoring with hard gates for risk, liquidity, and freshness.

## Thresholds
Scores below execution threshold are withheld.

## Monitoring
Ranking throughput, score drift, execution conversion.

## Validation
Same inputs must produce same ranking.


## Cross-references
- `../core/market-intelligence.md`
- `../../execution/trading/strategies.md`
- `../../execution/risk-policy/risk-engine.md`
- `../../execution/transactions/execution-engine.md`

## Operational Contract
Defines the scoring inputs, weighting model, thresholds, tie-breaking, and confidence factors used to rank opportunities.

## Example
A route with low gas and high historical success outranks a marginally profitable alternative.

## Required details
- Define thresholds, tie-breaks, freshness, and score drift rules.

## Ranking rules
- Define freshness, tie-breakers, thresholds, and invalidation behavior.
- Define how ranking output feeds execution.
