# Arbitrage Window Manager

## Purpose
Defines the lifecycle of arbitrage windows from detection through expiry or execution.

## Ownership
- Owns window creation, timing budgets, expiry, and stale-opportunity invalidation.
- Does not own trade execution or route scoring.

## Window contract
- Must define latency budget per leg, expiry conditions, and timing synchronization.
- Must define what happens when the opportunity becomes stale mid-flow.

## Cross-references
- `TRADING-LIFECYCLE.md`
- `OPPORTUNITY-RANKING.md`
- `RISK-ENGINE.md`
- `ORCHESTRATOR.md`
