# Runtime Operations

## Purpose
Defines worker lifecycle, scheduler behavior, queue management, orchestration, caching, plugins, extension handling, recovery workflows, failover, backup, restore, upgrade, migration, health monitoring, telemetry, diagnostics, logging, and alerting.

## Shared runtime contract
All background services must define lifecycle, inputs, outputs, failure handling, retry policy, monitoring, and recovery behavior.

## Worker lifecycle
Init -> Ready -> Running -> Degraded -> Recovering -> Running -> Stopped.

## Scheduler
The scheduler triggers delayed, recurring, and safety-critical jobs according to policy and priority.

## Queue management
Queues must preserve priority, durability, and backpressure behavior.

## Task orchestration
Tasks may be chained only when dependencies and recovery points are explicit.

## Cache lifecycle
Cache entries must define creation, freshness, invalidation, and rebuild policy.

## Synchronisation
Shared state must remain consistent across worker boundaries and survive process restart.

## Plugin architecture
Plugins must declare capabilities, lifecycle hooks, and failure boundaries.

## Extension framework
Extensions may add capabilities only through approved interfaces.

## Recovery workflows
Recovery must restore consistent state before live work resumes.

## Failover
Failover should promote a safe standby or degrade safely if standby is unavailable.

## Backup and restore
Backups must be verifiable and restore must replay consistency checks before release.

## Upgrade and migration
Upgrades must preserve schema compatibility or provide explicit migration steps.

## Health monitoring
Health must capture process liveness, queue pressure, and subsystem readiness.

## Telemetry
Telemetry must expose latency, queue depth, worker health, retry counts, and recovery duration.

## Diagnostics
Diagnostics must preserve traces, counters, and failure reason codes.

## Logging
Logging must be structured, timestamped, and correlated with request IDs.

## Alerting
Alerts fire on worker failure, backlog growth, safety-state change, backup failure, or restore failure.

## Cross-references
- `MONITORING-OBSERVABILITY.md`
- `ERROR-HANDLING-LOGGING.md`
- `SIMULATION-ENGINE.md`
- `USER-FLOWS.md`
