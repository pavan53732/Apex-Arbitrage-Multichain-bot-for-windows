---
metadata_schema_version: 1.0
document_id: DOC-0051
title: Traceability Matrix Legacy
plane: Repository Operating Model
domain: Traceability
class: Historical
authority: Historical
status: Superseded
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-repository-docs/registries/TRACEABILITY-REGISTRY.md
related_concepts:
  - CONCEPT-0008
dependencies:
  - DOC-0008
consumers: []
validator_coverage: []
supersedes: []
superseded_by:
  - DOC-0008
last_updated: 2026-07-29
concept_role: Historical Reference
owned_domains: []
type: REFERENCE
purpose: Traceability Matrix documentation.
scope: Reference documentation.
---

# Traceability Matrix

**Owner:** Architecture Team  
**Last Updated:** 2026-07-27  
**Status:** Canonical Authority  
**Version:** 1.2.0

---

## Overview

The Traceability Matrix is the single source of truth linking every requirement, design decision, implementation module, test, and documentation artifact in the Apex platform. This document enables autonomous verification that every specification has been implemented, tested, and documented without gaps or orphans.

---

## Matrix Structure

### Requirement → Design → Implementation → Test → Documentation

Each row represents one complete traceability chain.

| **Req ID** | **Requirement** | **ADR / Design** | **Module** | **Config Key** | **Test Case** | **Doc** | **Owner** | **Status** | **Notes** |
|---|---|---|---|---|---|---|---|---|---|
| REQ-AI-001 | AI must support multi-provider failover | ADR-0001 | ai-orchestration | `ai.providers.fallback_chain` | test-ai-failover-001 | AI-PROVIDER-MANAGER.md | AI Team | ✓ | Provider routing with exponential backoff |
| REQ-AI-002 | AI context window must be deterministic | ADR-0005 | ai-context-builder | `ai.context.max_tokens` | test-context-determinism-001 | AI-CONTEXT-WINDOW-MANAGEMENT.md | AI Team | ✓ | Window pruning via priority matrix |
| REQ-AI-003 | AI tool invocation must have explicit priority and fallback | ADR-0001 | ai-tool-invocation | `ai.tools.priority_config` | test-tool-invocation-001 | AI-TOOL-INVOCATION-CONTRACT.md | AI Team | ✓ | Tool selection via learned ranking |
| REQ-AI-004 | Prompt lifecycle must be fully observable | ADR-0005 | ai-pipeline | `ai.prompts.lifecycle_logging` | test-prompt-lifecycle-001 | PROMPT-LIFECYCLE.md | AI Team | ✓ | Capture construction, execution, result |
| REQ-TRADE-001 | Trading engine must enforce slippage limits | ADR-0002 | trading-engine | `trade.slippage_max_bps` | test-slippage-001 | TRADING-ENGINE.md | Trading Team | ✓ | Checked at execution gateway |
| REQ-TRADE-002 | Trading must support rollback on failure | ADR-0002 | execution-engine | `trade.rollback_timeout_ms` | test-trade-rollback-001 | EXECUTION-ENGINE.md | Trading Team | ✓ | Wallet state restoration on revert |
| REQ-TRADE-003 | Risk engine must block trades exceeding limits | ADR-0002 | risk-engine | `risk.max_position_usd`, `risk.max_per_trade_usd` | test-risk-enforcement-001 | RISK-ENGINE.md | Risk Team | ✓ | Real-time position check before execution |
| REQ-EXEC-001 | Execution must be atomic or fully reverted | ADR-0002 | transaction-executor | `exec.atomic_timeout_ms` | test-atomicity-001 | EXECUTION-ENGINE.md | Execution Team | ✓ | Wrapped in transaction lifecycle |
| REQ-EXEC-002 | Execution must track and retry failed steps | ADR-0002 | retry-manager | `exec.retry_max_attempts`, `exec.retry_backoff_ms` | test-retry-001 | FAILURE-RECOVERY-MATRIX.md | Execution Team | ✓ | Exponential backoff with jitter |
| REQ-CONFIG-001 | Configuration must be hot-reloadable for non-critical keys | ADR-0006 | config-manager | See CONFIGURATION-REFERENCE.md | test-config-reload-001 | CONFIGURATION.md | Config Team | ✓ | Live merge without service restart |
| REQ-CONFIG-002 | Configuration must validate on load | ADR-0006 | config-validator | (via schema) | test-config-validation-001 | CONFIGURATION-REFERENCE.md | Config Team | ✓ | JSON schema enforcement |
| REQ-PLUGIN-001 | Plugins must run in isolation sandbox | ADR-0003 | plugin-executor | `plugin.sandbox_enabled` | test-plugin-sandbox-001 | PLUGIN-SANDBOX-CONTRACT.md | Plugin Team | ✓ | No direct memory/FS access |
| REQ-PLUGIN-002 | Plugins must declare capabilities and permissions | ADR-0003 | plugin-manifest-parser | (via manifest.json) | test-plugin-manifest-001 | APP-BUILDER-PLUGIN-SYSTEM.md | Plugin Team | ✓ | Manifest-driven capability grant |
| REQ-RUNTIME-001 | Runtime must support graceful startup/shutdown | ADR-0006 | runtime-orchestrator | `runtime.startup_timeout_ms`, `runtime.shutdown_timeout_ms` | test-startup-shutdown-001 | RUNTIME-OPERATIONS.md | Runtime Team | ✓ | Sequenced subsystem bringup/teardown |
| REQ-RUNTIME-002 | Runtime must detect and recover from subsystem failures | ADR-0006 | failure-detector | `runtime.health_check_interval_ms` | test-recovery-001 | RECOVERY-AND-FAILOVER.md | Runtime Team | ✓ | Health check → isolation → restart → recovery |
| REQ-DASHBOARD-001 | Dashboard must restore workspace state on reload | ADR-0007 | workspace-manager | `dashboard.workspace_persistence_path` | test-workspace-restore-001 | DASHBOARD-WORKSPACES.md | Dashboard Team | ✓ | Persisted layout, widgets, focus |
| REQ-EVENT-001 | Events must have explicit ownership and delivery guarantee | ADR-0002 | event-bus | `event.retention_days`, `event.delivery_policy` | test-event-delivery-001 | EVENT-OWNERSHIP-MATRIX.md | Event Team | ✓ | Producer/consumer mapping with SLA |
| REQ-SECURITY-001 | All secrets must follow lifecycle rules | ADR-0006 | secret-manager | `secret.rotation_interval_days` | test-secret-lifecycle-001 | SECRET-LIFECYCLE.md | Security Team | ✓ | Encrypted storage, rotation, audit log |
| REQ-SECURITY-002 | Trust boundaries must be enforced at subsystem edges | ADR-0006 | trust-enforcer | See TRUST-BOUNDARIES.md | test-trust-boundary-001 | TRUST-BOUNDARIES.md | Security Team | ✓ | Explicit permission checks at IPC, plugin, wallet |
|| REQ-RESOURCE-001 | Resource budgets must be enforced and observable | ADR-0006 | resource-manager | `resource.memory_limit_mb`, `resource.cpu_budget_percent` | test-resource-limit-001 | RESOURCE-BUDGET-SPECIFICATION.md | Ops Team | ✓ | Real-time enforcement with backpressure |
| REQ-AI-005 | Prompt lifecycle must have defined compression strategy | ADR-0005 | ai-pipeline | `ai.context.prune_strategy`, `ai.context.prune_threshold` | test-prompt-compression-001 | PROMPT-LIFECYCLE.md | AI Team | ✓ | Priority/LRU/FIFO with segment hierarchy |
| REQ-AI-006 | AI tool invocation must define explicit timeout/retry/circuit-breaker | ADR-0001 | ai-tool-executor | `ai.tools.timeout_ms`, `ai.providers.retry.*` | test-tool-circuit-breaker-001 | AI-TOOL-INVOCATION-CONTRACT.md | AI Team | ✓ | Per-tool timeout, exponential backoff, CB |
| REQ-AI-007 | Prompt memory injection must respect TTL and capacity limits | ADR-0005 | ai-context-builder | `ai.memory.ttl_days`, `ai.memory.max_entries` | test-memory-injection-001 | PROMPT-LIFECYCLE.md | AI Team | ✓ | Recency + relevance scoring |
| REQ-EVENT-002 | Events must have explicit ordering and priority routing | ADR-0002 | event-bus | `event.batch_size`, `event.max_queue_size` | test-event-priority-001 | EVENT-OWNERSHIP-MATRIX.md | Event Team | ✓ | Key-based ordering, 4 priority levels |
| REQ-EVENT-003 | Failed events must route to dead-letter queue | ADR-0002 | event-bus | `event.dead_letter_enabled`, `event.dead_letter_max_retries` | test-dlq-routing-001 | EVENT-OWNERSHIP-MATRIX.md | Event Team | ✓ | DLQ with replay support |
| REQ-CONFIG-003 | Configuration must define reload/restart semantics per key | ADR-0006 | config-manager | See CONFIGURATION-REFERENCE.md | test-config-reload-semantics-001 | CONFIGURATION-REFERENCE.md | Config Team | ✓ | Per-key reload column in reference |
| REQ-CONFIG-004 | Configuration must support profile inheritance and merge | ADR-0006 | config-manager | See CONFIGURATION-PROFILES.md | test-config-profile-merge-001 | CONFIGURATION-PROFILES.md | Config Team | ✓ | Deep merge with array replacement |
| REQ-PLUGIN-003 | Plugin sandbox must enforce memory and CPU limits | ADR-0003 | plugin-executor | `plugin.sandbox.memory_limit_mb`, `plugin.sandbox.cpu_quota_percent` | test-plugin-sandbox-limits-001 | PLUGIN-SANDBOX-CONTRACT.md | Plugin Team | ✓ | Per-plugin resource quotas |
| REQ-RUNTIME-003 | Runtime must support sequenced startup/shutdown with timeouts | ADR-0006 | runtime-orchestrator | `runtime.startup_timeout_ms`, `runtime.shutdown_timeout_ms` | test-startup-sequence-001 | BOOTSTRAP-SEQUENCE.md | Runtime Team | ✓ | Dependency-ordered subsystem bringup |
| REQ-RUNTIME-004 | Worker pool must support min/max/idle lifecycle | ADR-0006 | worker-pool | `runtime.worker.min_workers`, `runtime.worker.max_workers`, `runtime.worker.idle_timeout_ms` | test-worker-lifecycle-001 | WORKER-POOL.md | Runtime Team | ✓ | Dynamic pool scaling |
| REQ-DASHBOARD-002 | Dashboard must support workspace autosave and restore | ADR-0007 | workspace-manager | `dashboard.workspace_autosave_interval_ms` | test-workspace-autosave-001 | DASHBOARD-WORKSPACES.md | Dashboard Team | ✓ | Periodic persistence |
| REQ-SECURITY-003 | Audit logging must have configurable retention | ADR-0006 | audit-logger | `security.audit.enabled`, `security.audit.retention_days` | test-audit-retention-001 | SECURITY.md | Security Team | ✓ | Configurable retention with rotation |
| REQ-RESOURCE-002 | Resource manager must enforce per-plugin resource budgets | ADR-0006 | resource-manager | `plugin.sandbox.memory_limit_mb`, `plugin.sandbox.cpu_quota_percent` | test-resource-plugin-enforcement-001 | RESOURCE-BUDGET-SPECIFICATION.md | Ops Team | ✓ | Isolated per-plugin enforcement |
| REQ-RUNTIME-005 | Orchestrator must coordinate 5-phase startup with latch gates | ADR-0006 | runtime-orchestrator | `runtime.startup_timeout_ms`, `runtime.startup.*_timeout_ms` | test-orchestrator-startup-001 | ORCHESTRATOR.md | Runtime Team | ✓ | Phase-gated initialization with per-phase budgets |
| REQ-RUNTIME-006 | Platform mode must transition based on aggregate health score | ADR-0006 | runtime-orchestrator | `runtime.mode_transition_threshold` | test-mode-transition-001 | ORCHESTRATOR.md | Runtime Team | ✓ | 9-mode state machine with health score thresholds |
| REQ-RUNTIME-007 | Shutdown must follow reverse startup order with drain timing | ADR-0006 | runtime-orchestrator | `runtime.shutdown_timeout_ms` | test-shutdown-order-001 | ORCHESTRATOR.md | Runtime Team | ✓ | Reverse-order drain with per-subsystem budgets |
| REQ-RUNTIME-008 | Sleep/resume must coordinate checkpoint/reconnect/reconcile cycle | ADR-0006 | runtime-orchestrator | `runtime.sleep_checkpoint_timeout_ms` | test-sleep-resume-001 | ORCHESTRATOR.md | Runtime Team | ✓ | WM_POWERBROADCAST handling with checkpoint persistence |
| REQ-IPC-001 | IPC must use named pipes with message-based envelope protocol | ADR-0002 | ipc-bridge | `ipc.connection_timeout_ms` | test-ipc-envelope-001 | IPC-PROTOCOL.md | Runtime Team | ✓ | Named pipe with DACL security, envelope schema |
| REQ-IPC-002 | IPC must enforce delivery semantics per channel (at_most_once/at_least_once/exactly_once) | ADR-0002 | ipc-bridge | `ipc.dedup_window_ms` | test-ipc-delivery-001 | IPC-PROTOCOL.md | Runtime Team | ✓ | 3 delivery modes with ack protocol for exactly_once |
| REQ-IPC-003 | IPC messages crossing trust boundaries must be anonymized | ADR-0006 | ipc-bridge | See IPC-PROTOCOL.md §8.1 | test-ipc-anonymization-001 | IPC-PROTOCOL.md | Security Team | ✓ | No wallet addresses, private keys, or trade details to T3 |
| REQ-IPC-004 | IPC protocol must support backward-compatible version negotiation | ADR-0002 | ipc-bridge | See IPC-PROTOCOL.md §6 | test-ipc-version-001 | IPC-PROTOCOL.md | Runtime Team | ✓ | IPC-HELLO with version negotiation, additive-only changes |
| REQ-E2E-001 | End-to-end signal flow must be documented from market data to dashboard | ADR-0002 | trading-engine | `trading.timeout_ms` | test-e2e-signal-flow-001 | END-TO-END-WIRING-CONTRACT.md | Architecture Team | ✓ | Full opportunity-to-dashboard flow with failure branching |
| REQ-E2E-002 | Every runtime flow must have step-by-step sequencing with failure branches | ADR-0006 | runtime-orchestrator | See RUNTIME-FLOW-LIFECYCLE.md | test-runtime-flow-001 | RUNTIME-FLOW-LIFECYCLE.md | Runtime Team | ✓ | 10 documented flows with explicit step sequences |
| REQ-STATE-001 | All state machines must be indexed with inter-machine coupling documented | ADR-0006 | runtime-orchestrator | See STATE-MACHINE-INDEX.md | test-state-machine-coupling-001 | STATE-MACHINE-INDEX.md | Architecture Team | ✓ | 9 state machines with coupling, startup/shutdown sequencing |
| REQ-RECOVERY-001 | Recovery must follow phased ordering (foundation → infrastructure → application → extensions) | ADR-0006 | recovery-coordinator | See RECOVERY-COORDINATION.md | test-recovery-phasing-001 | RECOVERY-COORDINATION.md | Runtime Team | ✓ | 4-phase recovery with dependency ordering |
| REQ-FF-001 | Feature flags must define rollout stages with canary/beta/production gates | ADR-0006 | feature-flag-manager | See FEATURE-FLAG-GOVERNANCE-AND-ROLLOUT-MATRIX.md | test-feature-flag-001 | FEATURE-FLAG-GOVERNANCE-AND-ROLLOUT-MATRIX.md | Architecture Team | ✓ | 3 rollout stages with percentage-based gates |
| REQ-WIN-001 | Windows platform must support 4-process model with tray lifecycle | ADR-0006 | windows-app | `windows.tray_behavior` | test-windows-process-001 | WINDOWS-APP-ARCHITECTURE.md | Windows Team | ✓ | 4-process model, 7 tray states, sleep/resume handling |
| REQ-WIN-002 | Windows service must have lifecycle state machine with recovery actions | ADR-0006 | windows-service | `windows.service.*` | test-windows-service-001 | WINDOWS-SERVICE-INTEGRATION.md | Windows Team | ✓ | 11 service states with SCM integration |
| REQ-WIN-003 | Windows network must detect and recover from 8 network disruption types | ADR-0006 | windows-network | `windows.network.*` | test-windows-network-001 | WINDOWS-NETWORK-RESILIENCE.md | Windows Team | ✓ | 8 detections with reconnect backoff |
| REQ-PLUGIN-004 | Plugin lifecycle must define discovery, dependency resolution, and capability negotiation | ADR-0003 | plugin-manager | `plugin.scan_interval`, `plugin.load_timeout_ms` | test-plugin-lifecycle-001 | PLUGIN-LIFECYCLE.md | Plugin Team | ✓ | 13 states from DISCOVERED to UNLOADED |
| REQ-EVENT-004 | Event bus must support exactly_once delivery with ordering key dedup | ADR-0002 | event-bus | `event.dedup_window_ms` | test-event-exactly-once-001 | EVENT-BUS.md | Event Team | ✓ | SPSC per key, dedup window, ack protocol |
| REQ-EVENT-005 | Event bus must route failed events to dead-letter queue with replay | ADR-0002 | event-bus | `event.dead_letter_enabled` | test-dlq-replay-001 | EVENT-BUS.md | Event Team | ✓ | DLQ with structured replay and max retries |
| REQ-TEST-001 | Testing must cover 10 layers from unit to chaos to security testing | ADR-0006 | testing-framework | See TESTING.md | test-testing-layers-001 | TESTING.md | QA Team | ✓ | 10-layer pyramid with per-layer contracts |
| REQ-DB-001 | Database must define query patterns and partitioning strategy | ADR-0006 | database | See DATABASE-SCHEMA.md §4 | test-db-query-pattern-001 | DATABASE-SCHEMA.md | Data Team | ✓ | Per-table query patterns, backup/restore, partitioning |

