---
type: REFERENCE
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Maps publishers, consumers, delivery guarantees, ordering, priority, and retention for every event in the system.
scope: None
last_updated: 2026-07-29
canonical_source: docs/EVENT-OWNERSHIP-MATRIX.md
---

# Event Ownership Matrix

## Document type
Document type: [REFERENCE]

## Version
**Version:** 0.2.0 | **Status:** Draft | **Last Updated:** 2026-07-27 | **Owner:** Runtime Team

## Purpose
Maps publishers, consumers, delivery guarantees, ordering, priority, and retention for every event in the system.

---

## Event Ownership Matrix

| Event | Publisher | Consumer(s) | Delivery | Ordering | Priority | Retention | Payload Schema |
|-------|-----------|-------------|----------|----------|----------|-----------|----------------|
| `trade.opportunity.detected` | Opportunity Detector | Trading Engine, Risk Engine, AI Pipeline | At-least-once | Key (trade_id) | High | 7 days | `OpportunityDetected` |
| `trade.opportunity.ranked` | Opportunity Ranker | Trading Engine, Execution Engine | At-least-once | Key (trade_id) | High | 7 days | `OpportunityRanked` |
| `trade.opened` | Trading Engine | Execution Engine, Risk Engine, Dashboard, Audit | Exactly-once | Key (trade_id) | Critical | 90 days | `TradeOpened` |
| `trade.executing` | Execution Engine | Trading Engine, Dashboard, Monitoring | At-least-once | Key (trade_id) | High | 30 days | `TradeExecuting` |
| `trade.executed` | Execution Engine | Trading Engine, Portfolio, Wallet, Dashboard, Audit | Exactly-once | Key (trade_id) | Critical | 365 days | `TradeExecuted` |
| `trade.failed` | Execution Engine | Trading Engine, Risk Engine, Dashboard, Audit | Exactly-once | Key (trade_id) | Critical | 365 days | `TradeFailed` |
| `trade.rollback` | Execution Engine | Trading Engine, Wallet, Dashboard | At-least-once | Key (trade_id) | Critical | 30 days | `TradeRollback` |
| `trade.settled` | Trading Engine | Portfolio, Dashboard, Audit, Notification | Exactly-once | Key (trade_id) | Critical | 365 days | `TradeSettled` |
| `trade.cancelled` | Trading Engine | Execution Engine, Dashboard, Notification | At-least-once | Key (trade_id) | High | 30 days | `TradeCancelled` |
| `chain.block.new` | Chain Adapter | Market Data, Opportunity Detector, Chain Intelligence | At-most-once | Key (chain_id + block) | Medium | 1 day | `NewBlock` |
| `chain.rpc.failed` | Chain Adapter | RPC Manager, Runtime | At-least-once | Key (chain_id) | High | 7 days | `RPCFailed` |
| `chain.rpc.switched` | RPC Manager | Chain Adapter, Monitoring | At-least-once | Key (chain_id) | Medium | 7 days | `RPCSwitched` |
| `price.updated` | Market Data | Routing Engine, Opportunity Detector, Slippage Model | At-most-once | Key (pair_id) | Medium | 1 day | `PriceUpdated` |
| `price.spike` | Market Data | Risk Engine, Opportunity Detector, Monitoring | At-least-once | Key (pair_id) | High | 7 days | `PriceSpike` |
| `liquidity.changed` | DEX Adapter | Routing Engine, Slippage Model | At-most-once | Key (pair_id + dex) | Medium | 1 day | `LiquidityChanged` |
| `wallet.balance.changed` | Wallet Manager | Portfolio, Trading Engine, Dashboard | At-least-once | Key (wallet_id) | Medium | 7 days | `BalanceChanged` |
| `wallet.transaction.pending` | Wallet Manager | Execution Engine, Dashboard | At-least-once | Key (tx_hash) | High | 7 days | `TxPending` |
| `wallet.transaction.confirmed` | Wallet Manager | Execution Engine, Trading Engine, Portfolio | Exactly-once | Key (tx_hash) | Critical | 90 days | `TxConfirmed` |
| `wallet.transaction.failed` | Wallet Manager | Execution Engine, Trading Engine, Dashboard | Exactly-once | Key (tx_hash) | Critical | 90 days | `TxFailed` |
| `risk.limit.exceeded` | Risk Engine | Trading Engine, Dashboard, Notification | Exactly-once | Key (limit_type) | Critical | 30 days | `RiskLimitExceeded` |
| `risk.circuit.breaker.tripped` | Risk Engine | Trading Engine, Runtime, Dashboard, Notification | Exactly-once | — | Critical | 90 days | `CircuitBreakerTripped` |
| `risk.circuit.breaker.reset` | Risk Engine | Trading Engine, Runtime | Exactly-once | — | Critical | 90 days | `CircuitBreakerReset` |
| `ai.provider.failed` | AI Gateway | AI Orchestrator, Runtime | At-least-once | Key (provider) | High | 7 days | `ProviderFailed` |
| `ai.provider.switched` | AI Orchestrator | AI Pipeline, Monitoring | At-least-once | Key (provider) | Medium | 7 days | `ProviderSwitched` |
| `ai.tool.invoked` | AI Pipeline | AI Orchestrator, Audit | At-least-once | Key (tool + call_id) | Low | 7 days | `ToolInvoked` |
| `ai.tool.result` | AI Pipeline | AI Orchestrator, Memory | At-least-once | Key (call_id) | Low | 7 days | `ToolResult` |
| `ai.prompt.built` | Context Builder | AI Pipeline, Audit | At-least-once | Key (session_id) | Low | 1 day | `PromptBuilt` |
| `ai.cost.exceeded` | AI Cost Manager | AI Pipeline, Dashboard, Notification | Exactly-once | — | High | 30 days | `CostExceeded` |
| `plugin.installed` | Plugin Manager | Runtime, Dashboard | At-least-once | Key (plugin) | Medium | 30 days | `PluginInstalled` |
| `plugin.removed` | Plugin Manager | Runtime, Dashboard | At-least-once | Key (plugin) | Medium | 30 days | `PluginRemoved` |
| `plugin.error` | Plugin Executor | Plugin Manager, Dashboard, Monitoring | At-least-once | Key (plugin) | High | 7 days | `PluginError` |
| `runtime.starting` | Runtime Orchestrator | All Subsystems, Dashboard | At-least-once | — | Critical | 7 days | `RuntimeStarting` |
| `runtime.started` | Runtime Orchestrator | All Subsystems, Dashboard | Exactly-once | — | Critical | 7 days | `RuntimeStarted` |
| `runtime.shutting_down` | Runtime Orchestrator | All Subsystems, Dashboard | Exactly-once | — | Critical | 7 days | `RuntimeShuttingDown` |
| `runtime.stopped` | Runtime Orchestrator | Dashboard, Monitoring | Exactly-once | — | Critical | 7 days | `RuntimeStopped` |
| `runtime.health.failed` | Health Checker | Runtime Orchestrator, Self-Healer | At-least-once | Key (subsystem) | Critical | 7 days | `HealthFailed` |
| `runtime.health.restored` | Health Checker | Runtime Orchestrator, Self-Healer | At-least-once | Key (subsystem) | High | 7 days | `HealthRestored` |
| `runtime.failover.started` | Runtime Orchestrator | All Subsystems, Dashboard, Notification | Exactly-once | — | Critical | 30 days | `FailoverStarted` |
| `runtime.failover.completed` | Runtime Orchestrator | All Subsystems, Dashboard | Exactly-once | — | Critical | 30 days | `FailoverCompleted` |
| `runtime.config.reload` | Config Manager | All Subsystems | Exactly-once | — | High | 7 days | `ConfigReload` |
| `dashboard.workspace.saved` | Workspace Manager | Dashboard | At-most-once | Key (workspace) | Low | 30 days | `WorkspaceSaved` |
| `dashboard.workspace.restored` | Workspace Manager | Dashboard | At-most-once | Key (workspace) | Low | 30 days | `WorkspaceRestored` |
| `dashboard.widget.updated` | Widget Manager | Dashboard | At-most-once | Key (widget) | Low | 1 day | `WidgetUpdated` |
| `system.error` | Any Subsystem | Error Handler, Monitoring, Audit | Exactly-once | Key (error_code) | Critical | 365 days | `SystemError` |
| `system.warning` | Any Subsystem | Monitoring, Audit | At-least-once | Key (error_code) | Medium | 30 days | `SystemWarning` |
| `security.violation` | Security Enforcer | Security, Audit, Notification | Exactly-once | Key (violation_id) | Critical | 365 days | `SecurityViolation` |
| `secret.rotated` | Secret Manager | Security, Audit | Exactly-once | Key (secret_name) | Critical | 365 days | `SecretRotated` |

