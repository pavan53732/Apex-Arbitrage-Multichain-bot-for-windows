# Transaction Lifecycle

## Purpose
Defines submission, confirmation, replacement, cancellation, and finality handling for chain transactions.

## Ownership
- Owns transaction state, receipt tracking, replacement, cancellation, and finality boundaries.
- Does not own trade ranking or risk policy.

## Missing details covered
- Replacement logic must define nonce bumping and retry limits.
- Persistence must define how state survives Windows restarts.
- Recovery must define reorg, pending, and failed transaction handling.

## Cross-references
- `EXECUTION-ENGINE.md`
- `DATABASE-SCHEMA.md`
- `GAS-OPTIMISATION.md`
- `WALLET-MANAGEMENT.md`
