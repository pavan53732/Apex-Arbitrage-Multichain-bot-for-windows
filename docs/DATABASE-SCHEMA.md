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
- Strategy versions.
- Sessions.
- Session states.
- Execution plans.
- Execution attempts.
- Orders.
- Transactions.
- Transaction receipts.
- Positions.
- Portfolio snapshots.
- AI tasks.
- AI prompts.
- AI prompt versions.
- AI decisions.
- Events.
- Alerts.
- Audit logs.
- Diagnostics exports.
- Market snapshots.
- Feature snapshots.
- Score snapshots.
- Queue records.
- Worker records.
- Scheduler records.
- Cache metadata.
- Recovery records.
- Backup records.
- Migration records.

## Persistence rules
- Each durable entity must have a primary key, timestamps, and a version or hash field where replay matters.
- Every stateful lifecycle must persist terminal state, reason code, and correlation id.
- Strategy, AI, execution, and session records must link by snapshot id and correlation id.
- No transient runtime cache may be the only source of truth for a durable state transition.

## Relational rules
- Execution plans must reference a strategy version and session id.
- Orders must reference an execution plan.
- Transactions must reference an order and chain.
- AI decisions must reference prompt version, model, provider, and context hash.
- Market scores must reference snapshot id and feature snapshot hash.
- Alerts must reference subsystem and reason code.
- Recovery records must reference affected entities and resolution state.

## Indexing rules
- Index by correlation id, snapshot id, terminal state, and created timestamp.
- Index AI tasks by provider, model, and decision state.
- Index execution and transaction tables by chain id and status.

## Retention
- Keep audit and recovery records according to policy.
- Keep operational snapshots long enough for replay, reconciliation, and incident analysis.
- Prune ephemeral history only after durable rollup.

## Migrations
- Migrations must be versioned, reversible where possible, and idempotent.
- Schema changes must preserve replay compatibility for active histories.
- Breaking changes require explicit compatibility notes in the migration record.

## Backup and restore
- Backups must include all durable entities and referential metadata.
- Restore must validate foreign keys, versions, and hash integrity before the system resumes live work.
- Restored state must reconcile with chain and runtime state before execution continues.

## Cross-references
- `TRADING-ENGINE.md`
- `EXECUTION-ENGINE.md`
- `AI-PIPELINE.md`
- `MARKET-DATA.md`
- `MARKET-INTELLIGENCE.md`
- `RUNTIME-OPERATIONS.md`
- `USER-FLOWS.md`
- `VERSIONING.md`
