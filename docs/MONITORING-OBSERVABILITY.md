# MONITORING-OBSERVABILITY.md

## Purpose
Defines runtime health, telemetry, diagnostics, metrics, and alerting behavior for the APEX desktop application.

## Scope
Covers application health checks, performance monitoring, AI provider diagnostics, chain connectivity metrics, execution telemetry, local diagnostics, and support bundles.

## Related Documents
- [ERROR-HANDLING-LOGGING.md](./ERROR-HANDLING-LOGGING.md)
- [PERFORMANCE-TARGETS.md](./PERFORMANCE-TARGETS.md)
- [WINDOWS-DESKTOP.md](./WINDOWS-DESKTOP.md)

## Health Domains
- app boot health
- database health
- AI provider health
- RPC connectivity health
- strategy scheduler health
- execution pipeline health
- updater health

## Core Metrics
- app start time
- renderer ready time
- DB query latency
- RPC latency by chain
- quote freshness
- provider response latency
- provider error rate
- strategy scan cycle duration
- opportunities generated vs executed
- risk rejections by reason

## Diagnostics Bundle
Support export may include:
- redacted logs
- version/build metadata
- enabled providers/chains (without secrets)
- feature flags
- error summaries
- health-check snapshots

## Alerting Model
APEX is desktop-local first. Alerts should be:
- in-app status indicators,
- warning banners,
- local notifications for critical user action,
- optional future webhook/email integration only if specified elsewhere.
