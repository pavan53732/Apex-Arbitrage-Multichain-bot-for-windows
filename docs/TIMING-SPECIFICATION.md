# Timing Specification

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.1.0 | **Status:** Canonical | **Last Updated:** 2026-07-27 | **Owner:** Ops Team

## Purpose
Defines timeout budgets, retry intervals, worker heartbeats, shutdown timing, startup timing, inter-leg timing, and event delivery timing for every subsystem — with exact values, ranges, and config key references.

---

## 1. Startup Timing Budget

| Phase | Timeout | Config Key | Action on Expiry |
|-------|---------|------------|------------------|
| Phase 1: Kernel Bootstrap (Config, Secrets, Audit) | 10,000 ms | `runtime.startup.phase1_timeout_ms` | FAILED (cannot proceed without config) |
| Phase 2: Infrastructure (Event Bus, DB, Registry, Workers) | 15,000 ms | `runtime.startup.phase2_timeout_ms` | FAILED (core infra missing) |
| Phase 3: Domain Services (RPC, Wallet, Market, AI) | 20,000 ms | `runtime.startup.phase3_timeout_ms` | DEGRADED (may continue without AI) |
| Phase 4: Application (Risk, Trading, Plugins, Dashboard) | 10,000 ms | `runtime.startup.phase4_timeout_ms` | DEGRADED (may continue without plugins) |
| Phase 5: Go-live (Trading READY, Dashboard READY) | 5,000 ms | `runtime.startup.phase5_timeout_ms` | DEGRADED (dashboard not ready) |
| **Total startup budget** | **60,000 ms** | `runtime.startup_timeout_ms` | **Transition to FAILED** |

---

## 2. Shutdown Timing Budget

| Phase | Timeout | Config Key | Action on Expiry |
|-------|---------|------------|------------------|
| Phase 1: Graceful Drain (trades, AI, plugins) | 10,000 ms | `runtime.shutdown.phase1_timeout_ms` | Force-mark in-flight trades for crash recovery |
| Phase 2: Forced Stop (workers, AI cancel, market unsub) | 10,000 ms | `runtime.shutdown.phase2_timeout_ms` | Cancel remaining tasks |
| Phase 3: Teardown (event bus, DB, secrets, audit) | 10,000 ms | `runtime.shutdown.phase3_timeout_ms` | Force close connections |
| **Total shutdown budget** | **30,000 ms** | `runtime.shutdown_timeout_ms` | **Force terminate process** |

---

## 3. Trading and Execution Timing

| Budget | Default | Range | Config Key | Description |
|--------|---------|-------|------------|-------------|
| Trade total timeout (detection → settlement) | 120,000 ms | 60,000–360,000 | `trading.timeout_ms` | Hard limit for entire trade lifecycle |
| Leg execution timeout (per leg) | 30,000 ms | 10,000–120,000 | `execution.mempool_timeout_ms` | Time waiting for TX inclusion in mempool |
| Confirmation timeout (per leg) | 60,000 ms | 30,000–300,000 | `execution.confirmation_timeout_ms` | Time waiting for block confirmations |
| Inter-leg budget (leg 1 confirmed → leg 2 submitted) | 100 ms | 50–500 | `execution.inter_leg_budget_ms` | Window between leg 1 confirmation and leg 2 submission |
| Gas estimation timeout | 5,000 ms | 2,000–30,000 | `execution.gas_estimate_timeout_ms` | Timeout for gas estimation call |
| TX signing timeout | 5,000 ms | 2,000–30,000 | `execution.signing_timeout_ms` | Timeout for wallet signing operation |
| TX broadcast timeout | 10,000 ms | 5,000–60,000 | `execution.broadcast_timeout_ms` | Timeout for RPC broadcast |
| Pending execution timeout | 10,000 ms | 5,000–60,000 | `execution.pending_timeout_ms` | Time in PENDING state before abort |
| Stuck TX grace (nonce replacement window) | 60,000 ms | 30,000–300,000 | `execution.stuck_grace_ms` | Window before escalation |
| Recovery timeout (unwind leg) | 120,000 ms | 60,000–300,000 | `execution.recovery_timeout_ms` | Time for partial/full recovery |

---

## 4. AI Pipeline Timing

| Budget | Default | Range | Config Key | Description |
|--------|---------|-------|------------|-------------|
| Prompt construction (DRAFT → READY) | 10,000 ms | 5,000–60,000 | `ai.draft_timeout_ms` | Total prompt assembly time |
| Provider request timeout | 30,000 ms | 5,000–120,000 | `ai.providers.timeout_ms` | Time waiting for full AI response |
| Streaming chunk timeout | 5,000 ms | 1,000–30,000 | `ai.providers.streaming_timeout_ms` | Time waiting for next streaming chunk |
| Tool invocation timeout | 15,000 ms | 1,000–60,000 | `ai.tools.timeout_ms` | Per-tool execution timeout |
| Fallback provider cooldown | 60,000 ms | 10,000–300,000 | `ai.providers.failure_cooldown_ms` | Time before retrying failed provider |
| Circuit breaker open duration | 120,000 ms | 60,000–600,000 | `ai.providers.circuit_breaker_duration_ms` | Provider circuit breaker cooldown |

---

## 5. Runtime Timing

