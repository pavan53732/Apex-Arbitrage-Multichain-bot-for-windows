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
Document type: [CONTRACT]

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

## Ranking rules
- Scores below the execution threshold are withheld, not discarded silently.
- Same inputs must produce the same ranking; tie-breaks are explicit and deterministic.
- Freshness is a hard gate: a stale candidate cannot outrank a fresh one.
- Score drift is monitored; a persistent drift triggers recalibration review.
- Ranking output feeds the execution engine in deterministic order.
- Score breakdowns are exposed so a withheld candidate shows why.
- Ranking inputs are versioned; a rerun with the same inputs reproduces the order.
- Risk and liquidity gates are evaluated before edge scoring.
- Confidence is combined with edge under the declared weighting model.
- Ranking runs on the detection cadence and on market change events.
- Ranked output carries the snapshot it was computed from.
- Tie-breaks favor lower risk, then lower gas, then faster execution.
- Ranking throughput and conversion are monitored per the operations contracts.
- Recalibration is a reviewed change, never an automatic adjustment.
- Ranking output is consumed read-only by execution and the dashboard.

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

Defines the scoring inputs, weighting model, thresholds, tie-breaking, and confidence factors used to rank opportunities. Detection and lifecycle are owned by their documents; this document owns the ranking order.

## Example
A route with low gas and high historical success outranks a marginally profitable alternative because tie-breaks favor lower risk.
