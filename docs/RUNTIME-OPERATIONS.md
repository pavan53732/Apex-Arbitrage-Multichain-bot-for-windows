# Runtime Operations

## Purpose
Defines worker lifecycle, scheduling, queues, orchestration, cache, plugins, recovery, failover, backup, restore, upgrade, migration, health monitoring, telemetry, diagnostics, logging, and alerting.

## Ownership
- Owns runtime orchestration, worker lifecycle, scheduling, queues, cache coordination, failover, and operational tooling.
- Does not own trading rules, AI policy, or risk policy.

## Worker lifecycle
Stopped -> Starting -> Warmup -> Ready -> Busy -> Draining -> Stopped.

## Scheduler
- Schedules time-based, priority-based, and dependency-based jobs.
- Must honor execution-critical priority over enrichment tasks.

## Queue management
- Queues are ordered, bounded, and observable.
- Dead-letter queues capture unrecoverable tasks.
- Retries must be idempotent and bounded.

## Task orchestration
For authoritative runtime state machine and orchestration flow, see `ORCHESTRATOR.md`.

## Cache lifecycle
Warm -> Active -> Expiring -> Invalidated -> Purged.

## Synchronisation
- Shared state must be synchronised via authoritative main-process state.
- Renderer and workers consume replicated state, not source-of-truth state.

## Plugin architecture
- Plugins are allowlisted, signed, and capability-scoped.
- Extension points require documented contracts and versioning.

## Recovery workflows
- Rebuild authoritative state from persistence.
- Reconcile queue and worker state before resuming.
- Block live work when recovery is incomplete.

## Failover
- Fail over to standby workers or providers when healthy replacements exist.
- Fail closed when no safe replacement exists.

## Backup and restore
- Backups must be versioned, encrypted, and verifiable.
- Restore must validate integrity before re-admission.

## Upgrade and migration
- Upgrades are staged, reversible, and compatibility checked.
- Migrations must be idempotent and auditable.

## Health monitoring
- Worker health.
- Queue depth.
- Scheduler lag.
- Cache hit rate.
- Recovery state.

## Telemetry
- Counters, gauges, histograms, and event traces.
- High-cardinality labels must be controlled.

## Diagnostics
- Support bundle generation.
- State snapshot export.
- Failure timeline.

## Logging
- Structured, correlation-id-based, and redacted.

## Alerting
- Queue saturation.
- Worker churn.
- Recovery failure.
- Upgrade failure.

## Cross-references
- `MONITORING-OBSERVABILITY.md`
- `DATABASE-SCHEMA.md`
- `AI-PIPELINE.md`
- `TRADING-ENGINE.md`
- `VERSIONING.md`
- `AI-COST-MANAGEMENT.md`

- `HEALTHCHECKS.md`


For runtime state transitions and failover probes, see `ORCHESTRATOR.md` and `HEALTHCHECKS.md`.


## Enterprise Contract – Runtime Operations
- Interfaces: `INTERFACE-AGENT-MESSAGE.md`, `INTERFACE-NOTIFICATION-CHANNEL.md`.
- State machine: `ORCHESTRATOR.md`, `SHUTDOWN-LIFECYCLE.md`.
- Security boundaries: `SECURITY-CONTRACTS.md`.
- Performance SLOs: `PERFORMANCE-SLOS.md`.
- Failure modes: worker failure, queue backlog, shutdown interruption; recover via drain, checkpoint, retry, and alerting.

For orchestrator sequencing, see `ORCHESTRATOR.md`.
For health probes, see `HEALTHCHECKS.md`.
For recovery logic, see `RECOVERY-AND-FAILOVER.md`.
For shutdown semantics, see `SHUTDOWN-LIFECYCLE.md`.