---
metadata_schema_version: 1.0
document_id: DOC-0090
title: Task Scheduler
plane: Product Specification
domain: Runtime
class: Specification
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/runtime/task-scheduler.md
related_concepts:
  - CONCEPT-0090
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Runtime
type: CONTRACT
purpose: "Defines task scheduling, priority queues, and task lifecycle."
scope: Task scheduling for runtime components.
---

# Task Scheduler

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-29 | **Owner:** Runtime Team

## Purpose
Defines the task scheduling system — cron-style scheduling, interval-based scheduling, one-shot tasks, scheduler behavior, task priority, queue integration, retry scheduling, and cross-subsystem integration contracts.

---

## 1. Scheduler Architecture

### 1.1 Scheduler Components

| Component | Responsibility | Thread | Priority |
|-----------|---------------|--------|----------|
| **Cron Engine** | Evaluate cron expressions, trigger scheduled tasks | Timer/Scheduler thread | Normal |
| **Interval Timer** | Run periodic tasks at fixed intervals | Timer/Scheduler thread | Normal |
| **One-Shot Dispatcher** | Execute delayed tasks at specific time | Timer/Scheduler thread | Normal |
| **Retry Scheduler** | Re-queue failed tasks with exponential backoff | Timer/Scheduler thread | Normal |
| **Worker Bridge** | Submit tasks to Worker Pool | Main (Service) thread | Normal |

### 1.2 Scheduling Flow

```
Schedule Definition → Cron Engine / Interval Timer / One-Shot Dispatcher
  → Evaluate Trigger → Create Task → Worker Bridge → Worker Pool → Execute
  → On Completion → Emit Result Event
  → On Failure → Retry Scheduler → Re-queue (if retryable)
```

---

## 2. Scheduled Task Inventory

| Task ID | Type | Schedule | Priority | Timeout | Retryable | Max Retries | Description |
|---------|------|----------|----------|---------|-----------|------------|-------------|
| `scheduler.health_check` | Interval | 30s | P2 | 5000ms | Yes | 3 | Periodic health check of all subsystems |
| `scheduler.provider_health` | Interval | 60s | P2 | 10000ms | Yes | 3 | AI provider health probes |
| `scheduler.gas_price_update` | Interval | 15s | P1 | 5000ms | Yes | 2 | Gas price refresh for active chains |
| `scheduler.wallet_balance_refresh` | Interval | 10s | P1 | 3000ms | Yes | 2 | Wallet balance refresh |
| `scheduler.chain_block_monitor` | Interval | 5s | P1 | 5000ms | No | 0 | Block height tracking for active chains |
| `scheduler.strategy_weight_update` | Cron | `0 */5 * * *` (every 5 min) | P3 | 500ms | No | 0 | Strategy weight recalculation |
| `scheduler.daily_reflection` | Cron | `0 0 * * *` (daily midnight) | P3 | 30000ms | Yes | 1 | AI daily strategy reflection |
| `scheduler.config_reload_check` | Interval | 60s | P2 | 2000ms | No | 0 | Check for config file changes |
| `scheduler.db_maintenance` | Cron | `0 3 * * *` (daily 3am) | P3 | 30000ms | Yes | 1 | SQLite WAL checkpoint, cleanup |
| `scheduler.metrics_flush` | Interval | 30s | P3 | 2000ms | No | 0 | Flush accumulated metrics to storage |
| `scheduler.secret_rotation_check` | Cron | `0 0 1 * *` (monthly) | P1 | 10000ms | No | 0 | Check secrets nearing rotation deadline |
| `scheduler.event_dlq_purge` | Interval | 24h | P2 | 5000ms | No | 0 | Purge DLQ entries older than 90 days |
| `scheduler.workspace_autosave` | Interval | 30s | P3 | 1000ms | No | 0 | Dashboard workspace autosave |
| `scheduler.log_rotation` | Cron | `0 0 * * *` (daily midnight) | P3 | 5000ms | No | 0 | Log file rotation and compression |
| `scheduler.market_data_cache_prune` | Interval | 5min | P3 | 1000ms | No | 0 | Prune stale market data cache entries |
| `scheduler.ai_cost_reset` | Cron | `0 0 1 * *` (monthly) | P1 | 1000ms | No | 0 | Reset monthly AI cost tracking |

---

## 3. Scheduling Behavior

### 3.1 Cron Engine

- Standard cron expression format: `minute hour day month weekday`.
- Supports extended syntax: `*/N` (every N), `L` (last day), `W` (nearest weekday).
- Timezone: `scheduler.timezone` (default `UTC`, configurable).
- If a cron trigger fires while the previous instance is still running → skip (do not overlap).
- Cron tasks are evaluated every second; misfire window: `scheduler.misfire_grace_ms` (default 5000ms).

### 3.2 Interval Timer

- Fixed interval between task completions (not between starts).
- If task duration > interval → next run starts immediately after completion.
- If interval is 0 → continuous polling (no delay between completions).
- Interval jitter: random ±`scheduler.interval_jitter_pct` (default 5%) to prevent thundering herd.

