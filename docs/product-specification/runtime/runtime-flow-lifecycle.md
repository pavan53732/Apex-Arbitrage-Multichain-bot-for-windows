---
metadata_schema_version: 1.0
document_id: DOC-0089
title: Runtime Flow Lifecycle
plane: Product Specification
domain: Runtime
class: Specification
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/runtime/runtime-flow-lifecycle.md
related_concepts:
  - CONCEPT-0089
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
purpose: "Defines the complete set of runtime flows — worker creation/shutdown, plugin discovery/load/unload/update, provider initialization/failure, configuration reload, dashboard initialization/workspace restore, AI initialization/fallback, recovery/failover, hot-reload/restart boundary, Windows sleep/resume/power events, and update installation/rollback."
scope: None
---

# Runtime Flow Lifecycle

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-27 | **Owner:** Runtime Team

## Purpose
Defines the complete set of runtime flows — worker creation/shutdown, plugin discovery/load/unload/update, provider initialization/failure, configuration reload, dashboard initialization/workspace restore, AI initialization/fallback, recovery/failover, hot-reload/restart boundary, Windows sleep/resume/power events, and update installation/rollback.

---

## 1. Worker Creation and Shutdown Flow

### Creation
```
1. Pool detects queue depth > threshold OR scaling policy triggers growth.
2. Allocate thread resources (stack: 2 MB, config context).
3. Spawn thread → SPAWNED state.
4. Thread loads worker config, registers with pool → INITIALIZING.
5. Registration confirmed → IDLE (available for task assignment).
6. If init fails → FAILED (single retry → IDLE or TERMINATED).
   Timeout: runtime.worker.init_timeout_ms (5s).
```

### Shutdown
```
1. Shutdown signal received by pool.
2. All IDLE workers → DRAINING → TERMINATED (immediate, no pending tasks).
3. All BUSY workers → DRAINING (wait for current task to complete, up to shutdown_timeout_ms).
4. All PAUSED workers → DRAINING (resume briefly for cleanup).
5. Each draining worker completes current task → TERMINATED (thread joined, resources freed).
6. If shutdown timeout exceeded → force TERMINATED (thread detached).
7. Pool verifies all workers TERMINATED before pool shutdown complete.
```

---

## 2. Plugin Discovery, Load, Unload, and Update Flow

### Discovery
```
1. Plugin scanner runs on startup and periodically (scan_interval: 60s).
2. Scans plugin directory (`%APPDATA%/Apex/plugins/`) for plugin.yaml manifest files.
3. For each found manifest:
   a. DISCOVERED → VALIDATING (schema + security + capability check).
   b. VALIDATING → VALIDATED or REJECTED.
4. If auto-install policy allows and manifest valid:
   a. VALIDATED → INSTALLING → INSTALLED.
5. If auto-load policy allows:
   a. INSTALLED → LOADING → ACTIVE.
```

### Load
```
1. Plugin Manager receives load request (startup auto-load or user trigger).
2. Sandbox process spawned (isolated heap, limited resources per plugin.sandbox.*).
3. IPC channels established between sandbox host and sandbox process.
4. Capability grants verified against manifest declaration.
5. Plugin onInit hook called within sandbox → timeout: plugin.load_timeout_ms (15s).
6. If init succeeds → ACTIVE (plugin operational).
7. If init fails → FAILED (single retry via LOADING → ACTIVE or UNLOADED).
```

### Unload
```
1. Plugin Manager receives remove request (user action or failed update rollback).
2. If ACTIVE: send shutdown signal → onShutdown hook → wait up to unload_timeout_ms.
3. If SUSPENDED: resume briefly for cleanup → then shutdown signal.
4. UNLOADING: sandbox process terminated; IPC channels closed; files deleted.
5. Registry entry removed → UNLOADED (terminal).
```

### Update
```
1. Update Manager detects new version (marketplace check, auto-update, or manual trigger).
2. If plugin is ACTIVE: brief SUSPENDED pause.
3. Old version files archived to `%APPDATA%/Apex/plugins/archive/<plugin_id>/<old_version>/`.
4. New version files downloaded and installed.
5. New sandbox spawned → LOADING → onInit hook → ACTIVE (with new version).
6. If update fails:
   a. Rollback: load archived old version → LOADING → ACTIVE.
   b. If rollback also fails → UNLOADED (plugin fully removed).
   Timeout: plugin.update_timeout_ms (60s).
```

---

## 3. Provider Initialization and Provider-Failure Flow

