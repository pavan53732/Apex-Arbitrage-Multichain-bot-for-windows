# Slippage Model

## Purpose
Defines how expected slippage is estimated and bounded.

## Rules
- Slippage ceilings are strategy- and route-specific.
- Quotes must be fresh enough for the configured slippage budget.
- Estimated impact plus safety margin must remain below configured limits.

## Cross-references
- `docs/EXECUTION-ENGINE.md`
- `docs/STRATEGIES.md`
- `docs/ROUTING-ENGINE.md`
