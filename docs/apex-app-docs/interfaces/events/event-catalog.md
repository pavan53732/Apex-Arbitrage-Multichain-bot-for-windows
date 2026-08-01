---
metadata_schema_version: 1.0
document_id: DOC-0363
title: Event Catalog
plane: Product Specification
domain: Interfaces
class: Reference
authority: Reference
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/interfaces/events/event-catalog.md
related_concepts:
  - CONCEPT-0253
dependencies:
  - DOC-0253
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Reference
owned_domains: []
type: REFERENCE
purpose: "Canonical registry of all platform events — including payload fields, producers, consumers, versioning rules, delivery guarantees, ordering constraints, retention, and ownership linkage."
scope: None
---

# Event Catalog

## Document type
Document type: [REFERENCE]

## Version
**Version:** 0.2.0 | **Status:** Draft | **Last Updated:** 2026-07-27 | **Owner:** Runtime Team

## Purpose
Canonical registry of all platform events — including payload fields, producers, consumers, versioning rules, delivery guarantees, ordering constraints, retention, and ownership linkage.

---

## 1. Event Category Index

Events are organized into categories. Each category has a prefix and a canonical owner.

| Category | Prefix | Owner | Delivery Guarantee | Priority | Retention |
|----------|--------|-------|-------------------|----------|-----------|
| Trading | `trade.` | Trading Engine | Exactly-once | Critical | 365 days |
| Execution | `execution.` | Execution Engine | Exactly-once | Critical | 90 days |
| Risk | `risk.` | Risk Engine | Exactly-once | Critical | 90 days |
| System | `system.` | Runtime Orchestrator | At-least-once | High | 30 days |
| Security | `security.` | Security Manager | Exactly-once | Critical | 365 days |
| Network | `network.` | Network Manager | At-least-once | High | 7 days |
| AI | `ai.` | AI Pipeline | At-least-once | Medium | 30 days |
| Plugin | `plugin.` | Plugin Manager | At-least-once | Medium | 30 days |
| Dashboard | `dashboard.` | Dashboard Shell | At-least-once | Low | 7 days |
| Config | `config.` | Config Manager | At-least-once | Medium | 7 days |
| Health | `health.` | Health Checker | At-least-once | Low | 7 days |

---

## 2. Event Definitions

### 2.1 Trading Events
| Event | Payload | Producer | Consumer(s) | Ordering Key |
|-------|---------|----------|-------------|--------------|
| `trade.opportunity.detected` | `{opportunity_id, strategy_id, chains, pairs, spread, profit_est, ts}` | Opportunity Scanner | Trading Engine, Risk Engine | `opportunity_id` |
| `trade.risk.checked` | `{trade_id, checks: [{name, passed, value, limit}], result}` | Risk Engine | Trading Engine | `trade_id` |
| `trade.started` | `{trade_id, wallet_id, strategy_id, chain_ids, amount, ts}` | Trading Engine | Event Store, Dashboard, Notification | `trade_id` |
| `trade.leg.executing` | `{trade_id, leg, chain, tx_hash, ts}` | Execution Engine | Trading Engine, Event Store | `trade_id` |
| `trade.leg.confirmed` | `{trade_id, leg, chain, tx_hash, block_number, gas_used, ts}` | Execution Engine | Trading Engine, Risk Engine | `trade_id` |
| `trade.leg.failed` | `{trade_id, leg, chain, reason, retry_count, ts}` | Execution Engine | Trading Engine, Risk Engine | `trade_id` |
| `trade.completed` | `{trade_id, profit_usd, gas_total_usd, duration_ms, legs: [...]}` | Trading Engine | Event Store, Dashboard, Notification | `trade_id` |
| `trade.aborted` | `{trade_id, reason, leg_in_progress, recovery_action, ts}` | Trading Engine | Event Store, Dashboard, Notification | `trade_id` |

