# APEX IPC Protocol

> **Version:** 1.0.0 | **Last Updated:** July 25, 2026 | **Scope:** Preload API, Channels, Validation, Errors, Security

---

## 1. Overview

APEX uses Electron IPC to connect the sandboxed renderer to privileged main-process services. IPC is part of the security boundary, not just a transport mechanism, so every channel must be explicitly documented, validated, and tested.

---

## 2. Architecture

```text
Renderer UI
  -> window.apex.*
  -> preload.ts
  -> ipcRenderer.invoke/send
  -> ipcMain.handle/on
  -> main-process service layer
```

### 2.1 Design Rules

- preload exposes a narrow API surface only
- renderer never accesses raw `ipcRenderer` directly
- every invoke channel has typed request and response contracts
- every request is runtime-validated
- all privileged side effects happen after validation only

---

## 3. Preload Surface

Representative preload shape:

```ts
contextBridge.exposeInMainWorld('apex', {
  ai: {
    getProviders: () => ipcRenderer.invoke('ai.getProviders'),
    saveProvider: (payload) => ipcRenderer.invoke('ai.saveProvider', payload),
    testConnection: (payload) => ipcRenderer.invoke('ai.testConnection', payload),
  },
  trades: {
    getHistory: (payload) => ipcRenderer.invoke('trades.getHistory', payload),
  },
  app: {
    health: () => ipcRenderer.invoke('app.health'),
  }
});
```

The renderer should consume only this typed `window.apex` interface.

---

## 4. Channel Catalogue

### 4.1 AI Channels

| Channel | Request | Response |
|---------|---------|----------|
| `ai.getProviders` | none | provider summaries |
| `ai.saveProvider` | provider config payload | success/error |
| `ai.deleteProvider` | `{ id }` | success/error |
| `ai.testConnection` | `{ id }` or inline config | latency + compatibility result |
| `ai.resetProvider` | `{ id }` | success/error |
| `ai.resetAll` | none | success/error |
| `ai.clearCache` | optional namespace | success/error |

### 4.2 Wallet Channels

| Channel | Request | Response |
|---------|---------|----------|
| `wallet.getAll` | none | wallet summaries |
| `wallet.importKey` | encrypted-wallet input fields | success/error |
| `wallet.deleteWallet` | `{ id }` | success/error |
| `wallet.unlock` | `{ id, passphrase }` | scoped unlock or signing result |

### 4.3 Trade Channels

| Channel | Request | Response |
|---------|---------|----------|
| `trades.getHistory` | paging/filter payload | paginated trade rows |
| `trades.getActive` | none | active trades |
| `trades.getById` | `{ id }` | trade detail |

### 4.4 Skill Channels

| Channel | Request | Response |
|---------|---------|----------|
| `skills.getAll` | none | skill list |
| `skills.toggle` | `{ id, enabled }` | success/error |
| `skills.configure` | `{ id, config }` | success/error |

### 4.5 Agent Channels

| Channel | Request | Response |
|---------|---------|----------|
| `agents.getAll` | none | agent list |
| `agents.toggle` | `{ id, enabled }` | success/error |
| `agents.getLogs` | `{ id, limit }` | agent log entries |

### 4.6 App and Window Channels

| Channel | Request | Response |
|---------|---------|----------|
| `app.getVersion` | none | version string |
| `app.health` | none | health snapshot |
| `app.checkUpdate` | none | update status |
| `app.installUpdate` | none | success/error |
| `app.exportLogs` | options | export result |
| `settings.get` | `{ key }` | setting value |
| `settings.set` | `{ key, value }` | success/error |
| `window.minimize` | none | success |
| `window.maximize` | none | success |
| `window.close` | none | success |

---

## 5. Request/Response Contracts

### 5.1 Standard Response Envelope

```ts
interface IPCSuccess<T> {
  ok: true;
  data: T;
}

interface IPCFailure {
  ok: false;
  error: {
    code: string;
    message: string;
    details?: unknown;
  };
}

type IPCResponse<T> = IPCSuccess<T> | IPCFailure;
```

### 5.2 Example Request Type

```ts
interface SaveProviderRequest {
  name: string;
  providerType: 'openai-compatible' | 'anthropic' | 'custom';
  baseUrl: string;
  apiKey: string;
  model: string;
  timeoutMs?: number;
}
```

---

## 6. Validation Rules

### 6.1 Runtime Validation

Every handler must validate with Zod or equivalent.

```ts
const SaveProviderSchema = z.object({
  name: z.string().min(1).max(100),
  providerType: z.enum(['openai-compatible', 'anthropic', 'custom']),
  baseUrl: z.string().url(),
  apiKey: z.string().min(1).max(500),
  model: z.string().min(1).max(200),
  timeoutMs: z.number().int().positive().max(120000).optional(),
});
```

### 6.2 Validation Principles

- reject unknown shapes early
- constrain string lengths
- validate URLs, enums, numbers, and UUIDs explicitly
- never rely on renderer TypeScript alone for safety

---

## 7. Error Codes

| Code | Meaning |
|------|---------|
| `IPC_ERROR_VALIDATION` | Request payload failed runtime validation |
| `IPC_ERROR_UNAUTHORISED` | Operation is not allowed in current state |
| `IPC_ERROR_NOT_FOUND` | Target record does not exist |
| `IPC_ERROR_CONFLICT` | Resource state prevents the operation |
| `IPC_ERROR_PROVIDER` | Upstream provider interaction failed |
| `IPC_ERROR_TIMEOUT` | Operation exceeded allowed duration |
| `IPC_ERROR_INTERNAL` | Unclassified main-process failure |

Errors should be stable enough for renderer-side UX branching.

---

## 8. Security Restrictions

- No IPC channel returns raw provider keys.
- No IPC channel returns raw private keys.
- No generic “eval”, file-write, or shell-execution channel should exist.
- New channels require a documented threat review.
- Multi-window support must partition channels by window purpose if added later.

---

## 9. Event Channels vs Invoke Channels

Use `invoke/handle` for request-response operations. Use event channels sparingly for:

- trade status streaming
- agent status updates
- update-progress notifications

Event payloads should also be typed and documented. Avoid loose string payloads.

---

## 10. Adding a New Channel

1. define TypeScript request/response types
2. define runtime validation schema
3. implement main-process handler
4. expose narrow preload wrapper
5. add integration test
6. update this document and API reference
7. review whether the channel expands privileged authority

---

## 11. Testing Requirements

Every IPC channel should have:

- unit test for validation failure path
- unit or integration test for success path
- security review for secret exposure risk
- packaged-build smoke test for preload availability

---

## 12. Performance Guidance

- batch list refreshes where practical
- avoid tight polling loops from the renderer
- prefer event-driven updates for live trade state
- keep IPC payloads compact and serialisable

---

IPC is one of the most sensitive contracts in the application because it binds untrusted UI code to privileged desktop capabilities. Its discipline should be treated as part of the security model, not only as API hygiene.
