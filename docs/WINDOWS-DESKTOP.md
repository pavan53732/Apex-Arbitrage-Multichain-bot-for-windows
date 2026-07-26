# APEX Windows Desktop Application

> **Version:** 3.0.0 | **Target:** Windows 10/11 x64 | **Distribution:** Electron `.exe` | **Runtime Model:** No Docker, No WSL

---

## 1. Overview

APEX is designed as a native-feeling Windows desktop application delivered as a single installable Electron package. The application embeds its UI, application services, local database, and desktop integrations into one deployable product.

Primary goals:

- one-step install for non-server users
- local encrypted configuration and wallet management
- long-running background operation through tray support
- simple update and release workflow

---

## 2. Desktop Architecture

```text
Electron Main Process
  - app lifecycle
  - tray
  - updater
  - SQLite
  - AI pipeline services
  - blockchain services
  - IPC handlers
        ^
        |
contextBridge / preload
        |
        v
Renderer (React + TypeScript)
  - dashboard
  - settings
  - trades
  - skills
  - agents
```

### 2.1 Main Process Responsibilities

- own privileged services and secrets
- receive and validate IPC requests
- host local database connections
- run background schedulers and event bus
- integrate with Windows lifecycle events

### 2.2 Renderer Responsibilities

- present dashboards and settings UI
- display real-time state updates
- collect user commands and configuration input
- never own privileged application authority

---

## 3. Repository Layout

Recommended desktop package layout:

```text
packages/desktop/
  electron/
    main.ts
    preload.ts
    ipc/
    tray.ts
    updater.ts
    safe-storage.ts
    window-manager.ts
  src/
    pages/
    components/
    stores/
    hooks/
    lib/
  electron-builder.yml
  vite.config.ts
  package.json
```

A monorepo split remains compatible with shared packages for `ai`, `agents`, `skills`, `chains`, `strategies`, and `contracts`.

---

## 4. Build Pipeline

### 4.1 Development Flow

1. install dependencies
2. start renderer dev server
3. launch Electron main process
4. connect preload bridge
5. validate IPC and local database startup

### 4.2 Production Build Flow

1. type-check TypeScript
2. build renderer assets with Vite
3. compile/bundle Electron main and preload
4. rebuild native modules for Electron ABI
5. package installer with `electron-builder`
6. publish artifacts to GitHub Releases

### 4.3 Native Module Rebuild

Modules such as `better-sqlite3` must be rebuilt against the exact Electron runtime. This should be automated with `electron-rebuild` or equivalent in CI and local release builds.

---

## 5. electron-builder Configuration

Representative concerns for `electron-builder.yml`:

| Setting | Purpose |
|--------|---------|
| `appId` | stable Windows application identity |
| `productName` | user-facing app name |
| `directories.output` | artifact output location |
| `files` | production bundle allowlist |
| `asar` | package app resources |
| `nsis.perMachine` | keep false for per-user install |
| `publish` | GitHub Releases integration |

Representative baseline:

```yaml
appId: com.apex.arbitrage
productName: APEX
asar: true
files:
  - dist/**
  - electron/**
  - package.json
win:
  target:
    - nsis
publish:
  provider: github
```

---

## 6. NSIS Installer Strategy

### 6.1 Installer Goals

- no admin requirement for normal install
- per-user install path
- clean uninstall path
- shortcut creation
- update compatibility

### 6.2 Recommended Behaviour

- install under user-local application data location
- create Start Menu and optional desktop shortcut
- register uninstaller entry
- preserve user data across upgrades unless explicitly removed

### 6.3 Uninstall Policy

Offer a clear choice between:

- uninstall application only
- uninstall application and purge local data

This prevents accidental deletion of logs, trade history, or configuration when the user is only reinstalling.

---

## 7. Auto-Update Flow

```text
app start
  -> check for update metadata
  -> compare version
  -> notify user if newer build exists
  -> background download
  -> verify package
  -> prompt for restart to install
```

### 7.1 Update Requirements

- GitHub Releases publishing
- versioned release tags
- generated `latest.yml`
- strong verification before install