### 3.3 One-Shot Dispatcher

- Execute a task at a specific timestamp (absolute scheduling).
- After execution, task is removed from schedule (no repeat).
- If one-shot task misses its window by > `scheduler.misfire_grace_ms` → discard with warning.
- Used for: delayed retry, startup initialization tasks, one-time migrations.

### 3.4 Retry Scheduler

```
1. Task fails → determine if retryable (from task definition).
2. If retryable → calculate backoff: base_delay × 2^(attempt_count) × jitter
   base_delay: scheduler.retry.base_delay_ms (default 1000ms)
   max_delay: scheduler.retry.max_delay_ms (default 30000ms)
   jitter: random ±scheduler.retry.jitter_pct (default 10%)
3. Submit one-shot task at: now + backoff.
4. If attempt_count >= max_retries → mark as PERMANENT_FAILURE, emit event.
5. Retry task uses same priority as original task.
```

---

## 4. Priority Integration with Worker Pool

| Scheduler Priority | Worker Pool Priority Queue | Preemption |
|-------------------|--------------------------|------------|
| P0 (none scheduled) | P0 Critical | Can preempt P2/P3 |
| P1 | P1 High | Can preempt P3 |
| P2 | P2 Medium | No preemption |
| P3 | P3 Low | No preemption |

- Scheduler submits tasks to Worker Pool via `runtime.worker.submit` API.
- Task includes: `{task_id, task_type, priority, timeout_ms, payload, retryable, max_retries}`.
- Worker Pool respects priority ordering (see WORKER-POOL.md §2.2).

---

## 5. Cross-Subsystem Integration

### 5.1 Who Calls Task Scheduler

| Caller | Purpose | Contract |
|--------|---------|----------|
| Health Checker | Register health check task | `scheduler.register` API |
| AI Provider Manager | Register provider health probe | `scheduler.register` API |
| Wallet Manager | Register balance refresh task | `scheduler.register` API |
| Gas Optimiser | Register gas price update | `scheduler.register` API |
| Config Manager | Register config reload check | `scheduler.register` API |
| Risk Engine | Register strategy weight update | `scheduler.register` API |
| AI Pipeline | Register daily reflection | `scheduler.register` API |
| Database Layer | Register DB maintenance | `scheduler.register` API |
| Recovery Coordination | Schedule delayed recovery task | `scheduler.oneshot` API |

### 5.2 Who Task Scheduler Calls

| Target | Purpose | Contract |
|--------|---------|----------|
| Worker Pool | Execute scheduled task | `runtime.worker.submit` API |
| Event Bus | Emit scheduler events | `scheduler.*` events |
| Retry Handler | Re-queue failed tasks | `scheduler.retry` internal |

### 5.3 Events Task Scheduler Emits

| Event | Payload | Consumer |
|-------|---------|----------|
| `scheduler.task.triggered` | `{task_id, task_type, schedule_type, triggered_at}` | Dashboard (scheduled task view) |
| `scheduler.task.completed` | `{task_id, task_type, duration_ms, result}` | Task caller, Dashboard |
| `scheduler.task.failed` | `{task_id, task_type, error, retryable, attempt, next_retry_at}` | Task caller, Health |
| `scheduler.task.permanent_failure` | `{task_id, task_type, error, total_attempts}` | Health, Dashboard (Critical for P1) |
| `scheduler.task.skipped` | `{task_id, task_type, reason: "previous still running"}` | Dashboard |

### 5.4 Configuration Task Scheduler Owns

| Config Key | Default | Description |
|-----------|---------|-------------|
| `scheduler.timezone` | `UTC` | Cron timezone |
| `scheduler.misfire_grace_ms` | `5000` | Misfire tolerance window |
| `scheduler.interval_jitter_pct` | `0.05` | Interval randomization |
| `scheduler.retry.base_delay_ms` | `1000` | Retry base delay |
| `scheduler.retry.max_delay_ms` | `30000` | Retry maximum delay |
| `scheduler.retry.jitter_pct` | `0.10` | Retry randomization |
| `scheduler.max_concurrent_tasks` | `50` | Max concurrently scheduled tasks |
| `scheduler.overlap_policy` | `skip` | Policy for overlapping cron runs |

---

## Cross-References

- **WORKER-POOL.md** — Worker thread lifecycle, priority queues, task processing.
- **THREADING-MODEL.md** — Thread architecture, scheduling thread role.
- **HEALTHCHECKS.md** — Health check scheduling and results.
- **AI-PROVIDER-MANAGER.md** — Provider health probes.
- **WALLET-MANAGEMENT.md** — Wallet balance refresh.
- **GAS-OPTIMISATION.md** — Gas price update scheduling.
- **CONFIGURATION.md** — Config reload scheduling.
- **SECRET-LIFECYCLE.md** — Secret rotation scheduling.
- **DATABASE-SCHEMA.md** — Database maintenance scheduling.
- **CONFIGURATION-REFERENCE.md** — Scheduler config keys (`scheduler.*`).
- **END-TO-END-WIRING-CONTRACT.md** — Cross-subsystem wiring.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Runtime Team |
