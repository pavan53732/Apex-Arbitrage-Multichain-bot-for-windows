# Runtime Operations

## Purpose
Defines workers, scheduling, queues, failover, backups, restore, upgrades, and diagnostics.

## Ownership
- Owns worker lifecycle, scheduler policy, queue orchestration, cache maintenance, failover, backup, restore, upgrade, and migration workflows.
- Consumes monitoring, logging, configuration, and recovery owners.

## Responsibilities
- Start and stop background workers deterministically.
- Schedule recurring and one-off tasks.
- Route jobs through typed queues with retry and dead-letter handling.
- Maintain cache invalidation and state synchronization.
- Execute restore, upgrade, and migration steps in a safe order.
- Surface health, diagnostics, and alerts.

## Worker lifecycle
Stopped -> Starting -> Ready -> Busy -> Draining -> Stopped.
Failure paths: Ready -> Failed -> Recovering -> Ready or Stopped.

### Transition rules
- Starting -> Ready only after configuration validation, dependency checks, and warmup complete.
- Ready -> Busy only when a queued job is assigned.
- Busy -> Draining when shutdown or maintenance is requested.
- Any state -> Failed when a worker encounters an unrecoverable fault.
- Failed -> Recovering when automated restart is allowed.
- Recovering -> Ready only after health checks pass.
- Recovering -> Stopped when recovery budget is exceeded or operator stop is requested.

## Scheduler model
- Tasks have id, owner, priority, run window, retry policy, timeout, and concurrency class.
- Higher priority tasks may preempt lower priority queued work only when safe.
- Scheduler must avoid duplicate execution of idempotent jobs.
- Scheduler decisions must be reproducible from task metadata and current state.

## Queue management
- Separate queues for market data, AI, execution, reconciliation, alerts, and maintenance.
- Each queue has bounded concurrency and bounded retry.
- Poison messages move to dead-letter storage with reason codes.
- Queue state changes must emit durable events for monitoring and recovery.

## Cache lifecycle
- Warm on startup where safe.
- Invalidate on chain, provider, strategy, or configuration changes.
- Expire stale market and quote data by TTL.

## Failover and recovery
- Prefer local recovery before operator escalation.
- Restart failed workers with backoff and circuit breaking.
- Fail closed for execution, wallet, and risk queues.
- Promote fallback workers only after primary health degrades below threshold.

## Backup and restore
- Back up configuration, strategy definitions, database snapshots, and exports.
- Restore must validate version compatibility before activation.
- Restore must not activate partially migrated state.

## Upgrade and migration
- Migrations run before application activation.
- Failed migrations must halt startup and leave previous state intact.
- Upgrade tasks must be idempotent and auditable.

## Diagnostics
- Health checks, telemetry, logs, queue depth, and worker status are exposed through operator APIs.
- Diagnostics exports must preserve correlation ids and avoid secrets.

## Cross-references
- `MONITORING-OBSERVABILITY.md`
- `ERROR-HANDLING-LOGGING.md`
- `CONFIGURATION.md`
- `DATABASE-SCHEMA.md`
- `DEPLOYMENT.md`
- `QUEUE-MANAGEMENT.md`
- `RECOVERY-AND-FAILOVER.md`
- `WORKER-ARCHITECTURE.md`
