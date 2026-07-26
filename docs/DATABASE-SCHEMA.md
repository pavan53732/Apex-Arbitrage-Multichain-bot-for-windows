# Database Schema

## Purpose
Defines persistence model, tables, indexes, retention, migrations, and backup/restore expectations.

## Ownership
- Owns durable entities, relational constraints, migrations, and retention policy.
- Transient cache data does not belong here.

## Core entities
- Settings.
- Wallets.
- Chains.
- DEXs.
- Tokens.
- Pairs.
- Opportunities.
- Strategies.
- Sessions.
- Execution plans.
- Orders.
- Transactions.
- Positions.
- Portfolio snapshots.
- AI tasks.
- Events.
- Alerts.
- Audit logs.
- Diagnostics exports.
- Prompt versions.
- Market snapshots.
- Queue records.
- Worker records.
- Recovery records.

## Persistence rules
- Each durable entity must have a stable primary key and timestamps.
- Execution and reconciliation tables must support idempotency keys.
- Audit logs are append-only.
- Sensitive material must be encrypted or stored outside the DB according to security policy.
- Lifecycle tables must include terminal-state timestamps and source correlation ids.

## Reference integrity
- Session records must reference execution plans, risk decisions, and terminal state.
- Execution plans must reference routes, orders, and transactions.
- AI tasks must reference prompt versions, model ids, and validation results.
- Queue and worker records must reference recovery and monitoring metadata.

## Migration rules
- Migrations are ordered, reversible where practical, and versioned.
- Schema changes must not break read paths for the immediately previous application version.
- Failed migrations must halt activation before live work starts.

## Retention
- Operational events may be retained shorter than financial records.
- Audit, order, execution, and position history must follow compliance retention policy.
- Low-value transient diagnostics may be pruned by retention job, but terminal state records must remain.

## Backup and restore
- Schema backup must be consistent with configuration and file exports.
- Restore must validate version compatibility before enabling writes.
- Restore must not activate partially migrated state.

## Cross-references
- `ORDER-MANAGEMENT.md`
- `TRANSACTION-LIFECYCLE.md`
- `POSITION-MANAGEMENT.md`
- `PORTFOLIO-MANAGEMENT.md`
- `STATE-MANAGEMENT.md`
- `RUNTIME-OPERATIONS.md`
