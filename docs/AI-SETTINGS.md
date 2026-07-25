# APEX AI Settings Page - Complete Specification (v3)

> **Version:** 3.0.0 | **Last Updated:** July 25, 2026
> **Scope:** The full user-facing AI Configuration page, every field, every state, every action.

---

## 1. Overview

The AI Settings page is the **central configuration hub** for cloud AI providers.
The user sets their base URL, model name, and API key, then APEX can route every
AI call through those endpoints. Supports **OpenAI-compatible** (OpenAI, Groq,
Together, OpenRouter, DeepSeek, Mistral, Azure, **local/self-hosted LLMs that
expose an OpenAI-compatible endpoint such as LM Studio, Ollama, vLLM, llama.cpp
server, LocalAI, LMDeploy** — collectively referred to here as "Self-Hosted /
Local Congo-compatible endpoints") and **Anthropic native** providers.

**User can save, test, and reset any provider, any time, without restarting.**

Access:
- Sidebar → Settings → AI Configuration
- Top bar gear icon
- First-run wizard
- Tray menu → Settings

---

## 2. Page Layout

### 2.1 Header
- **Title:** "AI Configuration"
- **Subtitle:** "Configure your cloud AI providers for APEX intelligence"
- **Status indicator (aggregate):**
  - Green dot + "All providers healthy"
  - Yellow dot + "Some providers untested"
  - Red dot + "No providers working"
  - Gray dot + "No providers configured"
- **Right side:** "Add Provider" (primary), "Reset All" (ghost), "?" (opens help)

### 2.2 Provider Cards (vertical list, collapsible)
1. **OpenAI** (pre-configured template, requires key)
2. **Anthropic** (pre-configured template, requires key)
3. **Custom Provider** (blank, user can add many)

Each card:
- **Header:** name (editable), type chip ("OpenAI-Compatible" / "Anthropic Native" / "Self-Hosted Local"), status dot, enable toggle, kebab menu (Duplicate, Reset, Delete)
- **Body** (when expanded): all fields per provider type (see §3)
- **Footer:** Test Connection (ghost), Save (primary, disabled until dirty + valid), Reset (ghost)

---

## 3. Provider Fields by Type

### 3.1 OpenAI-Compatible (Cloud)
| Field | Type | Default | Validation |
|-------|------|---------|------------|
| **Name** | text | "OpenAI" | required, 1-60 chars |
| **Provider Type** | select | "openai_compatible" | locked to OpenAI-compatible |
| **Base URL** | text | `https://api.openai.com` | must start with `https://`, no trailing slash |
| **Model Name** | text + suggestions | `gpt-4o` | non-empty; suggestions include `gpt-4o`, `gpt-4o-mini`, `gpt-4-turbo`, `o1`, `o1-mini` |
| **API Key** | password | empty | required if enabled, min 10 chars, never logged |
| **Max Tokens** | number | 4096 | 1 – 128,000 |
| **Temperature** | slider | 0.2 | 0.0 – 2.0 |
| **Top P** | slider | 1.0 | 0.0 – 1.0 (advanced disclosure) |
| **Rate Limit RPM** | number | 500 | 1 – 10,000 |
| **Rate Limit TPM** | number | 150,000 | 1,000 – 10,000,000 |
| **Request Timeout (ms)** | number | 30,000 | 1,000 – 120,000 (advanced) |
| **Custom Headers** | key-value editor | empty | each header `^[A-Za-z0-9-]{1,64}$` name, max 20 (advanced) |
| **Proxy URL** | text | empty | optional `http://` or `socks5://` URL (advanced) |
| **Priority** | number | 1 | 1 (highest) – 10 (lowest); lower = preferred in failover |
| **Enabled** | toggle | off until key saved | — |

**Compatible providers (preload templates — pick from a dropdown to autofill):**
- OpenAI (`https://api.openai.com`)
- Azure OpenAI (asks for resource name + deployment, builds URL)
- Groq (`https://api.groq.com/openai`)
- Together AI (`https://api.together.xyz/v1`)
- OpenRouter (`https://openrouter.ai/api/v1`)
- DeepSeek (`https://api.deepseek.com/v1`)
- Mistral (`https://api.mistral.ai/v1`)
- Perplexity (`https://api.perplexity.ai`)
- Fireworks (`https://api.fireworks.ai/inference/v1`)
- Anyscale (`https://api.endpoints.anyscale.com/v1`)

### 3.2 Anthropic Native
| Field | Type | Default | Validation |
|-------|------|---------|------------|
| **Name** | text | "Anthropic" | required |
| **Provider Type** | select | "anthropic_native" | locked |
| **Base URL** | text | `https://api.anthropic.com` | must be HTTPS |
| **Model Name** | text + suggestions | `claude-sonnet-4-20250514` | suggestions: `claude-sonnet-4-20250514`, `claude-opus-4-20250514`, `claude-3-5-sonnet-20241022`, `claude-3-5-haiku-20241022`, `claude-3-haiku-20240307` |
| **API Key** | password | empty | must start with `sk-ant-` (warning if not, not blocked) |
| **Anthropic Version** | text | `2023-06-01` | required, yyyy-mm-dd |
| **Max Tokens** | number | 4096 | 1 – 128,000 |
| **Temperature** | slider | 0.2 | **0.0 – 1.0** (Anthropic limit) |
| **Top P** | slider | 1.0 | 0.0 – 1.0 (advanced) |
| **Top K** | number | empty | 0 – 500 (advanced) |
| **Rate Limit RPM** | number | 300 | 1 – 10,000 |
| **Rate Limit TPM** | number | 100,000 | 1,000 – 10,000,000 |
| **Request Timeout (ms)** | number | 30,000 | 1,000 – 120,000 |
| **Custom Headers** | key-value | empty | max 20 (advanced) |
| **Proxy URL** | text | empty | optional (advanced) |
| **Priority** | number | 2 | 1 – 10 |
| **Enabled** | toggle | off until key saved | — |

### 3.3 Self-Hosted / Local Congo-Compatible *(new in v3)*
This provider type covers any local or self-hosted server that exposes an
**OpenAI-compatible** HTTP API. The user points APEX at it via a `http://`
base URL. No API key is required by default (but supported if the local
server enforces one).

> **Why "Congo-compatible":** The user's APEX setup treats local servers the
> same as any OpenAI-compatible endpoint. The local server is commonly
> called "Congo" in the user's environment (e.g. LM Studio, Ollama with
> OpenAI shim, vLLM, llama.cpp server, LocalAI). The terminology is
> preserved here to match user expectations, but **technically it is just
> an OpenAI-compatible base URL over HTTP**.

