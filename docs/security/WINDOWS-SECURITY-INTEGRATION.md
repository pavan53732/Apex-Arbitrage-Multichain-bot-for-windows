---
type: CONTRACT
owner: Windows Team
status: Canonical
version: 1.0.0
purpose: Defines how Windows-specific security features protect credentials, signing, sandboxing, supply chain security, and IPC hardening — with DPAPI, Credential Manager, SmartScreen, AppContainer, Defender, code signing, and secure update chain contracts.
scope: None
last_updated: 2026-07-29
canonical_source: docs/security/WINDOWS-SECURITY-INTEGRATION.md
---

# Windows Security Integration

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-27 | **Owner:** Windows Team

## Purpose
Defines how Windows-specific security features protect credentials, signing, sandboxing, supply chain security, and IPC hardening — with DPAPI, Credential Manager, SmartScreen, AppContainer, Defender, code signing, and secure update chain contracts.

---

## 1. Secret Storage on Windows

### 1.1 Storage Methods

| Secret Type | Storage Method | API | Encryption | Recovery |
|-------------|-------------|-----|------------|----------|
| **Wallet private keys** | Windows Credential Manager | `CredWrite` / `CredRead` | DPAPI (user-level) | Re-authenticate on loss |
| **Exchange API keys** | Windows Credential Manager | `CredWrite` / `CredRead` | DPAPI (user-level) | Re-enter on loss |
| **AI provider API keys** | DPAPI-encrypted file | `CryptProtectData` / `CryptUnprotectData` | DPAPI (user-level) | Re-enter on loss |
| **Database credentials** | DPAPI-encrypted file | `CryptProtectData` / `CryptUnprotectData` | DPAPI (user-level) | Re-enter on loss |
| **Session tokens** | In-memory only | — | Process isolation | None (ephemeral) |
| **Config secrets** | DPAPI-encrypted config section | `CryptProtectData` | DPAPI (user-level) | Re-enter on loss |

### 1.2 DPAPI Behavior

| Scenario | Behavior |
|---------|----------|
| **User logged in** | DPAPI uses user's login credentials for encryption |
| **User not logged in** | DPAPI cannot decrypt — secrets inaccessible |
| **Sleep/hibernation** | Secrets zeroed before sleep; DPAPI key not accessible during sleep |
| **Different user account** | DPAPI cannot decrypt (user-bound encryption) |
| **System restore** | DPAPI master key may be invalid → secrets must be re-entered |

---

## 2. SmartScreen & Code Signing

### 2.1 Code Signing Contract

| Component | Signing Method | Certificate Type | SmartScreen Impact |
|-----------|-------------|------------------------------------|
| **Installer (MSIX)** | Authenticode | EV certificate | No SmartScreen warning |
| **Installer (NSIS)** | Authenticode | EV certificate | No SmartScreen warning |
| **Main executable** | Authenticode | Standard certificate | No warning (signed) |
| **Backend executable** | Authenticode | Standard certificate | No warning (signed) |
| **Portable ZIP** | SHA-256 checksum only | No certificate | Manual verification |
| **Update packages** | Authenticode + SHA-256 | Standard certificate | No warning (signed + verified) |

### 2.2 SmartScreen Bypass Rules

- EV-signed installers: immediate SmartScreen bypass (established reputation).
- Standard-signed installers: SmartScreen warns until reputation established (100+ downloads).
- Unsigned: SmartScreen blocks (user must manually override).
- Portable ZIP: no SmartScreen (ZIP files not scanned).

### 2.3 Update Chain Security

```
1. Update manifest signed with Authenticode + SHA-256.
2. Downloaded update package verified against manifest checksum.
3. Signature chain validated (root → intermediate → leaf → manifest).
4. If any step fails → update rejected, operator notified.
5. Update applied only after full verification.
6. On update failure → rollback to previous version (previous version also verified).
```

---

## 3. AppContainer Sandbox

### 3.1 Plugin Sandbox via AppContainer

| Capability | Allowed | Enforcement |
|------------|---------|-------------|
| **Network access** | No | AppContainer blocks all network calls |
| **File system access** | Plugin data directory only | AppContainer restricts to virtualized path |
| **Registry access** | No | AppContainer blocks |
| **IPC access** | Single plugin channel only | IPC bridge restricts |
| **Process creation** | No | AppContainer blocks |
| **Clipboard access** | No | AppContainer blocks |
| **Camera/Microphone** | No | AppContainer blocks |
| **GPU acceleration** | No (software rendering only) | AppContainer restricts |

### 3.2 AppContainer Creation

