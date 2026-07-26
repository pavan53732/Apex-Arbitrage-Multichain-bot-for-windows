# Transaction Lifecycle

## Purpose
Defines transaction construction, signing, submission, confirmation, replacement, failure, and reconciliation.

## Responsibilities
- Build transaction payloads.
- Manage nonce usage and signing state.
- Track pending and final states.
- Resolve reorg and replacement outcomes.

## Business rules
- Nonces must remain strictly ordered per wallet and chain.
- Transactions that exceed safety limits must not be signed.
- Reorg recovery must preserve determinism in final accounting.

## State machine
Constructed -> Signed -> Submitted -> Pending -> Confirmed | Replaced | Dropped | Reorged | Failed -> Reconciled.

## Inputs
- Wallet state.
- Route plan.
- Execution request.
- Gas policy.

## Outputs
- Signed transactions.
- Receipts.
- Confirmation and finality events.
- Reconciliation records.

## Interfaces
- IPC: transaction.submit, transaction.status, transaction.replace, transaction.replay.
- Depends on wallet, execution, chain, monitoring, and database layers.

## Recovery
- Replay from last consistent wallet nonce after a recoverable failure.
- Reconcile receipt state after reorg or dropped transaction detection.

## Testing
- Nonce collision tests.
- Reorg and replay tests.
- Confirmation threshold tests.