### 2.2 Execution Events
| Event | Payload | Producer | Consumer(s) | Ordering Key |
|-------|---------|----------|-------------|--------------|
| `execution.submitted` | `{exec_id, trade_id, leg, chain, tx_hash, nonce, ts}` | Execution Engine | Trading Engine | `exec_id` |
| `execution.confirmed` | `{exec_id, trade_id, leg, chain, tx_hash, block_number, confirmations, gas_used, ts}` | Execution Engine | Trading Engine | `exec_id` |
| `execution.reverted` | `{exec_id, trade_id, leg, chain, tx_hash, revert_reason, block_number, ts}` | Execution Engine | Trading Engine, Risk Engine | `exec_id` |
| `execution.stuck` | `{exec_id, trade_id, chain, tx_hash, mempool_time_ms, ts}` | Execution Engine | Trading Engine | `exec_id` |
| `execution.retried` | `{exec_id, trade_id, leg, attempt, new_tx_hash, gas_price_multiplier, ts}` | Execution Engine | Trading Engine | `exec_id` |

### 2.3 Risk Events
| Event | Payload | Producer | Consumer(s) | Ordering Key |
|-------|---------|----------|-------------|--------------|
| `risk.check.passed` | `{trade_id, check_name, value, limit, ts}` | Risk Engine | Trading Engine | `trade_id` |
| `risk.check.failed` | `{trade_id, check_name, value, limit, reason_code, ts}` | Risk Engine | Trading Engine | `trade_id` |
| `risk.circuit_breaker.tripped` | `{breaker_type, chain_or_subsystem, cooloff_ms, trigger_value, threshold, ts}` | Risk Engine | Trading Engine, Runtime | `breaker_type` |
| `risk.circuit_breaker.reset` | `{breaker_type, chain_or_subsystem, cooloff_duration_ms, ts}` | Risk Engine | Trading Engine | `breaker_type` |

### 2.4 System Events
| Event | Payload | Producer | Consumer(s) | Ordering Key |
|-------|---------|----------|-------------|--------------|
| `system.startup.phase` | `{phase_id, phase_name, duration_ms, status}` | Runtime | Dashboard, Audit | `phase_id` |
| `system.shutdown.phase` | `{phase_id, phase_name, duration_ms, status}` | Runtime | Dashboard, Audit | `phase_id` |
| `system.mode.transition` | `{from_mode, to_mode, reason}` | Runtime | Dashboard, Audit | — |
| `system.recovery.completed` | `{scan_id, trades_recovered, trades_lost, critical_errors}` | Runtime | Dashboard, Notification | `scan_id` |
| `system.error` | `{error_code, subsystem, message, severity, stack_trace}` | Any | Runtime, Event Store, Dashboard | `error_code` |
| `system.warning` | `{warning_code, subsystem, message, severity}` | Any | Runtime, Event Store | `warning_code` |

### 2.5 Security Events
| Event | Payload | Producer | Consumer(s) | Ordering Key |
|-------|---------|----------|-------------|--------------|
| `security.violation` | `{violation_id, severity, domain_from, domain_to, reason, ts}` | Security Gateway | Runtime, Audit, Notification | `violation_id` |
| `secret.created` | `{secret_id, classification, owner, ts}` | Secret Manager | Audit | `secret_id` |
| `secret.rotated` | `{secret_id, classification, old_id, new_id, ts}` | Secret Manager | Audit, Notification | `secret_id` |
| `secret.expired` | `{secret_id, classification, expiry_ts}` | Secret Manager | Audit, Dashboard | `secret_id` |
| `secret.compromised` | `{secret_id, classification, severity, ts}` | Secret Manager | Runtime, Audit, Notification | `secret_id` |

### 2.6 Network Events
| Event | Payload | Producer | Consumer(s) | Ordering Key |
|-------|---------|----------|-------------|--------------|
| `network.rpc.connected` | `{chain_id, endpoint, latency_ms, ts}` | Network Manager | Health, Registry | `chain_id` |
| `network.rpc.disconnected` | `{chain_id, endpoint, reason, ts}` | Network Manager | Health, Runtime | `chain_id` |
| `network.rpc.error` | `{chain_id, endpoint, error_code, retry_count, ts}` | Network Manager | Health | `chain_id` |

