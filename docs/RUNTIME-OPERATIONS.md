# Runtime Operations

## Document type
Document type: [REFERENCE]

## Version
**Version:** 0.2.0 | **Status:** Draft | **Last Updated:** 2026-07-27 | **Owner:** Runtime Team

## Purpose
Defines how the backend runs, recovers, and stays observable in production — with explicit startup/shutdown/recovery sequencing, operator failure handling, and Windows-specific behavior.

---

## 1. Runtime Modes

| Mode | Description | Trading | AI | UI | Plugins |
|------|-------------|---------|----|----|---------|
| **Active** | Full operation | Enabled | Enabled | Enabled | Enabled |
| **Service** | Headless background service | Enabled | Enabled | Disabled | Enabled |
| **Tray** | System tray with minimal UI | Enabled | Enabled | Minimal | Enabled |
| **Recovery** | Post-crash restoration | Paused | Disabled | Recovery UI only | Disabled (until checked) |
| **Maintenance** | Manual operator mode | Disabled | Disabled | Full | Disabled |
| **Safe** | Safe mode (no plugins, no AI, no trades) | Disabled | Disabled | Full | Disabled |

---

## 2. Startup Sequence

### 2.1 Phase 1: Kernel Bootstrap (critical)
```
1. Config Manager loads default config from `config/default.yaml`.
2. Config Manager applies profile overlay (`config/profiles/<name>.yaml`).
3. Config Manager validates all keys against schema.
4. Secret Manager initializes storage backend (OS keychain).
5. Audit Logger starts.
6. Diagnostics/telemetry initializes (console + file).
```

### 2.2 Phase 2: Infrastructure
```
7. Event Bus starts (ring buffer allocation, channel creation).
8. Database Pool opens connections.
9. Registry Service loads (chain, token, DEX registries).
10. Worker Pool initializes (`runtime.worker.min_workers` threads).
```

### 2.3 Phase 3: Domain Services
```
11. Network Manager establishes RPC connections to configured chains.
12. Wallet Manager initializes wallets.
13. Market Data engine starts price feed subscriptions.
14. AI Pipeline initializes provider connections.
```

### 2.4 Phase 4: Application
```
15. Risk Engine loads risk policies.
16. Trading Engine initializes (no trading until fully ready).
17. Plugin Manager scans and validates installed plugins.
18. Dashboard (if UI mode) initializes workspace and restores state.
```

### 2.5 Phase 5: go-live
```
19. Trading Engine transitions to READY.
20. Dashboard signals readiness to user.
21. Health Check thread starts periodic probes.
```

Total startup budget: `runtime.startup_timeout_ms` (default 60000ms). If exceeded, transition to Safe mode.

---

## 3. Shutdown Sequence

### 3.1 Phase 1: Graceful Drain
```
1. Dashboard signals shutdown warning to user.
2. Trading Engine stops accepting new opportunities.
3. In-flight trades are allowed to complete (up to `runtime.shutdown_trade_grace_ms`).
4. AI Pipeline drains pending requests (up to `runtime.shutdown_ai_grace_ms`).
5. Plugin Manager signals all plugins to stop.
```

### 3.2 Phase 2: Forced Stop
```
6. If trade grace expired, in-flight trades are marked for crash recovery.
7. Worker Pool drains tasks and stops threads.
8. AI Pipeline cancels remaining requests.
9. Market Data unsubscribes from price feeds.
```

### 3.3 Phase 3: Teardown
```
10. Event Bus flushes remaining events to dead-letter queue.
11. Database Pool closes connections (flush pending writes).
12. Secret Manager locks keychain access.
13. Config Manager saves last-known-good config.
14. Audit Logger flushes and stops.
```

Total shutdown budget: `runtime.shutdown_timeout_ms` (default 30000ms). If exceeded, force terminate.

---

## 4. Recovery Sequencing

### 4.1 Crash Recovery
Triggered when runtime starts after an unclean shutdown (no graceful shutdown record).

