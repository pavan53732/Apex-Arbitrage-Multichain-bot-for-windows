---
type: REFERENCE
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Defines memory allocation, ownership, cleanup, and eviction policies for all subsystems — process memory, caches, AI memory stores, and workspace state.
scope: None
last_updated: 2026-07-29
canonical_source: docs/ai/memory/MEMORY-LIFECYCLE.md
---

# Memory Lifecycle

## Document type
Document type: [REFERENCE]

## Version
**Version:** 0.2.0 | **Status:** Draft | **Last Updated:** 2026-07-27 | **Owner:** Runtime Team

## Purpose
Defines memory allocation, ownership, cleanup, and eviction policies for all subsystems — process memory, caches, AI memory stores, and workspace state.

---

## 1. Memory Categories

| Category | Owner | Allocation | Persistence | Cleanup Trigger |
|----------|-------|------------|-------------|-----------------|
| **Process heap** | All subsystems | `malloc`/`new` | None | Scope exit / `delete` |
| **Working state** | Trading, AI, Runtime | Stack + heap | Session | Session end |
| **AI memory store** | AI Memory | Persistent store (SQLite) | Cross-session | TTL expiry, capacity eviction |
| **Config cache** | Config Manager | Heap | Process lifetime | Config reload |
| **Registry cache** | Registry System | Heap | Process lifetime | Registry update event |
| **Workspace state** | Dashboard | Persistent file | Cross-session | Workspace close, explicit save |
| **Event bus buffer** | Event Bus | Ring buffer (pre-allocated) | Session | Event consumption + retention expiry |
| **Log buffer** | Logging | Ring buffer | Session | Log flush interval |
| **Plugin sandbox** | Plugin Executor | Process-isolated heap | Plugin session | Plugin unload |

---

## 2. Allocation Rules

| Rule | Enforcement |
|------|-------------|
| All allocations must have a defined owner | Owner field in allocation tracking |
| Long-lived allocations must be bounded | Budget cap per subsystem (see `RESOURCE-BUDGET-SPECIFICATION.md`) |
| Ephemeral allocations (request-scoped) must use RAII | C++ `std::unique_ptr`, `std::vector` on stack |
| Large allocations (>1 MB) must be logged | Log at `debug` level with caller stack trace |
| Plugins must not allocate memory outside their sandbox | Enforced by sandbox process boundary |

---

## 3. Ownership Model

```
Owner (subsystem) → Memory Region → References
```

- Each memory region has exactly one owner.
- Other subsystems may reference the region via shared pointer (`std::shared_ptr`) or handle (index/lookup key).
- References must not outlive the owner's lifecycle. Use `std::weak_ptr` for observers.
- Cross-subsystem memory transfer must be explicit (serialize → message → deserialize).

---

## 4. Eviction Policies

| Cache / Store | Eviction Policy | Threshold | Action |
|---------------|-----------------|-----------|--------|
| AI memory store | LRU + score-based | `ai.memory.max_entries`: 1000 | Evict lowest-scored entries |
| AI context window | Priority-based pruning | `ai.context.prune_threshold`: 7000 tokens | Drop lowest-priority segments |
| Registry cache | TTL-based | 300 seconds | Invalidate on TTL expiry |
| Event bus buffer | FIFO + retention | `event.retention_days`: 7, `event.max_queue_size`: 10000 | Drop oldest events |
| Log buffer | FIFO | 10 MB | Rotate to disk |
| Process heap | OS paging | 90% of `resource.memory_limit_mb` | Trigger GC / log warning |

### Eviction Algorithm (for scored stores)

```
Score = recency_weight × recency_normalized + relevance_weight × relevance_score
```

| Parameter | Default | Range |
|-----------|---------|-------|
| `recency_weight` | 0.4 | 0.0–1.0 |
| `relevance_weight` | 0.6 | 0.0–1.0 |

---

## 5. Cleanup Lifecycle

### Session Memory Cleanup

On session end (user logout, timeout, explicit close):
1. Working state freed (scope exit).
2. AI context window flushed to archive (see `PROMPT-LIFECYCLE.md`).
3. Event bus buffers drained.
4. Plugin sandbox state cleaned.
5. Workspace state saved to persistent store (if autosave enabled).
6. Log buffer flushed to disk.

### Process Memory Cleanup

On process shutdown:
1. All subsystems receive shutdown signal.
2. Each subsystem frees its owned memory regions.
3. Plugin sandboxes are terminated.
4. Database connections closed.
5. Persistent stores synced to disk.

---

## 6. Memory Monitoring

| Metric | Source | Threshold | Action |
|--------|--------|-----------|--------|
| Process RSS | OS | `resource.memory_limit_mb`: 1024 MB | Log warning at 80%, force GC at 95%, abort at 100% |
| Per-subsystem allocation | Built-in tracker | Budget per subsystem | Log allocation leak warnings |
| AI memory store size | AI Memory | `ai.memory.max_entries` | Evict on insert |
| Cache hit ratio | Registry / Config | < 80% | Flag for cache tuning review |
| Fragmentation | `malloc` stats | > 30% fragmentation | Trigger defragmentation / notify Ops |

---

## 7. Leak Detection

- A memory tracker records all allocations per subsystem.
- On subsystem shutdown, all un-freed allocations are reported as potential leaks.
- Leaks exceeding 1 MB total trigger `system.warning` event.
- Leaks exceeding 10 MB total trigger `system.error` event with subsystem name and allocation backtrace.

---

## Cross-References

- **RESOURCE-BUDGET-SPECIFICATION.md** — Memory budgets per subsystem.
- **AI-MEMORY.md** — AI-specific memory store governance.
- **PROMPT-LIFECYCLE.md** — Context window memory lifecycle.
- **CACHE-MANAGER.md** — Cache-specific eviction policies.
- **EVENT-BUS.md** — Event bus ring buffer management.
- **DIAGNOSTICS.md** — Memory diagnostics and profiling.
- **CONFIGURATION-REFERENCE.md** — Memory config keys (`resource.memory_limit_mb`, `ai.memory.*`).

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 0.2.0 | 2026-07-27 | Complete memory lifecycle with categories, ownership, eviction, cleanup, monitoring | Runtime Team |
| 0.1.0 | 2026-07-27 | Initial stub | Runtime Team |