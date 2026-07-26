# Liquidity Analysis

## Purpose
Defines route viability, depth scoring, execution impact, and pool health assessment.

## Inputs
Pool depth, route candidates, token pairs, volatility, and freshness.

## Outputs
Liquidity score, fill probability, route viability, and impact estimate.

## Algorithm
- Measure usable depth against target size.
- Penalize fragmented or stale liquidity.
- Estimate price impact and fill probability.
- Produce a route viability decision.

## Cross-references
- `MARKET-DATA.md`
- `SLIPPAGE-MODEL.md`
- `ROUTING-ENGINE.md`