| Field | Type | Default | Validation |
|-------|------|---------|------------|
| **Name** | text | "Local Congo" | required |
| **Provider Type** | select | "self_hosted" | locked |
| **Base URL** | text | `http://localhost:1234/v1` | must start with `http://` (local) or `https://` (self-hosted remote); no trailing slash |
| **Model Name** | text | empty | must exactly match a model name served by the local server |
| **API Key** | password | empty | **optional**; only required if the local server is configured to enforce auth |
| **Max Tokens** | number | 4096 | 1 – model's context window |
| **Temperature** | slider | 0.2 | 0.0 – 2.0 |
| **Top P** | slider | 1.0 | 0.0 – 1.0 |
| **Rate Limit RPM** | number | 1000 | local servers typically have no limit; user-tunable |
| **Rate Limit TPM** | number | 1,000,000 | local-only; tunable |
| **Request Timeout (ms)** | number | 120,000 | local models can be slow on first token; default is generous |
| **Custom Headers** | key-value | empty | max 20 (advanced) |
| **Discover Models** | button | — | Sends `GET {base_url}/v1/models` and populates the Model Name suggestions |
| **Health Check URL** | text | empty | optional; if set, APEX pings it for status (e.g. `http://localhost:1234/health`) |
| **Priority** | number | 3 | 1 – 10 |
| **Enabled** | toggle | off until base URL saved | — |

**Preset templates (auto-fill base URL and defaults):**
- **LM Studio:** `http://localhost:1234/v1` — local OpenAI-compatible, OpenAI-compatible models
- **Ollama (with OpenAI shim):** `http://localhost:11434/v1` — open-source model runner, OpenAI-compatible since Ollama 0.1.14
- **vLLM:** `http://localhost:8000/v1` — high-throughput inference server
- **llama.cpp server:** `http://localhost:8080/v1` — `llama-server --api`
- **LocalAI:** `http://localhost:8080/v1` — drop-in OpenAI replacement
- **Jan:** `http://localhost:1337/v1` — local AI client/server
- **LMDeploy:** `http://localhost:23333/v1` — production server framework
- **Custom** — user types the URL

