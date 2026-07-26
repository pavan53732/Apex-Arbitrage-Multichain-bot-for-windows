# MONITORING-OBSERVABILITY.md

## Purpose
Defines how APEX measures health, performance, diagnostics, and operational visibility.

## Scope
Metrics, health checks, telemetry, diagnostics, alert conditions, local observability, and optional external reporting.

## Health Domains
- app startup health
- main/renderer bridge health
- database health
- chain RPC health
- DEX quote health
- AI provider health
- updater health
- strategy scheduler health

## Core Metrics
| Metric | Type | Description |
|---|---|---|
| `app_startup_ms` | histogram | time from process start to ready UI |
| `ipc_roundtrip_ms` | histogram | end-to-end IPC latency |
| `ai_request_ms` | histogram | provider latency |
| `ai_request_failures_total` | counter | failed provider requests |
| `rpc_request_ms` | histogram | chain RPC latency |
| `quote_success_rate` | gauge/derived | successful quotes over window |
| `db_query_ms` | histogram | DB operation latency |
| `risk_rejections_total` | counter | rejected operations by risk engine |
| `strategy_runs_total` | counter | strategy evaluations executed |
| `unhandled_errors_total` | counter | last-resort failures |

## Health Check Requirements
- startup self-check validates config, DB access, secure storage, and provider readiness.
- each external dependency should expose a probe result and last-success timestamp.
- degraded mode must be visible in UI diagnostics.

## Telemetry Rules
- local-first diagnostics by default.
- external telemetry optional and opt-in where required.
- no secrets or raw prompts in telemetry payloads.
- telemetry must honor privacy and security policy.

## Alert Conditions
- repeated provider failure over threshold,
- repeated RPC timeout over threshold,
- IPC contract mismatch,
- DB migration failure,
- risk circuit breaker activation,
- unexpected renderer crash loop.

## Diagnostics UI
Renderer should offer a diagnostics page showing:
- versions,
- provider health,
- chain health,
- DB path/status,
- last sync times,
- redacted recent errors.

## Cross-References
- [`ERROR-HANDLING-LOGGING.md`](./ERROR-HANDLING-LOGGING.md)
- [`PERFORMANCE-TARGETS.md`](./PERFORMANCE-TARGETS.md)
- [`WINDOWS-DESKTOP.md`](./WINDOWS-DESKTOP.md)
- [`BUILD-RELEASE-CICD.md`](./BUILD-RELEASE-CICD.md)
