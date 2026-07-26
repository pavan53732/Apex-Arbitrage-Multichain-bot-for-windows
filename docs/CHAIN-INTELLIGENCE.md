# Chain Intelligence

## Purpose
Owns chain-level scoring, health classification, and execution suitability for supported networks.

## Why this is separate
Chain scoring has its own lifecycle, health model, and consumer set that do not safely merge into market data or routing without creating duplicated authority.

## Responsibilities
- Score chain health, finality, RPC stability, congestion, and fee conditions.
- Provide deterministic chain suitability scores to routing, execution, and strategy owners.
- Emit alerts for chain degradation and reorg risk.

## Inputs
- RPC health.
- Congestion metrics.
- Finality windows.
- Fee estimates.
- Reorg observations.

## Outputs
- Chain scores.
- Suitability class.
- Reject reasons.
- Health events.

## Cross-references
- `MARKET-DATA.md`
- `ROUTING-ENGINE.md`
- `EXECUTION-ENGINE.md`
- `MONITORING-OBSERVABILITY.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