> **HTTP allowed:** unlike cloud providers, self-hosted endpoints may use
> `http://` because they run on `localhost`. APEX will display a warning
> if a self-hosted provider is configured with a non-loopback host over
> `http://` (security advisory).

---

## 4. Per-Provider Actions

| Action | Behavior |
|--------|----------|
| **Save** | Validate → encrypt API key → write to SQLite → toast "Saved" |
| **Test Connection** | Send a 1-token probe (e.g. "ping"); show toast with latency, model, token count |
| **Reset** | Confirmation modal → clear all fields to defaults for this provider |
| **Delete** | Custom providers only; confirmation modal → remove from SQLite |
| **Duplicate** | Clones the provider as a new card with "-copy" suffix |
| **Expand/Collapse** | Click card header to toggle body |
| **Enable/Disable** | Toggle switch; disabled providers are skipped by router but kept in DB |

Disabled providers are visually muted (60% opacity) and their kebab menu adds "Enable".

---

## 5. Global Actions (bottom of page)

| Action | Behavior |
|--------|----------|
| **Save All** | Save all dirty providers atomically; rollback on any failure |
| **Reset All** | Two-step confirmation (typed "RESET") → wipe all providers, keys, overrides |
| **Clear AI Cache** | Removes all cached responses; next calls hit network |
| **Export Diagnostics** | Downloads JSON with config + connection log + cost summary (**no keys**) |
| **Import Config** | Loads JSON; prompts per-provider for "Keep existing key / Use imported key / Skip" |

---

## 6. Data Persistence

### 6.1 Storage Strategy
- **Configs (non-secret):** SQLite `ai_providers` table, plaintext columns
- **API keys:** Electron `safeStorage.encryptString()` → BLOB column `api_key_encrypted`; decrypted only in main process, only at call time, zeroed after use
- **No keys** in localStorage, sessionStorage, cookies, IndexedDB, logs, telemetry, diagnostics export, or anywhere outside the encrypted BLOB

### 6.2 Schema — `ai_providers` table
```sql
CREATE TABLE ai_providers (
  id                  INTEGER PRIMARY KEY AUTOINCREMENT,
  provider_id         TEXT UNIQUE NOT NULL,         -- uuid, used in IPC
  name                TEXT NOT NULL,
  provider_type       TEXT NOT NULL CHECK(provider_type IN
                          ('openai_compatible','anthropic_native','self_hosted')),
  base_url            TEXT NOT NULL,
  model_name          TEXT,
  api_key_encrypted   BLOB,                         -- safeStorage-encrypted; nullable for self_hosted
  anthropic_version   TEXT,                         -- only for anthropic_native
  max_tokens          INTEGER DEFAULT 4096,
  temperature         REAL DEFAULT 0.2,
  top_p               REAL DEFAULT 1.0,
  top_k               INTEGER,                       -- anthropic only
  rate_limit_rpm      INTEGER DEFAULT 500,
  rate_limit_tpm      INTEGER DEFAULT 150000,
  timeout_ms          INTEGER DEFAULT 30000,
  custom_headers_json TEXT,                         -- JSON array of {name, value}
  proxy_url           TEXT,
  health_check_url    TEXT,                         -- self_hosted only
  priority            INTEGER DEFAULT 5,
  is_enabled          INTEGER DEFAULT 0,
  is_builtin          INTEGER DEFAULT 0,            -- OpenAI/Anthropic templates
  created_at          TEXT NOT NULL,                -- ISO 8601
  updated_at          TEXT NOT NULL
);
```

### 6.3 Built-in Defaults (created on first launch, disabled)
- **OpenAI:** `https://api.openai.com`, `gpt-4o`, priority 1
- **Anthropic:** `https://api.anthropic.com`, `claude-sonnet-4-20250514`, priority 2
- **Self-Hosted Local:** `http://localhost:1234/v1`, empty model, priority 3, optional key

---

## 7. Validation Rules