### 7.2 Recommended UI States

- checking for updates
- update available
- downloading update
- ready to restart
- update failed

---

## 8. Portable Mode

Portable mode is useful for controlled environments, demos, and users who prefer self-contained directories.

### 8.1 Trigger

- `portable.flag` file located alongside the executable

### 8.2 Behaviour

- store app data relative to the executable directory
- keep logs, DB, and cache in a local `data/` path
- still rely on Windows user-context encryption for secrets

### 8.3 Constraints

Portable mode changes file location, not trust boundaries. DPAPI still binds secrets to the Windows user profile that created them.

---

## 9. Windows-Specific Integrations

### 9.1 System Tray

Tray behaviour should support:

- show/hide main window
- current status summary
- start/stop monitoring
- quick access to settings
- quit application

### 9.2 Startup Integration

Optional startup entry under the current-user registry hive:

```text
HKCU\Software\Microsoft\Windows\CurrentVersion\Run
```

### 9.3 Power and Session Events

The main process should respond to:

- suspend/sleep
- resume
- network reconnect
- screen lock/unlock if relevant to wallet operations

Long-running scanners and price feeds should pause and recover intentionally rather than assuming continuity.

### 9.4 DPI and Multi-Monitor Support

The renderer should be tested at common Windows scale factors such as 100%, 125%, 150%, and 200%. Layouts must remain stable across monitor changes and high-DPI displays.

---

## 10. Security Model on Desktop

Recommended Electron hardening:

- `nodeIntegration: false`
- `contextIsolation: true`
- `sandbox: true`
- strict preload API surface
- blocked external navigation
- external URLs opened via system browser

The desktop shell exists to provide access to Windows-native capabilities, but it must preserve the same least-privilege boundary documented in `SECURITY.md`.

---

## 11. Packaging and Distribution Workflow

### 11.1 Release Pipeline

1. push tagged version
2. run CI build on Windows runner
3. install dependencies with clean lockfile
4. build renderer and main process
5. rebuild native modules
6. package NSIS installer
7. publish installer and update metadata to GitHub Releases

### 11.2 Release Artifacts

| Artifact | Purpose |
|---------|---------|
| `.exe` installer | primary installable package |
| `latest.yml` | update metadata for `electron-updater` |
| checksums | integrity verification |
| release notes | user-visible change log |

---

## 12. Code Signing and SmartScreen

### 12.1 Code Signing

Code signing is strongly recommended before wide production rollout. Without signing, Windows SmartScreen will present warning friction to users.

### 12.2 Recommended Path

- early internal builds may remain unsigned
- public beta should move to standard code signing
- broad public release benefits from stronger certificate reputation and cleaner install UX

### 12.3 SmartScreen Guidance

Documentation should explain what users will see when unsigned builds are used, and how to verify the official release source.

---

## 13. Performance Budgets

| Metric | Target |
|--------|--------|
| Cold start | < 3 seconds |
| Warm start | < 1 second |
| Idle memory | < 200 MB |
| Active memory | < 500 MB |
| Installer size | < 150 MB |
| Installed size | < 400 MB |

### 13.1 Optimisation Priorities

- lazy-load heavy renderer routes
- use worker threads for CPU-heavy background tasks
- minimise renderer polling in favour of event-driven updates
- index hot database paths
- aggressively cache static reference data

---

## 14. Testing Expectations for Desktop Packaging

Desktop-specific validation should cover:

- fresh install
- upgrade install
- uninstall and data retention behaviour
- tray behaviour
- startup registration
- auto-update success and rollback handling
- high-DPI layout stability
- packaged build security flags

---

## 15. Distribution Recommendations

- Publish stable builds through GitHub Releases first.
- Keep beta and stable channels separate if auto-update is enabled for both.
- Document Windows prerequisites clearly, even if minimal.
- Prefer one predictable installer path over multiple packaging formats in early releases.

---

The Windows desktop architecture is central to the project’s usability. It should feel like a self-contained trading workstation, not a wrapped web page.
