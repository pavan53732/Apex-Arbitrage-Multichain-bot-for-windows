# Transaction Lifecycle

## Purpose
Defines submission, confirmation, replacement, cancellation, and finality handling for chain transactions.

## Ownership
- Owns chain transaction state, receipt tracking, replacement, cancellation, and finality boundaries.
- Consumes execution plans and wallet state.

## Responsibilities
- Track nonce, submission, receipt, confirmation, replacement, cancellation, and reorg handling.
- Coordinate with gas optimisation and execution owners.
- Publish canonical transaction lifecycle events.

## State machine
Created -> Signed -> Submitted -> Pending -> Confirmed -> Finalized -> Settled.
Created -> Signed -> Submitted -> Pending -> Replaced -> Pending.
Submitted | Pending -> Cancelled.
Submitted | Pending -> Failed.
Pending -> ReorgObserved -> Pending | Failed.

### Transition rules
- Created -> Signed only after wallet authorization.
- Signed -> Submitted only after the broadcast request is accepted.
- Submitted -> Pending after node acceptance or mempool acknowledgement.
- Pending -> Confirmed on receipt inclusion.
- Confirmed -> Finalized after finality threshold is met.
- Finalized -> Settled after reconciliation and downstream persistence.
- Pending -> Replaced only when a higher-priority replacement is accepted.
- Pending -> Cancelled only when cancellation policy succeeds before final inclusion.
- Any non-terminal path must preserve nonce monotonicity.

## Inputs
- Signed transaction payload.
- Nonce state.
- Chain id and fee state.
- Receipt and confirmation updates.
- Reorg and finality signals.

## Outputs
- Transaction lifecycle events.
- Receipt records.
- Finality status.
- Reorg recovery tasks.

## Idempotency and retry
- Signed payload submission must be keyed by transaction hash or deterministic submission id.
- Duplicate submission requests must resolve to the same transaction record.
- Retry may only occur for transient broadcast failure before terminal acceptance.
- Replacement requests must preserve lineage to the original transaction record.

## Failure and recovery
- Broadcast failure returns a retryable or terminal error code.
- Receipt absence beyond policy triggers polling, then escalation.
- Reorg detection must move the transaction back to pending or failed, never directly to settled.
- Finality uncertainty requires explicit unresolved state rather than silent success.

## Persistence
- Persist hashes, nonce, chain id, sender, destination, value, calldata summary, fee fields, status, timestamps, and lineage.
- Persist receipt, revert reason, confirmation count, and finality metadata.
- Store only references to sensitive signing context, never raw secrets.

## Monitoring
- Broadcast latency.
- Confirmation latency.
- Finality latency.
- Reorg count.
- Replacement count.
- Cancellation count.
- Retry count by failure class.

## Cross-references
- `EXECUTION-ENGINE.md`
- `GAS-OPTIMISATION.md`
- `CHAIN-INTEGRATION.md`
- `DATABASE-SCHEMA.md`