### 2.7 AI Events
| Event | Payload | Producer | Consumer(s) | Ordering Key |
|-------|---------|----------|-------------|--------------|
| `ai.request.started` | `{request_id, requestor, intent, model, ts}` | AI Pipeline | AI Provider, Audit | `request_id` |
| `ai.request.completed` | `{request_id, model, latency_ms, tokens_used, cost_usd, ts}` | AI Pipeline | AI Performance | `request_id` |
| `ai.provider.failed` | `{request_id, provider, model, error_code, fallback_triggered, ts}` | AI Pipeline | AI Provider Manager | `provider` |
| `ai.provider.switched` | `{request_id, from_provider, to_provider, reason, ts}` | AI Pipeline | AI Provider Manager | — |

### 2.8 Plugin Events
| Event | Payload | Producer | Consumer(s) | Ordering Key |
|-------|---------|----------|-------------|--------------|
| `plugin.loaded` | `{plugin_id, name, version, capabilities, ts}` | Plugin Manager | Runtime, Dashboard | `plugin_id` |
| `plugin.unloaded` | `{plugin_id, name, reason, ts}` | Plugin Manager | Runtime, Dashboard | `plugin_id` |
| `plugin.crashed` | `{plugin_id, name, exit_code, last_words, ts}` | Plugin Manager | Runtime, Dashboard, Notification | `plugin_id` |
| `plugin.violation` | `{plugin_id, name, capability, violation, ts}` | Plugin Manager | Security, Runtime | `plugin_id` |

---

## 3. Delivery Guarantees

| Guarantee | Description | Used For |
|-----------|-------------|----------|
| **Exactly-once** | Event is delivered exactly one time. Producer stores until consumer acks + commits. | Trading, execution, risk, security events |
| **At-least-once** | Event may be delivered more than once (idempotent consumers). | System, network, AI, plugin, dashboard, config events |
| **Best-effort** | Event may be lost. No recovery if not delivered. | Health events, non-critical telemetry |

---

## 4. Ordering Rules

- Events with the same **ordering key** are delivered in FIFO order within a single SPSC channel.
- Events without an ordering key are distributed across multiple channels (unordered relative to each other).
- Cross-key ordering is not guaranteed (events with different keys may arrive in any order).
- Consumers must handle out-of-order delivery across keys by checking sequence numbers.

### Sequence Number Scheme
```
event_seq = monotonic counter (per producer per channel)
trade_seq  = trade._ events are sequenced by trade lifecycle step (0, 1, 2...)
```

---

## 5. Dead-Letter Queue (DLQ)

| Property | Value |
|----------|-------|
| Max retries before DLQ | `event.dead_letter_max_retries`: 3 |
| DLQ storage | Persistent (SQLite table `dead_letter_queue`) |
| DLQ replay | Manual via operator dashboard or `POST /api/admin/events/replay` |
| Auto-purge | After 90 days (or on explicit operator ack) |
| DLQ alert | `system.warning` event when DLQ exceeds 100 entries |

---

## 6. Event Version Compatibility

| Version Scheme | Used For | Compatibility |
|----------------|----------|---------------|
| Semantic (major.minor) | All events | Same major version: backward-compatible |
| Field additions | Producer adds optional fields | Consumer ignores unknown fields |
| Field removals | Major version bump | Consumer must migrate |
| Schema registry | All events registered in schema registry | Breaking changes require schema-registry review |

---

## Cross-References

- **EVENT-OWNERSHIP-MATRIX.md** — Publisher/consumer mapping, delivery guarantees, ordering, priority.
- **EVENT-SCHEMA-REGISTRY.md** (future) — Event schema definitions and versioning. Not yet authored; tracked as a known forward reference, not a broken link, per the Repository Canonicality Repair's identifier-normalization remediation.
- **TRADING-ENGINE.md** — Trade event flow.
- **CONFIGURATION-REFERENCE.md** — Event config keys (`event.*`).
- **TRACEABILITY-MATRIX.md** — Event requirement coverage.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 0.2.0 | 2026-07-27 | Full event catalog with 40+ event definitions, delivery guarantees, ordering, DLQ, versioning | Runtime Team |
| 0.1.0 | 2026-07-27 | Initial stub | Runtime Team |
