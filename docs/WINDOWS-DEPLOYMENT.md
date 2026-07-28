---
type: CONTRACT
owner: Windows Team
status: Canonical
version: 1.0.0
purpose: Defines how the Windows desktop trading app is packaged, signed, installed, updated, and rolled back — installer lifecycle, update lifecycle, code signing, rollback rules, and cross-subsystem integration.
scope: None
last_updated: 2026-07-29
canonical_source: docs/WINDOWS-DEPLOYMENT.md
---

# Windows Deployment

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-27 | **Owner:** Windows Team

## Purpose
Defines how the Windows desktop trading app is packaged, signed, installed, updated, and rolled back — installer lifecycle, update lifecycle, code signing, rollback rules, and cross-subsystem integration.

---

## 1. Package Formats

| Format | Description | Auto-Update | Install Path | Uninstall | Portable |
|--------|-------------|-------------|-------------|----------|----------|
| **MSIX** | Windows App Package (preferred) | Yes (via AppInstaller) | `%ProgramFiles%\Apex\` | Settings → Apps | No |
| **NSIS** | Nullsoft Installer (traditional) | Yes (via update service) | `%ProgramFiles%\Apex\` | Programs → Uninstall | No |
| **Portable ZIP** | Self-contained zip | No (manual) | Any directory | Delete folder | Yes |

### 1.1 MSIX Advantages
- Automatic updates via Windows AppInstaller.
- Clean uninstall (no leftover files/registry).
- Containerized file system (user data separated).
- Windows Store distribution (optional).

### 1.2 NSIS Advantages
- More flexible install options (custom path, components).
- Compatible with older Windows versions.
- No containerization overhead.

### 1.3 Portable ZIP Advantages
- No installation required.
- Run from USB drive.
- Zero registry footprint.

---

## 2. Installer Lifecycle

### 2.1 Installation Steps

| Step | Action | Rollback on Failure |
|------|--------|---------------------|
| **1. Pre-check** | Verify Windows version, disk space, dependencies | Cancel (no changes made) |
| **2. License** | Show license agreement, user must accept | Cancel |
| **3. Path selection** | Choose install directory (default: `%ProgramFiles%\Apex\`) | Cancel |
| **4. Component selection** | Choose components (core, AI, plugins, dev tools) | Cancel |
| **5. Create directories** | Create install + data directories | Delete created directories |
| **6. Copy files** | Copy application files to install directory | Delete copied files |
| **7. Code signing verify** | Verify Authenticode signature on all binaries | Alert user, offer to continue |
| **8. Register service** | Register Windows service (if service mode selected) | Unregister service |
| **9. Register auto-start** | Add to Windows Run key (if auto-start selected) | Remove Run key |
| **10. Register Defender** | Add app directory to Defender exclusion list (optional) | Remove exclusion |
| **11. Create shortcuts** | Desktop + Start Menu shortcuts | Delete shortcuts |
| **12. Write uninstaller** | Create uninstaller registry entry | Delete registry entry |
| **13. First-run** | Launch app → first-run wizard | — |

### 2.2 Installer Rollback

- On any step failure: rollback all previous steps in reverse order.
- Rollback is automatic (no user intervention needed).
- Partial installations are fully cleaned up.

---

## 3. Update Lifecycle

### 3.1 Update Detection

| Method | Description | Frequency |
|--------|-------------|-----------|
| **AppInstaller (MSIX)** | Windows checks for update manifest | Every 24h or on app launch |
| **Update service (NSIS)** | Background service checks update endpoint | Every 4h or on app launch |
| **Manual check** | User clicks "Check for updates" | On demand |

### 3.2 Update Process

```
1. New version detected (manifest version > current version).
2. Download update package to temp directory.
3. Verify update package:
   a. Authenticode signature valid.
   b. SHA-256 checksum matches manifest.
   c. Version matches manifest version.
4. If verification fails → reject update, notify operator.
5. If verification passes:
   a. Pause trading (existing trades complete).
   b. Save workspace state.
   c. Create rollback snapshot (copy current version to backup directory).
   d. Apply update (MSIX: Windows handles; NSIS: run update installer).
   e. Restart app.
   f. Verify new version starts successfully.
   g. If success → delete rollback snapshot after `update.rollback_retention_ms` (default 7 days).
   h. If failure → rollback to previous version.
