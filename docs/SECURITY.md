# APEX Security Architecture

> **Version:** 3.0.0 | **Last Updated:** July 25, 2026 | **Scope:** Windows Desktop, AI Pipeline, Blockchain Execution

---

## 1. Security Philosophy

APEX handles three classes of high-impact assets: AI provider API keys, wallet private keys, and live trade execution authority. A compromise of any one of them can directly produce unrecoverable financial loss.

The security model follows four core principles:

- **Defence in depth** — no single control protects a critical secret.
- **Least privilege** — the renderer never gains direct secret access.
- **Fail closed** — ambiguous or unsafe states halt privileged actions.
- **Auditability** — every security-relevant action is observable without exposing the secret itself.

---

## 2. Threat Model

### 2.1 Protected Assets

| Asset | Sensitivity | Risk if Compromised |
|-------|-------------|---------------------|
| AI provider API keys | High | Billing abuse, quota exhaustion, provider account suspension |
| Wallet private keys | Critical | Direct theft of all accessible funds |
| Session unlock passphrase | Critical | Decryption path to locally stored wallet material |
| Strategy parameters | Medium | Alpha leakage, front-running exposure, degraded profitability |
| Trade history and portfolio data | Medium | Privacy breach, operational intelligence leakage |
| Application binary integrity | High | Malicious code execution, silent credential exfiltration |

### 2.2 Threat Actors

| Actor | Capability | Primary Objective |
|------|------------|-------------------|
| Local malware | Read files, inspect memory, keylog | Extract credentials or hijack execution |
| Network attacker | Intercept or tamper with traffic | Capture secrets or alter provider responses |
| Rogue provider endpoint | Return manipulated responses | Prompt exfiltration, bad routing, denial of service |
| Physical-access attacker | Boot alternate OS, inspect disk | Offline credential extraction |
| Supply chain attacker | Dependency or build compromise | Backdoor the application |
| Renderer compromise/XSS | Script execution in UI | Escalate into privileged IPC actions |

### 2.3 Attack Vectors and Controls

| Vector | Example | Primary Mitigations |
|--------|---------|---------------------|
| Secret at-rest extraction | Reading SQLite/config files | DPAPI via `safeStorage`, encrypted BLOB storage, no plaintext persistence |
| Secret in-memory extraction | Heap dump during signing | Minimum-lifetime decryption, buffer zeroing, main-process-only handling |
| Renderer → main escalation | Malicious DOM script calls secret IPC | `contextIsolation`, `sandbox`, strict preload surface, schema validation |
| Network interception | MITM on AI API call | HTTPS/TLS enforcement, certificate validation, no secret in URL |
| Build/dependency compromise | Poisoned package version | lockfile enforcement, audit in CI, minimal dependency policy |
| Prompt exfiltration | Rogue provider returns tool injection text | strict tool dispatch validation, provider scoping, no secret-in-prompt policy |

---

## 3. Authentication and Authorisation Model

### 3.1 Trust Boundaries

```text
Renderer (untrusted UI surface)
  -> contextBridge API
  -> validated IPC channels only
Main Process (trusted application core)
  -> secret access
  -> signing
  -> provider HTTP calls
  -> database writes
```

### 3.2 Role Separation

| Layer | Allowed | Forbidden |
|------|---------|-----------|
| Renderer | Display data, collect user input, request approved operations | Raw secret access, direct filesystem access, direct network authority for privileged actions |
| Preload | Narrow API exposure through `contextBridge` | Business logic, secret handling, arbitrary channel forwarding |
| Main process | Decrypt secrets, sign txs, perform provider calls, validate IPC input | Returning secrets to renderer, bypassing schema validation |

### 3.3 Authorisation Rules

- Secret reads occur only inside dedicated main-process services.
- Trade execution requires both strategy approval and risk-engine approval before wallet unlock/signing.
- Settings mutations are restricted to whitelisted keys and typed schemas.
- No IPC handler returns private keys, provider API keys, derived keys, or raw encrypted blobs.

---

## 4. Encryption Architecture

### 4.1 Layered Model

```text
API key:
  plaintext key
    -> safeStorage / DPAPI encrypt
    -> SQLite BLOB

Private key:
  plaintext key
    -> Argon2id(passphrase, salt) derive AES-256 key
    -> AES-256-GCM encrypt
    -> safeStorage / DPAPI wrap encrypted payload
    -> SQLite BLOB
```

### 4.2 Argon2id Parameters

