# Execution Engine

## Purpose
The execution engine converts validated trading intents into executable plans, submits them to the correct chain or DEX path, and reconciles the full execution lifecycle.

## Ownership
- Owns executable plan lifecycle, route binding, submission, replacement, cancellation, and reconciliation.
- Does not own strategy generation or session orchestration.

## Responsibilities
- Normalize strategy output into executable instructions.
- Determine routing, submission ordering, and retry strategy.
- Manage transaction submission, confirmation, replacement, cancellation, and reconciliation.
- Coordinate gas, slippage, and MEV rules with the route plan.
- Persist execution history and reconcile chain results.

## Business rules
- Every execution must be risk-approved before submission.
- Execution fails closed when quote freshness, gas, slippage, or wallet readiness thresholds are invalid.
- Partial fills and partial confirmations must be tracked explicitly.
- Replacements are allowed only under fee policy and nonce safety rules.
- Reconciliation is mandatory before a plan is considered closed.
- Duplicate plan submission must be prevented by idempotency keys.

## State machine
Draft -> Validated -> Routed -> Submitted -> Confirming -> Filled | Replaced | Cancelled | Failed -> Reconciled.

### Transition rules
- Draft -> Validated only after schema validation and policy checks pass.
- Validated -> Routed only after route selection is complete.
- Routed -> Submitted only after wallet, nonce, gas, and MEV checks pass.
- Submitted -> Confirming after broadcast acknowledgement.
- Confirming -> Filled on terminal success.
- Confirming -> Replaced when fee bump or replacement policy is applied.
- Confirming -> Cancelled on explicit operator or safety cancel.
- Confirming -> Failed on irrecoverable broadcast, revert, or timeout beyond policy.
- Any terminal execution state -> Reconciled only after receipts, order records, and position updates are persisted.

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
- IPC: `execution.plan.create`, `execution.plan.submit`, `execution.plan.status`, `execution.plan.cancel`, `execution.plan.replace`, `execution.plan.reconcile`.
- Depends on: `ROUTING-ENGINE.md`, `ORDER-MANAGEMENT.md`, `TRANSACTION-LIFECYCLE.md`, `WALLET-MANAGEMENT.md`, `GAS-OPTIMISATION.md`, `SLIPPAGE-MODEL.md`, `MEV-PROTECTION.md`.

## Idempotency and retry
- `execution.plan.create` must return the same plan for the same idempotency key and immutable input snapshot.
- `execution.plan.submit` must not rebroadcast a plan already submitted under the same idempotency key.
- Retry is allowed for transient RPC or provider faults only.
- Retry backoff must be bounded and keyed by plan id.
- A retry must never relax safety, risk, or nonce validation.

## Recovery
- Retry transient RPC failures with bounded backoff.
- Replace or cancel on stale or invalidated quotes.
- Reconcile after chain reorgs before admitting new execution work.
- Idempotency keys must prevent duplicate plan submission across retries.
- If reconciliation cannot complete, mark the plan unresolved and block dependent work.

## Persistence
- Persist plan creation, route selection, submission attempts, receipts, cancellation reasons, and final terminal outcome.
- Store the execution idempotency key, route fingerprint, nonce, chain id, and correlation id.
- Persist reconciliation timestamps and recovery notes for auditability.

## Monitoring
- Plan creation latency.
- Submission success rate.
- Reorg recovery count.
- Replacement count.
- Rejection rate by validation rule.
- Duplicate submission prevention count.

## Testing
- Route selection tests.
- Partial fill tests.
- RPC failure injection.
- Reorg recovery tests.
- Duplicate submission tests.
- Idempotency replay tests.

## Cross-references
- `TRADING-ENGINE.md`
- `ORDER-MANAGEMENT.md`
- `TRANSACTION-LIFECYCLE.md`
- `DATABASE-SCHEMA.md`
- `MONITORING-OBSERVABILITY.md`