---

## Delivery Guarantees

| Guarantee | Meaning | Implementation |
|-----------|---------|----------------|
| **Exactly-once** | Event is delivered exactly once to all consumers. Duplicate detection via dedup key. | Consumer tracks processed event IDs; publisher includes unique `event_id` + idempotency key. |
| **At-least-once** | Event is delivered at least once. Duplicates possible but tolerated. | Publisher retries on ack failure; consumer must be idempotent. |
| **At-most-once** | Event is delivered at most once. May be lost on failure. | Fire-and-forget; no retry. Used for high-volume, low-criticality data. |

---

## Ordering Rules

- **Key-based ordering**: Events with the same ordering key are delivered in publish order to all consumers of that key.
- **Global ordering**: Not guaranteed across different keys. If global ordering is required, use a single global key (with performance implications).
- **Partition assignment**: The event bus assigns events with the same key to the same partition/worker.
- **Strict FIFO per key**: Within a key, events are not reordered. If a consumer receives event N+1 before event N, it must defer processing until N arrives or timeout.

---

## Priority Levels

| Priority | Meaning | Handling |
|----------|---------|----------|
| **Critical** | System integrity at stake. | Delivery bypasses queues, uses dedicated high-priority channel. Consumer processes synchronously if possible. |
| **High** | Important for correct operation. | Prioritized over Medium/Low in queue scheduling. Consumer processes within 100ms. |
| **Medium** | Normal operational events. | Standard queue scheduling. Consumer processes within 1s. |
| **Low** | Informational / audit / telemetry. | Batched delivery. Consumer processes within 5s. May be sampled. |

