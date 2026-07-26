# Execution Engine

## Purpose
The execution engine converts validated trading intents into executable plans, submits them to the appropriate chain or DEX path, and reconciles the full execution lifecycle.

## Responsibilities
- Normalize strategy output into executable instructions.
- Determine routing, submission ordering, and retry strategy.
- Manage transaction submission, confirmation, replacement, cancellation, and reconciliation.
- Coordinate gas, slippage, and MEV rules with the route plan.

## Business rules
- Every execution must be risk-approved before submission.
- Execution must fail closed when quote freshness, gas, or slippage thresholds are invalid.
- Partial fills and partial confirmations must be tracked explicitly.
- Replacements are allowed only under fee policy and nonce safety rules.

## State machine
Draft -> Validated -> Routed -> Submitted -> Confirming -> Filled | Replaced | Cancelled | Failed -> Reconciled.

## Inputs
- Strategy intent.
- Risk approval.
- Market data and quote freshness.
- Wallet and nonce state.
- Gas and slippage constraints.
- Routing and MEV decisions.

## Outputs
- Execution plans.
- Submitted transaction bundles.
- Lifecycle events.
- Final reconciliation records.

## Interfaces
- IPC: execution.plan.create, execution.plan.submit, execution.plan.status, execution.plan.cancel, execution.plan.replace.
- Depends on routing engine, order manager, transaction lifecycle, wallet management, gas optimization, slippage model, MEV protection.

## Recovery
- Retry transient RPC failures with bounded backoff.
- Replace or cancel on stale or invalidated quotes.
- Reconcile after chain reorgs before admitting new execution work.

## Monitoring
- Plan creation latency.
- Submission success rate.
- Reorg recovery count.
- Replacement count.
- Rejection rate by validation rule.

## Testing
- Route selection tests.
- Partial fill tests.
- RPC failure injection.
- Reorg recovery tests.

