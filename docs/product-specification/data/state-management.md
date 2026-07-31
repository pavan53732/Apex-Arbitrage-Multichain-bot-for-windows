---
metadata_schema_version: 1.0
document_id: DOC-0267
title: State Management
plane: Product Specification
domain: Data
class: Specification
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/data/state-management.md
related_concepts:
  - CONCEPT-0267
dependencies: []
consumers:
  - DOC-0049
  - DOC-0079
  - DOC-0251
  - DOC-0258
  - DOC-0269
  - DOC-0271
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: CONTRACT
purpose: "Defines how APEX manages runtime state — state domains, ownership, synchronization rules, full subsystem state machine index, timeout semantics, Windows sleep/resume recovery, and persistence expectations."
scope: None
---

# State Management

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.1.0 | **Status:** Canonical | **Last Updated:** 2026-07-27 | **Owner:** Runtime Team

## Purpose
Defines how APEX manages runtime state — state domains, ownership, synchronization rules, full subsystem state machine index, timeout semantics, Windows sleep/resume recovery, and persistence expectations.

---

## 1. State Domains

| Domain | Owner Process | Persistence | Synchronization | Source of Truth |
|--------|--------------|-------------|-----------------|-----------------|
| **Window lifecycle** | Main (UI) | Ephemeral | IPC push to backend | Main process |
| **IPC request lifecycle** | Main + Preload | Ephemeral | Request/response IPC | Main process |
| **Strategy runtime status** | Main (Trading) | Optional snapshot (DB) | Event push to dashboard | Trading Engine |
| **Risk state / kill switches** | Main (Risk) | Persisted + in-memory cache | Event push to dashboard + DB | Risk Engine (DB as durable truth) |
| **Quotes and route cache** | Main (Market Data) | Short-lived memory only | Event push to trading | Market Data Engine |
| **UI layout and preferences** | Renderer + Settings Service | Persisted (workspace JSON) | Settings API → IPC → DB | Workspace Manager |
| **Form state** | Renderer | Ephemeral | None (local) | Renderer |
| **AI conversation/task context** | Main (AI Orchestrator) | Persisted selectively (DB) | Event push to memory store | AI Pipeline (DB as durable truth) |
| **Audit trail** | Main (DB) | Persisted | DB write → event push | Database (durable) |
| **Execution state (in-flight)** | Main (Execution) | Persisted (DB) before each transition | Event push + DB write | Execution Engine (DB + chain) |
| **Wallet nonce/balance** | Main (Wallet) | Persisted (DB) + chain verification | Event push to trading | Chain (primary) + DB (cache) |
| **Plugin sandbox state** | Plugin process | Ephemeral (isolated) | IPC typed channel to host | Plugin Manager |
| **Config cache** | Main (Config) | Persisted + in-memory cache | Config reload event to all subsystems | Config Manager (DB + file) |
| **Event bus buffer** | Main (Event Bus) | Ring buffer (transient) + DLQ (DB) | SPSC channels per key | Event Bus |

---

## 2. Source of Truth Rules

| Rule | Description | Enforcement |
|------|-------------|-------------|
| Main process is authoritative for trading, provider, chain, and safety state | No other process may override execution state | IPC bridge validates all mutations |
| Database is the source of truth for durable history | Not transient execution state (in-flight state may differ from DB briefly) | Trade state persisted BEFORE each state transition |
| Chain is the source of truth for on-chain state | Wallet balance, nonce, TX status verified against chain on recovery | Execution Engine queries chain for crash resume |
| Cache is an acceleration layer only | Cached data may be stale; must be reconciled with authoritative source on demand | TTL-based invalidation + explicit refresh on state change |
| Renderer copies must be reconciled | If renderer state differs from main, main response wins | Renderer reconciliation on each IPC response |
| Plugin sandbox is isolated | Plugin state is ephemeral and never authoritative for platform state | Process isolation; no shared memory |

---

## 3. Synchronization Rules

```
1. Renderer action → preload API → typed IPC command
2. Main process validates input (role check + schema validation)
3. Service mutates state AND optionally persists (persist before state transition for critical state)
4. Main emits event or response via IPC
5. Renderer updates derived local stores (reconciliation to main response)
```

### Critical State Persistence Rule
For trades, execution legs, and risk state: **state must be persisted to DB BEFORE the state transition is committed**. This ensures crash recovery can reconstruct the last-known state.

