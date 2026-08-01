---
metadata_schema_version: 1.0
document_id: DOC-0336
title: Monitoring Observability
plane: Product Specification
domain: Operations
class: Specification
authority: Canonical
status: Active
owner: Ops Team
version: 1.0.0
canonical_source: docs/apex-app-docs/operations/monitoring/monitoring-observability.md
related_concepts:
  - CONCEPT-0336
dependencies: []
consumers:
  - DOC-0399
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Operations
type: CONTRACT
purpose: "Defines metrics catalog, alert thresholds, health states, telemetry rules, dashboards, diagnostic exports, and Windows-specific observability integration for all subsystems."
scope: None
---

# Monitoring Observability

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.1.0 | **Status:** Canonical | **Last Updated:** 2026-07-27 | **Owner:** Ops Team

## Purpose
Defines metrics catalog, alert thresholds, health states, telemetry rules, dashboards, diagnostic exports, and Windows-specific observability integration for all subsystems.

---

## 1. Metrics Catalog

### 1.1 Trading Metrics

| Metric | Type | Unit | Source | Collection Interval | Alert Threshold |
|--------|------|------|--------|---------------------|-----------------|
| `trading.opportunities.detected_total` | Counter | count | Opportunity Detector | 1s | < 1/min for 30 min → stale feed warning |
| `trading.opportunities.ranked_total` | Counter | count | Opportunity Ranker | 1s | — |
| `trading.trades.started_total` | Counter | count | Trading Engine | 1s | — |
| `trading.trades.completed_total` | Counter | count | Trading Engine | 1s | — |
| `trading.trades.aborted_total` | Counter | count | Trading Engine | 1s | > 5/hr → investigation |
| `trading.trades.profit_usd_sum` | Gauge | USD | Trading Engine | 5s | Daily loss > risk.max_daily_loss_usd → Critical |
| `trading.trade_latency_p50_ms` | Histogram | ms | Trading Engine | 5s | > 1000 ms → warning |
| `trading.trade_latency_p99_ms` | Histogram | ms | Trading Engine | 5s | > 5000 ms → throttle |
| `trading.active_trades_count` | Gauge | count | Trading Engine | 1s | > trade.max_concurrent_trades → throttle |
| `trading.slippage_actual_bps_avg` | Gauge | bps | Trading Engine | 5s | > trade.slippage_tolerance_bps → warning |

### 1.2 Execution Metrics

| Metric | Type | Unit | Source | Collection Interval | Alert Threshold |
|--------|------|------|--------|---------------------|-----------------|
| `execution.legs.submitted_total` | Counter | count | Execution Engine | 1s | — |
| `execution.legs.confirmed_total` | Counter | count | Execution Engine | 1s | — |
| `execution.legs.failed_total` | Counter | count | Execution Engine | 1s | > 3/hr → investigation |
| `execution.legs.stuck_total` | Counter | count | Execution Engine | 1s | > 1/hr → nonce replacement investigation |
| `execution.confirmation_latency_p50_ms` | Histogram | ms | Execution Engine | 5s | > 5000 ms → slow chain warning |
| `execution.confirmation_latency_p99_ms` | Histogram | ms | Execution Engine | 5s | > 30000 ms → chain investigation |
| `execution.gas_used_avg` | Gauge | gas units | Execution Engine | 5s | — |
| `execution.gas_price_gwei_avg` | Gauge | gwei | Execution Engine | 5s | > 500 gwei → gas spike throttle |

### 1.3 AI Metrics

| Metric | Type | Unit | Source | Collection Interval | Alert Threshold |
|--------|------|------|--------|---------------------|-----------------|
| `ai.requests.total` | Counter | count | AI Pipeline | 1s | — |
| `ai.requests.completed_total` | Counter | count | AI Pipeline | 1s | — |
| `ai.requests.failed_total` | Counter | count | AI Pipeline | 1s | > 5/min → provider investigation |
| `ai.requests.latency_p50_ms` | Histogram | ms | AI Pipeline | 5s | > 3000 ms → warning |
| `ai.requests.latency_p99_ms` | Histogram | ms | AI Pipeline | 5s | > 10000 ms → fallback or throttle |
| `ai.tokens.input_total` | Counter | tokens | AI Pipeline | 5s | — |
| `ai.tokens.output_total` | Counter | tokens | AI Pipeline | 5s | — |
| `ai.cost.usd_sum` | Gauge | USD | AI Cost Manager | 5s | > ai.cost.max_monthly_usd → BLOCK |
| `ai.provider.fallback_total` | Counter | count | AI Pipeline | 1s | > 3 in 5 min → throttle to 1 req/min |
| `ai.memory.entries_count` | Gauge | count | AI Memory | 5s | > ai.memory.max_entries → eviction |
| `ai.context.compression_total` | Counter | count | Context Builder | 1s | > 30% of requests → review context limits |
| `ai.confidence.avg` | Gauge | 0–1 | AI Pipeline | 5s | < 0.7 → review model performance |

### 1.4 Runtime Metrics

