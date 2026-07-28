---
type: REFERENCE
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Defines recovery procedures by failure class — detection, classification, halt, retry, reconciliation, notification — with explicit playbooks for every subsystem.
scope: None
last_updated: 2026-07-29
canonical_source: docs/RECOVERY-PLAYBOOK.md
---

# Recovery Playbook

## Document type
Document type: [REFERENCE]

## Version
**Version:** 0.2.0 | **Status:** Draft | **Last Updated:** 2026-07-27 | **Owner:** Runtime Team

## Purpose
Defines recovery procedures by failure class — detection, classification, halt, retry, reconciliation, notification — with explicit playbooks for every subsystem.

---

## 1. Recovery Framework

All recoveries follow this sequence:

```
1. DETECT   → Identify failure via health check, event, or metric threshold
2. CLASSIFY → Determine severity (Critical / High / Medium / Low)
3. HALT     → Stop affected subsystem (if critical); isolate boundary
4. RETRY    → Attempt automated recovery (if applicable)
5. RECONCILE → Verify side effects, read external state, restore consistency
6. NOTIFY   → Emit recovery event; alert operator if operator intervention needed
```

---

## 2. Recovery Playbooks

### 2.1 RPC Connection Failure

| Attribute | Value |
|-----------|-------|
| **Severity** | High |
| **Detection** | Health check: ping RPC endpoint; 3 consecutive failures |
| **Halt scope** | Trading on affected chain only |
| **Retry** | Switch to fallback RPC endpoint. Retry primary every `runtime.rpc.reconnect_interval_ms` (30s). |
| **Reconcile** | On reconnect, sync block height and replay missed events. |
| **Escalation** | If both primary and fallback fail for 5 min → emit `network.rpc.disconnected` (Critical). |
| **Recovery** | Auto-resume trading on chain when RPC responds. |

### 2.2 AI Provider Failure

| Attribute | Value |
|-----------|-------|
| **Severity** | High |
| **Detection** | Provider returns 5xx / timeout / quota exceeded |
| **Halt scope** | AI-dependent operations (opportunity scoring may degrade) |
| **Retry** | Follow fallback chain: Primary → Secondary → Tertiary (see `AI-PIPELINE.md` §5.3). |
| **Reconcile** | No state reconciliation (AI is stateless per request). |
| **Escalation** | All providers fail → emit `ai.critical.all_providers_failed`. |
| **Recovery** | Auto-resume on primary when retry interval elapses. |

### 2.3 Trade Leg Failure

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical (if money at risk) |
| **Detection** | Execution Engine reports `execution.reverted` or `execution.stuck` |
| **Halt scope** | This trade only. Chain circuit breaker may trip. |
| **Retry** | Follow retry strategy in `EXECUTION-ENGINE.md` §4. |
| **Reconcile** | Query on-chain state to determine actual outcome. |
| **Escalation** | If uncleared after 5 min → operator notification (`system.warning`). |
| **Recovery** | Partial recovery or full unwind per `TRADING-ENGINE.md` §4. |

### 2.4 Plugin Crash

| Attribute | Value |
|-----------|-------|
| **Severity** | Medium |
| **Detection** | Plugin process exits with non-zero code |
| **Halt scope** | This plugin only |
| **Retry** | Auto-restart plugin once |
| **Reconcile** | Plugin state is ephemeral; no reconciliation needed |
| **Escalation** | Second crash → plugin disabled, operator notified |
| **Recovery** | Operator must re-enable plugin manually |

### 2.5 Configuration Load Failure

| Attribute | Value |
|-----------|-------|
| **Severity** | Medium |
| **Detection** | Config schema validation fails on startup or reload |
| **Halt scope** | None (previous config kept active) |
| **Retry** | N/A |
| **Reconcile** | Log error, continue with previous config |
| **Escalation** | If startup config is invalid → Safe mode |
| **Recovery** | Operator edits config and triggers reload |

### 2.6 Database Connection Loss

| Attribute | Value |
|-----------|-------|
| **Severity** | High |
| **Detection** | DB pool connection fails |
| **Halt scope** | All persistence-dependent operations (trades still execute, but not persisted) |
| **Retry** | Reconnect every 5s, up to 60s |
| **Reconcile** | On reconnect, replay missed writes from in-memory buffer |
| **Escalation** | If buffer exceeds 1000 entries → pause new trades |
| **Recovery** | Auto-resume when DB connection restored |

### 2.7 Secret Rotation Failure

| Attribute | Value |
|-----------|-------|
| **Severity** | High |
| **Detection** | New secret fails verification (e.g., API call with new key returns 401) |
| **Halt scope** | Calls using that secret |
| **Retry** | Rotate again with a new secret |
| **Reconcile** | Verify old secret still works; if not, halt all operations using it |
| **Escalation** | After 3 failed rotations → security team paged |
| **Recovery** | Manual secret reset by operator |

### 2.8 Memory Exhaustion

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Detection** | `process.rss_bytes` exceeds Warning threshold (80% of limit) |
| **Halt scope** | Gradual: Warning → Throttle → Hard limit |
| **Retry** | Force GC, evict caches, pause non-critical subsystems |
| **Reconcile** | N/A |
| **Escalation** | Hard limit hit → Safe mode, operator paged |
| **Recovery** | Operator investigates and resolves (increase limit, reduce load, restart) |

---

## 3. Recovery Coordination

When multiple subsystems fail simultaneously, the Recovery Coordinator orchestrates:

1. **Priority**: Critical trades first, then AI, then plugins, then dashboard.
2. **Dependency**: If a subsystem depends on another (e.g., trading depends on RPC), recover the dependency first.
3. **Order**: Recover in reverse startup order (UI → Application → Infrastructure → Kernel).
4. **Fallback**: If coordinated recovery fails → Safe mode with operator intervention.

---

## Cross-References

- **RUNTIME-OPERATIONS.md** — Startup/shutdown/recovery sequencing.
- **TRADING-ENGINE.md** — Trade recovery paths.
- **EXECUTION-ENGINE.md** — Execution retry and resume.
- **AI-PIPELINE.md** — AI provider fallback.
- **PLUGIN-LIFECYCLE.md** — Plugin crash recovery.
- **HEALTHCHECKS.md** — Health probe definitions.
- **CONFIGURATION-REFERENCE.md** — Recovery config keys (`runtime.*`, `execution.*`).

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 0.2.0 | 2026-07-27 | Complete recovery playbook with 8 failure scenarios, coordination framework, escalation paths | Runtime Team |
| 0.1.0 | 2026-07-27 | Initial stub | Runtime Team |