# APEX Deployment & Release Guide

> **Version:** 3.0.0 | **Last Updated:** July 25, 2026
> **Scope:** Building, packaging, releasing, and distributing APEX desktop builds.

---

## 1. Overview

APEX is distributed as a single Windows `.exe` installer (NSIS, per-user, no
admin). Releases are published to **GitHub Releases**; users are notified via
in-app auto-update (electron-updater). No Docker, no server, no app store.

---

## 2. Build Matrix

| Target | OS | Arch | Format |
|--------|----|----|--------|
| `win-x64` | Windows 10/11 | x64 | NSIS installer (.exe) |
| `win-x64-portable` | Windows 10/11 | x64 | Portable .zip (planned v3.1) |
| `win-arm64` | Windows 11 | arm64 | Planned v3.1 |

macOS and Linux are **not** targets in v3. The codebase is mostly
cross-platform (Electron + Node + TS), so a Mac build is feasible; demand
will drive the decision.

---

## 3. Prerequisites (for build machine)

- **OS:** Windows 10/11 or Windows Server 2019+
- **Node.js:** 20 LTS
- **npm:** 10+
- **Python:** 3.10+ (for `node-gyp` during `electron-rebuild`)
- **Visual Studio Build Tools:** 2022 with C++ workload
- **Disk:** 10GB free
- **RAM:** 8GB+ recommended
- **Time:** ~10 minutes for a clean build

---

## 4. Local Build

```bash
# Clone
git clone https://github.com/pavan53732/Apex-Arbitrage-Multichain-bot-for-windows.git
cd Apex-Arbitrage-Multichain-bot-for-windows

# Install
npm ci

# Dev mode (hot reload)
npm run dev

# Production build (Windows only)
npm run build:win
# → produces:
#   release/APEX-Setup-3.0.0.exe           (NSIS installer)
#   release/APEX-Setup-3.0.0.exe.blockmap  (for delta updates)
#   release/latest.yml                      (auto-update manifest)
```

### 4.1 What `build:win` Does
1. `npm ci` (already done)
2. `vite build` — bundles the renderer
3. `tsc -p tsconfig.main.json` — compiles the main process
4. `electron-rebuild` — rebuilds `better-sqlite3` against Electron's Node ABI
5. `electron-builder --win nsis --x64` — packages + signs (when cert available)

### 4.2 Environment Variables

| Var | Purpose | Example |
|-----|---------|---------|
| `CSC_LINK` | Path to code-signing cert (.pfx) | `./certs/apex.pfx` |
| `CSC_KEY_PASSWORD` | Cert password | (from secret) |
| `GH_TOKEN` | GitHub token for publishing releases | (from secret) |
| `APEX_VERSION` | Override version (else read from `package.json`) | `3.0.0` |

---

## 5. Code Signing

### 5.1 Current State (v3.0)
APEX is **not yet code-signed**. Windows SmartScreen will warn on first install.
Users see "More info → Run anyway". This is documented in `USER-GUIDE.md`.

### 5.2 Roadmap (v3.1)
- Purchase an Authenticode certificate (e.g. from Sectigo, DigiCert)
- Store the `.pfx` in GitHub Actions secrets
- Sign the `.exe` and the NSIS installer during `electron-builder`
- Submit the cert to Microsoft's SmartScreen reputation program
- SmartScreen warnings disappear once reputation builds

### 5.3 Signing Config
`electron-builder.yml`:
```yaml
win:
  target: nsis
  certificateFile: ${env.CSC_LINK}
  certificatePassword: ${env.CSC_KEY_PASSWORD}
  signingHashAlgorithms: ['sha256']
  publisherName: 'APEX'
```

---

## 6. Auto-Update (electron-updater)

### 6.1 How It Works
- On startup + every 4 hours, APEX fetches `latest.yml` from the GitHub Releases
- If the version is newer, it shows a toast
- User can defer; APEX downloads in the background
- "Restart to Install" replaces the running app, preserving user data

### 6.2 Publishing
electron-builder auto-publishes when given a `GH_TOKEN`:
```bash
GH_TOKEN=<token> npm run build:win -- --publish always
```
This creates a draft GitHub release, uploads `.exe` + `.blockmap` + `latest.yml`.

### 6.3 Delta Updates
electron-builder generates `.blockmap` files enabling **differential updates**:
- A user on v3.0.0 updating to v3.0.1 downloads only the diff (~5MB instead of ~150MB)
- Enabled automatically when `electronUpdater.autoDownload = true`

### 6.4 Channels
- `latest` — stable releases
- `beta` — pre-releases (tagged with `-beta.N`)
- `alpha` — internal builds (tagged with `-alpha.N`)

