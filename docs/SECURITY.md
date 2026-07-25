# APEX Security Architecture

> **Version:** 2.0.0 | **Last Updated:** July 25, 2026

---

## 1. Overview

APEX handles: AI API keys, wallet private keys, trade execution authority.
Security is first-class at every layer.

---

## 2. Threat Model

**Assets:** API keys, private keys, strategy params, portfolio data, app integrity
**Actors:** Malware, network attackers, rogue endpoints, physical access, supply chain
**Vectors:** Key extraction, API interception, renderer XSS, dependency compromise, memory dump

---

## 3. API Key Security

### Storage
- Electron safeStorage (DPAPI on Windows) | SQLite BLOB encrypted
- NEVER plaintext on disk | NEVER in localStorage/cookies | NEVER in logs | NEVER in diagnostics

### In-Memory
- Decrypted only for API call | Minimum duration | Zeroed after (Buffer.fill(0)) | Not in renderer

### Transmission
- ONLY to configured base_url | HTTPS (TLS 1.2+) | HTTP rejected
- In Authorization/x-api-key header | NEVER in URL params or body

### User Controls
- Show/hide toggle | Reset (delete) | Reset All | Immediate, irreversible

---

## 4. Wallet Private Key Security

- Encrypted with user passphrase (argon2id) + safeStorage layer
- Decrypted only for signing | Main process only | Zeroed after
- Use dedicated trading wallets | Hardware wallet planned

---

## 5. Electron Hardening

- nodeIntegration: false | contextIsolation: true | sandbox: true | webSecurity: true
- No remote module | No eval() | CSP enforced
- IPC via contextBridge only | Handlers validate inputs | Channels whitelisted
- will-navigate blocked | new-window blocked | External links in browser

---

## 6. Network Security

- HTTPS/WSS only | Cert validation | No telemetry by default | Auto-update HTTPS + signature

---

## 7. Data Privacy

- All local | No cloud trade storage | Prompts to configured providers only
- Prompts NEVER contain keys | User can clear all data | Uninstall removes data

---

## 8. Dependency Security

- npm audit in CI | Dependabot | Lock file enforced | Electron updated <2 weeks | No dev deps in prod

---

## 9. Logging

**Logged:** Startup/shutdown, API metadata, trade events, errors
**NEVER Logged:** API keys, private keys, full prompts, full responses
**Storage:** Daily rotation, 7 days max, 50MB max, user can export/clear

---

## 10. Release Checklist

- [ ] npm audit clean | [ ] Electron latest | [ ] CSP tested | [ ] nodeIntegration off
- [ ] No keys in source | [ ] HTTPS enforced | [ ] safeStorage used | [ ] IPC validated
- [ ] Navigation blocked | [ ] Code signed | [ ] Logs clean

---

*Security is a requirement, not a feature. When in doubt, choose more secure.*