### Initialization
```
1. AI Pipeline reads provider config from ai.providers.* keys.
2. For each configured provider:
   a. Validate API key reference (env var exists, key accessible in secret store).
   b. Validate base_url (if custom) resolves.
   c. Establish connection (ping with minimal request → verify 200 response).
   d. Provider registered in provider registry → READY.
3. All providers initialized → AI Pipeline READY.
   Timeout: ai.providers.init_timeout_ms (15s per provider).
```

### Provider Failure
```
1. Provider returns error (5xx, timeout, rate limit, quota exceeded).
2. AI Pipeline evaluates fallback chain:
   a. Check next provider in fallback chain (Anthropic → Local).
   b. Verify next provider is not in cooldown (failure_cooldown_ms: 60s).
   c. Re-route request to next provider → RUNNING.
3. If fallback succeeds → COMPLETED (log fallback usage).
4. If all providers fail → ALL_FAILED:
   a. Emit ai.critical.all_providers_failed event.
   b. Return structured error to caller.
   c. AI advisory mode disabled until provider recovers.
5. Provider circuit breaker:
   a. 5 failures in 60s → circuit opens for 120s.
   b. After cooldown → half-open (1 probe attempt).
   c. Probe success → circuit closes.
   d. Probe failure → circuit reopens for another 120s.
```

---

## 4. Configuration Reload Flow

```
1. Config Manager detects config file change (file watcher or SIGHUP/reload event).
2. Parse new config values.
3. Validate ALL new values against schema (all-or-nothing).
4. If validation fails:
   a. Reject entire batch → keep old config.
   b. Emit config.validation.failed event.
   c. Log warning with offending key paths.
5. If validation passes:
   a. Identify affected subsystems (which keys changed).
   b. Build dependency-ordered notification list.
   c. Send config.updated event to each affected subsystem.
   d. Each subsystem applies new value atomically.
   e. For Restart-required keys: mark for restart; do NOT apply immediately.
   f. Log config change to config_history table.
6. Hot-reload keys: applied immediately (no restart).
7. Restart-required keys: queued; applied on next startup.
```

---

## 5. Dashboard Initialization and Workspace Restore Flow

### Initialization
```
1. Shell loads: title bar, side panel frame, status bar (no data yet).
2. IPC channels opened: subscribe to event streams for active widgets.
3. Layout restored from workspace JSON (or default layout if first launch).
4. Workspace state loaded: active tab, panel positions, widget configs.
5. Widgets initialized in order: system → wallet → trading → AI → plugins.
6. Dashboard signals dashboard.ready event.
7. Data begins flowing: IPC events populate widgets with live data.
```

### Workspace Restore (after crash/restart)
```
1. Load workspace JSON from workspace_persistence_path.
2. Validate workspace JSON schema.
3. If valid: restore panels, tabs, widgets as saved.
4. If invalid/corrupt: fall back to default workspace layout.
5. Re-subscribe to IPC event channels for restored widgets.
6. Widgets refresh data from backend (discard stale cached data).
7. Workspace autosave re-enabled.
```

---

## 6. AI Initialization and Fallback Flow

### Initialization
```
1. AI Pipeline startup:
   a. Load AI config (ai.* keys).
   b. Initialize provider connections (see Provider Initialization flow).
   c. Load AI memory store from database.
   d. Load tool registry from AI-TOOLS.md definitions.
   e. AI Pipeline → READY.
2. AI Orchestrator startup:
   a. Load orchestration policies.
   b. Register as event consumer for trade/risk/state events.
   c. AI Orchestrator → READY.
```

### Fallback
```
1. Primary provider fails → switch to secondary (see Provider Failure flow).
2. All remote providers fail → attempt local provider (Ollama):
   a. Check if local provider is configured and GPU available.
   b. If available → route request to local.
   c. If not available → ALL_FAILED (AI advisory disabled).
3. AI advisory disabled behavior:
   a. Trading Engine continues with risk-only decisions (no AI input).
   b. Dashboard shows "AI Offline" status.
   c. Periodic provider retry every ai.providers.failure_cooldown_ms (60s).
   d. Auto-resume when any provider responds.
```

---

## 7. Recovery and Failover Orchestration Flow

```
1. Health check detects subsystem failure.
2. Recovery Coordinator classifies failure severity and scope.
3. Containment: isolate affected subsystem; pause dependent subsystems.
4. Recovery ordering (see RECOVERY-COORDINATION.md §5):
   a. Phase 1: Foundation (Event Bus, Database, Config).
   b. Phase 2: Infrastructure (RPC, Wallet, Market Data).
   c. Phase 3: Application (Trading, Execution, Risk, AI).
   d. Phase 4: Extensions (Plugins, Dashboard).
5. Each subsystem restored per its playbook (see RECOVERY-PLAYBOOK.md).
6. Reconciliation: verify state against external truth (chain, DB, event store).
7. Release: subsystem fully operational; normal operation resumes.
8. If recovery fails → Safe mode; operator intervention required.
```

