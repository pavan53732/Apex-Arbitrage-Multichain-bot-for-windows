# Opportunity Detection

## Purpose
Identifies candidate opportunities from market data and strategy inputs.

## Inputs
Market data, volatility, liquidity, price dislocation, and strategy configuration.

## Outputs
Candidate opportunity record and detection score.

## Algorithm
- Scan for spreads, trends, or statistical signals.
- Filter stale or unviable candidates.
- Emit normalized opportunity records for ranking.

## Cross-references
- `MARKET-DATA.md`
- `OPPORTUNITY-RANKING.md`
- `STRATEGIES.md`
