---
metadata_schema_version: 1.0
document_id: DOC-0254
title: IPC Protocol
plane: Product Specification
domain: Interfaces
class: Specification
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/interfaces/ipc/ipc-protocol.md
related_concepts:
  - CONCEPT-0254
dependencies: []
consumers:
  - DOC-0264
  - DOC-0427
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Interfaces
type: CONTRACT
purpose: Defines inter-process communication protocol.
scope: IPC for all runtime components.
---

# IPC Protocol

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-29 | **Owner:** Runtime Team

## Purpose
Defines the single authoritative IPC (Inter-Process Communication) protocol for the Apex platform — covering the transport mechanism, message envelope format, serialization, typed channels, error handling, versioning, backward compatibility, and the complete channel catalog that connects all subsystems across trust boundaries. This contract enables an autonomous engineer to implement the exact IPC infrastructure without making assumptions.

---

## 1. Transport Architecture

### 1.1 Process Model

The Apex platform runs as two processes on Windows:

| Process | Role | Trust Domain | IPC Role |
|---------|------|-------------|----------|
| **Backend process** | Trading engine, AI, risk, execution, database, event bus, workers | T1 (Application) + T2 (AI) | IPC Server (creates named pipe endpoints) |
| **Desktop/UI process** | Dashboard shell, widgets, tray, workspace manager | T3 (Desktop) | IPC Client (connects to named pipe endpoints) |

Plugin sandboxes run as additional child processes with IPC channels to the backend process only (never to the UI process directly).

### 1.2 Transport Selection

| Transport | Use Case | Why |
|-----------|----------|-----|
| **Named pipes (primary)** | Backend ↔ Desktop UI | Windows-native; bidirectional; supports async I/O; no firewall issues; handles both directions |
| **stdin/stdout JSON** | Backend ↔ Plugin sandbox | Simple; isolated; no OS-level sharing; process lifetime bound to parent |
| **In-process queues** | Backend ↔ Backend subsystems | Same process; zero IPC overhead; typed Rust channels |

**Named Pipe Configuration:**
- Pipe name: `\\.\pipe\apex-arbitrage-{session_id}` (unique per session)
- Mode: `PIPE_ACCESS_DUPLEX` (bidirectional)
- Message mode: `PIPE_READMODE_MESSAGE` (message-based, not stream)
- Buffer size: 64 KB input, 64 KB output
- Max instances: 2 (backend + desktop)
- Timeout: `ipc.connection_timeout_ms` (5s)
- Security: DACL restricting to current user SID only

### 1.3 Connection Lifecycle

```
1. Backend process creates named pipe on startup (Phase 4).
2. Desktop process connects to pipe within ipc.connection_timeout_ms.
3. Desktop sends IPC-HELLO message with version and session_id.
4. Backend validates version compatibility (see §6).
5. If compatible → connection established; both sides subscribe to channels.
6. If incompatible → backend sends IPC-ERROR with version mismatch; desktop shows "Update Required".
7. On disconnect: desktop re-attempts connection every 2s (up to 5 attempts).
8. After 5 failures: desktop shows "Backend Unavailable" and offers restart.
```

---

## 2. Message Envelope Format

### 2.1 Envelope Schema

Every IPC message must use this envelope:

```json
{
  "version": 1,
  "type": "<message_type>",
  "correlation_id": "<uuid>",
  "timestamp": "<unix_ms>",
  "source": "<producer_identity>",
  "target": "<consumer_identity_or_channel>",
  "payload": { ... },
  "metadata": {
    "priority": "<critical|high|medium|low>",
    "delivery": "<at_most_once|at_least_once|exactly_once>",
    "ordering_key": "<optional_key>",
    "retry_count": 0,
    "ttl_ms": 30000
  }
}
```

### 2.2 Envelope Field Rules

| Field | Required | Type | Rules |
|-------|----------|------|-------|
| `version` | Yes | uint32 | Must match negotiated protocol version (see §6). Current: 1. |
| `type` | Yes | string | Must be a registered type from IPC-MESSAGE-CATALOG.md. Format: `<domain>.<action>` (e.g., `trade.started`). |
| `correlation_id` | Yes | UUID | Unique per request; echoed in responses. Enables request-response matching. |
| `timestamp` | Yes | uint64 | Unix milliseconds; monotonic per source; used for ordering and TTL calculation. |
| `source` | Yes | string | Identity of producer subsystem (e.g., `trading-engine`, `dashboard`, `plugin:market-scanner`). |
| `target` | Yes | string | Target subsystem or channel name (e.g., `dashboard`, `event-bus`, `trading-engine`). |
| `payload` | Yes | object | Domain-specific data; schema defined per message type in IPC-MESSAGE-CATALOG.md. |
| `metadata.priority` | Yes | enum | `critical`, `high`, `medium`, `low`. Maps to event bus priority queues. |
| `metadata.delivery` | Yes | enum | See §3 for delivery semantics per message type. |
| `metadata.ordering_key` | Conditional | string | Required for exactly-once messages; must be `trade_id` for trade messages. |
| `metadata.retry_count` | Yes | uint32 | Incremented on each retry; max 3. |
| `metadata.ttl_ms` | Yes | uint32 | Time-to-live; message discarded after TTL expires. Default: 30000. |