| Budget | Default | Range | Config Key | Description |
|--------|---------|-------|------------|-------------|
| Health check interval | 5,000 ms | 1,000–60,000 | `runtime.health_check_interval_ms` | Periodic probe cadence |
| Health check probe timeout | 3,000 ms | 500–30,000 | `runtime.health_check_timeout_ms` | Per-probe timeout |
| Worker idle timeout (scale down) | 30,000 ms | 5,000–300,000 | `runtime.worker.idle_timeout_ms` | Time before idle worker terminates |
| Worker init timeout | 5,000 ms | 1,000–30,000 | `runtime.worker.init_timeout_ms` | Worker thread initialization |
| Degraded timeout (→ recovery) | 300,000 ms | 60,000–600,000 | `runtime.degraded_timeout_ms` | Time in DEGRADED before recovery |
| Recovery timeout (→ FAILED) | 120,000 ms | 30,000–360,000 | `runtime.recovery_timeout_ms` | Time in RECOVERING before FAILED |
| Auto-restart delay (after failure) | 10,000 ms | 5,000–120,000 | `service.auto_restart_delay_ms` | Delay before auto-restart |
| RPC reconnect interval | 30,000 ms | 10,000–120,000 | `runtime.rpc.reconnect_interval_ms` | Interval between RPC reconnect attempts |

---

## 6. Retry Timing

| Retry Type | Initial Backoff | Multiplier | Max Backoff | Jitter | Max Attempts | Total Budget |
|-----------|----------------|-----------|-------------|--------|-------------|-------------|
| Execution TX retry | 1,000 ms | 2.0 | 10,000 ms | 200 ms | 3 | 7,000 ms |
| AI provider retry | 1,000 ms | 2.0 | 10,000 ms | 200 ms | 3 | 7,000 ms |
| RPC reconnect | 5,000 ms | 1.0 (linear) | 60,000 ms | 0 ms | 10 | 300,000 ms |
| DB reconnect | 5,000 ms | 1.0 (linear) | 60,000 ms | 0 ms | 5 | 150,000 ms |
| Plugin restart | 0 ms (immediate) | — | — | — | 1 | 15,000 ms |
| Config reload retry | 0 ms | — | — | — | 0 | 0 ms (manual) |

---

## 7. Event Delivery Timing

| Metric | Target | Threshold | Action |
|--------|--------|-----------|--------|
| Event publish latency (P50) | 0.1 ms | > 1 ms | Investigate event bus performance |
| Event publish latency (P99) | 1 ms | > 5 ms | Backpressure; drop low-priority events |
| Event consume latency (P50) | 0.5 ms | > 5 ms | Consumer backlog investigation |
| Event consume latency (P99) | 5 ms | > 20 ms | Consumer throttle or DLQ routing |
| Event delivery guarantee enforcement | 0 retries for at-most-once; ≤ 3 for at-least-once; exactly-once via dedup | DLQ overflow | Critical alert |
| DLQ max retry age | 3 attempts × 7 days retention | > 100 entries | system.warning event |

---

## 8. Dashboard and UI Timing

| Budget | Default | Range | Config Key | Description |
|--------|---------|-------|------------|-------------|
| IPC message deserialize | < 1 ms | — | — | Target for IPC reception |
| Data normalization | < 5 ms | — | — | Target for widget data transform |
| Widget update debounce | 50 ms | 10–200 | `dashboard.widget_debounce_ms` | High-frequency update batching |
| Render budget (60fps target) | < 16 ms | — | — | Widget render per frame |
| Workspace autosave interval | 30,000 ms | 5,000–300,000 | `dashboard.workspace_autosave_interval_ms` | Periodic persistence |
| Workspace save debounce | 500 ms | 100–5,000 | `dashboard.workspace_save_debounce_ms` | Delay after change before save |

---

## 9. Worker Heartbeat

| Aspect | Value | Description |
|--------|-------|-------------|
| Heartbeat interval | `runtime.health_check_interval_ms` (5,000 ms) | Workers report status to pool manager |
| Heartbeat timeout | 2 × heartbeat interval | If 2 heartbeats missed → worker considered failed |
| Task progress heartbeat | Every 1,000 ms during long tasks | Long-running tasks emit progress signals |
| Pool manager heartbeat | Every `runtime.health_check_interval_ms` | Pool manager reports pool status to runtime orchestrator |

---

## Cross-References

- **EXECUTION-ENGINE.md** — Execution timeout handling.
- **AI-PIPELINE.md** — AI provider timeout and retry.
- **RUNTIME-OPERATIONS.md** — Startup/shutdown timing.
- **WORKER-POOL.md** — Worker heartbeat and pool timing.
- **EVENT-BUS.md** — Event delivery latency targets.
- **DASHBOARD-RUNTIME.md** — Dashboard timing budgets.
- **CONFIGURATION-REFERENCE.md** — All timing config keys.
- **END-TO-END-WIRING-CONTRACT.md** — Total end-to-end timing budget.
- **TRACEABILITY-MATRIX.md** — Timing requirement coverage.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.1.0 | 2026-07-27 | Complete timing specification with 9 categories, exact values, ranges, retry timing, event timing, heartbeats | Ops Team |
| 1.0.0 | 2025-01-15 | Initial stub (2 lines) | Ops Team |
