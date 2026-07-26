# Threading Model

## Document type
Document type: [REFERENCE]

## Version
**Version:** 0.2.0 | **Status:** Draft | **Last Updated:** 2026-07-27 | **Owner:** Runtime Team

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

## 5. Deadlock Detection

- A runtime lock-order validator tracks all `std::mutex` acquisitions.
- If a cycle is detected (A → B → A), a `system.error` event is emitted and the thread is terminated.
- A deadlock dump is written to `runtime/logs/deadlock-<timestamp>.json` containing the full lock graph.
- Threads that fail to acquire a lock within `runtime.startup_timeout_ms` (default: 60000ms) are considered deadlocked and recovery is triggered.

---

## Cross-References

- **CONCURRENCY-MODEL.md** — Locks, queues, cancellation, and deadlock avoidance.
- **WORKER-POOL.md** — Worker thread lifecycle and pool orchestration.
- **EVENT-BUS.md** — Event bus threading model.
- **ARCHITECTURE.md** — System threading boundaries.
- **BOOTSTRAP-SEQUENCE.md** — Thread startup sequencing.
- **SHUTDOWN-LIFECYCLE.md** — Thread shutdown sequencing.
- **CONFIGURATION-REFERENCE.md** — Thread config keys (`runtime.worker.*`).

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 0.2.0 | 2026-07-27 | Complete threading architecture with roles, safety rules, lifecycles | Runtime Team |
| 0.1.0 | 2026-07-27 | Initial stub | Runtime Team |