# Monitoring and Observability

## Purpose
Defines health checks, telemetry, diagnostics, alerts, and operator-facing observability for all subsystems.

## Ownership
- Owns metrics, traces, health states, alerts, dashboards, and diagnostic exports.
- Consumes error taxonomy and runtime operations status.

## Health states
Healthy, Degraded, Recovering, Unhealthy, Stopped.

## Responsibilities
- Publish subsystem health in a consistent schema.
- Track latency, throughput, rejection, failure, and recovery metrics.
- Emit actionable alerts with stable reason codes.
- Provide diagnostics suitable for support and postmortem analysis.

## Telemetry rules
- Metrics must be namespaced by subsystem and environment.
- High-cardinality labels must be bounded.
- Sensitive values must be redacted before export.
- Alert payloads must include subsystem, severity, reason code, and recommended operator action.

## Event and IPC ownership
- `monitoring.health.*` events originate from this subsystem.
- `monitoring.alert.*` events are emitted for operator-visible alerts.
- Diagnostics exports are triggered via explicit IPC commands from operator tools.

## Failure and recovery
- Monitoring failures must fail open (never block trading) but must surface their own health degradation.
- Alert delivery failures must be retried with bounded backoff; unresolved failures must be visible in the UI.

## Persistence
- Persist alert history, health snapshots, and diagnostic export metadata for audit and debugging.
- Do not persist raw secrets, private keys, or full transaction payloads.

## Monitoring
- Metric emission success rate.
- Alert volume by severity.
- Time-to-detect and time-to-acknowledge critical failures.
- Health-state transition counts per subsystem.

## Cross-references
- `ERROR-HANDLING-LOGGING.md`
- `RUNTIME-OPERATIONS.md`
- `PERFORMANCE-TARGETS.md`
- `SECURITY.md`
- `TRADING-ENGINE.md`
- `EXECUTION-ENGINE.md`
