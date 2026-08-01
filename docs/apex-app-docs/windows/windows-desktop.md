---
metadata_schema_version: 1.0
document_id: DOC-0238
title: Windows Desktop
plane: Product Specification
domain: Windows
class: Specification
authority: Canonical
status: Active
owner: Windows Team
version: 1.0.0
canonical_source: docs/apex-app-docs/windows/windows-desktop.md
related_concepts:
  - CONCEPT-0238
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Windows
type: CONTRACT
purpose: "Defines the Windows desktop shell behavior — tray lifecycle, window lifecycle, minimize-to-tray, restore-from-tray, first-run behavior, login recovery, offline UI, degraded states, multi-window, and cross-subsystem integration."
scope: None
---

# Windows Desktop

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-27 | **Owner:** Windows Team

## Purpose
Defines the Windows desktop shell behavior — tray lifecycle, window lifecycle, minimize-to-tray, restore-from-tray, first-run behavior, login recovery, offline UI, degraded states, multi-window, and cross-subsystem integration.

---

## 1. Window Lifecycle

### 1.1 Window States

| State | Description | Visual | User Action Available |
|-------|-------------|--------|---------------------|
| **Creating** | Window being initialized | Not visible | None |
| **Normal** | Window visible, full functionality | Full dashboard | All |
| **Minimized** | Window minimized to taskbar | Taskbar icon only | Restore, Tray |
| **Tray-only** | Window hidden, tray icon visible | Tray icon only | Show, Context menu |
| **Floating panels** | Main window + floating widget windows | Main + separate windows | All |
| **Full-screen** | Full-screen on single monitor | Full-screen dashboard | Exit full-screen |
| **Closing** | Window closing (minimize-to-tray) | Brief animation → tray | None |
| **Restoring** | Window restoring from tray | Brief animation → visible | All |

### 1.2 Window Lifecycle Flow

```
First Launch → Creating → Normal
  Normal → Minimized → Tray-only (on close button)
  Normal → Full-screen → Normal (toggle)
  Tray-only → Restoring → Normal (on tray click)
  Normal → Closing → Tray-only (default behavior)
  Tray-only → [Exit from context menu] → Full shutdown
```

### 1.3 Close Button Behavior

| Config | Default | Behavior |
|--------|---------|---------|
| `windows.desktop.close_to_tray` | `true` | Close button minimizes to tray (not exit) |
| `windows.desktop.close_to_tray = false` | `false` | Close button triggers full shutdown (with confirmation) |

---

## 2. Tray Integration

See **WINDOWS-APP-ARCHITECTURE.md §2** for full tray lifecycle. This document defines desktop-specific tray behavior:

| Tray Action | Desktop Effect | Keyboard Shortcut |
|------------|---------------|-------------------|
| **Single click** | Show/restore main window | — |
| **Right click** | Context menu | — |
| **Double click** | Show dashboard + activate window | — |
| **Balloon click** | Navigate to notification target | — |

### Tray Visibility Rules

- Tray icon visible when: window is tray-only, window is minimized, or `windows.tray.always_visible` = true.
- Tray icon hidden when: window is Normal AND `windows.tray.always_visible` = false.
- Tray icon ALWAYS visible in service mode (backend runs independently).

---

## 3. First-Run Experience

### 3.1 First-Run Wizard

| Step | Content | User Action | Validation |
|------|---------|-------------|-----------|
| **1. Welcome** | App introduction, version info | Next | — |
| **2. License** | License agreement | Accept / Decline | Must accept to continue |
| **3. Role Selection** | Choose operator/trader/viewer | Select role | Role stored in config |
| **4. Wallet Setup** | Import or create wallet | Import key / Create new | Wallet address validated |
| **5. Chain Selection** | Select chains to monitor | Toggle chains | At least 1 chain selected |
| **6. Provider Setup** | Enter AI provider API keys | Enter keys / Skip | Keys validated on entry (optional) |
| **7. Notifications** | Configure notification preferences | Toggle preferences | — |
| **8. Start** | Dashboard launches with configured settings | Start | All required steps completed |

### 3.2 First-Run State Persistence

- First-run state stored at `%APPDATA%/apex/first-run-state.json`.
- Completed steps persist across app restarts.
- If app crashes during wizard → resume from last completed step.

---

## 4. Login Recovery

### 4.1 Re-Authentication After Sleep

```
1. Windows resume detected (see WINDOWS-APP-ARCHITECTURE.md §3).
2. If `windows.security.require_reauth_on_wake` = true:
   a. Show lock screen overlay on dashboard.
   b. Operator must re-enter master password.
   c. Master password validated → secrets re-loaded from DPAPI.
   d. Dashboard unlocked.
3. If re-auth disabled → dashboard resumes immediately (secrets re-loaded from memory cache).
4. Re-auth timeout: 30s → if no response → dashboard stays locked.
```

