---
type: CONTRACT
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Defines the threading architecture — main thread, worker threads, background task rules, thread safety guarantees, and thread lifecycle.
scope: None
last_updated: 2026-07-29
canonical_source: docs/THREADING-MODEL.md
---

# Threading Model

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-27 | **Owner:** Runtime Team

## Purpose
Defines the threading architecture — main thread, worker threads, background task rules, thread safety guarantees, and thread lifecycle.

---

## 1. Thread Architecture

### Thread Roles

| Thread / Pool | Owner | Responsibility | Stack Size | Priority |
|---------------|-------|----------------|------------|----------|
| **Main (UI)** | Desktop Shell | UI rendering, IPC message dispatch, user input | 8 MB | Normal |
| **Main (Service)** | Runtime Orchestrator | Service orchestration, state machine transitions | 8 MB | High |
| **Event Bus** | Event Bus | Event routing, delivery, DLQ management | 4 MB | High |
| **Worker Pool** | Worker Pool | CPU-bound trading analysis, simulation, backtesting | 2 MB each | BelowNormal |
| **IO Pool** | RPC/Network | HTTP/WebSocket I/O, chain RPC calls | 2 MB each | Normal |
| **AI Pool** | AI Pipeline | AI provider calls, prompt processing, tool execution | 4 MB each | Normal |
| **Plugin Pool** | Plugin Executor | Plugin execution (sandboxed) | 4 MB each | BelowNormal |
| **Database** | Persistence Layer | SQLite / Postgres queries, migrations | 2 MB | Normal |
| **Health Check** | Health Checker | Periodic health probes | 1 MB | Low |
| **Timer / Scheduler** | Task Scheduler | Cron jobs, scheduled tasks, retry timers | 1 MB | Normal |

### Thread Counts

| Pool | Min Threads | Max Threads | Growth Policy |
|------|-------------|-------------|---------------|
| Worker Pool | `runtime.worker.min_workers`: 2 | `runtime.worker.max_workers`: 20 | On-demand, up to max |
| IO Pool | 4 | 32 | On-demand, up to max |
| AI Pool | 1 | 8 | On-demand, up to max |
| Plugin Pool | 1 | 4 | Per-plugin sandbox |
| Database | 1 | 4 | Fixed pool |

---

## 2. Thread Safety Rules

| Resource Type | Safety Mechanism | Contention Strategy |
|---------------|------------------|---------------------|
| Shared state (config, registry) | `std::shared_mutex` (rwlock) | Readers preferred; writers queue |
| Trading state (positions, orders) | Single-writer lease + `std::mutex` | Exclusive write; blocked reads yield |
| Event queue | Lock-free SPSC queue (event bus) | No contention on producer side |
| Plugin sandbox | Process-level isolation (not threads) | No shared memory between plugins |
| Database connection pool | `std::mutex` per pool | Short wait via condition variable |
| Log buffer | `std::mutex` + flush batch | Lock per write, batched flush |

### Prohibited Patterns

- **Lock inversion**: If lock A must be acquired before lock B everywhere, violation is detected by runtime lock-order validator.
- **Thread blocking in main thread**: Main thread must never block on I/O, DB, or AI calls. All blocking operations use async/futures.
- **Shared mutable state across pools**: State crossing pool boundaries must be serialized (message, event, or future).
- **Recursive locking**: Not permitted. Use `std::recursive_mutex` only in designated lock-order validator.

---

## 3. Async Patterns

All async operations use a consistent pattern:

```cpp
// C++ pseudo-code
std::future<Result> async_operation(Params params) {
    return std::async(std::launch::async, [params] {
        // Execute on IO or Worker pool
        return compute(params);
    });
}
```

| Pattern | Usage | Return Type |
|---------|-------|-------------|
| Fire-and-forget | Logging, telemetry, non-critical events | `void` |
| Future / Promise | RPC calls, provider requests, DB queries | `std::future<T>` |
| Callback | Event bus delivery, plugin responses | Function pointer + context |
| Coroutine | Streaming responses, websocket handling | `std::generator<T>` |

---

## 4. Thread Lifecycle

### Startup Sequence
1. Main (UI) thread starts.
2. IO Pool initialized (4 threads).
3. Database Pool initialized (1 thread).
4. Event Bus thread started.
5. Health Check thread started.
6. Worker Pool initialized (min workers).
7. AI Pool initialized (1 thread).
8. Plugin Pool initialized (1 thread).
9. Timer/Scheduler thread started.

