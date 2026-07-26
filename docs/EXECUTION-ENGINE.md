# Execution Engine

## Purpose
The execution engine converts validated trading intents into executable plans, submits them to the appropriate chain or DEX path, and reconciles the full execution lifecycle.

## Responsibilities
- Normalize strategy output into executable instructions.
- Determine routing, submission ordering, and retry strategy.
- Manage transaction submission, confirmation, replacement, cancellation, and reconciliation.
- Coordinate gas, slippage, and MEV rules with the route plan.

## Inputs
- Strategy intent.
- Risk approval.
- Market data and quote freshness.
- Wallet and nonce state.
- Gas, slippage, and MEV constraints.
- Routing output and chain-health state.

## Outputs
- Execution plans.
- Transaction bundles and submitted ids.
- Status and reconciliation events.
- Failure reasons and recovery actions.

## Business rules
- Every execution must be risk-approved before submission.
- Execution must fail closed when quote freshness, gas, or slippage thresholds are invalid.
- Partial fills and partial confirmations must be tracked explicitly.
- Replacements are allowed only under fee policy and nonce safety rules.
- Chain reorgs must trigger reconciliation before new execution admission.

## State machine
Draft -> Validated -> Routed -> Submitted -> Confirming -> Filled | Replaced | Cancelled | Failed -> Reconciled.

## Interfaces
- IPC: `execution.plan.create`, `execution.plan.submit`, `execution.plan.status`, `execution.plan.cancel`, `execution.plan.replace`.
- Depends on routing engine, order management, transaction lifecycle, wallet management, gas optimisation, slippage model, and MEV protection.

## Data model
- Execution plan id.
- Strategy id.
- Opportunity id.
- Quote snapshot id.
- Chain id.
- Nonce state.
- Fee policy snapshot.
- Slippage policy snapshot.
- Risk approval id.
- Transaction/bundle ids.
- Final fill and reconciliation status.

## Recovery
- Retry transient RPC failures with bounded backoff.
- Replace or cancel on stale or invalidated quotes.
- Reconcile after chain reorgs before admitting new execution work.
- Preserve idempotency by deduplicating plan ids and bundle ids.

## Monitoring
- Plan creation latency.
- Submission success rate.
- Reorg recovery count.
- Replacement count.
- Rejection rate by validation rule.
- Time to final reconciliation.

## Testing
- Route selection tests.
- Partial fill tests.
- RPC failure injection.
- Reorg recovery tests.
- Duplicate submission prevention tests.

## Cross-references
- `docs/TRADING-ENGINE.md`
- `docs/ROUTING-ENGINE.md`
- `docs/ORDER-MANAGEMENT.md`
- `docs/TRANSACTION-LIFECYCLE.md`
- `docs/GAS-OPTIMISATION.md`
- `docs/SLIPPAGE-MODEL.md`
- `docs/MEV-PROTECTION.md`