---

## Requirement Categories

### AI (REQ-AI-*)
- Multi-provider failover and fallback chains
- Context window determinism and pruning
- Tool invocation priority and fallback
- Prompt lifecycle observability
- Memory and reflection governance
- Safety boundaries and guardrails

### Trading (REQ-TRADE-*)
- Slippage enforcement
- Rollback and atomicity
- Risk limit enforcement
- Order routing and optimization
- Fee calculation
- Settlement and reconciliation

### Execution (REQ-EXEC-*)
- Atomic execution or full revert
- Retry and recovery
- Timeout handling
- State machine compliance
- Transaction lifecycle

### Configuration (REQ-CONFIG-*)
- Hot reload for live keys
- Schema validation on load
- Profile merging and override
- Secret integration
- Conflict resolution

### Plugin System (REQ-PLUGIN-*)
- Sandbox isolation
- Capability declaration
- Manifest governance
- API stability
- Plugin lifecycle

### Runtime (REQ-RUNTIME-*)
- Graceful startup/shutdown
- Subsystem failure detection and recovery
- Health checking
- Failover orchestration
- Hot reload

### Dashboard (REQ-DASHBOARD-*)
- Workspace state persistence
- Component lifecycle
- Layout composition
- Data binding
- Permission enforcement

### Events (REQ-EVENT-*)
- Explicit ownership
- Delivery guarantees
- Retention and replay
- Ordering and deduplication
- Dead-letter handling

