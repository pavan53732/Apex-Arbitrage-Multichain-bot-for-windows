---
type: CONTRACT
owner: Windows Team
status: Canonical
version: 1.0.0
purpose: Defines the Windows desktop application structure — process model, Windows integration, tray lifecycle, sleep/resume handling, portable mode, auto-start, crash dump generation, registry usage, DPI scaling, multi-monitor support, and cross-subsystem integration contracts.
scope: None
last_updated: 2026-07-29
canonical_source: docs/WINDOWS-APP-ARCHITECTURE.md
---

# Windows App Architecture

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-27 | **Owner:** Windows Team

## Purpose
Defines the Windows desktop application structure — process model, Windows integration, tray lifecycle, sleep/resume handling, portable mode, auto-start, crash dump generation, registry usage, DPI scaling, multi-monitor support, and cross-subsystem integration contracts.

---

## 1. Process Model

### 1.1 Process Architecture

| Process | Role | Priority | Memory Budget | Startup Order | Shutdown Order |
|---------|------|----------|--------------|--------------|---------------|
| **Main (Electron)** | Desktop shell, IPC broker, tray, lifecycle | Normal | 150 MB | 1 | Last |
| **Renderer (Electron)** | Dashboard UI, widgets | Normal | 100 MB | 2 (after Main) | 2 |
| **Backend (Node)** | Trading engine, AI pipeline, event bus | High | 200 MB | 3 (after UI) | 1 (flush state first) |
| **Plugin Sandbox** | Plugin execution (per-plugin) | BelowNormal | 50 MB per plugin | On-demand | Per plugin |

### 1.2 Inter-Process Communication

| IPC Path | Direction | Transport | Protocol | Latency Target |
|---------|-----------|-----------|----------|---------------|
| Main → Renderer | Commands, state updates | Electron IPC | Typed channels | < 1ms |
| Renderer → Main | User actions, config changes | Electron IPC | Typed commands | < 1ms |
| Main → Backend | Trading commands, AI requests | Named pipe / TCP | IPC-PROTOCOL | < 5ms |
| Backend → Main | Events, status updates | Named pipe / TCP | IPC-PROTOCOL | < 5ms |
| Main → Plugin | Plugin commands | Named pipe | IPC-PROTOCOL | < 10ms |
| Plugin → Main | Plugin results | Named pipe | IPC-PROTOCOL | < 10ms |

### 1.3 Process Lifecycle

```
1. Main process starts → initialize IPC broker, load config.
2. Main creates Backend process (spawn child).
3. Main creates Renderer window (Electron BrowserWindow).
4. IPC bridge established between all processes.
5. Backend initializes: event bus → trading engine → AI → health.
6. Dashboard shell rendered → workspace restored → widgets initialized.
7. App signals system.startup.phase complete.

Shutdown (reverse):
1. Dashboard signals system.shutdown.phase started.
2. Backend: flush pending trades → persist state → stop workers → stop event bus.
3. Renderer: close all widgets → save workspace.
4. Main: close IPC bridge → terminate Backend → close Renderer → exit.
```

---

## 2. System Tray Lifecycle

### 2.1 Tray Icon States

| State | Icon | Tooltip | Context Menu |
|-------|------|---------|-------------|
| **Starting** | Grey icon with spinner | "Apex starting..." | None (waiting for backend) |
| **Active** | Green icon | "Apex: Active — monitoring spreads" | Show dashboard, Pause, Settings, Exit |
| **Paused** | Yellow icon | "Apex: Paused" | Resume, Settings, Exit |
| **Halted** | Red icon | "Apex: Halted by operator" | Show dashboard (read-only), Resume, Settings, Exit |
| **Error** | Red icon with X | "Apex: Error — check dashboard" | Show dashboard, Restart, Exit |
| **Offline** | Grey icon with ! | "Apex: Offline — no network" | Show dashboard, Settings, Exit |
| **Updating** | Blue icon with arrow | "Apex: Updating..." | None (update in progress) |

### 2.2 Tray Context Menu Actions

