# APEX Windows Desktop Application - Packaging and Distribution

> **Version:** 2.0.0 | **Target:** Windows 10/11 x64 | **No Docker. No WSL.**

---

## 1. Overview

Native Windows .exe via Electron. Bundles Node.js plus Chromium. All backend in
Electron main process. No external dependencies.

User flow: Download .exe -> Install (no admin) -> Launch -> Configure AI -> Trade

---

## 2. Stack

Electron 31+ | electron-builder 24+ | NSIS installer | electron-updater
React 18 + TypeScript + Vite | Tailwind + shadcn/ui | Zustand | better-sqlite3 | safeStorage

---

## 3. Structure

    packages/desktop/
      electron/ (main.ts, preload.ts, ipc-handlers.ts, tray.ts, updater.ts, safe-storage.ts, window-manager.ts)
      src/ (App.tsx, pages/, components/, stores/, hooks/, lib/)
      electron-builder.yml, vite.config.ts, package.json

---

## 4. Main Process

- BrowserWindow management, backend services hosting, IPC, tray, auto-update
- safeStorage encryption, SQLite init, Windows events (sleep/resume/network)
- Window: 1400x900 default, 1024x680 min, frameless custom title bar
- Security: nodeIntegration false, contextIsolation true, sandbox true

### IPC Bridge
window.minimize/maximize/close | ai.getProviders/saveProvider/deleteProvider/testConnection/resetProvider/resetAll/clearCache
trades.getHistory/getActive | skills.getAll/toggle/configure | agents.getAll/toggle/getLogs
app.getVersion/checkUpdate/installUpdate | settings.get/set

---

## 5. System Tray

APEX icon | Menu: Show/Hide, Status, Active Trades, P&L, Start/Stop, Settings, Quit
Double-click: toggle | Close: minimize to tray | Quit: tray menu or Ctrl+Q

---

## 6. Auto-Update

Start check + every 4h + manual | Toast notification | Background download | Restart to install
Provider: GitHub Releases (pavan53732/Apex-Arbitrage-Multichain-bot-for-windows)

---

## 7. electron-builder

appId: com.apex.arbitrage | NSIS | per-user (no admin) | Desktop+StartMenu shortcuts | publish: github

---

## 8. Windows Features

- DPI: 100/125/150/200 percent tested | Firewall: outbound HTTPS only
- Startup: optional HKCU registry | Power: pause on sleep, resume on wake
- Portable: portable.flag file -> data in app dir

---

## 9. Performance

Startup <3s | Idle <200MB | Active <500MB | 60fps | Installer <150MB | Installed <400MB

---

## 10. Build/Release

Tag v* -> GitHub Actions -> Node 20 -> npm ci -> build -> electron-rebuild -> electron-builder --win -> Upload .exe + latest.yml

---

*No Docker, no containers, no WSL. Pure Windows native via Electron.*