### Security (REQ-SECURITY-*)
- Secret lifecycle and rotation
- Trust boundary enforcement
- Permission model
- Audit logging
- Encryption standards

### Resources (REQ-RESOURCE-*)
- Memory limits and enforcement
- CPU budgeting
- Observable metrics
- Backpressure handling
- Capacity planning

---

## Ownership and Governance

Each requirement is owned by one team. That team is responsible for:
1. Ensuring the requirement is implemented correctly.
2. Writing and maintaining the test case.
3. Keeping the design doc (ADR) and implementation doc in sync.
4. Responding to traceability audits.

**Audit Frequency:** Monthly. Run `scripts/validate_traceability.sh` to check for orphans.

---

## Implementation Roadmap

| Phase | Target | Status | Owner |
|---|---|---|---|
| Phase 1: Critical Contracts | Q1 2025 | ✓ Complete | Architecture |
| Phase 2: Threading & Concurrency | Q1 2025 | ✓ Complete | Runtime |
| Phase 3: Engine Deepening | Q2 2025 | ✓ Complete | Domain Teams |
| Phase 4: Full Audit & Validation | Q2 2025 | ✓ Complete | QA |
| Phase 5: Cross-System Integration + Windows | Q3 2026 | ✓ Complete | Architecture + Windows |
| Phase 6: Final Readiness Audit | Q3 2026 | ✓ Complete | Architecture |