### Shutdown Sequence (reverse)
1. Timer/Scheduler stopped.
2. Plugin Pool drained and stopped.
3. AI Pool drained and stopped.
4. Worker Pool drained and stopped.
5. Health Check stopped.
6. Event Bus drained and stopped.
7. Database Pool flushed and stopped.
8. IO Pool flushed and stopped.
9. Main (UI) thread exited.

---

## 5. Thread Ownership Matrix

| Resource | Owner Thread/Pool | Accessors | Locking | Transfer Mechanism |
|----------|------------------|-----------|---------|-------------------|
| **Trading state** (positions, orders) | Main (Service) | Worker Pool (read-only), Risk Engine (read-only) | Single-writer lease | Event broadcast |
| **Configuration** | Main (Service) | All pools (read-only) | `shared_mutex` rwlock | Config change event |
| **Registry data** (chains, providers, plugins) | Main (Service) | All pools (read-only) | `shared_mutex` rwlock | Registry update event |
| **Event queue** | Event Bus thread | Producers (any), Consumers (any) | Lock-free SPSC | Direct enqueue/dequeue |
| **Wallet state** | Main (Service) | Execution Engine (read-only) | `shared_mutex` rwlock | Wallet change event |
| **AI context** | AI Pool | AI Pipeline (same pool) | Per-request isolation | Internal |
| **Database connections** | Database Pool | Any (via DB API) | Pool mutex | Connection lease |
| **Plugin sandbox** | Plugin Pool | Plugin Manager (same pool) | Process isolation | IPC message |
| **Health check results** | Health Check thread | Dashboard (read-only) | `shared_mutex` rwlock | Health event |
| **Dashboard workspace** | Main (UI) | Dashboard Runtime (same thread) | No lock needed (single thread) | IPC channel |

### Thread Ownership Rules
1. **Single-writer principle**: Each resource has exactly one owning thread that may mutate it.
2. **Read-only access**: All other threads access resources via read-only snapshots (events).
3. **No cross-pool mutation**: A thread from one pool must never directly mutate state owned by another pool.
4. **Lease transfer**: If a thread needs temporary write access, it acquires a lease with timeout. Lease holder is the sole writer for the lease duration.
5. **Lease timeout**: If lease exceeds `runtime.lease_timeout_ms` (default 30000ms), lease is forcibly revoked and resource reverts to primary owner.

---

## 6. Queue Ownership & Bounded Capacity

| Queue | Owner | Producer Pool | Consumer Pool | Max Size | Overflow Policy | Priority |
|-------|-------|-------------|-------------|----------|----------------|----------|
| **Event bus (critical)** | Event Bus | Trading, Execution, Risk | Trading, Dashboard, Notification | 10000 | Drop oldest (keep Critical priority) | Priority-based |
| **Event bus (standard)** | Event Bus | System, Network, Config | Dashboard, Health, Log Stream | 50000 | Drop oldest | FIFO |
| **Worker task queue** | Worker Pool | Trading Engine, AI Pipeline | Worker threads | 200 | Reject (return BUSY to caller) | Priority-based |
| **AI request queue** | AI Pipeline | Trading Engine, Dashboard | AI Pool threads | 50 | Queue (wait for slot) | Priority-based |
| **IO request queue** | IO Pool | Any (RPC, HTTP, WS) | IO Pool threads | 500 | Queue (wait for slot) | FIFO |
| **Plugin command queue** | Plugin Pool | Dashboard, Plugin Manager | Plugin sandbox processes | 20 | Reject (return BUSY) | FIFO |
| **Database query queue** | Database Pool | Any (via DB API) | Database threads | 100 | Queue (wait for connection) | FIFO |
| **IPC outbound queue** | Main (UI) | Backend → Dashboard | Dashboard Runtime | 1000 | Drop oldest non-critical | Priority-based |

### Queue Bounded Capacity Rules
- All queues have hard bounds — no unbounded growth.
- Overflow policies are enforced per queue type.
- Queue depth is monitored: metric `runtime.queue.<name>.depth` updated every 5s.
- If any queue exceeds 80% capacity → `system.warning` event emitted.
- If any queue exceeds 95% capacity → `system.error` event emitted with severity HIGH.

---

## 7. CPU & GPU Budgeting

### 7.1 CPU Budget Allocation