---

## Dead-Letter Queue (DLQ)

- All events with delivery guarantee `At-least-once` or `Exactly-once` that fail after `event.dead_letter_max_retries` (default: 3) are routed to the DLQ.
- DLQ events are preserved for `event.retention_days` (default: 7).
- DLQ consumers can replay events manually via admin API.
- DLQ overflow triggers `system.error` with severity `critical`.

---

## Replay Rules

- Events with retention >= 30 days support replay.
- Replay is key-range or time-range based.
- Replay requests are submitted via admin API and executed as a background job.
- Consumers receive a replay flag in the event envelope to distinguish live vs replay delivery.

---

## Event Version Compatibility

- Events carry a `version` field (semver).
- Consumers must handle the current major version and one previous major version.
- Breaking changes increment the major version and trigger a migration window (2 release cycles).

---

## Cross-References

- **EVENT-CATALOG.md** — Canonical event definitions and payload schemas.
- **TRACEABILITY-MATRIX.md** — Requirement-to-document mapping and governance validation.
- **EVENT-BUS.md** — Event bus architecture and delivery mechanism.
- **CONFIGURATION-REFERENCE.md** — Event config keys (`event.*`).
- **FAILURE-RECOVERY-MATRIX.md** — Recovery actions for event failures.
- **ARCHITECTURE.md** — System event flow boundaries.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 0.2.0 | 2026-07-27 | Full publisher/consumer matrix with guarantees, ordering, priority, retention | Runtime Team |
| 0.1.0 | 2026-07-27 | Initial stub created | Runtime Team |