| Action | Availability | Effect | Confirmation |
|--------|-------------|--------|-------------|
| **Show Dashboard** | Always | Show/restore main window | None |
| **Pause Trading** | Active mode | Switch to Paused mode | None (instant) |
| **Resume Trading** | Paused/Halted mode | Switch to Active mode | None (instant) |
| **Settings** | Always | Open Settings page | None |
| **Restart** | Error mode | Restart backend process | Confirm dialog |
| **Exit** | Always | Full shutdown sequence | Confirm dialog (unless `tray.exit_no_confirm`) |
| **About** | Always | Show version info dialog | None |

### 2.3 Tray Behavior

- Minimize to tray: closing the main window hides it (not exits).
- Restore from tray: clicking tray icon shows main window.
- Tray icon click: single click = show dashboard; right-click = context menu.
- Tray balloon notifications: max 1 per 5s; queued and shown sequentially.
- Tray persistence: tray icon remains during backend-only mode (service mode).

---

## 3. Sleep/Resume Handling

### 3.1 Windows Power Event Handling

| Power Event | Action | Detail |
|-------------|--------|--------|
| **Suspend (sleep)** | 1. Zero all secrets in memory. 2. Cancel all pending AI requests. 3. Persist current workspace. 4. Mark all widgets SUSPENDED. 5. Close WebSocket connections. 6. Emit system.power.suspend event. | Must complete within `windows.power.suspend_timeout_ms` (default 3000ms) |
| **Resume (wake)** | 1. Re-authenticate operator (if lock screen). 2. Re-establish RPC connections. 3. Re-subscribe to event streams. 4. Resume widgets from SUSPENDED. 5. Run crash recovery scan for incomplete trades. 6. Emit system.power.resume event. | Full resume within `windows.power.resume_timeout_ms` (default 10000ms) |
| **Hibernate** | Same as Suspend (full state preservation). | Same timeout |
| **Critical battery** | 1. Pause all trading. 2. Persist workspace. 3. Show notification. 4. If battery < 5% → force shutdown. | Immediate |
| **Low battery** | Show notification, suggest pause trading. | None (advisory) |

### 3.2 Sleep/Resume Sequence Diagram

```
[Suspend]
  Windows → Main process → WM_POWERBROADCAST (PBT_APMSUSPEND)
    → Secrets zeroed
    → AI requests cancelled
    → Workspace persisted
    → Widgets suspended
    → WebSocket closed
    → Backend enters low-power mode

[Resume]
  Windows → Main process → WM_POWERBROADCAST (PBT_APMRESUMEAUTOMATIC)
    → Operator re-auth
    → RPC reconnect (with backoff)
    → Event stream re-subscribe
    → Widgets resume
    → Recovery scan (incomplete trades)
    → Backend resumes normal mode
```

---

## 4. Portable Mode

### 4.1 Portable Mode Detection

```
1. On startup, check if executable is in a "portable" directory:
   - If `portable_marker` file exists next to executable → portable mode.
   - If running from USB/removable drive (Windows volume info) → portable mode.
2. Portable mode changes:
   - All data stored relative to executable directory (not %APPDATA%).
   - No Windows registry entries.
   - No Windows service installation.
   - No auto-start registration.
   - No Windows Credential Manager (use encrypted file instead).
   - Config path: ./config/ (relative).
   - Workspace path: ./workspaces/ (relative).
   - Database path: ./data/ (relative).
   - Logs path: ./logs/ (relative).
```

### 4.2 Portable Mode Constraints

| Feature | Installed Mode | Portable Mode |
|---------|---------------|---------------|
| **Config storage** | `%APPDATA%/apex/config/` | `./config/` |
| **Workspace storage** | `%APPDATA%/apex/workspaces/` | `./workspaces/` |
| **Database** | `%APPDATA%/apex/data/` | `./data/` |
| **Secret storage** | Windows Credential Manager | Encrypted file (DPAPI not available) |
| **Auto-start** | Windows registry | Not available |
| **Windows service** | SCM registration | Not available |
| **Notifications** | Windows Action Center | Tray balloon only |
| **Code signing** | Authenticode verified | Self-verified (checksum) |
| **Update** | Automatic via update service | Manual (download + replace) |

---

## 5. Auto-Start

### 5.1 Auto-Start Registration

| Mode | Registry Key | Location | Effect |
|------|-------------|----------|--------|
| **Tray mode** | `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\ApexArbitrage` | Current User Run | Start tray icon on login |
| **Service mode** | Windows Service Control Manager | Services database | Start backend service on boot |

