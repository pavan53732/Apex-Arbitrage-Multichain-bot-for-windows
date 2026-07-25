# APEX AI Settings Page - Complete Specification

> **Version:** 2.0.0 | **Last Updated:** July 25, 2026

---

## 1. Overview

Central configuration hub for cloud AI providers. Users set base URL, model name,
API key. Supports OpenAI-compatible and Anthropic native. Save, test, reset anytime.

Access: Sidebar > Settings > AI Configuration | Top bar gear | First-run wizard

---

## 2. Page Layout

### Header
- Title: AI Configuration
- Subtitle: Configure your cloud AI providers for APEX intelligence
- Status: Green (connected) | Yellow (untested) | Red (none/failing)

### Provider Cards (vertical list)
1. OpenAI (pre-configured template)
2. Anthropic (pre-configured template)
3. Custom Provider (blank, add multiple)

Each card: name (editable), type selector, status dot, expand/collapse, enable switch, priority

### Fields (OpenAI-Compatible)
- **Base URL:** https://api.openai.com (default), must be HTTPS
- **Model Name:** gpt-4o (default), suggestions dropdown
- **API Key:** password input, show/hide toggle, NEVER logged
- **Max Tokens:** 4096 default, 1-128000
- **Temperature:** 0.2 default, 0.0-2.0 slider
- **Rate Limit RPM:** 500 default
- **Rate Limit TPM:** 150000 default

### Fields (Anthropic Native)
- **Base URL:** https://api.anthropic.com
- **Model Name:** claude-sonnet-4-20250514
- **API Key:** sk-ant-...
- **Max Tokens:** 4096
- **Temperature:** 0.2
- **Anthropic Version:** 2023-06-01

---

## 3. Actions

### Per-Provider
- **Save:** Validate plus save to encrypted store. Disabled until valid.
- **Test Connection:** Send test prompt, show success/error toast with latency
- **Reset:** Confirmation dialog, clear to defaults
- **Delete:** Custom only, confirmation required

### Global
- **Add Custom Provider:** New blank card
- **Save All:** Save all modified at once
- **Reset All:** Clear ALL configs plus keys with confirmation
- **Clear AI Cache:** Remove cached responses

---

## 4. Data Persistence

- Configs in SQLite | Keys encrypted via Electron safeStorage (DPAPI)
- Keys NEVER plaintext on disk, NEVER in logs, NEVER sent except to base_url

### Schema (ai_providers table)
id, provider_id, name, provider_type, base_url, model_name, api_key_encrypted (BLOB),
max_tokens, temperature, rate_limit_rpm, rate_limit_tpm, priority, is_enabled, created_at, updated_at

### Defaults
- OpenAI: api.openai.com, gpt-4o, priority 1, disabled until key set
- Anthropic: api.anthropic.com, claude-sonnet-4-20250514, priority 2, disabled until key set

---

## 5. Validation

- Base URL: https:// required | Model: non-empty | API Key: min 10 chars for enabled
- Max Tokens: 1-128000 | Temperature: 0.0-2.0 | RPM: 1-10000 | TPM: 1000-10M
- At least one provider enabled required | Warning if only one (no failover)

---

## 6. First-Run

1. Welcome dialog -> Redirect to AI Settings -> OpenAI expanded
2. After save plus test: success -> Dashboard

---

## 7. Agent-Level Overrides

- Table: agent -> assigned provider | Default: Auto
- Pin specific agents to providers | Reset per row

---

## 8. Diagnostics

- Connection Log (last 20) | Error Log (last 10) | Cache Stats | Cost Summary
- Export Diagnostics (JSON, no keys)

---

## 9. Shortcuts

Ctrl+S Save | Ctrl+T Test | Ctrl+R Reset | Ctrl+N Add | Esc Close | Tab Navigate

---

*Most critical config surface. Configure in under 60 seconds.*
