---
metadata_schema_version: 1.0
document_id: DOC-0355
title: Capacity Planning
plane: Product Specification
domain: Performance
class: Reference
authority: Canonical
status: Active
owner: Ops Team
version: 1.0.0
canonical_source: docs/product-specification/performance/capacity-planning.md
related_concepts:
  - CONCEPT-0355
dependencies: []
consumers:
  - DOC-0049
  - DOC-0059
  - DOC-0354
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: "Defines maximum supported throughput, concurrent operations, and sizing limits for all subsystems — workers, tasks, plugins, models, wallets, strategies, chains, and events per second."
scope: Capacity Planning scope and boundaries.
---

# Capacity Planning

## Document type
Document type: [REFERENCE]

## Version
**Version:** 0.2.0 | **Status:** Draft | **Last Updated:** 2026-07-27 | **Owner:** Ops Team

## Purpose
Defines maximum supported throughput, concurrent operations, and sizing limits for all subsystems — workers, tasks, plugins, models, wallets, strategies, chains, and events per second.

---

## 1. System-Wide Capacity Limits

| Resource | Maximum | Unit | Scaling Factor |
|----------|---------|------|----------------|
| Active workers | 20 | threads | Per CPU core (4× core count recommended max) |
| Concurrent tasks | 100 | count | Per worker (5× worker count) |
| Installed plugins | 50 | count | Fixed limit |
| Active AI models | 8 | count | Per provider |
| Managed wallets | 100 | count | Fixed limit |
| Active strategies | 10 | count | Per trading engine |
| Connected chains | 20 | count | Fixed limit |
| Registered DEXes | 200 | count | Across all chains |
| Tracked tokens | 5000 | count | Across all chains |
| Events per second | 10000 | EPS | Peak throughput |
| Active event subscriptions | 500 | count | Per event bus instance |

---

## 2. Throughput Estimates

### Normal Operation

| Operation | Throughput | Latency P50 | Latency P99 |
|-----------|------------|-------------|-------------|
| Event publish | 10,000 EPS | 0.1 ms | 1 ms |
| Event consume | 5,000 EPS | 0.5 ms | 5 ms |
| Price update | 1,000 EPS (per chain) | 50 ms | 200 ms |
| Trade execution | 10 TPS | 500 ms | 2000 ms |
| AI request (no tools) | 5 RPS | 1000 ms | 5000 ms |
| AI request (with tools) | 2 RPS | 3000 ms | 10000 ms |
| Plugin invocation | 100 RPS | 10 ms | 100 ms |
| Config reload | 10 RPS | 50 ms | 200 ms |

### Peak Load

| Operation | Throughput | Latency P50 | Latency P99 |
|-----------|------------|-------------|-------------|
| Event publish | 25,000 EPS | 0.5 ms | 5 ms |
| Event consume | 10,000 EPS | 2 ms | 20 ms |
| Price update (flash crash) | 10,000 EPS | 200 ms | 1000 ms |
| Trade execution | 50 TPS | 1000 ms | 5000 ms |

---

## 3. Sizing Guidelines

### Minimum Hardware

| Component | Specification |
|-----------|---------------|
| CPU | 4 cores @ 2.0 GHz |
| RAM | 4 GB |
| Disk | 20 GB (SSD recommended) |
| Network | 100 Mbps |
| OS | Windows 10/11 64-bit, Ubuntu 22.04+, macOS 13+ |

### Recommended Hardware

| Component | Specification |
|-----------|---------------|
| CPU | 8 cores @ 3.0 GHz |
| RAM | 16 GB |
| Disk | 50 GB (NVMe SSD) |
| Network | 1 Gbps |
| GPU | 8 GB VRAM (for local AI inference) |

### Scaling Limits by Hardware

| Hardware Tier | Max Workers | Max Chains | Max Events/s | Max Trades/s |
|---------------|-------------|------------|--------------|--------------|
| Minimum | 4 | 5 | 2,000 | 2 |
| Recommended | 12 | 15 | 10,000 | 10 |
| High-end (32 GB, 16 cores) | 20 | 25 | 25,000 | 50 |