```
1. Create AppContainer profile with unique SID.
2. Grant capabilities: plugin data directory + IPC channel.
3. Launch plugin process in AppContainer context.
4. Monitor resource usage (CPU, memory, handles).
5. On violation → terminate process + emit plugin.violation event.
6. On process exit → clean up AppContainer profile.
```

---

## 4. IPC Hardening

### 4.1 IPC Security Rules

| Rule | Implementation | Enforcement |
|------|---------------|-------------|
| **Authentication** | Process identity verification (PID + signature) | IPC bridge validates before accepting message |
| **Schema validation** | All messages must conform to typed schema | IPC bridge rejects invalid messages |
| **Permission check** | Message action must match sender's role | IPC bridge checks permission matrix |
| **Rate limiting** | Max messages per second per channel | IPC bridge enforces |
| **Encryption** | Named pipe encrypted (Windows ACL) | OS-level enforcement |
| **Isolation** | Plugin processes on separate named pipe | OS-level ACL |

### 4.2 IPC Threat Mitigations

| Threat | Mitigation |
|--------|------------|
| **Process injection** | Validate sender PID + binary signature before accepting IPC message |
| **Message tampering** | Schema validation + checksum on each message |
| **Man-in-the-middle** | Named pipe ACL restricts to authorized processes only |
| **Flooding** | Rate limiting per channel |
| **Privilege escalation** | Permission matrix enforced per message; no sudo-equivalent actions |
| **DLL injection** | Code signing verified at startup; AppContainer for plugins |

---

## 5. Supply Chain Security

### 5.1 Dependency Verification

| Check | Implementation | Config Key |
|-------|---------------|------------|
| **NPM audit** | Run `npm audit` on every build | `build.security.npm_audit: true` |
| **Lockfile verification** | Verify `package-lock.json` integrity hash | `build.security.lockfile_verify: true` |
| **Binary integrity** | Verify all binary dependencies via SHA-256 | `build.security.binary_integrity: true` |
| **License compliance** | Scan for restricted licenses | `build.security.license_scan: true` |
| **Known vulnerabilities** | Snyk/OSV scan before release | `build.security.vulnerability_scan: true` |

### 5.2 Release Security Checklist

```
1. All dependencies audited (npm audit — 0 critical/high).
2. Lockfile integrity verified.
3. All binaries integrity-checked (SHA-256).
4. No restricted licenses.
5. Vulnerability scan passed.
6. Code signing completed (Authenticode).
7. SmartScreen reputation established.
8. Update manifest signed.
9. Release tagged and published.
```

---

## 6. Cross-Subsystem Integration

| Caller | Purpose | Contract |
|--------|---------|----------|
| Plugin Manager | Create AppContainer sandbox | `plugin.sandbox.create` API |
| Config Manager | Get/set DPAPI-encrypted secrets | `secret.get` / `secret.set` APIs |
| Windows App Architecture | Sleep/resume → zero/restore secrets | `system.power.suspend` / `system.power.resume` |
| Update Manager | Verify update signature | `update.verify` API |
| Installer | Register Defender exclusions | `windows.defender.exclusion` API |

| Config Key | Default | Description |
|-----------|---------|-------------|
| `security.secret.storage_backend` | `windows_credential_manager` | Secret storage method |
| `build.signing.enabled` | `true` | Authenticode signing |
| `windows.defender.exclusion_enabled` | `false` | Defender exclusion registration |
| `plugin.sandbox.isolation` | `appcontainer` | Plugin sandbox type |
| `build.security.npm_audit` | `true` | NPM audit on build |

---

## Cross-References

- **SECURITY.md** — Platform security baseline.
- **SECURITY-CONTRACTS.md** — Security contracts and policies.
- **SECRET-LIFECYCLE.md** — Secret lifecycle and rotation.
- **PERMISSION-MODEL.md** — Permission enforcement.
- **TRUST-BOUNDARIES.md** — Trust domain enforcement.
- **PLUGIN-SANDBOX-CONTRACT.md** — Plugin sandbox isolation.
- **CODE-SIGNING.md** — Authenticode signing detail.
- **IPC-PROTOCOL.md** — IPC security protocol.
- **WINDOWS-DEPLOYMENT.md** — Installer and signing.
- **WINDOWS-APP-ARCHITECTURE.md** — Process model and power events.
- **CONFIGURATION-REFERENCE.md** — Security config keys.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-27 | Production-grade Windows security integration: 6 secret storage methods with DPAPI behavior (5 scenarios), code signing contract (6 components), SmartScreen bypass rules, update chain security (6-step verification), AppContainer sandbox (8 capabilities), IPC hardening (6 rules + 6 threat mitigations), supply chain security (5 verification checks + release checklist), cross-subsystem integration | Windows Team |
| 0.1.0 | 2026-07-27 | Initial stub | Windows Team |
