---
type: INDEX
owner: Architecture Team
status: Canonical
version: 1.0.0
purpose: Provides a single authoritative index tying all major lifecycle state machines together — showing inter-state-machine coupling, shared transitions, startup/shutdown sequencing, and recovery coordination across the entire platform.
scope: None
last_updated: 2026-07-29
canonical_source: docs/state-machines/STATE-MACHINE-INDEX.md
---

# System-Wide State Machine Index

## Document type
Document type: [INDEX]

## Version
**Version:** 1.1.0 | **Status:** Canonical | **Last Updated:** 2026-07-27 | **Owner:** Architecture Team

## Purpose
Provides a single authoritative index tying all major lifecycle state machines together — showing inter-state-machine coupling, shared transitions, startup/shutdown sequencing, and recovery coordination across the entire platform.

---

## 1. State Machine Inventory

| State Machine | Owner Document | States | Layer | Coupling |
|---------------|---------------|--------|-------|----------|
| Engine Lifecycle | ENGINE-STATE-MACHINE.md | 7 (INITIALISING, READY, RUNNING, DEGRADED, RECOVERING, FAILED, STOPPED) | Runtime (Layer 2) | Master lifecycle; gates all other machines |
| Execution Lifecycle | EXECUTION-STATE-MACHINE.md | 14 (PENDING, QUEUED, SIGNING, BROADCASTING, IN_MEMPOOL, STUCK, REPLACED, CONFIRMING, FINALIZED, REVERTED, FAILED, RETRYING, PARTIAL_RECOVERY, ABORTED) | Trading (Layer 3) | Depends on Engine RUNNING |
| Worker Lifecycle | WORKER-STATE-MACHINE.md | 8 (SPAWNED, INITIALIZING, IDLE, BUSY, PAUSED, DRAINING, FAILED, TERMINATED) | Runtime (Layer 2) | Depends on Engine state |
| Plugin Lifecycle | PLUGIN-STATE-MACHINE.md | 13 (DISCOVERED, VALIDATING, VALIDATED, REJECTED, INSTALLING, INSTALLED, LOADING, ACTIVE, SUSPENDED, UPDATING, FAILED, UNLOADING, UNLOADED) | Plugin (Layer 13) | Depends on Engine RUNNING |
| Service Lifecycle | SERVICE-STATE-MACHINE.md | 11 (INSTALLING, INSTALLED, STARTING, RUNNING, PAUSED, STOPPING, STOPPED, FAILED, SUSPENDED, RESUMING, RECOVERING) | Windows (Layer 9) | OS-level; gates Engine lifecycle |
| AI Orchestration | AI-STATE-MACHINE.md | 10 (IDLE, DRAFT, READY, RUNNING, WAITING, TOOL_CALLING, COMPLETED, FAILED, RETRYING, CANCELLED) | AI (Layer 6) | Depends on Engine RUNNING; drives Prompt Lifecycle |
| Trade Lifecycle | TRADING-LIFECYCLE.md | Defined in trading lifecycle doc | Trading (Layer 3) | Depends on Engine RUNNING; triggers Execution Lifecycle |
| Shutdown Lifecycle | SHUTDOWN-LIFECYCLE.md | Defined in shutdown lifecycle doc | Runtime (Layer 2) | Triggered by Engine STOPPED |
| Prompt Lifecycle | PROMPT-LIFECYCLE.md | 11 (IDLE, CONSTRUCTING, INJECTING_MEMORY, INJECTING_CONTEXT, COMPRESSING, VALIDATING, READY, EXECUTING, COMPLETED, ARCHIVING, FAILED) | AI (Layer 6) | Driven by AI DRAFT → READY transitions |

---

## 2. Inter-State-Machine Coupling

### Engine → All Other Machines

The Engine state machine is the **master lifecycle coordinator**. All other state machines depend on its state:

| Engine State | Effect on Other Machines |
|--------------|-------------------------|
| **INITIALISING** | All machines blocked; subsystems are being brought up |
| **READY** | Plugin, AI, Worker machines may start initializing; trading NOT yet active |
| **RUNNING** | All machines operational; trading, execution, AI, workers all active |
| **DEGRADED** | Degraded subsystem's machine paused; others continue |
| **RECOVERING** | Affected subsystem machine in recovery; others continue or pause per dependency |
| **FAILED** | All machines stopped; operator intervention required |
| **STOPPED** | All machines terminated; process exit imminent |

### Service → Engine Coupling

| Service State | Engine State | Coupling |
|---------------|-------------|----------|
| STARTING | INITIALISING | Service start triggers Engine init |
| RUNNING | RUNNING or READY | Service operational; Engine follows |
| SUSPENDED | — (checkpoint saved) | Windows sleep pauses everything |
| RESUMING | RECOVERING (after resume) | Resume triggers recovery scan → Engine RECOVERING |
| STOPPING | STOPPED | Service stop triggers Engine shutdown |
| FAILED | FAILED | Service failure triggers Engine failure |

### Trade → Execution Coupling

| Trade State | Execution State | Coupling |
|-------------|----------------|----------|
| EXECUTING_LEG_1 | PENDING → QUEUED → SIGNING → BROADCASTING → IN_MEMPOOL → CONFIRMING → FINALIZED | Trade drives execution through full pipeline |
| LEG_1_FAILED | FAILED or REVERTED | Trade failure drives execution failure |
| ABORTED | ABORTED | Trade abort drives execution abort |

### AI → Prompt Coupling