| Field | Rule | Error message |
|-------|------|---------------|
| Base URL (OpenAI/Anthropic) | starts with `https://` | "Base URL must use HTTPS" |
| Base URL (Self-Hosted) | starts with `http://` (loopback) or `https://` | "Base URL must be http://localhost or https://" |
| Base URL (non-loopback http) | forbidden | "HTTP only allowed for loopback addresses (security risk)" |
| Model Name | non-empty | "Model name is required" |
| API Key (cloud) | min 10 chars if enabled | "API key is required to enable this provider" |
| API Key (self-hosted) | optional | — |
| Anthropic API Key | warn if not `sk-ant-` prefix | "Doesn't look like an Anthropic key (expected sk-ant-...)" |
| Max Tokens | 1 – 128,000 | "Must be between 1 and 128000" |
| Temperature (OpenAI/Self-Hosted) | 0.0 – 2.0 | "Must be 0.0 – 2.0" |
| Temperature (Anthropic) | 0.0 – 1.0 | "Anthropic limits temperature to 0.0 – 1.0" |
| RPM | 1 – 10,000 | — |
| TPM | 1,000 – 10,000,000 | — |
| At least one provider enabled | — | "Enable at least one provider to use AI features" |
| Warning if only one enabled | — | "No fallback configured — trades will halt if this provider fails" |

---

## 8. First-Run Wizard

1. Welcome card → "Let's set up your AI provider"
2. Choose path:
   - **Quick:** Use OpenAI → paste key → test → done
   - **Quick:** Use Anthropic → paste key → test → done
   - **Local:** Use a self-hosted server → start it, copy base URL → discover models → done
   - **Advanced:** Configure all three
3. Successful test → "Continue to Dashboard"
4. Failed test → show error, "Try Again" / "Use Anyway" / "Skip for Now"

User can re-open this wizard any time from Help → "Run Setup Wizard".

---

## 9. Agent-Level Overrides (tab 2)

A second tab on the page: **"Agent Overrides"**

A table view, one row per registered agent (see `AGENTS.md`):
| Column | Content |
|--------|---------|
| Agent | name + category chip |
| Provider | select ("Auto" / per-provider dropdown) |
| Model | text (overrides agent's `model_preference`) |
| Temperature | number (empty = use agent default) |
| Max Tokens | number (empty = use default) |
| Daily Quota | number (calls/24h, null = unlimited) |
| Enabled | toggle |

A "Reset This Agent" button per row, plus "Reset All Agents" at the top right.

A "Bulk Assign" dropdown lets the user pin all agents to a single provider (e.g. "Use Anthropic for everything").

---

## 10. Diagnostics Tab (tab 3)

- **Connection Log:** last 20 successful test calls, timestamp + provider + latency + status
- **Error Log:** last 10 errors, timestamp + provider + error class + sanitized message
- **Cache Stats:** entries, hit rate, size on disk
- **Cost Summary:** today / 7d / 30d per provider, with chart
- **Token Usage:** same windows, per agent
- **Export Diagnostics** button → JSON download (no keys)

---

## 11. Keyboard Shortcuts (in this page)

| Shortcut | Action |
|----------|--------|
| `Ctrl+S` | Save current focused provider |
| `Ctrl+T` | Test current focused provider |
| `Ctrl+R` | Reset current focused provider (with confirm) |
| `Ctrl+N` | Add new provider |
| `Ctrl+Tab` | Next field / next card |
| `Esc` | Close any open modal |
| `Tab` / `Shift+Tab` | Navigate forward / back |

---

## 12. Security Considerations (cross-ref `SECURITY.md`)

- API keys never leave the main process unencrypted
- No HTTPS for loopback; HTTP for non-loopback is rejected at the validation layer
- All AI calls go through the AI Pipeline which enforces HTTPS / loopback + cert validation
- Reset All wipes the encryption blob irreversibly
- Custom headers must not contain `Authorization` overrides for cloud providers (rejected at validation; users must use the API Key field)
- The page never autofills API keys (no browser-level autofill for password inputs)
- Clipboard: "Copy API Key" button is **not** offered (reduces leak surface); reveal-with-eye is the only way to see it

---

## 13. Empty / Error / Loading States

- **Empty (no providers enabled):** centered illustration + "Configure your first AI provider" + "Add Provider" CTA
- **Loading (initial):** skeleton of 3 provider cards
- **Test in progress:** spinner on Test button, "Testing..." label
- **Test failed:** error toast with class, "Retry" action, "Copy details" action
- **Save failed:** inline error under offending field + error toast

---

*This page is the front door to APEX's intelligence. It must feel safe, fast, and obvious.*