| Parameter | Value | Purpose |
|----------|-------|---------|
| Algorithm | Argon2id | Balanced resistance to GPU and side-channel attacks |
| Memory cost | 64 MB | Raises brute-force cost materially |
| Iterations | 3 | Practical desktop latency with stronger derivation than single-pass KDFs |
| Parallelism | 1 | Predictable performance across Windows targets |
| Salt size | 16 bytes | Unique salt per stored key |
| Output length | 32 bytes | AES-256 key material |

### 4.3 AES-GCM Envelope Format

Stored inner private-key payload:

```text
[version:1][salt:16][iv:12][tag:16][ciphertext:n]
```

### 4.4 DPAPI / safeStorage Constraints

- Encrypted material is bound to the same Windows user context.
- A copied database is not directly usable on another machine or user account.
- Portable mode still inherits DPAPI binding; portability applies to files, not decryptability.

---

## 5. Credential Lifecycle

### 5.1 AI Provider API Keys

1. User enters provider configuration in AI Settings.
2. Main process validates `name`, `base_url`, `model`, and key format.
3. API key is encrypted with `safeStorage` and stored as a BLOB.
4. Key is decrypted only for outbound request construction.
5. Key material is dereferenced immediately after the request completes.
6. Deletion removes the row and invalidates future use locally.

### 5.2 Wallet Private Keys

1. User imports a dedicated trading key.
2. A random salt is generated.
3. Argon2id derives a wrapping key from the user passphrase.
4. Private key is encrypted with AES-256-GCM.
5. The encrypted payload is wrapped again with DPAPI via `safeStorage`.
6. Decryption happens only during signing and only in the main process.
7. Sensitive buffers are zeroed after use.

### 5.3 Rotation Policy

- Provider keys should be replaceable from the AI Settings page without editing files manually.
- Wallet rotation should create a new stored record and require re-confirmation of allowed chains/roles.
- Revoked or deleted credentials should never remain cached in plaintext memory longer than the active call/signing window.

---

## 6. Secure Storage Implementation

### 6.1 Storage Rules

- No secrets in `localStorage`, cookies, plaintext JSON, or logs.
- Secrets live only in encrypted SQLite BLOBs or transient process memory.
- The renderer never persists secret material independently.

### 6.2 Security-Relevant Tables

| Table | Sensitive Fields | Notes |
|------|------------------|------|
| `ai_providers` | `key_blob` | DPAPI-encrypted provider key |
| `wallets` | `outer_blob` | DPAPI-wrapped AES-GCM payload |
| `settings` | selective | no plaintext secret values |
| `logs` | none by policy | scrubbed metadata only |

### 6.3 What Must Never Be Stored

- User passphrases
- Plaintext private keys
- Plaintext provider keys
- Full prompt payloads containing high-risk operational context unless explicitly required and user-approved

---

## 7. IPC Security Model

### 7.1 IPC Principles

- All IPC is deny-by-default.
- Only documented channels are registered.
- Every input is validated before business logic runs.
- Every output is sanitised before returning to the renderer.

### 7.2 Representative Channel Catalogue

| Channel | Purpose | Secret Returned? |
|---------|---------|------------------|
| `ai.getProviders` | List configured providers | No |
| `ai.saveProvider` | Persist/update provider config | No |
| `ai.testConnection` | Validate provider endpoint and credentials | No |
| `wallet.importKey` | Store encrypted wallet material | No |
| `wallet.unlock` | Unlock for signing scope only | No |
| `trades.getHistory` | Query execution history | No |
| `skills.toggle` | Enable or disable a skill | No |
| `app.health` | Return runtime health snapshot | No |

### 7.3 Validation Pattern

```ts
const SaveProviderSchema = z.object({
  name: z.string().min(1).max(100),
  base_url: z.string().url(),
  api_key: z.string().min(1).max(500),
  model: z.string().min(1).max(200),
});
```

Validation failure must terminate the request immediately and return a typed error object.

### 7.4 Sender Restrictions

- IPC calls originate only from the trusted renderer window.
- Any future multi-window design must validate sender identity and partition channel access by window purpose.

---

## 8. Content Security Policy

Recommended baseline:

```text
default-src 'none';
script-src 'self';
style-src 'self' 'unsafe-inline';
img-src 'self' data:;
font-src 'self';
connect-src 'none';
worker-src 'self';
frame-src 'none';
object-src 'none';
base-uri 'none';
form-action 'none';
```

### 8.1 Rationale