```

### 3.3 Update Failure Rollback

```
1. New version fails to start (crash on startup, health check failure).
2. Rollback initiated:
   a. Restore previous version from rollback snapshot.
   b. Restore workspace state.
   c. Restart app with previous version.
   d. Verify rollback successful.
   e. Notify operator with failure details.
3. Rollback timeout: `update.rollback_timeout_ms` (default 30000ms).
4. If rollback also fails → operator must manually reinstall.
```

---

## 4. Code Signing

See **WINDOWS-SECURITY-INTEGRATION.md §2** for full code signing contract. This document defines the signing process:

| Step | Action | Verification |
|------|--------|-------------|
| **1. Build** | Compile all binaries | — |
| **2. Sign binaries** | Authenticode sign all executables + DLLs | `signtool verify /pa` |
| **3. Sign installer** | Authenticode sign MSIX/NSIS installer | `signtool verify /pa` |
| **4. Sign update manifest** | Sign manifest.json with SHA-256 + certificate | Custom verification |
| **5. Create checksums** | SHA-256 checksums for all files | Verify checksums |
| **6. Package** | Create MSIX/NSIS/ZIP package | — |
| **7. Verify** | Run full verification on packaged product | All steps pass |

---

## 5. Uninstallation

| Step | Action |
|------|--------|
| **1. Confirm** | Ask user for confirmation |
| **2. Stop service** | Stop Windows service if running |
| **3. Close app** | Terminate all app processes |
| **4. Unregister** | Remove service, auto-start, Defender exclusions |
| **5. Delete files** | Delete install directory (keep `%APPDATA%/apex/` for user data option) |
| **6. Clean registry** | Remove all registry entries |
| **7. Delete shortcuts** | Remove desktop + Start Menu shortcuts |
| **8. User data option** | Ask: "Keep user data?" → Yes: preserve `%APPDATA%/apex/`, No: delete |

---

## 6. Cross-Subsystem Integration

| Caller | Purpose | Contract |
|--------|---------|----------|
| Update Manager | Check/download/apply updates | `update.check` / `update.apply` APIs |
| Windows Service Integration | Install/uninstall service during install/uninstall | `service.install` / `service.uninstall` |
| Config Manager | Preserve config across updates | `%APPDATA%/apex/config/` not deleted |
| Workspace Manager | Preserve workspaces across updates | `%APPDATA%/apex/workspaces/` not deleted |
| Security Manager | Verify update signatures | `update.verify.signature` API |
| Health Checker | Verify new version health after update | `health.check.all` API |

| Config Key | Default | Description |
|-----------|---------|-------------|
| `update.check_interval_ms` | `14400000` | Update check interval (4h) |
| `update.auto_install` | `true` | Automatic update installation |
| `update.rollback_retention_ms` | `604800000` | Rollback snapshot retention (7 days) |
| `update.rollback_timeout_ms` | `30000` | Rollback timeout |
| `build.signing.enabled` | `true` | Code signing enabled |
| `windows.uninstall.keep_user_data` | `true` | Preserve user data on uninstall |

---

## Cross-References

- **DEPLOYMENT.md** — Platform deployment overview.
- **BUILD-RELEASE-CICD.md** — CI/CD pipeline for building and signing.
- **UPDATE-MANAGER.md** — Update checking and application logic.
- **WINDOWS-APP-ARCHITECTURE.md** — Process model and startup.
- **WINDOWS-SERVICE-INTEGRATION.md** — Service install/uninstall.
- **WINDOWS-SECURITY-INTEGRATION.md** — Code signing and verification.
- **SECURITY-CONTRACTS.md** — Security contracts.
- **CODE-SIGNING.md** — Code signing detail.
- **CONFIGURATION-REFERENCE.md** — Update and deployment config keys.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-27 | Production-grade Windows deployment: 3 package formats with pros/cons, 13-step installer lifecycle with rollback per step, update process (8 steps with verification), update failure rollback (4 steps), code signing process (7 steps), 8-step uninstallation, cross-subsystem integration | Windows Team |
| 0.1.0 | 2026-07-27 | Initial stub | Windows Team |
