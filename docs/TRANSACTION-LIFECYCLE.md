# Transaction Lifecycle

## Purpose
Defines transaction submission, confirmation, replacement, cancellation, reorg handling, and final settlement semantics.

## State machine
Created -> Signed -> Broadcast -> Pending -> Confirmed -> Finalized -> Settled | Replaced | Cancelled | Failed.

## Rules
- Transaction ids and nonce ids must be tracked separately.
- Reorgs require confirmation rollback and reconciliation.
- Replacement and cancellation must preserve nonce ordering.

## Cross-references
- `docs/EXECUTION-ENGINE.md`
- `docs/GAS-OPTIMISATION.md`
- `docs/ORDER-MANAGEMENT.md`
- `docs/DATABASE-SCHEMA.md`
