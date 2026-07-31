---
metadata_schema_version: 1.0
document_id: DOC-0337
title: Recovery Coordination
plane: Product Specification
domain: Operations
class: Specification
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/operations/recovery/recovery-coordination.md
related_concepts:
  - CONCEPT-0337
dependencies: []
consumers:
  - DOC-0423
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Operations
type: CONTRACT
purpose: "Defines the unified repository-wide recovery coordination contract — how subsystems coordinate during multi-failure scenarios, recovery ordering, escalation thresholds, reconciliation tasks, operator intervention rules, and failover orchestration across the entire platform."
scope: None
---

# Recovery Coordination

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-27 | **Owner:** Runtime Team

## Purpose
Defines the unified repository-wide recovery coordination contract — how subsystems coordinate during multi-failure scenarios, recovery ordering, escalation thresholds, reconciliation tasks, operator intervention rules, and failover orchestration across the entire platform.

---

## 1. Recovery Lifecycle

All recoveries follow a standard lifecycle (from `./recovery-and-failover.md`):

```
DETECTED → CLASSIFIED → CONTAINED → RESTORED → RECONCILED → RELEASED
```

### Lifecycle Phase Definitions

| Phase | Description | Entry Condition | Exit Condition | Timeout | Owner |
|-------|-------------|-----------------|----------------|---------|-------|
| **DETECTED** | Failure identified | Health check, metric threshold, or event triggers detection | Failure scope confirmed | Detection latency ≤ 5s | Health Checker |
| **CLASSIFIED** | Failure categorized by severity and scope | Detection confirmed | Severity assigned; affected subsystems listed | Classification time ≤ 10s | Recovery Coordinator |
| **CONTAINED** | Affected subsystem isolated; unsafe work paused | Classification complete | All affected subsystems paused or isolated; boundaries secured | Containment time ≤ 30s | Recovery Coordinator |
| **RESTORED** | Affected subsystem restarted or fallback activated | Containment complete | Subsystem operational (may be degraded) | Restoration time varies per subsystem (see §4) | Per-subsystem owner |
| **RECONCILED** | State verified against external truth sources | Restoration complete | All in-flight state reconciled; no orphaned transactions | Reconciliation time varies per subsystem (see §4) | Per-subsystem owner |
| **RELEASED** | Subsystem fully operational; recovery complete | Reconciliation verified | Normal operation resumes; all limits cleared | Release time ≤ 5s | Recovery Coordinator |

---

## 2. Recovery Coordinator Responsibilities

The Recovery Coordinator is a dedicated subsystem that orchestrates multi-failure recovery:

| Responsibility | Description |
|---------------|-------------|
| **Detection aggregation** | Collects health check failures, metric threshold breaches, and error events from all subsystems |
| **Classification** | Assigns severity (Critical/High/Medium/Low) and determines affected subsystem scope |
| **Containment coordination** | Orchestrates subsystem isolation in correct order; prevents cascade failures |
| **Recovery ordering** | Schedules subsystem recovery in dependency-first order (see §5) |
| **Reconciliation oversight** | Verifies that each subsystem's reconciliation is complete before releasing |
| **Escalation management** | Escalates to operator when automated recovery fails or is not possible |
| **State persistence** | Persists recovery phase, affected subsystems, and reconciliation status |
| **Event emission** | Emits recovery lifecycle events at each phase transition |

---

## 3. Failure Classification

### Severity Classification Matrix

| Severity | Examples | Containment Scope | Recovery Strategy | Operator Notification | SLA |
|----------|---------|-------------------|-------------------|----------------------|-----|
| **Critical** | Private key leak, wallet drain, core service crash, memory exhaustion at hard limit | Entire subsystem or platform | Immediate halt + automated recovery attempt + operator intervention | Immediate (all channels) | Acknowledge: 15 min; Contain: 1 hr |
| **High** | RPC connection loss, AI provider failure, trade leg failure, database connection loss | Affected subsystem + dependent subsystems | Automated recovery (fallback, restart) | Dashboard + event log | Acknowledge: 1 hr; Contain: 4 hr |
| **Medium** | Plugin crash, config validation failure, stale price feed | Single subsystem only | Automated retry or restart | Dashboard notification | Acknowledge: 4 hr; Contain: 24 hr |
| **Low** | Schema validation warning, cache miss, rate limit bump | None (local handling) | Log and continue | Event log only | Next business day |

### Failure Domain Classification

