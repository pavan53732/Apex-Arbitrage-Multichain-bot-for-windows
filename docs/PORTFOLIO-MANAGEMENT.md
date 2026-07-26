# Portfolio Management

## Purpose
Aggregates balances and positions into portfolio value, allocation, and utilization snapshots.

## Responsibilities
- Compute total value, allocation, exposure, and utilization.
- Aggregate positions and wallet balances.
- Feed risk, reporting, and UI dashboards.

## Cross-references
- `docs/POSITION-MANAGEMENT.md`
- `docs/WALLET-MANAGEMENT.md`
- `docs/MARKET-DATA.md`

## Operational Contract
Defines portfolio ownership, allocation, rebalancing, exposure limits, and wallet/strategy bindings.

## Example
A portfolio rebalance is blocked if exposure exceeds policy.

## Required details
- Define multi-wallet aggregation and reconciliation.