| State Type | Persist Before Transition? | Reason |
|-----------|--------------------------|--------|
| Trade state | Yes | Money at risk; must survive crash |
| Execution leg state | Yes | In-flight TX must be recoverable |
| Risk circuit breaker state | Yes | Trading halt must survive crash |
| Wallet nonce | Yes | Nonce gaps cause execution failures |
| AI task state | No (persist after completion) | Advisory; no money at risk |
| Plugin state | No (ephemeral) | Isolated sandbox; no platform impact |
| Dashboard workspace | Yes (on autosave) | User preferences must survive restart |

---

## 4. Subsystem State Machine Index

All subsystem state machines are defined in dedicated contract documents. This section provides the authoritative index:

| Subsystem | State Machine Doc | Initial State | Terminal States | Recovery from Crash |
|-----------|-------------------|---------------|-----------------|---------------------|
| Engine | ENGINE-STATE-MACHINE.md | INITIALISING | STOPPED, FAILED | Recovery scan → RUNNING or FAILED |
| Execution | EXECUTION-STATE-MACHINE.md | PENDING | FINALIZED, ABORTED, FAILED | Query chain → resume or abort |
| Worker | WORKER-STATE-MACHINE.md | SPAWNED | TERMINATED | Workers re-created on startup |
| Plugin | PLUGIN-STATE-MACHINE.md | DISCOVERED | UNLOADED, REJECTED | Scan installed → LOADING → ACTIVE |
| Service (Windows) | SERVICE-STATE-MACHINE.md | INSTALLING | STOPPED | Auto-restart or manual |
| AI Orchestration | AI-STATE-MACHINE.md | IDLE | COMPLETED, FAILED, CANCELLED | Stateless per request; no crash recovery needed |
| Trade | TRADING-LIFECYCLE.md | IDLE | COMPLETED, REJECTED, ABORTED | Scan DB for in-flight → chain query → reconcile |
| Shutdown | SHUTDOWN-LIFECYCLE.md | RUNNING | STOPPED | — (shutdown is terminal) |
| Prompt | PROMPT-LIFECYCLE.md | IDLE | IDLE (after archiving) | Stateless per session |

### Timeout Semantics
- Each subsystem state machine has its own timeout table (see respective docs).
- Global timeout budget for trade: `trading.timeout_ms` (120s).
- Global timeout budget for startup: `runtime.startup_timeout_ms` (60s).
- Global timeout budget for shutdown: `runtime.shutdown_timeout_ms` (30s).

---

## 5. Windows Sleep/Resume/RDP Recovery

### Sleep/Resume

| Event | Action |
|-------|--------|
| **Sleep (WM_POWERBROADCAST: PBT_APMSUSPEND)** | Save checkpoint for all in-flight state; close RPC connections; stop timers; zero secrets in memory; transition to SUSPENDED |
| **Resume (WM_POWERBROADCAST: PBT_APMRESUMEAUTOMATIC)** | Recovery scan: re-establish RPC connections; query chain state for in-flight trades; reconcile DB vs chain; resume timers; transition from SUSPENDED → RESUMING → RUNNING or RECOVERING |

### RDP / Fast User Switching

| Event | Action |
|-------|--------|
| **Session disconnect (RDP)** | Continue running (service mode); pause UI updates; save workspace |
| **Session reconnect** | Resume UI; re-subscribe to IPC channels; refresh dashboard data |
| **Fast user switch** | Pause UI rendering for disconnected session; continue background operations; restore UI on switch back |

---

## 6. Conflict Resolution Rules

| Conflict | Resolution | Reason |
|----------|------------|--------|
| Renderer optimistic update differs from main response | Main response wins | Main is authoritative |
| DB state differs from in-memory state after crash | DB + chain state wins | Durable truth |
| Config file differs from cached config | Config file wins (after validation) | File is persistent; cache is ephemeral |
| Two subsystems claim different trade state | DB state + on-chain query wins | External truth resolves ambiguity |
| Workspace file corrupt | Fall back to default workspace | Safe default over corrupt state |

---

## Cross-References

- **STATE-MACHINE-INDEX.md** — Inter-state-machine coupling.
- **DATABASE-SCHEMA.md** — DDL and persistence details.
- **IPC-PROTOCOL.md** — Typed IPC protocol.
- **DATA-FLOW.md** — Data flow patterns.
- **EVENT-FLOW.md** — Event flow patterns.
- **MEMORY-LIFECYCLE.md** — Memory allocation and eviction.
- **CACHE-MANAGER.md** — Cache eviction policies.
- **TRACEABILITY-MATRIX.md** — REQ-RUNTIME-001, REQ-RUNTIME-002.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.1.0 | 2026-07-27 | Full state domains, source-of-truth rules, state machine index, persistence-before-transition rule, Windows recovery, conflict resolution | Runtime Team |
| 1.0.0 | 2025-01-15 | Initial stub | Runtime Team |