---

## 3. Delivery Semantics

| Delivery Mode | Use When | Mechanism | Failure Handling |
|---------------|----------|-----------|-----------------|
| **at_most_once** | UI updates, non-critical notifications | Fire and forget; no ack required | Lost messages are acceptable; next update will correct |
| **at_least_once** | Trade status, health events, config updates | Retry up to 3 times; ack optional | May produce duplicates; consumer must dedup via correlation_id |
| **exactly_once** | Trade execution commands, config reload triggers | Ack required + dedup via ordering_key + correlation_id | If no ack within ttl_ms → retry with same correlation_id; consumer dedup on receipt |

### 3.1 Acknowledgment Protocol

For exactly-once messages:

```
1. Sender sends message with correlation_id = C.
2. Receiver processes message.
3. Receiver sends IPC-ACK with correlation_id = C, result = OK or ERROR.
4. If sender does not receive ACK within ttl_ms:
   a. Retry same message (same correlation_id, incremented retry_count).
   b. After 3 retries → send IPC-ERROR to sender's error handler; message considered lost.
5. Receiver tracks processed correlation_ids for dedup window (5 minutes).
6. If receiver sees duplicate correlation_id → dedup (skip processing, send ACK again).
```

---

## 4. Typed Channel Catalog

Each trust domain crossing uses a dedicated typed channel. Messages on a channel have a specific producer, consumer, and payload schema.

### 4.1 Backend → Desktop Channels

| Channel | Direction | Producer | Consumer | Payload Type | Delivery | Rate Limit | Priority |
|---------|-----------|----------|----------|-------------|----------|------------|----------|
| `channel.trades` | Backend → Desktop | Trading Engine | Dashboard | Trade summary (anonymized) | at_most_once | 50 msg/s | high |
| `channel.wallet` | Backend → Desktop | Wallet Manager | Dashboard | Balance summary (anonymized) | at_most_once | 10 msg/s | medium |
| `channel.risk` | Backend → Desktop | Risk Engine | Dashboard | Risk status (anonymized) | at_most_once | 10 msg/s | high |
| `channel.health` | Backend → Desktop | Orchestrator | Dashboard | Platform mode + subsystem status | at_least_once | 5 msg/s | critical |
| `channel.ai_status` | Backend → Desktop | AI Pipeline | Dashboard | AI provider status + mode | at_most_once | 2 msg/s | low |
| `channel.notifications` | Backend → Desktop | Notification Handler | Desktop tray/center | Notification payload | at_least_once | 5 msg/s | medium |
| `channel.plugin_events` | Backend → Desktop | Plugin Manager | Dashboard | Plugin state changes | at_most_once | 5 msg/s | low |

### 4.2 Desktop → Backend Channels

| Channel | Direction | Producer | Consumer | Payload Type | Delivery | Rate Limit | Priority |
|---------|-----------|----------|----------|-------------|----------|------------|----------|
| `channel.ui_commands` | Desktop → Backend | Dashboard | Trading Engine / Config | User actions (start/stop strategy, config edit) | exactly_once | 5 msg/s | high |
| `channel.workspace` | Desktop → Backend | Dashboard | Config Manager | Workspace save/load requests | at_least_once | 2 msg/s | medium |
| `channel.dashboard_config` | Desktop → Backend | Dashboard | Config Manager | Dashboard config changes | exactly_once | 1 msg/s | medium |

### 4.3 Backend ↔ Plugin Sandbox Channels

| Channel | Direction | Producer | Consumer | Payload Type | Delivery | Priority |
|---------|-----------|----------|----------|-------------|----------|----------|
| `channel.plugin_invoke` | Backend → Sandbox | Plugin Manager | Plugin process | Tool call request | exactly_once | medium |
| `channel.plugin_result` | Sandbox → Backend | Plugin process | Plugin Manager | Tool call result | exactly_once | medium |
| `channel.plugin_event` | Sandbox → Backend | Plugin process | Event Bus | Custom event (per manifest declaration) | at_least_once | low |