| Metric | Type | Unit | Source | Collection Interval | Alert Threshold |
|--------|------|------|--------|---------------------|-----------------|
| `runtime.health_score` | Gauge | 0–1 | Runtime Orchestrator | 5s | < 0.5 → Safe mode |
| `runtime.mode` | State | text | Runtime Orchestrator | 1s | Unexpected mode change → investigation |
| `runtime.startup_duration_ms` | Gauge | ms | Runtime | on startup | > 60,000 ms → FAILED |
| `runtime.shutdown_duration_ms` | Gauge | ms | Runtime | on shutdown | > 30,000 ms → force terminate |
| `runtime.workers.active_count` | Gauge | count | Worker Pool | 1s | > runtime.worker.max_workers × 0.9 → scaling |
| `runtime.workers.idle_count` | Gauge | count | Worker Pool | 1s | All idle for 5 min → opportunity drought |
| `runtime.event_bus.queue_depth` | Gauge | count | Event Bus | 1s | > 80% of max → backpressure |
| `runtime.event_bus.dlq_count` | Gauge | count | Event Bus | 1s | > 100 → Critical alert |
| `runtime.recovery.duration_ms` | Gauge | ms | Recovery Coordinator | on recovery | > 120,000 ms → FAILED |
| `runtime.recovery.count` | Counter | count | Recovery Coordinator | 1s | > 3/day → stability investigation |

### 1.5 Resource Metrics

| Metric | Type | Unit | Source | Collection Interval | Alert Threshold |
|--------|------|------|--------|---------------------|-----------------|
| `resource.rss_mb` | Gauge | MB | OS stats | 5s | > 80% of limit → warning; > 100% → Critical |
| `resource.cpu_percent` | Gauge | % | OS stats | 5s | > 80% for 60s → warning |
| `resource.disk_usage_mb` | Gauge | MB | OS stats | 60s | > 90% of available → Critical |
| `resource.network.connections_active` | Gauge | count | Network Manager | 1s | > max_connections → throttle |
| `resource.network.latency_p50_ms` | Histogram | ms | Network Manager | 5s | > 1000 ms → RPC investigation |
| `resource.network.latency_p99_ms` | Histogram | ms | Network Manager | 5s | > 5000 ms → fallback RPC |

### 1.6 Plugin Metrics

| Metric | Type | Unit | Source | Collection Interval | Alert Threshold |
|--------|------|------|--------|---------------------|-----------------|
| `plugin.active_count` | Gauge | count | Plugin Manager | 1s | — |
| `plugin.crash_total` | Counter | count | Plugin Manager | 1s | > 2/5min for same plugin → disable |
| `plugin.memory_mb_avg` | Gauge | MB | Sandbox monitor | 5s | > 90% of sandbox limit → pause |
| `plugin.cpu_percent_avg` | Gauge | % | Sandbox monitor | 5s | > 90% of quota → throttle |

---

## 2. Alert Thresholds and Actions

| Alert | Condition | Severity | Action | Notification Channel |
|-------|-----------|----------|--------|----------------------|
| Trade loss exceeds daily limit | `trading.trades.profit_usd_sum` daily total < -risk.max_daily_loss_usd | Critical | Pause trading; circuit breaker; operator page | Dashboard + Notification + Event Log |
| AI cost exceeds monthly budget | `ai.cost.usd_sum` > ai.cost.max_monthly_usd | High | Block AI requests; dashboard notification | Dashboard + Event Log |
| Memory approaching limit | `resource.rss_mb` > 80% of limit | Medium | Log warning; force GC at 90%; Safe mode at 100% | Dashboard + Event Log |
| RPC connection degraded | `resource.network.latency_p99_ms` > 5000 ms | High | Switch to fallback RPC | Dashboard + Event Log |
| Event bus overflow | `runtime.event_bus.queue_depth` > 80% | Medium | Backpressure; drop low-priority | Event Log |
| DLQ overflow | `runtime.event_bus.dlq_count` > 100 | Critical | Alert operator; manual replay needed | Dashboard + All channels |
| Disk space low | `resource.disk_usage_mb` > 90% | High | Archive old data; operator alert | Dashboard + Notification |
| Trade latency spike | `trading.trade_latency_p99_ms` > 5000 ms | Medium | Reduce concurrent trades | Event Log |
| Worker pool saturated | `runtime.workers.active_count` > 90% of max | Medium | Scale workers (if under max); throttle submissions | Event Log |
| Health score critical | `runtime.health_score` < 0.3 | Critical | Safe mode; all trading disabled | All channels |

---

## 3. Windows-Specific Observability

| Integration | Method | Data | Frequency |
|-------------|--------|------|-----------|
| Windows Event Log | Write structured events for Critical/High severity | Error code, subsystem, severity, recommendation | Real-time |
| Windows Performance Counters | Register custom counters for key metrics | RSS, CPU, trade count, event depth | 5s |
| Windows Tray Icon | Display aggregate health (color: green/yellow/red) | Health score, trade count, balance summary | 5s |
| Windows Notification Center | Push critical alerts to OS notification system | Trade completed, circuit breaker, health failure | Real-time (Critical only) |
| ETW (Event Tracing for Windows) | Optional: trace-level logging for performance analysis | All events with timing data | Configurable |

---

## Cross-References

- **HEALTHCHECKS.md** — Health probe definitions and thresholds.
- **METRICS.md** — Detailed metric definitions.
- **DIAGNOSTICS.md** — Diagnostic artifact schema and workflow.
- **RECOVERY-COORDINATION.md** — Recovery coordination.
- **RESOURCE-BUDGET-SPECIFICATION.md** — Resource budgets and enforcement.
- **PERFORMANCE-TARGETS.md** — Performance SLOs.
- **CONFIGURATION-REFERENCE.md** — `resource.*`, `event.*` config keys.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.1.0 | 2026-07-27 | Full metrics catalog (50+ metrics), alert thresholds, Windows observability, health score integration | Ops Team |
| 1.0.0 | 2025-01-15 | Initial stub | Ops Team |
