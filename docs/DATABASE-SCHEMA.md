# Database Schema

## Purpose
Defines persistence model, tables, indexes, retention, migrations, and backup/restore expectations.

## Responsibilities
- Own durable entities for orders, transactions, strategies, portfolios, positions, wallets, market snapshots, AI artifacts, and audit logs.
- Define primary keys, indexes, retention, and migration rules.
- Map lifecycle state to persisted records and reconciliation metadata.

## Cross-references
- `docs/ORDER-MANAGEMENT.md`
- `docs/TRANSACTION-LIFECYCLE.md`
- `docs/POSITION-MANAGEMENT.md`
- `docs/PORTFOLIO-MANAGEMENT.md`
- `docs/RUNTIME-OPERATIONS.md`