### 5.2 Auto-Start Behavior

- Auto-start is OFF by default (`windows.auto_start.enabled: false`).
- Operator can enable via Settings page → triggers registry write.
- On auto-start: Main process starts → tray icon appears → backend starts in background.
- Dashboard does NOT automatically show on auto-start (stays in tray until user clicks).
- Auto-start removal: Settings page → triggers registry key delete.

---

## 6. Crash Dump Generation

### 6.1 Crash Dump Configuration

| Setting | Value | Config Key |
|---------|-------|------------|
| **Dump type** | MiniDumpNormal (stack + modules) | `windows.crash.dump_type` |
| **Dump path** | `%APPDATA%/apex/crashdumps/` | `windows.crash.dump_path` |
| **Max dump files** | 10 (oldest auto-deleted) | `windows.crash.max_dump_files` |
| **Dump on exception** | Yes (structured exceptions) | `windows.crash.dump_on_exception` |
| **Dump on OOM** | Yes (memory exhaustion) | `windows.crash.dump_on_oom` |
| **Upload to server** | No (privacy) | `windows.crash.auto_upload: false` |

### 6.2 Crash Recovery Flow

```
1. Crash detected (SEH exception, unhandled exception, OOM).
2. MiniDumpWriteDump called → dump file written.
3. Error message displayed to user (modal dialog).
4. User chooses: "Restart" or "Exit".
5. On "Restart":
   a. Backend process respawned.
   b. Workspace restored from last autosave.
   c. Recovery scan for incomplete trades.
   d. Crash dump details logged.
6. On "Exit": clean shutdown (no recovery).
```

---

## 7. Registry Usage

| Registry Key | Purpose | Written By | Portable Mode |
|-------------|---------|-----------|---------------|
| `HKCU\...\Run\ApexArbitrage` | Auto-start registration | Settings page | Not written |
| `HKCU\Software\Apex\Settings` | User preferences (minimal) | Config Manager | Not written |
| `HKLM\Software\Apex\Service` | Service registration | Installer | Not written |
| `HKLM\...\Windows\CurrentVersion\Uninstall\Apex` | Uninstall entry | Installer | Not written |

### Registry Rules
- Minimal registry usage — most config stored in files.
- Registry keys cleaned on uninstall.
- Portable mode: zero registry writes.

---

## 8. DPI Scaling

### 8.1 DPI Awareness

- Per-monitor DPI aware: `DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2`.
- All layout stored in logical pixels (1x scale).
- Render scale applied per monitor at paint time.
- Font size: base × monitor DPI scale.
- Minimum effective: 1920×1080 at 150% (1280×720 logical).

### 8.2 DPI Change Handling

| Event | Action |
|-------|--------|
| Monitor DPI change | Re-render widgets on affected monitor |
| DPI change during drag | Re-scale ghost widget |
| Mixed DPI monitors | Per-monitor rendering |
| Startup DPI detection | Validate saved dimensions against DPI |

---

## 9. Multi-Monitor Support

See **DASHBOARD-LAYOUT.md §6** for full multi-monitor layout rules. This document defines the Windows-level integration:

| Feature | Implementation |
|---------|---------------|
| Monitor enumeration | Windows `EnumDisplayMonitors` API |
| Monitor change detection | `WM_DISPLAYCHANGE` message |
| Per-monitor DPI | `GetDpiForMonitor` API |
| Window placement | `SetWindowPos` with monitor-relative coordinates |
| Full-screen support | Per-monitor full-screen mode |
| Multi-window | Floating panels as independent windows |

---

## 10. Windows Defender Interactions

| Interaction | Behavior | Config Key |
|------------|----------|------------|
| **Exclusion registration** | On install, add app directory to Defender exclusion list (optional) | `windows.defender.exclusion_enabled: false` |
| **SmartScreen** | Authenticode-signed installer bypasses SmartScreen warning | `build.signing.enabled: true` |
| **Real-time protection** | Defender does not scan config/data directories (exclusion) | — |
| **Defender alerts** | If Defender blocks a plugin → show notification, disable plugin | — |

---

## 11. Cross-Subsystem Integration

### 11.1 Who Calls Windows App Architecture