---

## 4. Concurrency Models by Load

| Load Level | Description | Worker Strategy | Queue Strategy | AI Strategy |
|------------|-------------|-----------------|----------------|-------------|
| **Idle** | No active trades, monitoring only | Min workers (2) | Minimal polling | No AI calls |
| **Normal** | 1–5 active trades, regular monitoring | Scaled to demand (2–8) | Normal event processing | AI on demand |
| **Busy** | 5–20 active trades, high volatility | Max workers (12–20) | Priority queuing | AI calls batched |
| **Peak** | 20+ trades, flash crash, many chains | All workers saturated | Backpressure active | AI calls rate-limited |

---

## 5. Plugin Capacity

| Metric | Limit | Notes |
|--------|-------|-------|
| Max installed plugins | 50 | Hard limit `plugin.max_plugins` |
| Max concurrently running plugins | 20 | Limited by worker pool |
| Max events per plugin per second | 100 | Rate-limited at plugin host |
| Max memory per plugin sandbox | 256 MB | Configurable via `plugin.sandbox.memory_limit_mb` |
| Max CPU per plugin sandbox | 10% | Configurable via `plugin.sandbox.cpu_quota_percent` |

---

## 6. AI Capacity

| Metric | Limit | Notes |
|--------|-------|-------|
| Max concurrent AI requests | 8 | Limited by AI pool size |
| Max AI requests per second | 5 | Normal operation, higher with multiple providers |
| Max tokens per request | `ai.context.max_tokens`: 8192 | Configurable |
| Max memory entries | `ai.memory.max_entries`: 1000 | Configurable |
| Max monthly AI cost | `ai.cost.max_monthly_usd`: $100 | Hard cap |

---

## 7. Storage Capacity

| Store | Max Size | Growth Rate | Retention |
|-------|----------|-------------|-----------|
| Trade history | 10 GB | 100 MB/day | 365 days |
| Event history | 5 GB | 50 MB/day | `event.retention_days`: 7 |
| AI memory store | 1 GB | 10 MB/day | `ai.memory.ttl_days`: 30 |
| Log files | 5 GB (rotated) | 50 MB/day | 30 days (compressed) |
| Workspace state | 500 MB | 5 MB/day | Until workspace deleted |
| Audit log | 2 GB | 20 MB/day | `security.audit.retention_days`: 365 |

---

## 8. Monitoring & Alerting Thresholds

| Metric | Warning | Critical | Action |
|--------|---------|----------|--------|
| CPU usage | > 60% for 5 min | > 80% for 2 min | Scale back workers, throttle AI |
| RAM usage | > 70% | > 90% | Force memory cleanup, pause plugins |
| Event queue depth | > 5000 | > 8000 | Backpressure, drop low-priority |
| Trade latency P99 | > 2000 ms | > 5000 ms | Reduce concurrent trades |
| AI latency P99 | > 5000 ms | > 10000 ms | Fall back to faster model |
| Disk usage | > 70% | > 90% | Archive old data, alert operator |

---

## Cross-References

- **RESOURCE-BUDGET-SPECIFICATION.md** — Per-subsystem resource budgets.
- **PERFORMANCE-TARGETS.md** — Performance SLOs and targets.
- **MONITORING-OBSERVABILITY.md** — Alerting and dashboard metrics.
- **WORKER-POOL.md** — Worker pool scaling.
- **CONCURRENCY-MODEL.md** — Concurrency primitives and limits.
- **CONFIGURATION-REFERENCE.md** — Capacity-related config keys.
- **DATABASE-SCHEMA.md** — Storage sizing.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 0.2.0 | 2026-07-27 | Complete capacity plan with throughput estimates, sizing, storage, monitoring | Ops Team |
| 0.1.0 | 2026-07-27 | Initial stub | Ops Team |