| AI State | Prompt Lifecycle State | Coupling |
|----------|------------------------|----------|
| DRAFT | CONSTRUCTING → INJECTING_MEMORY → INJECTING_CONTEXT → COMPRESSING → VALIDATING | AI DRAFT triggers full prompt construction pipeline |
| READY | READY | AI ready means prompt is ready |
| RUNNING | EXECUTING | AI execution = prompt dispatch to provider |
| TOOL_CALLING | EXECUTING (tool injection) | AI tool call injects tool result into prompt |
| COMPLETED | COMPLETED → ARCHIVING | AI completion triggers prompt archiving |
| FAILED | FAILED | AI failure = prompt failure |

---

## 3. Startup Sequence State Coupling

All state machines initialize in a specific order during startup:

```
1. Service → STARTING (if service mode)
2. Engine → INITIALISING
   a. Worker Pool → SPAWNED → INITIALIZING → IDLE
   b. Event Bus → INITIALISING → READY
   c. Database → INITIALISING → READY
   d. Config Manager → INITIALISING → READY
   e. Secret Manager → INITIALISING → READY
3. Engine → READY (latch countdown complete)
   f. Chain/RPC → INITIALISING → READY
   g. Wallet → INITIALISING → READY
   h. Market Data → INITIALISING → READY
   i. AI Pipeline → INITIALISING → READY
4. Engine → RUNNING
   j. Trading Engine → READY → RUNNING
   k. Plugin Manager → DISCOVERED → VALIDATING → VALIDATED → LOADING → ACTIVE
   l. Dashboard → IDLE → LOADING → READY
5. Service → RUNNING
```

**Latch**: `std::latch(6)` — Event Bus, Database, Chain/RPC, Wallet, Market Data, AI Pipeline must all reach READY before Engine transitions to RUNNING.

---

## 4. Shutdown Sequence State Coupling

Shutdown follows reverse startup order:

```
1. Service → STOPPING
2. Engine → STOPPED
   a. Trading Engine → STOPPED (no new trades; in-flight complete)
   b. AI Pipeline → IDLE (drain pending requests)
   c. Plugin Manager → ACTIVE → SUSPENDED → UNLOADING → UNLOADED
   d. Dashboard → IDLE (close UI)
3. Infrastructure shutdown:
   e. Market Data → STOPPED (unsubscribe feeds)
   f. Wallet → STOPPED (lock keychain)
   g. Chain/RPC → STOPPED (close connections)
   h. Worker Pool → IDLE → DRAINING → TERMINATED
   i. Database → STOPPED (flush + close)
   j. Event Bus → DRAINED → STOPPED
4. Engine → STOPPED (confirmed)
5. Service → STOPPED
```

---

## 5. Recovery Coordination

When multiple state machines need recovery simultaneously:

| Priority | Machine | Recovery First? | Reason |
|----------|---------|-----------------|--------|
| 1 | Engine | Yes | Master coordinator; must be RUNNING for others to recover |
| 2 | Event Bus | Yes | All recovery events flow through event bus |
| 3 | Database | Yes | Recovery state is persisted in database |
| 4 | Worker Pool | Yes | Workers needed for recovery tasks |
| 5 | Chain/RPC | Yes | Need chain state for trade reconciliation |
| 6 | Wallet | Yes | Need wallet state for in-flight trade recovery |
| 7 | Trading | After dependencies | Must reconcile in-flight trades first |
| 8 | AI | After core | Advisory; not critical for recovery |
| 9 | Plugin | Last | Disabled during recovery; checked after core |
| 10 | Dashboard | Last | UI can wait; shows recovery progress |

### Recovery Coupling Rules

- Engine must reach RUNNING before any subsystem recovery begins.
- Event Bus must be operational before any recovery events are emitted.
- Database must be connected before trade reconciliation queries.
- Trading Engine recovery must wait for Chain/RPC and Wallet recovery.
- Plugin recovery is deferred until core subsystems are healthy.

---

## 6. Configuration Reload State Handling

| Engine State | Config Reload Allowed? | Effect |
|--------------|----------------------|--------|
| INITIALISING | No (all config applied on startup) | Config loaded at init |
| READY | Yes (hot-reload keys only) | Subsystems receive `config.updated` event |
| RUNNING | Yes (hot-reload keys only) | Subsystems receive `config.updated` event; restart-required keys queued |
| DEGRADED | Yes (hot-reload keys only) | Same as RUNNING |
| RECOVERING | No (config changes blocked during recovery) | Queued for post-recovery |
| FAILED | No (operator must restart) | Config changes not applied |
| STOPPED | No (no active processing) | Config changes applied on next start |

---

## Cross-References

- **ENGINE-STATE-MACHINE.md** — Engine lifecycle states.
- **EXECUTION-STATE-MACHINE.md** — Execution lifecycle states.
- **WORKER-STATE-MACHINE.md** — Worker lifecycle states.
- **PLUGIN-STATE-MACHINE.md** — Plugin lifecycle states.
- **SERVICE-STATE-MACHINE.md** — Service lifecycle states.
- **AI-STATE-MACHINE.md** — AI orchestration states.
- **PROMPT-LIFECYCLE.md** — Prompt lifecycle states.
- **TRADING-LIFECYCLE.md** — Trade lifecycle states.
- **SHUTDOWN-LIFECYCLE.md** — Shutdown lifecycle states.
- **STATE-MANAGEMENT.md** — Global state management contract.
- **TRACEABILITY-MATRIX.md** — REQ-RUNTIME-001 through REQ-RUNTIME-004.
- **DOCUMENTATION-MAP.md** — Document authority hierarchy.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.1.0 | 2026-07-27 | New: system-wide state machine index with coupling, startup/shutdown sequencing, recovery coordination | Architecture Team |