### 4.2 Session Recovery After Crash

```
1. App crash → restart → check for saved session state.
2. If session state found → restore workspace, widgets, filters.
3. If session state corrupt → use default workspace.
4. Recovery scan for incomplete trades (see RECOVERY-COORDINATION.md).
5. Show "Recovery complete" notification with results summary.
```

---

## 5. Offline & Degraded UI States

### 5.1 UI State Matrix

| Condition | UI State | Visual | Actions |
|-----------|----------|--------|---------|
| **Online, Active** | Full dashboard | Normal | All |
| **Online, Paused** | Paused trading | Yellow "Paused" banner | Resume, Settings |
| **Online, Halted** | Halted by operator | Red "Halted" banner | Resume (operator only) |
| **Offline** | Offline mode | "Offline" banner + grey overlay on trading widgets | View cached data |
| **Degraded (AI down)** | Partial degradation | "AI unavailable" info banner | Trading continues (no AI assistance) |
| **Degraded (RPC issues)** | Partial degradation | "Chain issues" warning on affected chain widgets | Trading paused for affected chains |
| **Recovery mode** | Recovery | "Recovering..." overlay | View recovery progress |
| **Emergency** | Minimal | Only P0 widgets visible | Operator actions only |

### 5.2 Offline Dashboard Behavior

| Widget | Offline Behavior |
|--------|-----------------|
| **Spread monitor** | Show "Offline" overlay with last cached spread |
| **Trade list** | Show cached trade history (no new trades) |
| **Wallet balance** | Show cached balance with "Last updated: X" |
| **Risk gauges** | Show last cached risk state |
| **System stats** | Show local system stats (CPU, RAM) — still works |
| **Log stream** | Show local logs only — no remote events |
| **Charts** | Show cached chart data |

---

## 6. Multi-Window Behavior

### 6.1 Window Types

| Window | Ownership | Visibility | Z-Order | Taskbar |
|--------|-----------|-----------|---------|---------|
| **Main dashboard** | Main (UI) process | Always (or tray-only) | Normal | Yes (if visible) |
| **Floating panels** | Main (UI) process | Per-panel | Always-on-top (if enabled) | No |
| **Settings dialog** | Main (UI) process | Modal | Above main | No |
| **About dialog** | Main (UI) process | Modal | Above main | No |
| **First-run wizard** | Main (UI) process | Modal | Above main | No |

### 6.2 Window Activation Rules

- Main window activation: click tray icon, click taskbar icon, Alt+Tab.
- Floating panel activation: click panel title bar.
- Only one main window (not multiple dashboard instances).
- Multiple floating panels allowed (up to `dashboard.max_floating_panels`).

---

## 7. Cross-Subsystem Integration

| Caller | Purpose | Contract |
|--------|---------|----------|
| Dashboard Runtime | Window state management | `dashboard.window.state` event |
| Windows App Architecture | Tray/power integration | `system.power.*` / `windows.tray.action` events |
| Config Manager | UI config change | `config.updated` event |
| Notification Center | Desktop notification delivery | `notification.show` IPC command |
| Health Checker | Degraded state notification | `health.degraded` IPC channel |

| Config Key | Default | Description |
|-----------|---------|-------------|
| `windows.desktop.close_to_tray` | `true` | Close → tray vs shutdown |
| `windows.tray.always_visible` | `true` | Tray icon always visible |
| `windows.security.require_reauth_on_wake` | `true` | Re-auth after sleep |
| `windows.desktop.show_on_startup` | `true` | Show dashboard on start |
| `windows.desktop.recent_tray_count` | `5` | Recent items in tray context menu |

---

## Cross-References

- **WINDOWS-APP-ARCHITECTURE.md** — Process model, tray lifecycle, power events.
- **DASHBOARD-RUNTIME.md** — Dashboard initialization and state management.
- **DASHBOARD-LAYOUT.md** — Layout model, floating panels, multi-monitor.
- **WINDOWS-NOTIFICATION-INTEGRATION.md** — Toast and tray notifications.
- **WORKSPACE-MANAGER.md** — Workspace persistence and recovery.
- **RECOVERY-COORDINATION.md** — Crash recovery coordination.
- **PERMISSION-MODEL.md** — Role selection in first-run wizard.
- **CONFIGURATION-REFERENCE.md** — Desktop config keys.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-27 | Production-grade Windows desktop shell: 8 window states with lifecycle flow, close button behavior, tray integration with visibility rules, 8-step first-run wizard, login recovery (re-auth after sleep + crash), offline & degraded UI state matrix (8 conditions), offline widget behavior (7 widgets), multi-window behavior, cross-subsystem integration | Windows Team |
| 0.1.0 | 2026-07-27 | Initial stub | Windows Team |