| Directive | Reason |
|-----------|--------|
| `default-src 'none'` | Strong deny-by-default baseline |
| `script-src 'self'` | Only bundled scripts execute |
| `connect-src 'none'` | Renderer does not make privileged network calls |
| `frame-src 'none'` | Prevent iframe injection and clickjacking vectors |
| `object-src 'none'` | Remove plugin/object attack surface |

---

## 9. Electron Sandbox Configuration

Recommended `BrowserWindow` security flags:

```ts
webPreferences: {
  nodeIntegration: false,
  contextIsolation: true,
  sandbox: true,
  webSecurity: true,
  preload: join(__dirname, 'preload.js'),
}
```

Additional controls:

- block `will-navigate` except allowed app routes
- deny `new-window`
- open external links in the system browser
- disable remote module usage entirely

---

## 10. Secrets Management at Runtime

### 10.1 Access Pattern

- Decrypt as late as possible.
- Hold in memory for the shortest practical interval.
- Overwrite mutable buffers where feasible.
- Never attach secrets to thrown errors or structured logs.

### 10.2 Zeroing Pattern

```ts
let keyBuffer: Buffer | null = Buffer.from(secretHex, 'hex');
try {
  // use keyBuffer
} finally {
  if (keyBuffer) {
    keyBuffer.fill(0);
    keyBuffer = null;
  }
}
```

---

## 11. Network Security

### 11.1 AI Provider Traffic

- HTTPS required for external endpoints.
- Loopback HTTP is acceptable only for local self-hosted providers such as LM Studio or Ollama.
- Secrets must be sent in headers, never in query strings.

### 11.2 Blockchain RPC Traffic

- Signed transactions are broadcast; private keys are never transmitted to RPC providers.
- Unsafe HTTP RPC endpoints should be flagged prominently in the UI.

### 11.3 Auto-Update

- Release metadata and binaries must be fetched over HTTPS.
- Code signing is strongly recommended before broad distribution.
- Update verification must fail closed on signature/hash mismatch.

---

## 12. Data Privacy

- Trade data, cache, memory, and configuration remain local by default.
- No telemetry is enabled by default.
- AI prompt traffic is sent only to user-configured provider endpoints.
- Clear-data flows should wipe cache, logs, memory, and nonessential local records in one action.

---

## 13. Dependency Security

### 13.1 Policy

- `npm audit` runs in CI.
- Lockfile use is mandatory.
- New dependencies require justification in review.
- Native modules must be tracked carefully because they expand the attack surface.

### 13.2 Supply Chain Controls

- Dependabot or equivalent update automation
- release SBOM generation
- no development-only packages in production bundles
- fast Electron security updates after upstream advisories

---

## 14. Logging Security

### 14.1 Allowed Log Data

| Category | Allowed |
|---------|---------|
| Provider call metadata | provider id, model, latency, token counts, status |
| Trade lifecycle | trade id, chain, strategy, approval/rejection reason code |
| App lifecycle | startup, shutdown, migrations, update checks |
| Errors | sanitised messages and typed codes |

### 14.2 Forbidden Log Data

- API keys or fragments of them
- private keys or passphrases
- decrypted payloads
- full prompts if they may expose sensitive strategy context

---

## 15. Incident Response

### 15.1 Immediate Containment

1. Stop the application.
2. Revoke AI provider keys.
3. Move funds from affected wallets using a clean environment.
4. Isolate the machine if malware is suspected.

### 15.2 Investigation

- export scrubbed logs
- inspect provider usage dashboards
- inspect chain activity on explorers
- run malware scans and verify installed binaries

### 15.3 Recovery

- reinstall from a trusted release
- issue new provider keys
- rotate wallet credentials
- avoid restoring suspect encrypted databases without review

---

## 16. Security Best Practices for Contributors

- Never commit secrets.
- Never bypass Zod or equivalent runtime validation for IPC.
- Never expose new privileged methods through preload without documentation and tests.
- Prefer allowlists over blocklists.
- Treat all AI/provider output as untrusted input.
- Test with release-like Electron security flags enabled.

---

## 17. Release Security Checklist

- [ ] No secrets in source, logs, or build artifacts
- [ ] All BrowserWindows have `nodeIntegration: false`
- [ ] All BrowserWindows have `contextIsolation: true`
- [ ] All BrowserWindows have `sandbox: true`
- [ ] IPC surface matches documentation
- [ ] CSP verified in packaged build
- [ ] Update verification tested
- [ ] Dependency audit reviewed
- [ ] Critical secrets flow tested end-to-end

---

Security in APEX is a system property, not a single feature. Every new agent, skill, provider, and execution path must preserve the same trust boundaries defined here.