### 4.4 Backend Internal Channels (In-Process)

| Channel | Type | Producer | Consumer | Delivery | Priority |
|---------|------|----------|----------|----------|----------|
| `internal.trade_events` | Rust `mpsc` channel | Trading Engine | Event Bus dispatcher | at_least_once | high |
| `internal.execution_events` | Rust `mpsc` channel | Execution Engine | Event Bus dispatcher | at_least_once | critical |
| `internal.health_events` | Rust `mpsc` channel | Orchestrator | Event Bus dispatcher | at_least_once | critical |
| `internal.ai_events` | Rust `mpsc` channel | AI Pipeline | Event Bus dispatcher | at_least_once | medium |
| `internal.config_events` | Rust `mpsc` channel | Config Manager | Affected subsystems | exactly_once | high |

---

## 5. Error Handling Protocol

### 5.1 Error Response Format

```json
{
  "version": 1,
  "type": "ipc.error",
  "correlation_id": "<original_correlation_id>",
  "timestamp": "<unix_ms>",
  "source": "<failing_subsystem>",
  "target": "<original_sender>",
  "payload": {
    "error_code": "<APEX_ERROR_CODE>",
    "error_category": "<network|validation|permission|timeout|internal>",
    "message": "Human-readable description",
    "details": { ... },
    "retry_allowed": true,
    "retry_after_ms": 5000
  },
  "metadata": {
    "priority": "critical",
    "delivery": "at_least_once",
    "ordering_key": null,
    "retry_count": 0,
    "ttl_ms": 10000
  }
}
```

### 5.2 Error Categories

| Category | Meaning | Consumer Action |
|----------|---------|-----------------|
| `network` | RPC/WebSocket/network failure | Retry with backoff; switch to fallback if available |
| `validation` | Payload schema validation failed | Fix payload; do NOT retry with same payload |
| `permission` | Capability check or trust boundary violation | Log security event; do NOT retry |
| `timeout` | Processing exceeded timeout budget | Retry with longer timeout or alternate path |
| `internal` | Internal subsystem error | Retry once; if persists → escalate to recovery |

### 5.3 IPC-Level Error Handling

| Error | Handling |
|-------|----------|
| Named pipe disconnected | Desktop: reconnect every 2s (up to 5); Backend: buffer messages in memory (up to 1000) |
| Named pipe full (write fails) | Sender: backpressure; retry after 100ms; if persists → log warning, discard at_most_once messages |
| Version mismatch | Backend sends IPC-ERROR with `error_code: APEX_IPC_VERSION_MISMATCH`; Desktop shows update prompt |
| Payload too large (> 64KB envelope limit) | Sender must chunk large payloads into multiple messages with same correlation_id |
| Deserialization failure | Receiver sends IPC-ERROR with `error_category: validation`; Sender must not retry same payload |

---

## 6. Versioning and Backward Compatibility

### 6.1 Protocol Version Negotiation

```
1. Desktop sends IPC-HELLO: { "protocol_version": 1, "client_version": "1.2.3" }
2. Backend checks:
   a. If protocol_version matches → IPC-ACK with { "accepted": true }
   b. If protocol_version is lower → IPC-ACK with { "accepted": true, "min_supported_features": [...] }
   c. If protocol_version is higher → IPC-ERROR with { "error_code": "APEX_IPC_VERSION_MISMATCH", "max_supported_version": 1 }
```

### 6.2 Backward Compatibility Rules

| Rule | Enforcement |
|------|-------------|
| New message types may be added | Unknown types are logged and ignored (at_most_once) or queued (at_least_once/exactly_once) |
| Payload fields may be added | Unknown fields are ignored by older consumers (forward-compatible) |
| Payload fields may NOT be removed | Removed fields must be deprecated for 2 versions before removal |
| Payload field types may NOT change | Type changes require a new message type |
| Delivery semantics may NOT be downgraded | `exactly_once` cannot become `at_least_once` |
| Channel rate limits may be tightened | But may NOT be loosened without version increment |

---

## 7. Serialization and Compression

### 7.1 Serialization Format

| Format | Use Case | Schema Reference |
|--------|----------|-----------------|
| **JSON** (primary) | Named pipe IPC, plugin stdin/stdout | schemas/ipc-envelope-v1.json |
| **Rust struct** (internal) | In-process channels | Rust type definitions (compile-time verified) |
| **Binary (MessagePack)** | Optional for high-throughput channels | schemas/ipc-envelope-v1.msgpack |

