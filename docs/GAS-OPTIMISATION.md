# Gas Optimisation

## Purpose
Defines gas estimation, repricing, replacement, batching, and submission timing rules.

## Ownership
- Owns gas estimation, fee policy, replacement thresholds, and submission timing.
- Feeds routing, execution, and transaction lifecycle.

## Responsibilities
- Estimate source and destination gas costs.
- Select fee caps, priority fees, and replacement thresholds.
- Decide when batching or single-shot execution is preferred.
- Expose gas safety data to routing and execution.

## Rules
- Gas policy must be bounded by operator configuration.
- Repricing must preserve nonce safety and idempotency.
- Fee bumps must not violate slippage or edge thresholds.
- Gas estimates must be refreshed when fee markets move materially.

## Outputs
- Gas estimate.
- Fee cap.
- Priority fee.
- Replacement threshold.
- Batching decision.

## Persistence
- Persist gas model version, estimate inputs, selected fees, replacement decisions, and route fingerprint.

## Monitoring
- Gas estimate error.
- Replacement count.
- Over-budget rejection count.

## Cross-references
- `EXECUTION-ENGINE.md`
- `TRANSACTION-LIFECYCLE.md`
- `MEV-PROTECTION.md`
