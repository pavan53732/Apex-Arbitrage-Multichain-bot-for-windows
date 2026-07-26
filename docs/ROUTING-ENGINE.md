# Routing Engine

## Purpose
Determines the optimal execution path across DEXs, chains, pools, and bridges.

## Inputs
Market data, liquidity analysis, gas estimates, MEV risk, and slippage model output.

## Outputs
Route candidate set, ranked route, route rationale, and execution constraints.

## Algorithm
- Generate valid candidate routes.
- Score each route by cost, latency, slippage, liquidity, and MEV risk.
- Choose the lowest-risk route that satisfies execution policy.

## Cross-references
- `EXECUTION-ENGINE.md`
- `GAS-OPTIMISATION.md`
- `SLIPPAGE-MODEL.md`
- `MEV-PROTECTION.md`
