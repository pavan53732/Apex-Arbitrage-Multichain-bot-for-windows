# Gas Optimisation

## Purpose
Defines gas estimation, repricing, replacement, batching, and submission timing rules.

## Responsibilities
- Estimate source and destination gas costs.
- Select fee caps, priority fees, and replacement thresholds.
- Decide when batching or single-shot execution is preferred.
- Expose gas safety data to routing and execution.

## Rules
- Gas policy must be bounded by operator configuration.
- Repricing must preserve nonce safety and idempotency.

## Cross-references
- `docs/EXECUTION-ENGINE.md`
- `docs/TRANSACTION-LIFECYCLE.md`
- `docs/MEV-PROTECTION.md`
