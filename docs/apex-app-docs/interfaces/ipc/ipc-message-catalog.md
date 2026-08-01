---
metadata_schema_version: 1.0
document_id: DOC-0264
title: IPC Message Catalog
plane: Product Specification
domain: Interfaces
class: Reference
authority: Reference
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/interfaces/ipc/ipc-protocol.md
related_concepts:
  - CONCEPT-0254
dependencies:
  - DOC-0254
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Reference
owned_domains: []
type: REFERENCE
purpose: "Catalogs every IPC message type used across the Apex platform — defining the type, producer, consumer, payload shape, delivery semantics, error behavior, and version for each message. This is the reference companion to IPC-PROTOCOL.md which defines the transport, envelope format, and channel structure. An autonomous engineer should use this catalog to implement exact message handlers for each typed channel."
scope: None
---

# IPC Message Catalog

## Document type
Document type: [REFERENCE]

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-27 | **Owner:** Runtime Team

## Purpose
Catalogs every IPC message type used across the Apex platform — defining the type, producer, consumer, payload shape, delivery semantics, error behavior, and version for each message. This is the reference companion to IPC-PROTOCOL.md which defines the transport, envelope format, and channel structure. An autonomous engineer should use this catalog to implement exact message handlers for each typed channel.

## Ownership
- Owns: The catalog of IPC message types and their payload schemas.
- Does not own: Transport mechanism, envelope format, channel definitions (owned by IPC-PROTOCOL.md).
- Does not own: Event bus event types (owned by EVENT-OWNERSHIP-MATRIX.md).

---

## 1. Backend → Desktop Messages

### 1.1 Trade Status Messages (channel.trades)

| Message Type | Producer | Consumer | Payload Shape | Delivery | Priority |
|-------------|----------|----------|---------------|----------|----------|
| `trade.started` | Trading Engine | Dashboard | `{trade_id, strategy_id, pair, chains, status: "started", timestamp}` | at_most_once | high |
| `trade.leg.executing` | Execution Engine | Dashboard | `{trade_id, leg: 1|2, chain_id, status: "executing", timestamp}` | at_most_once | high |
| `trade.leg.confirmed` | Execution Engine | Dashboard | `{trade_id, leg: 1|2, chain_id, gas_used_usd, timestamp}` | at_most_once | high |
| `trade.leg.failed` | Execution Engine | Dashboard | `{trade_id, leg: 1|2, chain_id, reason, timestamp}` | at_most_once | high |
| `trade.completed` | Trading Engine | Dashboard | `{trade_id, profit_usd, gas_total_usd, duration_ms, timestamp}` | at_most_once | high |
| `trade.aborted` | Trading Engine | Dashboard | `{trade_id, reason, recovery_action, timestamp}` | at_most_once | high |
| `trade.rollback` | Trading Engine | Dashboard | `{trade_id, leg_to_unwind, timestamp}` | at_most_once | high |

### 1.2 Wallet Status Messages (channel.wallet)

| Message Type | Producer | Consumer | Payload Shape | Delivery | Priority |
|-------------|----------|----------|---------------|----------|----------|
| `wallet.balance.update` | Wallet Manager | Dashboard | `{wallet_id, balance_usd, pending_tx_count, timestamp}` | at_most_once | medium |
| `wallet.state.change` | Wallet Manager | Dashboard | `{wallet_id, state: "ready"|"paused"|"locked", timestamp}` | at_most_once | medium |

### 1.3 Risk Status Messages (channel.risk)

| Message Type | Producer | Consumer | Payload Shape | Delivery | Priority |
|-------------|----------|----------|---------------|----------|----------|
| `risk.circuit_breaker.tripped` | Risk Engine | Dashboard | `{chain_id, reason, cooldown_ms, timestamp}` | at_least_once | critical |
| `risk.circuit_breaker.reset` | Risk Engine | Dashboard | `{chain_id, timestamp}` | at_least_once | high |
| `risk.status.update` | Risk Engine | Dashboard | `{limits, circuit_breakers, overall_status, timestamp}` | at_most_once | medium |

### 1.4 Platform Health Messages (channel.health)