```
1. Detect unclean shutdown: missing `runtime/shutdown.graceful` marker.
2. Load last-known-good config.
3. Scan event store for incomplete state transitions (trades, AI requests, plugin ops).
4. For each subsystem with incomplete state:
   a. Query external state (chain, provider) for actual status.
   b. Reconcile: advance or roll back based on actual state.
5. Report recovery results to operator via `system.recovery.completed` event.
6. Resume normal operation (or transition to Safe mode if recovery had critical failures).
```

### 4.2 Failover Recovery
Triggered when a critical subsystem fails and a backup is available.

| Subsystem | Failover | Recovery |
|-----------|----------|----------|
| RPC connection | Fallback RPC endpoint | Reconnect primary after `runtime.rpc.reconnect_interval_ms` |
| AI provider | Fallback provider model | Retry primary after `runtime.provider.retry_interval_ms` |
| Event Bus | In-memory buffer → disk DLQ | Replay from DLQ when event bus restarts |
| Database | Local SQLite → remote Postgres | Sync missed writes |

---

## 5. Operator Failure Handling

| Failure | Detection | Operator Action | Automated Response |
|---------|-----------|-----------------|-------------------|
| Wallet key not found | Startup check | Provide key via secure input | Block trading until key loaded |
| RPC connection failure | Health check | Check network, check RPC status | Fallback to secondary, retry every 30s |
| Disk full | Log write failure | Free disk space | Pause logging, emit critical alert |
| Memory exceeded | `resource.memory_limit_mb` hit | Restart app with higher limit | Force GC, evict caches, then Safe mode |
| AI provider quota exceeded | 429 response | Upgrade plan or switch provider | Fallback to secondary provider |
| Plugin crash | Plugin sandbox exit | Remove / update plugin | Auto-restart plugin once; second crash disables |
| Gas spike | Base fee > threshold | Wait for gas to normalize | Pause trading, resume when gas < threshold |

---

## 6. Windows-Specific Behavior

| Scenario | Behavior |
|----------|----------|
| **Service mode** | Runs as Windows service (no interactive session). Logs to Event Log. |
| **Tray mode** | Minimizes to system tray. Shows trade count, balance, health status. |
| **Sleep/resume** | On sleep: pause all operations, save checkpoint. On resume: full recovery scan. |
| **Power event** | On battery < 20%: throttle to minimum. On AC restore: resume normal. |
| **Windows update** | Before shutdown: checkpoint save. After update: recovery scan. |
| **Firewall change** | Re-check all network connections. Re-register with RPC endpoints. |

---

## 7. Observability

| Event | Trigger | Payload |
|-------|---------|---------|
| `runtime.startup.phase` | Startup phase complete | `{phase, duration_ms, status}` |
| `runtime.shutdown.phase` | Shutdown phase complete | `{phase, duration_ms, status}` |
| `runtime.mode.transition` | Mode change | `{from_mode, to_mode, reason}` |
| `runtime.recovery.completed` | Recovery scan done | `{trades_recovered, trades_lost, critical_errors}` |
| `runtime.operator.intervention` | Manual action required | `{subsystem, issue, severity, recommended_action}` |

---

## Cross-References

- **SERVICE-LIFECYCLE.md** — Windows service lifecycle.
- **SHUTDOWN-LIFECYCLE.md** — Detailed shutdown sequence.
- **HEALTHCHECKS.md** — Health probe definitions.
- **MONITORING-OBSERVABILITY.md** — Metric collection and alerting.
- **BOOTSTRAP-SEQUENCE.md** — Bootstrap entry point.
- **TRADING-ENGINE.md** — Trade lifecycle integration.
- **CONFIGURATION-REFERENCE.md** — Runtime config keys (`runtime.*`).
- **TRACEABILITY-MATRIX.md** — Runtime requirement coverage.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 0.2.0 | 2026-07-27 | Full startup/shutdown/recovery sequencing, operator failure handling, Windows behavior | Runtime Team |
| 0.1.0 | 2026-07-27 | Initial stub | Runtime Team |