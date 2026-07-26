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
- `MARKET-INTELLIGENCE.md`
- `STRATEGIES.md`
- `RISK-ENGINE.md`
- `EXECUTION-ENGINE.md`

## Operational Contract
Defines the scoring inputs, weighting model, thresholds, tie-breaking, and confidence factors used to rank opportunities.

## Example
A route with low gas and high historical success outranks a marginally profitable alternative.

## Required details
- Define thresholds, tie-breaks, freshness, and score drift rules.

## Ranking rules
- Define freshness, tie-breakers, thresholds, and invalidation behavior.
- Define how ranking output feeds execution.
