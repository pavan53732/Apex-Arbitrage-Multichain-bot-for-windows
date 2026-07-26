# Arbitrage Monitoring

## Document type
This document is an overview, reference, or index as noted below.

# Arbitrage Monitoring

## Purpose
Defines monitoring for spread windows, execution latency, fill status, and profitability.

## Ownership
- Owns spread visibility, arbitrage window timing, and per-trade P&L monitoring.
- Does not own execution mechanics or risk limits.

## Monitoring contract
- Must define live spread calculation, alert thresholds, and stale quote detection.
- Must define success, partial success, failed opportunity, and expired window states.

## Cross-references
- `METRICS.md`
- `OPPORTUNITY-RANKING.md`
- `PERFORMANCE-SLOS.md`
- `DECISION-LOG.md`

## Canonical ownership
This document defers to the canonical owners for implementation, policy, and schema details.
