# Order Management

## Purpose
Owns order creation, validation, lifecycle tracking, amendment, cancellation, and reconciliation.

## Ownership
- Owns canonical order records and order state transitions.
- Bridges execution plans to chain transactions and settlement records.

## Responsibilities
- Create canonical order records from execution plans.
- Validate order fields before submission.
- Track order state and exchange/chain acknowledgements.
- Handle amendments, cancellations, and terminal transitions.
- Persist order audit data for reconciliation and reporting.

## State machine
Draft -> Validated -> Placed -> PartiallyFilled -> Filled -> Reconciled.
Draft -> Validated -> Cancelled -> Reconciled.
Draft -> Validated -> Rejected -> Reconciled.
Placed -> Replaced -> Placed.
Placed | PartiallyFilled -> CancelRequested -> Cancelled | Filled.

### Transition rules
- Draft -> Validated only after schema, policy, and risk pre-checks.
- Validated -> Placed only after execution engine approval.
- Placed -> PartiallyFilled when a partial fill is confirmed.
- PartiallyFilled -> Filled on complete fill or settlement completion.
- Any active order -> CancelRequested only when cancellation policy is allowed.
- CancelRequested -> Cancelled only after acknowledgement or irreversible timeout handling.
- Rejected orders are terminal and never broadcast.

## Inputs
- Execution plan.
- Chain transaction updates.
- Fill and receipt events.
- Risk and cancellation signals.

## Outputs
- Order state updates.
- Fill records.
- Cancellation and rejection reasons.
- Reconciliation events.

## Idempotency and retry
- Creating an order with the same plan id and idempotency key must reuse the existing record.
- Cancellation requests must be idempotent.
- Retry must not duplicate fill records or overwrite terminal states.

## Persistence
- Persist order id, plan id, transaction lineage, asset ids, quantities, prices, fees, state, timestamps, and reject reasons.
- Persist fill slices and partial-fill metadata.
- Persist cancellation lineage and reconciliation result.

## Failure and recovery
- If transaction and order states diverge, order reconciliation must reconcile from chain truth.
- Stale or duplicate acknowledgements must be ignored by monotonic state rules.
- Unresolved orders must be surfaced to monitoring and recovery workflows.

## Monitoring
- Order create latency.
- Fill latency.
- Partial fill rate.
- Cancellation success rate.
- Reconciliation backlog.
- State divergence count.

## Cross-references
- `EXECUTION-ENGINE.md`
- `TRANSACTION-LIFECYCLE.md`
- `DATABASE-SCHEMA.md`
- `RISK-ENGINE.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