| Domain | Example Failures | Recovery Priority | Dependency |
|--------|-----------------|-------------------|------------|
| **Trading** | Leg failure, risk rejection, opportunity timeout | 5 (high) | Depends on RPC, Wallet |
| **Execution** | TX revert, stuck TX, nonce conflict | 5 (high) | Depends on RPC, Wallet |
| **RPC/Network** | Connection loss, endpoint failure | 2 (very high) | Required by Trading, Execution, Market Data |
| **Wallet** | Key unavailable, balance error | 3 (very high) | Required by Trading, Execution |
| **AI** | Provider failure, tool invocation error | 4 (high) | Advisory; not blocking |
| **Database** | Connection loss, query timeout | 2 (very high) | Required by all persistence-dependent subsystems |
| **Event Bus** | Buffer overflow, delivery failure | 1 (highest) | Required by all event-driven subsystems |
| **Plugin** | Crash, sandbox violation | 6 (medium) | Isolated; not blocking core |
| **Dashboard** | UI crash, IPC disconnection | 7 (low) | Not blocking core operations |

---

## 4. Per-Subsystem Recovery Timelines

| Subsystem | Detection | Containment | Restoration | Reconciliation | Total |
|-----------|-----------|-------------|-------------|----------------|-------|
| **Event Bus** | 2s | 5s | 10s (restart) | 5s (replay buffer) | 22s |
| **Database** | 3s | 5s | 15s (reconnect) | 10s (replay missed writes) | 33s |
| **RPC/Network** | 5s | 10s (isolate chain) | 15s (fallback endpoint) | 10s (sync block height) | 40s |
| **Wallet** | 3s | 5s | 10s (re-init) | 5s (verify balances) | 23s |
| **Trading** | 5s | 10s (halt new trades) | 20s (resume after deps) | 30s (reconcile in-flight) | 65s |
| **Execution** | 3s | 5s | 15s (resume after deps) | 20s (query chain state) | 43s |
| **AI Pipeline** | 5s | 5s | 10s (fallback provider) | 5s (stateless, no recon) | 25s |
| **Plugin** | 3s | 5s | 15s (restart once) | 5s (ephemeral state) | 28s |
| **Dashboard** | 5s | 5s | 10s (restart UI) | 5s (restore workspace) | 25s |

**Total worst-case multi-failure recovery**: 65s (trading subsystem, after all dependencies restored).

---

## 5. Recovery Ordering (Dependency-First)

When multiple subsystems fail simultaneously, recovery follows dependency order:

```
Phase 1 (Foundation):
  1. Event Bus → RESTORED (all events flow through this)
  2. Database → RESTORED (all persistence depends on this)
  3. Config Manager → RESTORED (all config queries depend on this)

Phase 2 (Infrastructure):
  4. RPC/Network → RESTORED (all chain operations depend on this)
  5. Wallet → RESTORED (all trading depends on this)
  6. Market Data → RESTORED (all pricing depends on this)

Phase 3 (Application):
  7. Trading Engine → RESTORED (after RPC + Wallet + Market Data)
  8. Execution Engine → RESTORED (after RPC + Wallet)
  9. Risk Engine → RESTORED (after Trading)
  10. AI Pipeline → RESTORED (after Config + Network)

Phase 4 (Extensions):
  11. Plugin Manager → RESTORED (after core subsystems)
  12. Dashboard → RESTORED (after all subsystems healthy)
```

**Rule**: A subsystem must not be RESTORED until all its dependencies are RESTORED.

---

## 6. Escalation Thresholds

| Condition | Action | Operator Notification |
|-----------|--------|----------------------|
| Single subsystem failure | Auto-recovery per playbook | Dashboard notification |
| 2 subsystems fail simultaneously | Coordinated recovery per §5 | Dashboard + event log |
| 3+ subsystems fail simultaneously | Platform-wide recovery; Safe mode if > 3 critical | All channels; operator intervention likely required |
| Recovery attempt fails (1st) | Second attempt with escalated strategy | Dashboard warning |
| Recovery attempt fails (2nd) | Third attempt + operator paged | All channels |
| Recovery attempt fails (3rd) | Halt automated recovery; operator must intervene | All channels; Critical severity |
| Total recovery time exceeds 5 min | Escalate to Safe mode | Critical alert |
| Critical subsystem (Event Bus, DB, Wallet) fails | Immediate containment + operator page | Immediate all channels |
| Memory or CPU hard limit hit | Force Safe mode | Critical alert |

---

## 7. Reconciliation Tasks

After restoration, each subsystem must reconcile its state:

