# Slippage Model

## Purpose
Defines how expected slippage is estimated and bounded.

## Ownership
- Owns slippage estimation, slippage budgets, and tolerance checks.
- Feeds routing and execution validation.

## Inputs
- Quote freshness.
- Order size.
- Pool depth.
- Route path.
- Volatility.
- Historical impact data.

## Model rules
- Slippage ceilings are strategy- and route-specific.
- Quotes must be fresh enough for the configured slippage budget.
- Estimated impact plus safety margin must remain below configured limits.
- High volatility increases estimated slippage and can invalidate a route.

## Outputs
- Expected slippage.
- Maximum allowed slippage.
- Reject reason.
- Route safety label.

## Validation
- Reject stale quotes.
- Reject routes whose estimated impact exceeds the configured ceiling.
- Reject if the safety margin cannot be computed.

## Persistence
- Persist model version, route fingerprint, quote hash, estimated slippage, max threshold, and reject reason.

## Monitoring
- Slippage estimate error.
- Slippage rejection count.
- Threshold breach count.

## Cross-references
- `EXECUTION-ENGINE.md`
- `STRATEGIES.md`
- `ROUTING-ENGINE.md`