| Pool | CPU Budget (% of total) | Max Concurrent Threads | Priority | Config Key |
|------|------------------------|----------------------|----------|------------|
| **Main (UI)** | 15% | 1 | Normal | — |
| **Main (Service)** | 10% | 1 | High | — |
| **Worker Pool** | 30% | Up to 20 | BelowNormal | `runtime.worker.max_workers` |
| **IO Pool** | 15% | Up to 32 | Normal | `runtime.io.max_threads` |
| **AI Pool** | 10% | Up to 8 | Normal | `runtime.ai.max_threads` |
| **Plugin Pool** | 5% | Up to 4 | BelowNormal | `runtime.plugin.max_threads` |
| **Database Pool** | 5% | Up to 4 | Normal | `runtime.db.max_connections` |
| **Health Check** | 2% | 1 | Low | — |
| **Timer/Scheduler** | 3% | 1 | Normal | — |
| **OS & overhead** | 5% | — | — | — |

### 7.2 CPU Throttling Rules

| Condition | Action | Threshold |
|-----------|--------|-----------|
| **Total CPU > 80%** | Reduce Worker Pool max threads by 50% | `runtime.cpu.high_threshold_pct: 80` |
| **Total CPU > 90%** | Disable Plugin Pool + Learning Agent | `runtime.cpu.critical_threshold_pct: 90` |
| **Total CPU > 95%** | Only P0 services active (Trading, Risk, Event Bus) | `runtime.cpu.emergency_threshold_pct: 95` |
| **CPU recovered (< 70%)** | Restore pools gradually (1 thread/min) | `runtime.cpu.recovery_threshold_pct: 70` |

### 7.3 GPU Budget

| Allocation | Budget | Purpose |
|-----------|--------|---------|
| **Dashboard rendering** | 15ms per frame | Widget rendering + compositing |
| **AI local inference** | When available, max 100ms per request | Local model inference (Ollama) |
| **GPU not available** | 0ms (all CPU fallback) | Software rendering |

---

## 8. Priority Inversion Handling

### 8.1 Priority Inversion Detection

```
1. Track thread priority and current resource lock held.
2. If a Low-priority thread holds a lock needed by a High-priority thread:
   → Priority inversion detected.
3. Prevention: Use priority inheritance protocol:
   - Low-priority thread temporarily elevated to High-priority while holding critical lock.
   - Lock released → thread returns to original priority.
4. Timeout: If priority inversion persists > runtime.priority_inversion_timeout_ms (default 5000ms):
   → Emit system.warning event with inversion details.
   → Force lock release after timeout (with rollback of incomplete work).
```

### 8.2 Priority Inheritance Matrix

| Lock | Protected Resource | Normal Owner Priority | Inheritance Target |
|------|-------------------|---------------------|-------------------|
| `trading_state_mutex` | Positions, orders | High (Service thread) | High → inherited to any |
| `config_rwlock` | Configuration | Normal (Service thread) | Inherits to requester's priority |
| `registry_rwlock` | Chain/provider/plugin registry | Normal (Service thread) | Inherits to requester's priority |
| `db_pool_mutex` | Database connections | Normal (DB thread) | Inherits to requester's priority |
| `event_queue_spsc` | Event bus (lock-free) | No lock needed | — |

---

## 9. Deadlock Detection & Prevention

### 9.1 Deadlock Detection

- Runtime lock-order validator tracks all `std::mutex` acquisitions.
- If a cycle is detected (A → B → A), `system.error` event emitted, thread terminated.
- Deadlock dump written to `runtime/logs/deadlock-<timestamp>.json` containing full lock graph.
- Threads failing to acquire a lock within `runtime.startup_timeout_ms` (default 60000ms) considered deadlocked → recovery triggered.

### 9.2 Deadlock Prevention Rules

1. **Lock ordering**: All locks must be acquired in a globally defined order (config → registry → trading → db → event → log).
2. **No nested locks**: A thread must not hold more than one mutex simultaneously unless following the lock order.
3. **Timeout on all lock acquisitions**: Every `std::mutex` acquisition uses `try_lock_for(timeout_ms)`.
4. **Lock-free where possible**: Event bus uses lock-free SPSC; health check uses rwlock.
5. **Watchdog timer**: A dedicated watchdog thread monitors all thread heartbeats; missing heartbeat for `runtime.thread_heartbeat_timeout_ms` (default 30000ms) → emit deadlock warning.

---

## 10. Resource Throttling

### 10.1 Throttling Policies