| Message Type | Producer | Consumer | Payload Shape | Delivery | Priority |
|-------------|----------|----------|---------------|----------|----------|
| `runtime.mode.transition` | Orchestrator | Dashboard | `{from_mode, to_mode, health_score, reason, timestamp}` | at_least_once | critical |
| `runtime.health.failed` | Orchestrator | Dashboard | `{subsystem, check_id, failures, threshold, timestamp}` | at_least_once | critical |
| `runtime.health.restored` | Orchestrator | Dashboard | `{subsystem, check_id, recovery_duration_ms, timestamp}` | at_least_once | high |
| `runtime.health.degraded` | Orchestrator | Dashboard | `{subsystem, check_id, failures, timestamp}` | at_least_once | medium |
| `runtime.config.reload.completed` | Config Manager | Dashboard | `{keys_changed_count, reload_duration_ms, timestamp}` | at_least_once | medium |
| `runtime.config.reload.failed` | Config Manager | Dashboard | `{keys_rejected, reason, timestamp}` | at_least_once | high |

### 1.5 AI Status Messages (channel.ai_status)

| Message Type | Producer | Consumer | Payload Shape | Delivery | Priority |
|-------------|----------|----------|---------------|----------|----------|
| `ai.provider.status` | AI Pipeline | Dashboard | `{provider, status: "ready"|"failed"|"cooldown", latency_ms, timestamp}` | at_most_once | low |
| `ai.mode.change` | AI Pipeline | Dashboard | `{mode: "advisory"|"disabled"|"fallback", timestamp}` | at_least_once | medium |

### 1.6 Notification Messages (channel.notifications)

| Message Type | Producer | Consumer | Payload Shape | Delivery | Priority |
|-------------|----------|----------|---------------|----------|----------|
| `notification.trade` | Notification Handler | Desktop tray | `{type: "trade_completed"|"trade_failed"|"trade_aborted", summary, severity, timestamp}` | at_least_once | medium |
| `notification.system` | Notification Handler | Desktop tray | `{type: "update_available"|"restart_required"|"critical_error", severity, timestamp}` | at_least_once | high |
| `notification.plugin` | Notification Handler | Desktop tray | `{type: "plugin_updated"|"plugin_failed", plugin_id, timestamp}` | at_least_once | low |

### 1.7 Plugin Event Messages (channel.plugin_events)

| Message Type | Producer | Consumer | Payload Shape | Delivery | Priority |
|-------------|----------|----------|---------------|----------|----------|
| `plugin.state.change` | Plugin Manager | Dashboard | `{plugin_id, from_state, to_state, timestamp}` | at_most_once | low |

---

## 2. Desktop → Backend Messages

### 2.1 UI Command Messages (channel.ui_commands)

| Message Type | Producer | Consumer | Payload Shape | Delivery | Priority |
|-------------|----------|----------|---------------|----------|----------|
| `ui.strategy.start` | Dashboard | Trading Engine | `{strategy_id, parameters_override}` | exactly_once | high |
| `ui.strategy.stop` | Dashboard | Trading Engine | `{strategy_id, drain: true|false}` | exactly_once | high |
| `ui.strategy.edit` | Dashboard | Config Manager | `{strategy_id, new_parameters, validation_required: true}` | exactly_once | high |
| `ui.trade.cancel` | Dashboard | Trading Engine | `{trade_id, reason: "user_cancel"}` | exactly_once | high |
| `ui.force_recovery` | Dashboard | Orchestrator | `{subsystem, action: "restart"|"reset"}` | exactly_once | critical |
| `ui.update.check` | Dashboard | Update Manager | `{channel: "canary"|"beta"|"production"}` | exactly_once | medium |

### 2.2 Workspace Messages (channel.workspace)

| Message Type | Producer | Consumer | Payload Shape | Delivery | Priority |
|-------------|----------|----------|---------------|----------|----------|
| `workspace.save` | Dashboard | Config Manager | `{workspace_id, layout, panels, active_tab}` | at_least_once | medium |
| `workspace.load` | Dashboard | Config Manager | `{workspace_id}` | at_least_once | medium |
| `workspace.list` | Dashboard | Config Manager | `{user_id}` | at_least_once | low |

