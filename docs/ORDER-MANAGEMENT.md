# Order Management

## Purpose
Owns order creation, validation, lifecycle tracking, amendment, cancellation, and reconciliation.

## Responsibilities
- Map execution plans to order records.
- Track open, pending, partial, filled, cancelled, rejected, and reconciled states.
- Maintain order-execution linkage and audit trail.
- Drive downstream transaction lifecycle records when order execution is chain-based.

## Cross-references
- `docs/EXECUTION-ENGINE.md`
- `docs/TRANSACTION-LIFECYCLE.md`
- `docs/DATABASE-SCHEMA.md`
