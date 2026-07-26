# Transaction Lifecycle

## Purpose
Defines on-chain transaction construction, signing, submission, confirmation, replacement, failure, and reconciliation.

## State machine
Constructed -> Signed -> Submitted -> Pending -> Confirmed | Replaced | Dropped | Reorged | Failed -> Reconciled.

## Interfaces
- IPC: transaction.submit, transaction.status, transaction.replace, transaction.replay.
- Depends on wallet, chain, execution, and monitoring.

## Testing
- Chain reorg tests.
- Nonce collision tests.