| Subsystem | Reconciliation Task | Source of Truth | Method |
|-----------|-------------------|-----------------|--------|
| **Trading** | Verify in-flight trades against on-chain state | Chain RPC | Query TX receipts for each in-flight trade; advance or abort based on on-chain result |
| **Execution** | Verify pending/stuck TXs against mempool and chain | Chain RPC | `eth_getTransactionByHash` + `eth_getTransactionReceipt` |
| **Wallet** | Verify balances and nonce sequences | Chain RPC | `eth_getBalance` + `eth_getTransactionCount` |
| **Market Data** | Verify price feeds are current | Chain RPC + DEX contracts | Re-subscribe to price feeds; verify last update timestamp |
| **Database** | Verify persistence completeness | Event store + on-chain state | Compare last persisted event ID vs actual event bus sequence |
| **Event Bus** | Verify no lost events | DLQ + consumer ack log | Replay DLQ entries; verify all critical events were consumed |
| **AI Pipeline** | No reconciliation needed | Stateless per request | Verify provider connections; resume from IDLE |
| **Plugin** | No reconciliation needed | Ephemeral state | Re-initialize sandbox; verify capabilities |
| **Dashboard** | Verify workspace persistence | Workspace files | Load workspace JSON; fall back to default if corrupt |

---

## 8. Operator Intervention Rules

| Scenario | Operator Action Required | Automated Actions |
|----------|--------------------------|-------------------|
| **Critical secret compromise** | Rotate secrets, verify wallet integrity, restart service | Isolate affected domain; emit security.violation |
| **Trading engine unrecoverable** | Manual state review, decide to restart or halt | Mark in-flight trades for manual review |
| **Database corruption** | Restore from backup or rebuild | Pause persistence-dependent operations |
| **All AI providers down** | Choose: manual operation, single provider config, or halt AI | Return cached responses if available |
| **Plugin sandbox escape** | Remove offending plugin, audit plugin ecosystem | Block all plugins; security scan |
| **Hardware resource exhaustion** | Increase limits, reduce load, or restart with adjusted config | Force GC, throttle, Safe mode |

### Operator Intervention Workflow

```
1. Recovery Coordinator detects automated recovery exhausted.
2. Emit `runtime.operator.intervention` event with:
   - subsystem name
   - issue description
   - severity
   - recommended action
   - current state snapshot
3. Dashboard shows intervention modal (blocking).
4. Operator reviews and takes action.
5. Operator action is recorded in audit trail.
6. Recovery Coordinator resumes from operator's decision point.
```

---

## 9. Recovery Events

| Event | Phase | Payload | Delivery |
|-------|-------|---------|----------|
| `runtime.recovery.detected` | DETECTED | `{subsystem, failure_type, severity}` | At-least-once, High priority |
| `runtime.recovery.classified` | CLASSIFIED | `{subsystem, severity, affected_scope, dependencies}` | At-least-once, High priority |
| `runtime.recovery.contained` | CONTAINED | `{subsystem, paused_subsystems, boundary_state}` | At-least-once, High priority |
| `runtime.recovery.restored` | RESTORED | `{subsystem, restoration_method, duration_ms}` | At-least-once, Medium priority |
| `runtime.recovery.reconciled` | RECONCILED | `{subsystem, reconciled_items, unreconciled_items}` | At-least-once, Medium priority |
| `runtime.recovery.released` | RELEASED | `{subsystem, total_recovery_ms, health_status}` | At-least-once, Medium priority |
| `runtime.operator.intervention` | Operator needed | `{subsystem, issue, severity, recommended_action, state_snapshot}` | Exactly-once, Critical priority |
| `runtime.recovery.failed` | Recovery exhausted | `{subsystem, attempts, last_error, operator_required}` | Exactly-once, Critical priority |

---

## Cross-References

- **RECOVERY-AND-FAILOVER.md** — Recovery lifecycle definitions (authoritative for lifecycle phases).
- **RECOVERY-PLAYBOOK.md** — Per-failure-class playbooks (authoritative for individual recovery procedures).
- **FAILURE-MATRIX.md** — Failure mode definitions (authoritative for failure catalog).
- **FAILURE-RECOVERY-MATRIX.md** — Failure-to-recovery mapping (authoritative for recovery actions).
- **ENGINE-STATE-MACHINE.md** — Engine lifecycle states (authoritative for engine recovery transitions).
- **STATE-MACHINE-INDEX.md** — Inter-state-machine coupling and recovery ordering.
- **HEALTHCHECKS.md** — Health probe definitions (authoritative for failure detection).
- **RUNTIME-OPERATIONS.md** — Startup/shutdown/recovery sequencing.
- **TRACEABILITY-MATRIX.md** — REQ-RUNTIME-002.
- **CONFIGURATION-REFERENCE.md** — `runtime.*` config keys.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-27 | New: unified recovery coordination contract with lifecycle phases, ordering, escalation, reconciliation, operator intervention | Runtime Team |