### 2.3 Dashboard Config Messages (channel.dashboard_config)

| Message Type | Producer | Consumer | Payload Shape | Delivery | Priority |
|-------------|----------|----------|---------------|----------|----------|
| `dashboard.config.update` | Dashboard | Config Manager | `{key_path, new_value}` | exactly_once | medium |

---

## 3. Backend ↔ Plugin Sandbox Messages

### 3.1 Plugin Invocation Messages (channel.plugin_invoke)

| Message Type | Producer | Consumer | Payload Shape | Delivery | Priority |
|-------------|----------|----------|---------------|----------|----------|
| `plugin.invoke` | Plugin Manager | Plugin sandbox | `{plugin_id, tool_name, args, timeout_ms, correlation_id}` | exactly_once | medium |

### 3.2 Plugin Result Messages (channel.plugin_result)

| Message Type | Producer | Consumer | Payload Shape | Delivery | Priority |
|-------------|----------|----------|---------------|----------|----------|
| `plugin.result.success` | Plugin sandbox | Plugin Manager | `{plugin_id, tool_name, result, correlation_id}` | exactly_once | medium |
| `plugin.result.error` | Plugin sandbox | Plugin Manager | `{plugin_id, tool_name, error_code, error_message, correlation_id}` | exactly_once | medium |

### 3.3 Plugin Event Messages (channel.plugin_event)

| Message Type | Producer | Consumer | Payload Shape | Delivery | Priority |
|-------------|----------|----------|---------------|----------|----------|
| `plugin.event.custom` | Plugin sandbox | Event Bus | `{plugin_id, event_type, payload, manifest_declared_type}` | at_least_once | low |

---

## 4. IPC Protocol Messages

| Message Type | Direction | Payload | Purpose |
|-------------|-----------|---------|---------|
| `ipc.hello` | Desktop → Backend | `{protocol_version, client_version, session_id}` | Connection handshake and version negotiation |
| `ipc.ack` | Bidirectional | `{correlation_id, result: "OK"|"ERROR", error_details}` | Exactly-once acknowledgment |
| `ipc.error` | Bidirectional | `{error_code, error_category, message, retry_allowed, retry_after_ms}` | Structured error response |
| `ipc.heartbeat` | Backend → Desktop | `{health_score, mode, timestamp}` | Periodic health status (5s interval) |
| `ipc.disconnect` | Bidirectional | `{reason, graceful: true|false}` | Clean disconnection signal |

---

## Error Behavior per Message Type

For any message type, if the consumer fails to process:

| Delivery Mode | Error Handling |
|---------------|----------------|
| at_most_once | Log error; discard; no retry. Next update will correct stale state. |
| at_least_once | Retry up to 3 times with exponential backoff (1s, 2s, 4s). After 3 retries → emit `system.warning` and buffer locally. |
| exactly_once | Send `ipc.error` back to producer. Producer retries with same `correlation_id` (dedup on consumer side). After 3 retries → escalate to Orchestrator for recovery decision. |

---

## Version Compatibility

All message types use additive versioning:
- New fields in payloads: Ignored by older consumers (forward-compatible).
- New message types: Ignored by older consumers (logged as unknown).
- Removed fields: Deprecated for 2 protocol versions before removal.
- Type changes: Require new message type name.

---

## Cross-References

- **IPC-PROTOCOL.md** — Transport, envelope format, channel definitions, delivery semantics, version negotiation.
- **EVENT-OWNERSHIP-MATRIX.md** — Backend internal event types (different from IPC messages).
- **DASHBOARD-RUNTIME.md** — Dashboard IPC bridge lifecycle.
- **PLUGIN-SDK.md** — Plugin sandbox IPC interface.
- **ORCHESTRATOR.md** — Platform mode transitions and health coordination.
- **CONFIGURATION-REFERENCE.md** — IPC config key definitions.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-27 | New: complete IPC message catalog — 7 backend→desktop categories, 3 desktop→backend categories, 3 plugin categories, 5 protocol messages, error behavior per delivery mode | Runtime Team |