---

## 8. Hot-Reload and Restart Boundary Flow

```
1. Config change detected → Config Manager validates.
2. Hot-reload keys identified (Reload: Yes in CONFIGURATION-REFERENCE.md):
   a. Applied immediately via config.updated event.
   b. Subsystems apply atomically.
   c. No service restart required.
3. Restart-required keys identified (Reload: No in CONFIGURATION-REFERENCE.md):
   a. Queued for next restart.
   b. Current value retained.
   c. Dashboard shows "Restart Required" notification with pending key list.
4. Operator triggers restart → graceful shutdown → startup with queued changes applied.
5. Boundary rules:
   a. ai.enabled (restart required) → cannot toggle AI on/off without restart.
   b. runtime.worker.max_workers (hot-reload) → pool scales immediately.
   c. security.secret.storage_backend (restart required) → cannot switch storage without restart.
```

---

## 9. Windows Sleep/Resume and Power-Event Flow

### Sleep
```
1. Windows signals WM_POWERBROADCAST: PBT_APMSUSPEND.
2. Save checkpoint: persist all in-flight state to DB.
3. Close all RPC/WebSocket connections.
4. Stop all timers (health checks, autosave, scheduled tasks).
5. Zero secrets in memory (SecureZeroMemory).
6. Emit runtime.mode.transition (Active → Suspended).
7. Process enters low-power wait state.
```

### Resume
```
1. Windows signals WM_POWERBROADCAST: PBT_APMRESUMEAUTOMATIC.
2. Transition from Suspended → Resuming.
3. Recovery scan:
   a. Re-establish RPC connections to all configured chains.
   b. Query chain for actual state of in-flight trades (see Execution crash resume).
   c. Re-subscribe to price feeds and market data.
   d. Verify wallet balances match DB cache.
4. If all checks pass → Resuming → Running (normal operation).
5. If issues detected → Resuming → Recovering (per RECOVERY-COORDINATION.md).
6. Emit runtime.health.restored or runtime.recovery.completed.
```

### Battery Events
```
1. Battery < 20%: Throttle mode (reduce AI calls, pause low-priority plugins, increase health check interval to 10s).
2. Battery < 5%: Emergency shutdown (save checkpoint → STOPPING → STOPPED).
3. AC Power restored: Resume from throttle to normal (if not shutdown).
```

---

## 10. Update Installation and Rollback Flow

### Installation
```
1. Update Manager detects new version (canary/beta/production channel).
2. Download update package (signed .exe or .zip).
3. Verify Authenticode signature against EV certificate.
4. Verify checksum against published hash.
5. Archive current version to rollback directory.
6. Install new version:
   a. Stop current process (graceful shutdown per §2 timing).
   b. Replace binaries with new version.
   c. Run pending schema migrations.
   d. Start new version → startup sequence.
7. Verify startup successful:
   a. All subsystems reach READY within startup_timeout_ms.
   b. Dashboard loads and shows correct version.
   c. Health check confirms all probes passing.
8. If startup successful → update complete; archive rollback after rollback_window expires.
```

### Rollback
```
1. If startup fails or canary/beta reports critical errors:
   a. Set rollout percentage to 0% (for canary/beta).
   b. Stop new version process.
   c. Restore archived previous version binaries.
   d. Start previous version → startup sequence.
   e. Verify rollback startup successful.
2. For production: immediate full rollback to previous version; root cause SLA: 24 hours.
3. Hotfix: commit fix → fast-track pipeline (canary → beta → production in 4 hours).
```

---

## Cross-References

- **RUNTIME-OPERATIONS.md** — Startup/shutdown/recovery sequencing.
- **RECOVERY-COORDINATION.md** — Recovery ordering and coordination.
- **RECOVERY-PLAYBOOK.md** — Per-failure-class playbooks.
- **STATE-MACHINE-INDEX.md** — State machine coupling during flows.
- **CONFIGURATION-REFERENCE.md** — Reload/restart key semantics.
- **PLUGIN-STATE-MACHINE.md** — Plugin lifecycle states.
- **WORKER-STATE-MACHINE.md** — Worker lifecycle states.
- **SERVICE-STATE-MACHINE.md** — Windows service and power events.
- **APP-BUILDER-WORKFLOW.md** — Update pipeline and rollback.
- **TRACEABILITY-MATRIX.md** — REQ-E2E-002, REQ-RUNTIME-008.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-27 | New: complete runtime flow lifecycle for 10 flows with step-by-step sequencing | Runtime Team |
