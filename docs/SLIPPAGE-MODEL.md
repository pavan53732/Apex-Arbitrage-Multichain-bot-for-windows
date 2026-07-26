# Slippage Model

## Purpose
Defines how expected slippage is estimated and bounded during routing and execution.

## Inputs
Route depth, target size, volatility, and freshness.

## Outputs
Expected slippage, maximum tolerated slippage, and rejection decision.

## Algorithm
- Estimate price impact from target size and route depth.
- Inflate tolerance when volatility rises, but never beyond policy.
- Reject routes that exceed configured tolerance.

## Cross-references
- `ROUTING-ENGINE.md`
- `EXECUTION-ENGINE.md`
- `RISK-ENGINE.md`