| Caller | Purpose | Contract |
|--------|---------|----------|
| Runtime Orchestrator | Startup/shutdown signal | `system.startup.phase` / `system.shutdown.phase` events |
| Config Manager | Windows config change | `config.updated` event |
| Dashboard Runtime | UI initialization | `dashboard.ready` event |
| Plugin Manager | Plugin sandbox creation | `plugin.sandbox.create` API |
| Service Lifecycle | Windows service registration | `service.install` / `service.uninstall` APIs |

### 11.2 Who Windows App Architecture Calls

| Target | Purpose | Contract |
|--------|---------|----------|
| Backend Process | Spawn/terminate | `child_process.spawn` / `child_process.kill` |
| IPC Bridge | Establish inter-process communication | IPC-PROTOCOL.md |
| Windows APIs | Tray, power, DPI, monitor, registry | Windows SDK |
| Event Bus | Emit power/mode events | `system.power.*` / `system.mode.*` events |
| Recovery Coordination | Post-crash/sleep recovery | `recovery.scan` API |

### 11.3 Events Windows App Architecture Emits

| Event | Payload | Consumer |
|-------|---------|----------|
| `system.power.suspend` | `{timestamp, cancelled_ai_requests, persisted_workspace}` | Health, Dashboard |
| `system.power.resume` | `{timestamp, recovery_scan_started}` | Health, Dashboard, Trading |
| `system.power.low_battery` | `{battery_pct, suggested_action}` | Dashboard, Notification |
| `system.power.critical_battery` | `{battery_pct, forced_shutdown}` | All |
| `windows.tray.action` | `{action, mode_before, mode_after}` | Dashboard, Audit |
| `windows.crash.dump_created` | `{dump_path, crash_type, process}` | Health, Operator |

### 11.4 Configuration Windows App Architecture Owns

| Config Key | Default | Description |
|-----------|---------|-------------|
| `windows.auto_start.enabled` | `false` | Auto-start on login |
| `windows.tray.exit_no_confirm` | `false` | Skip exit confirmation |
| `windows.power.suspend_timeout_ms` | `3000` | Sleep preparation timeout |
| `windows.power.resume_timeout_ms` | `10000` | Resume completion timeout |
| `windows.crash.dump_type` | `MiniDumpNormal` | Crash dump type |
| `windows.crash.max_dump_files` | `10` | Max crash dumps retained |
| `windows.defender.exclusion_enabled` | `false` | Defender exclusion list |
| `windows.portable.enabled` | `auto` | Portable mode (auto-detect) |

---

## Cross-References

- **ARCHITECTURE.md** — Platform architecture boundaries.
- **WINDOWS-DESKTOP.md** — Desktop shell behavior, tray menu, window lifecycle.
- **WINDOWS-SERVICE-INTEGRATION.md** — Windows Service Control Manager integration.
- **WINDOWS-NETWORK-RESILIENCE.md** — Network reconnect and proxy handling.
- **WINDOWS-NOTIFICATION-INTEGRATION.md** — Toast, tray, Action Center notifications.
- **WINDOWS-SECURITY-INTEGRATION.md** — DPAPI, Credential Manager, Defender.
- **WINDOWS-DEPLOYMENT.md** — Installer, update, rollback lifecycle.
- **IPC-PROTOCOL.md** — Inter-process communication protocol.
- **DASHBOARD-LAYOUT.md** — DPI scaling, multi-monitor layout rules.
- **WORKSPACE-MANAGER.md** — Workspace persistence and restore.
- **RECOVERY-COORDINATION.md** — Post-crash/sleep recovery coordination.
- **SECRET-LIFECYCLE.md** — Secret zeroing on sleep, re-auth on wake.
- **CONFIGURATION-REFERENCE.md** — Windows config keys (`windows.*`).
- **END-TO-END-WIRING-CONTRACT.md** — Cross-subsystem wiring.
- **TRACEABILITY-MATRIX.md** — REQ-WIN-001.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-27 | Production-grade Windows app architecture: 4-process model with IPC, tray lifecycle (7 states + context menu), sleep/resume handling (5 power events with sequence diagram), portable mode (12 feature differences), auto-start registration, crash dump generation, registry usage (4 keys), DPI scaling, multi-monitor, Defender interactions, cross-subsystem integration | Windows Team |
| 0.1.0 | 2026-07-27 | Initial stub | Windows Team |