| Resource | Throttle Trigger | Throttle Action | Recovery |
|----------|-----------------|----------------|---------|
| **Memory** | Total > `runtime.memory.max_mb` (80% physical) | Suspend P4 widgets, reduce Worker Pool | Gradual restore below 70% |
| **CPU** | Total > 80% | Reduce Worker Pool, disable P3 tasks | Gradual restore below 70% |
| **Network bandwidth** | > `runtime.network.max_mbps` | Rate-limit RPC calls, batch queries | Auto restore |
| **Disk I/O** | > `runtime.disk.max_iops` | Defer non-critical DB writes, batch | Auto restore |
| **IPC throughput** | > 100 msg/s per channel | Drop non-critical, keep Critical priority | Auto restore |
| **Event queue depth** | > 80% capacity | Drop oldest non-critical events | Auto restore |

### 10.2 Memory Pressure Handling

```
1. Monitor total memory usage every 5s.
2. Memory levels:
   NORMAL (< 70% of runtime.memory.max_mb)
   PRESSURE (70-80%): emit system.warning, start cleanup
   HIGH (80-90%): suspend P4 + P3 tasks, reduce Worker Pool, aggressive GC
   CRITICAL (90-95%): suspend P2 + P1 tasks, only P0 active
   EMERGENCY (> 95%): emergency GC, force-free all non-essential resources

3. Cleanup actions (in order):
   a. Clear widget data caches (P4 first, then P3, P2)
   b. Reduce Worker Pool to min_workers
   c. Suspend non-active workspace widgets
   d. Flush stale event queue entries
   e. Force database WAL checkpoint
   f. Emergency: restart backend process (preserving trading state)
```

---

## 11. Cross-Subsystem Integration

### 11.1 Who Calls Threading Model

| Caller | Purpose | Contract |
|--------|---------|----------|
| Runtime Orchestrator | Thread pool sizing, priority changes | `runtime.pool.resize` API |
| Config Manager | Thread pool config change | `config.updated` event |
| Health Checker | Thread health monitoring | `runtime.thread.heartbeat` metric |
| Trading Engine | Worker pool task submission | `runtime.worker.submit` API |
| AI Pipeline | AI pool request submission | `runtime.ai.submit` API |
| Plugin Manager | Plugin pool task submission | `runtime.plugin.submit` API |

### 11.2 Events Threading Model Emits

| Event | Payload | Consumer |
|-------|---------|----------|
| `runtime.pool.resized` | `{pool_name, old_size, new_size, reason}` | Dashboard, Health |
| `runtime.thread.deadlock` | `{thread_ids, lock_graph, dump_path}` | Dashboard, Operator (Critical) |
| `runtime.thread.priority_inversion` | `{holder_thread, waiter_thread, lock, duration_ms}` | Dashboard, Health |
| `runtime.memory.pressure` | `{level, usage_pct, cleanup_action}` | Dashboard, Health |
| `runtime.cpu.throttle` | `{level, cpu_pct, disabled_pools}` | Dashboard, Health |
| `runtime.queue.overflow` | `{queue_name, depth, max_depth, overflow_action}` | Dashboard, Health |

---

## Cross-References

- **CONCURRENCY-MODEL.md** — Locks, queues, cancellation, and deadlock avoidance.
- **WORKER-POOL.md** — Worker thread lifecycle and pool orchestration.
- **RESOURCE-MANAGER.md** — Resource management and throttling.
- **TASK-SCHEDULER.md** — Task scheduling and cron jobs.
- **EVENT-BUS.md** — Event bus threading model.
- **ARCHITECTURE.md** — System threading boundaries.
- **BOOTSTRAP-SEQUENCE.md** — Thread startup sequencing.
- **SHUTDOWN-LIFECYCLE.md** — Thread shutdown sequencing.
- **RESOURCE-BUDGET-SPECIFICATION.md** — Resource budgets per subsystem.
- **CAPACITY-PLANNING.md** — Capacity planning and sizing.
- **CONFIGURATION-REFERENCE.md** — Thread config keys (`runtime.*`).
- **END-TO-END-WIRING-CONTRACT.md** — Cross-subsystem wiring.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-27 | Production-grade threading contract: thread ownership matrix (10 resources), queue ownership & bounded capacity (8 queues), CPU/GPU budgeting with throttling, priority inversion handling with inheritance matrix, deadlock prevention rules (5 rules + watchdog), resource throttling policies (6 resources), memory pressure handling (5 levels + cleanup actions), cross-subsystem integration | Runtime Team |
| 0.2.0 | 2026-07-27 | Complete threading architecture with roles, safety rules, lifecycles | Runtime Team |
| 0.1.0 | 2026-07-27 | Initial stub | Runtime Team |