Users opt into channels in **Settings → General → Update Channel**.

---

## 7. GitHub Actions CI/CD

### 7.1 Workflow: `.github/workflows/release.yml`

Triggered on tag matching `v*`:
```yaml
name: Release
on:
  push:
    tags: ['v*']
jobs:
  build:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm ci
      - run: npm run build:win
        env:
          CSC_LINK: ${{ secrets.CSC_LINK }}
          CSC_KEY_PASSWORD: ${{ secrets.CSC_KEY_PASSWORD }}
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      - uses: softprops/action-gh-release@v2
        with:
          files: |
            release/APEX-Setup-*.exe
            release/latest.yml
            release/*.blockmap
```

### 7.2 Workflow: `.github/workflows/ci.yml`

Triggered on every PR:
- `npm ci`
- `npm run lint`
- `npm run typecheck`
- `npm run test`
- `npm run build:renderer` (sanity)

### 7.3 Secrets Required
- `CSC_LINK` (base64 of `.pfx`)
- `CSC_KEY_PASSWORD`
- `GITHUB_TOKEN` (auto-provided by Actions)

---

## 8. Installer (NSIS) Details

### 8.1 Configuration
`electron-builder.yml`:
```yaml
nsis:
  oneClick: false                  # show install options
  perMachine: false                # per-user install
  allowToChangeInstallationDirectory: true
  createDesktopShortcut: true
  createStartMenuShortcut: true
  shortcutName: APEX
  artifactName: APEX-Setup-${version}.${ext}
  deleteAppDataOnUninstall: false  # user chooses via checkbox
```

### 8.2 Install Behavior
- Per-user install (no admin required)
- Default location: `%LOCALAPPDATA%\Programs\APEX\`
- Optional data wipe on uninstall (user checkbox in uninstaller)
- Desktop + Start Menu shortcuts

### 8.3 Uninstaller
- Standard "Apps & Features" uninstall
- Optional checkbox: "Also remove all APEX data" — wipes `%APPDATA%\APEX\`
- Default: keep data (preserves API keys, settings, trade history)

---

## 9. Portable Mode

A user can run APEX without installing:
1. Download the portable archive (planned v3.1)
2. Extract to any folder
3. (Optional) Create `portable.flag` in the same folder
4. Run `APEX.exe`

With `portable.flag`:
- All data stays in the app folder (no `%APPDATA%`)
- Settings, keys, logs, DB all in `./data/`
- User can copy the folder to another machine (with keys re-added)

---

## 10. Data Migration (between versions)

### 10.1 Within v3.x
- Auto-migration on first launch
- Each migration is reversible (backup → migrate → on failure, restore)
- Migrations are tested against a copy of prod data

### 10.2 Across Major Versions
- v3 → v4: in-app "Migration Wizard" guides the user
- Settings are migrated; data is re-indexed; old DB backed up to `%APPDATA%\APEX\backups\`

---

## 11. Telemetry & Privacy

APEX ships with **zero telemetry** by default. What leaves the machine:
- AI calls to providers you configured (you chose these)
- Auto-update checks to GitHub (can be disabled)
- Crash reports: **opt-in only** (Settings → Privacy → Send crash reports)

What never leaves:
- API keys, private keys
- Trade history, portfolio
- User prompts, AI responses (in full)
- Settings, configurations

See `SECURITY.md` for the full threat model.

---

## 12. Release Checklist (Pre-Release)

- [ ] All tests pass on CI
- [ ] `npm audit` shows no high/critical vulns
- [ ] Electron version is latest stable
- [ ] `package.json` version bumped
- [ ] `CHANGELOG.md` updated for the release
- [ ] `docs/` version headers updated
- [ ] Local build runs without errors
- [ ] Installer installs and launches cleanly on a clean Windows VM
- [ ] First-run wizard works
- [ ] AI connection test works
- [ ] At least one skill runs end-to-end
- [ ] Auto-update from previous version works
- [ ] Logs contain no API keys
- [ ] Code signed (when cert available)

---

## 13. Rollback

If a release is broken:
1. Mark the GitHub release as "Pre-release" (auto-update will skip it)
2. Publish a hotfix (e.g. v3.0.1)
3. Users get the hotfix via auto-update

If the hotfix can't ship in time:
1. Re-publish the last known good release as `latest`
2. Investigate root cause; ship fix

---

## 14. Distribution Beyond GitHub Releases

Not in v3, but planned:
- **Microsoft Store** (requires MSIX, separate build)
- **Direct download** from a custom site
- **Auto-update from S3/B2** (alternative feed)

For now: **GitHub Releases only**.

---

*Ship small, ship often, ship safely.*