JSON is the default because it is debuggable, schema-verifiable, and compatible with plugin sandbox stdin/stdout. MessagePack may be used for performance-critical internal channels where both sides are Rust.

### 7.2 Compression

| Condition | Action |
|-----------|--------|
| Envelope size > 16 KB | Apply zlib compression; add `metadata.compression: "zlib"` |
| Envelope size > 64 KB | Chunk into multiple messages (see §5.3) |
| Envelope size ≤ 16 KB | No compression (latency impact > bandwidth savings) |

---

## 8. Security Considerations

| Threat | Mitigation |
|--------|------------|
| Named pipe snooping | DACL restricts pipe access to current user SID; pipe name includes session_id (random per instance) |
| Message injection | Envelope source field verified against registered producer; unknown sources → IPC-ERROR permission |
| Payload tampering | JSON schema validation on receipt; invalid payload → IPC-ERROR validation |
| Replay attack | Timestamp in envelope; reject messages older than ttl_ms; dedup window for exactly_once |
| Plugin sandbox escape | Plugin stdin/stdout only; no named pipe access; no shared memory; capability check on every plugin_invoke |
| Memory disclosure | at_most_once messages for T3 (Dashboard) must NOT contain wallet addresses, private keys, or full trade details; payloads are anonymized |

### 8.1 Anonymization Rules for Desktop (T3) Messages

| Data Type | Anonymization | Example |
|-----------|---------------|---------|
| Wallet address | Not included | `"balance_usd": 1234.56` (no address) |
| Private key | Never sent across IPC | — (stays in Wallet Manager in-process) |
| Trade details | Summary only | `"profit_usd": 45.67, "status": "completed"` (no tx_hash) |
| AI prompt content | Not included | `"ai_mode": "advisory"` (no prompt text) |
| Error details | Sanitized | `"error": "execution timeout"` (no stack traces) |

---

## 9. Performance Budgets

| Metric | Target | Config Key |
|--------|--------|------------|
| Named pipe round-trip latency | < 10ms (local) | `ipc.pipe_latency_budget_ms` |
| Message serialization (JSON) | < 2ms per message | — |
| Message serialization (MessagePack) | < 0.5ms per message | — |
| Channel throughput (all channels combined) | < 100 msg/s sustained | `ipc.max_throughput_msgs_per_sec` |
| Desktop reconnect time | < 5s (typical), < 10s (max) | `ipc.reconnect_timeout_ms` |
| Memory buffer for disconnected state | 1000 messages max | `ipc.buffer_max_messages` |
| Dedup window size | 5 minutes | `ipc.dedup_window_ms` |
| Compression threshold | 16 KB | `ipc.compression_threshold_bytes` |

---

## 10. IPC Configuration Ownership

| Config Key | Default | Authority | Reloadable |
|-----------|---------|-----------|------------|
| `ipc.connection_timeout_ms` | 5000 | IPC-PROTOCOL.md | No (restart required) |
| `ipc.pipe_latency_budget_ms` | 10 | IPC-PROTOCOL.md | Yes |
| `ipc.max_throughput_msgs_per_sec` | 100 | IPC-PROTOCOL.md | Yes |
| `ipc.reconnect_timeout_ms` | 10000 | IPC-PROTOCOL.md | No |
| `ipc.buffer_max_messages` | 1000 | IPC-PROTOCOL.md | Yes |
| `ipc.dedup_window_ms` | 300000 | IPC-PROTOCOL.md | Yes |
| `ipc.compression_threshold_bytes` | 16384 | IPC-PROTOCOL.md | Yes |
| `ipc.session_id` | (auto-generated) | IPC-PROTOCOL.md | No |

---

## Cross-References

- **IPC-MESSAGE-CATALOG.md** — Complete catalog of message types with payload schemas.
- **EVENT-BUS.md** — Event bus delivery semantics and event catalog.
- **EVENT-OWNERSHIP-MATRIX.md** — Event producer/consumer mapping.
- **DASHBOARD-RUNTIME.md** — Dashboard IPC bridge initialization and lifecycle.
- **PLUGIN-SDK.md** — Plugin sandbox IPC interface.
- **TRUST-BOUNDARIES.md** — Trust domain enforcement at IPC boundaries.
- **PERMISSION-MODEL.md** — Capability checks for IPC message authorization.
- **WINDOWS-APP-ARCHITECTURE.md** — Windows process model and named pipe integration.
- **CONFIGURATION-REFERENCE.md** — IPC config key definitions.
- **SECURITY.md** — IPC security hardening and anonymization.
- **TRACEABILITY-MATRIX.md** — REQ-RUNTIME-001, REQ-EVENT-001.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Runtime Team |
