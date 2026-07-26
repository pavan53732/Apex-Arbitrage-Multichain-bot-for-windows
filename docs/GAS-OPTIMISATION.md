# Gas Optimisation

## Purpose
Defines fee estimation, repricing, batching, and transaction timing rules.

## Inputs
Gas market data, congestion, transaction urgency, and execution constraints.

## Outputs
Fee estimate, priority policy, replacement policy, and gas budget decision.

## Algorithm
- Estimate base and priority fees.
- Reprice when congestion or fee spikes invalidate prior cost assumptions.
- Batch only when batching preserves safety and profitability.

## Cross-references
- `EXECUTION-ENGINE.md`
- `TRANSACTION-LIFECYCLE.md`