---

## Audit and Validation

### Automated Checks
- Run `validate_traceability.sh` to detect orphaned requirements, missing implementations, or untested features.
- Local Governance Platform workflow `.local governance/validate-traceability.yml` runs on every PR.

### Manual Review
- Monthly traceability review in Architecture sync.
- Quarterly executive summary for stakeholders.

---

## How to Add a New Requirement

1. Assign a new ID: `REQ-<DOMAIN>-<NN>` (e.g., `REQ-AI-005`).
2. Add one row to the matrix above with: requirement, ADR, module, config key, test case, doc, owner, status.
3. Create or link the design doc (ADR).
4. Implement the feature in the named module.
5. Write the test case.
6. Document in the named doc file.
7. Run traceability validation to confirm.
8. Open a PR and get sign-off from the requirement owner and architecture review.

---

## Cross-References

- **DOCUMENTATION-MAP.md** — Authoritative doc hierarchy and canonical sources.
- **MODULE-OWNERSHIP-MATRIX.md** — Which team owns each code module.
- **FAILURE-RECOVERY-MATRIX.md** — Failure modes and recovery paths.
- **AI-TOOL-INVOCATION-CONTRACT.md** — Detailed AI tool invocation specification.
- **PROMPT-LIFECYCLE.md** — Detailed prompt construction and execution lifecycle.
- **CONFIGURATION-REFERENCE.md** — All configuration keys and reload semantics.
- **EVENT-OWNERSHIP-MATRIX.md** — Event producer/consumer and delivery guarantees.
- **TRUST-BOUNDARIES.md** — Security and trust domain enforcement.
- **RESOURCE-BUDGET-SPECIFICATION.md** — Resource limits and enforcement.

---

## Version History

| Version | Date | Changes | Author |
|---|---|---|---|
| 1.0.0 | 2025-01-15 | Initial canonical traceability matrix | Architecture |
| 1.1.0 | 2026-07-27 | Add requirements for cross-system integration, state machine index, recovery coordination, feature flags | Architecture |
| 1.2.0 | 2026-07-27 | Add requirements for orchestrator, IPC protocol, Windows platform, plugin lifecycle, event bus, testing, database | Architecture |
