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
- Health updates must always include the source subsystem and the observed state transition.

## Event and IPC ownership
- `monitoring.health.*` events originate from this subsystem.
- `monitoring.alert.*` events are emitted for operator-visible alerts.
- Diagnostics exports are triggered via explicit IPC commands from operator tools.
- Monitoring may subscribe to all subsystem health events but must not mutate operational state.

## Failure and recovery
- Monitoring failures must fail open and never block trading, but they must surface their own health degradation.
- Alert delivery failures must be retried with bounded backoff; unresolved failures must be visible in the UI.
- If telemetry transport is unavailable, buffer only within bounded limits and then drop with explicit counters.

## Persistence
- Persist alert history, health snapshots, and diagnostic export metadata for audit and debugging.
- Do not persist raw secrets, private keys, or full transaction payloads.
- Persist alert acknowledgements and resolution timestamps when available.

## Monitoring
- Metric emission success rate.
- Alert volume by severity.
- Time-to-detect and time-to-acknowledge critical failures.
- Health-state transition counts per subsystem.
- Diagnostic export success rate.
- Telemetry buffer saturation.

## Cross-references
- `ERROR-HANDLING-LOGGING.md`
- `RUNTIME-OPERATIONS.md`
- `PERFORMANCE-TARGETS.md`
- `SECURITY.md`
- `TRADING-ENGINE.md`
- `EXECUTION-ENGINE.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Windows telemetry
- Must define Event Log and Windows performance telemetry integration.

## Required details
- Define Event Log, counters, dashboards, and alerting.
