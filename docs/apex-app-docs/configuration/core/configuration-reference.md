---
metadata_schema_version: 1.0
document_id: DOC-0387
title: Configuration Reference
plane: Product Specification
domain: Configuration
class: Reference
authority: Reference
status: Active
owner: Config Team
version: 1.0.0
canonical_source: docs/apex-app-docs/configuration/core/configuration.md
related_concepts:
  - CONCEPT-0381
dependencies:
  - DOC-0381
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Reference
owned_domains: []
type: REFERENCE
purpose: "Enumerates every configuration key, owner, type, default, validation, reload, and restart requirement."
scope: Configuration Reference scope and boundaries.
---

# Configuration Reference

## Document type
Document type: [REFERENCE]

## Version
**Version:** 0.2.0 | **Status:** Draft | **Last Updated:** 2026-07-27 | **Owner:** Config Team

## Purpose
Enumerates every configuration key, owner, type, default, validation, reload, and restart requirement.

---

## Configuration Key Reference

### AI Subsystem (`ai.*`)

| Key | Type | Default | Owner | Reload | Restart | Validation | Description |
|-----|------|---------|-------|--------|---------|------------|-------------|
| `ai.enabled` | bool | `true` | AI | No | Yes | Must be boolean | Master AI system toggle |
| `ai.providers.default` | string | `"openai"` | AI | Yes | No | Must match a defined provider in `providers.*` | Default provider for AI requests |
| `ai.providers.fallback_chain` | string[] | `["anthropic", "openai"]` | AI | Yes | No | Each entry must match a defined provider | Ordered fallback providers |
| `ai.providers.timeout_ms` | int | `30000` | AI | Yes | No | 1000–120000 | Provider request timeout |
| `ai.providers.retry.max_attempts` | int | `3` | AI | Yes | No | 0–10 | Max retries on provider failure |
| `ai.providers.retry.backoff_ms` | int | `1000` | AI | Yes | No | 100–60000 | Initial backoff between retries |
| `ai.providers.retry.backoff_multiplier` | float | `2.0` | AI | Yes | No | 1.0–5.0 | Exponential backoff multiplier |
| `ai.providers.retry.jitter_ms` | int | `200` | AI | Yes | No | 0–5000 | Random jitter added to backoff |
| `ai.context.max_tokens` | int | `8192` | AI | Yes | No | 1024–128000 | Max tokens in context window |
| `ai.context.prune_threshold` | int | `7000` | AI | Yes | No | 512–128000 | Tokens at which pruning triggers |
| `ai.context.prune_strategy` | enum | `"priority"` | AI | Yes | No | `priority`, `lru`, `fifo` | Context pruning strategy |
| `ai.prompts.lifecycle_logging` | bool | `true` | AI | Yes | No | Must be boolean | Log prompt construction lifecycle |
| `ai.prompts.max_history_messages` | int | `50` | AI | Yes | No | 1–500 | Max conversation history messages |
| `ai.prompts.system_prompt_template` | string | `""` | AI | No | Yes | Non-empty | Override system prompt template |
| `ai.tools.enabled` | bool | `true` | AI | Yes | No | Must be boolean | Enable AI tool calling |
| `ai.tools.priority_config` | string | `"learned"` | AI | Yes | No | `learned`, `static`, `manual` | Tool selection priority mode |
| `ai.tools.max_tools_per_call` | int | `10` | AI | Yes | No | 1–50 | Max tools allowed per invocation |
| `ai.tools.timeout_ms` | int | `15000` | AI | Yes | No | 1000–60000 | Per-tool execution timeout |
| `ai.memory.enabled` | bool | `true` | AI | Yes | No | Must be boolean | Enable AI memory system |
| `ai.memory.max_entries` | int | `1000` | AI | Yes | No | 10–10000 | Max memory entries retained |
| `ai.memory.ttl_days` | int | `30` | AI | Yes | No | 1–365 | Memory entry TTL in days |
| `ai.cost.max_monthly_usd` | float | `100.0` | AI | Yes | No | 0–100000 | Monthly AI cost cap |
| `ai.cost.max_per_request_usd` | float | `0.50` | AI | Yes | No | 0.01–100 | Per-request cost cap |
| `ai.safety.max_retries_on_safety_violation` | int | `2` | AI | Yes | No | 0–5 | Max re-attempts after safety block |

### Trading Subsystem (`trade.*`)

| Key | Type | Default | Owner | Reload | Restart | Validation | Description |
|-----|------|---------|-------|--------|---------|------------|-------------|
| `trade.enabled` | bool | `true` | Trading | No | Yes | Must be boolean | Master trading toggle |
| `trade.slippage_max_bps` | int | `50` | Trading | Yes | No | 0–1000 | Max slippage in basis points |
| `trade.slippage_default_bps` | int | `20` | Trading | Yes | No | 0–1000 | Default slippage assumption |
| `trade.slippage_tolerance_bps` | int | `30` | Trading | Yes | No | 0–1000 | Slippage tolerance before abort |
| `trade.rollback_timeout_ms` | int | `10000` | Trading | Yes | No | 1000–60000 | Timeout for trade rollback |
| `trade.min_profit_bps` | int | `10` | Trading | Yes | No | 0–1000 | Minimum profit threshold in bps |
| `trade.max_concurrent_trades` | int | `5` | Trading | No | Yes | 1–50 | Max simultaneous trades |
| `trade.default_gas_limit` | int | `300000` | Trading | Yes | No | 21000–10000000 | Default gas limit |
| `trade.gas_boost_percent` | int | `10` | Trading | Yes | No | 0–100 | Gas price boost percentage |
| `trade.confirmation_blocks` | int | `2` | Trading | Yes | No | 0–100 | Blocks to wait for confirmation |
| `trade.max_retry_on_failure` | int | `3` | Trading | Yes | No | 0–10 | Max trade retry attempts |

### Risk Subsystem (`risk.*`)

| Key | Type | Default | Owner | Reload | Restart | Validation | Description |
|-----|------|---------|-------|--------|---------|------------|-------------|
| `risk.enabled` | bool | `true` | Risk | No | Yes | Must be boolean | Master risk engine toggle |
| `risk.max_position_usd` | float | `100000.0` | Risk | Yes | No | 0–1e9 | Max single position value |
| `risk.max_per_trade_usd` | float | `10000.0` | Risk | Yes | No | 0–1e9 | Max value per trade |
| `risk.max_daily_loss_usd` | float | `5000.0` | Risk | Yes | No | 0–1e9 | Max daily loss limit |
| `risk.max_daily_trades` | int | `100` | Risk | Yes | No | 1–10000 | Max trades per day |
| `risk.min_interval_ms` | int | `1000` | Risk | Yes | No | 100–60000 | Min interval between trades |
| `risk.circuit_breaker_enabled` | bool | `true` | Risk | Yes | No | Must be boolean | Enable circuit breaker |
| `risk.circuit_breaker_loss_threshold` | float | `1000.0` | Risk | Yes | No | 0–1e9 | Loss trigger for circuit breaker |
| `risk.circuit_breaker_cooldown_ms` | int | `60000` | Risk | Yes | No | 1000–3600000 | Circuit breaker cooldown |

### Execution Subsystem (`exec.*`)

| Key | Type | Default | Owner | Reload | Restart | Validation | Description |
|-----|------|---------|-------|--------|---------|------------|-------------|
| `exec.enabled` | bool | `true` | Execution | No | Yes | Must be boolean | Master execution toggle |
| `exec.atomic_timeout_ms` | int | `30000` | Execution | Yes | No | 1000–120000 | Max time for atomic execution |
| `exec.retry_max_attempts` | int | `3` | Execution | Yes | No | 0–10 | Max execution retries |
| `exec.retry_backoff_ms` | int | `2000` | Execution | Yes | No | 100–60000 | Execution retry backoff |
| `exec.retry_backoff_multiplier` | float | `2.0` | Execution | Yes | No | 1.0–5.0 | Retry exponential multiplier |
| `exec.max_pending_transactions` | int | `10` | Execution | Yes | No | 1–100 | Max pending TX at once |
| `exec.tx_replacement_enabled` | bool | `true` | Execution | Yes | No | Must be boolean | Enable TX replacement |

### Runtime Subsystem (`runtime.*`)

| Key | Type | Default | Owner | Reload | Restart | Validation | Description |
|-----|------|---------|-------|--------|---------|------------|-------------|
| `runtime.startup_timeout_ms` | int | `60000` | Runtime | No | Yes | 1000–300000 | Max startup time |
| `runtime.shutdown_timeout_ms` | int | `30000` | Runtime | No | Yes | 1000–120000 | Max shutdown time |
| `runtime.health_check_interval_ms` | int | `5000` | Runtime | Yes | No | 1000–60000 | Health check polling interval |
| `runtime.health_check_timeout_ms` | int | `3000` | Runtime | Yes | No | 500–30000 | Per-check timeout |
| `runtime.worker.min_workers` | int | `2` | Runtime | Yes | No | 0–100 | Min worker pool size |
| `runtime.worker.max_workers` | int | `20` | Runtime | Yes | No | 1–200 | Max worker pool size |
| `runtime.worker.idle_timeout_ms` | int | `30000` | Runtime | Yes | No | 5000–300000 | Worker idle timeout |
| `runtime.failover.enabled` | bool | `true` | Runtime | Yes | No | Must be boolean | Enable automatic failover |
| `runtime.failover.max_attempts` | int | `3` | Runtime | Yes | No | 1–10 | Failover retry limit |
| `runtime.log.level` | enum | `"info"` | Runtime | Yes | No | `debug`, `info`, `warn`, `error` | Logging level |
| `runtime.log.max_files` | int | `10` | Runtime | No | Yes | 1–100 | Log file rotation count |

### Event Subsystem (`event.*`)

| Key | Type | Default | Owner | Reload | Restart | Validation | Description |
|-----|------|---------|-------|--------|---------|------------|-------------|
| `event.enabled` | bool | `true` | Runtime | No | Yes | Must be boolean | Event bus master toggle |
| `event.retention_days` | int | `7` | Runtime | Yes | No | 1–365 | Event retention in days |
| `event.delivery_policy` | enum | `"at_least_once"` | Runtime | No | Yes | `at_most_once`, `at_least_once`, `exactly_once` | Delivery guarantee |
| `event.max_queue_size` | int | `10000` | Runtime | Yes | No | 100–1000000 | Max event queue size |
| `event.batch_size` | int | `100` | Runtime | Yes | No | 1–10000 | Event batch processing size |
| `event.dead_letter_enabled` | bool | `true` | Runtime | Yes | No | Must be boolean | Enable dead-letter queue |
| `event.dead_letter_max_retries` | int | `3` | Runtime | Yes | No | 1–10 | DLQ retry limit |

### Dashboard Subsystem (`dashboard.*`)

| Key | Type | Default | Owner | Reload | Restart | Validation | Description |
|-----|------|---------|-------|--------|---------|------------|-------------|
| `dashboard.enabled` | bool | `true` | UI | No | Yes | Must be boolean | Dashboard master toggle |
| `dashboard.workspace_persistence_path` | string | `"~/.apex/workspaces"` | UI | No | Yes | Must be valid path | Workspace save directory |
| `dashboard.workspace_autosave_interval_ms` | int | `30000` | UI | Yes | No | 5000–300000 | Autosave frequency |
| `dashboard.layout.default` | string | `"default"` | UI | Yes | No | Must match profile name | Default layout profile |
| `dashboard.refresh_interval_ms` | int | `5000` | UI | Yes | No | 1000–60000 | UI refresh polling interval |

### Plugin Subsystem (`plugin.*`)

| Key | Type | Default | Owner | Reload | Restart | Validation | Description |
|-----|------|---------|-------|--------|---------|------------|-------------|
| `plugin.enabled` | bool | `true` | Plugin | No | Yes | Must be boolean | Plugin system toggle |
| `plugin.sandbox_enabled` | bool | `true` | Plugin | No | Yes | Must be boolean | Enable sandbox isolation |
| `plugin.sandbox.memory_limit_mb` | int | `256` | Plugin | Yes | No | 16–4096 | Per-plugin memory limit |
| `plugin.sandbox.cpu_quota_percent` | int | `25` | Plugin | Yes | No | 1–100 | Per-plugin CPU quota |
| `plugin.max_plugins` | int | `50` | Plugin | No | Yes | 1–500 | Max installed plugins |
| `plugin.auto_update` | bool | `false` | Plugin | Yes | No | Must be boolean | Auto-update plugins |
| `plugin.allow_network` | bool | `false` | Plugin | No | Yes | Must be boolean | Allow network access |
| `plugin.allow_filesystem` | bool | `false` | Plugin | No | Yes | Must be boolean | Allow FS access |

### Security Subsystem (`security.*`)

| Key | Type | Default | Owner | Reload | Restart | Validation | Description |
|-----|------|---------|-------|--------|---------|------------|-------------|
| `security.secret.rotation_interval_days` | int | `90` | Security | Yes | No | 1–365 | Secret rotation interval |
| `security.secret.storage_backend` | enum | `"encrypted_file"` | Security | No | Yes | `encrypted_file`, `os_keychain`, `vault`, `env` | Secret storage backend |
| `security.secret.min_length` | int | `16` | Security | Yes | No | 8–128 | Min secret length |
| `security.audit.enabled` | bool | `true` | Security | No | Yes | Must be boolean | Audit logging toggle |
| `security.audit.retention_days` | int | `365` | Security | Yes | No | 30–3650 | Audit log retention |
| `security.trust.enforce_ipc` | bool | `true` | Security | No | Yes | Must be boolean | Enforce IPC trust boundaries |
| `security.trust.enforce_plugin_isolation` | bool | `true` | Security | No | Yes | Must be boolean | Enforce plugin isolation |

### Resource Management (`resource.*`)

| Key | Type | Default | Owner | Reload | Restart | Validation | Description |
|-----|------|---------|-------|--------|---------|------------|-------------|
| `resource.memory_limit_mb` | int | `1024` | Ops | Yes | No | 64–65536 | Total app memory limit |
| `resource.cpu_budget_percent` | int | `80` | Ops | Yes | No | 1–100 | CPU budget percentage |
| `resource.disk_cache_max_mb` | int | `500` | Ops | Yes | No | 0–10240 | Disk cache size limit |
| `resource.network.max_connections` | int | `50` | Ops | Yes | No | 1–1000 | Max concurrent connections |
| `resource.network.request_timeout_ms` | int | `10000` | Ops | Yes | No | 1000–120000 | HTTP request timeout |

### Provider Configuration (`providers.*`)

| Key | Type | Default | Owner | Reload | Restart | Validation | Description |
|-----|------|---------|-------|--------|---------|------------|-------------|
| `providers.<name>.type` | string | — | AI | Yes | No | `openai`, `anthropic`, `custom:<id>` | Provider type |
| `providers.<name>.api_key_env` | string | — | AI | No | Yes | Must be valid env var name | Env var for API key |
| `providers.<name>.base_url` | string | `""` | AI | Yes | No | Valid URL or empty | Custom base URL |
| `providers.<name>.models` | string[] | `[]` | AI | Yes | No | At least one model | Available models |
| `providers.<name>.rate_limit.rpm` | int | `60` | AI | Yes | No | 1–100000 | Requests per minute limit |
| `providers.<name>.rate_limit.tpm` | int | `100000` | AI | Yes | No | 1000–10000000 | Tokens per minute limit |

### Chain Configuration (`chains.*`)

| Key | Type | Default | Owner | Reload | Restart | Validation | Description |
|-----|------|---------|-------|--------|---------|------------|-------------|
| `chains.<id>.enabled` | bool | `true` | Trading | No | Yes | Must be boolean | Enable specific chain |
| `chains.<id>.rpc_url` | string | — | Trading | Yes | No | Must be valid URL | Primary RPC URL |
| `chains.<id>.rpc_fallback_urls` | string[] | `[]` | Trading | Yes | No | Valid URLs | Fallback RPC URLs |
| `chains.<id>.ws_url` | string | — | Trading | Yes | No | Must be valid WS URL | WebSocket URL |
| `chains.<id>.block_time_ms` | int | — | Trading | Yes | No | 500–60000 | Chain block time |
| `chains.<id>.confirmations` | int | `1` | Trading | Yes | No | 0–100 | Required confirmations |
| `chains.<id>.gas_limit_buffer` | float | `1.1` | Trading | Yes | No | 1.0–2.0 | Gas limit multiplier |

### Wallet Configuration (`wallet.*`)

| Key | Type | Default | Owner | Reload | Restart | Validation | Description |
|-----|------|---------|-------|--------|---------|------------|-------------|
| `wallet.<address>.enabled` | bool | — | Trading | No | Yes | Must be boolean | Enable wallet |
| `wallet.<address>.network` | string | — | Trading | No | Yes | Must match chain ID | Wallet network |
| `wallet.<address>.max_gas_price_gwei` | int | `500` | Trading | Yes | No | 1–10000 | Max gas price for wallet |

---

## Conflict Resolution Rules

When multiple configuration sources define the same key, the following precedence applies:

1. **Encrypted user overrides** (highest)
2. **Session-only runtime overrides** (where allowed — see `Reload` column)
3. **Environment variables** (prefixed with `APEX_` — e.g. `APEX_RISK_MAX_POSITION_USD`)
4. **Profile-based overrides** (per `./configuration-profiles.md`)
5. **Installation profile defaults** (per-platform recommended defaults)
6. **Bundled application defaults**
7. **Secure hardcoded fallbacks** (lowest)

### Merge Behavior

- **Scalar values**: Higher-precedence source fully overrides lower.
- **Arrays**: Higher-precedence source replaces entire array (no merge).
- **Objects / nested keys**: Deep merge at the leaf level — keys present only in a lower-precedence source are retained unless explicitly set to `null` in a higher source.

### Profile Inheritance

```yaml
# Default profile
trade:
  slippage_max_bps: 50
  min_profit_bps: 10

# Aggressive profile (inherits Default, overrides)
profile: aggressive
extends: default
trade:
  slippage_max_bps: 100
  min_profit_bps: 5
```

---

## Reload Semantics

| Reload | Meaning |
|--------|---------|
| **Yes** | Key can be changed at runtime without service restart. The subsystem watches for config file changes or receives a `SIGHUP` / reload event. |
| **No** | Key requires a full service restart. Changing the value in the config file has no effect until the process is restarted. |

When a `Reload: Yes` key is changed:
1. The config manager validates the new value against schema.
2. The affected subsystem receives a `config.updated` event with the changed key path.
3. The subsystem applies the new value atomically.
4. If validation fails, the old value is retained and a warning is logged.

When a `Reload: Yes` batch of keys is changed simultaneously (e.g. via profile switch):
1. All new values are validated first.
2. If any single value fails validation, the entire batch is rejected (all-or-nothing).
3. On success, all affected subsystems are notified in dependency order.

---

## Validation Rules

- All keys are validated against their declared `type` on load.
- Enum values are validated against the exact set of allowed values (case-sensitive).
- Integer and float ranges are checked (inclusive bounds).
- String values with format constraints (URL, path, env-var-name) are validated via regex.
- If validation fails on startup: the application logs the error with the offending key and **refuses to start**.
- If validation fails on hot-reload: the **old value is retained**, a warning is logged, and the change is rejected.
- Arrays within defined length bounds (`<id>` wildcards are permitted for dynamic keys).

---

## Cross-References

- **CONFIGURATION.md** — Precedence, profiles, secret handling authority.
- **TRACEABILITY-MATRIX.md** — Requirement-to-document mapping and governance validation.
- **CONFIGURATION-PROFILES.md** — Profile inheritance and switching.
- **FEATURE-FLAGS.md** — Feature flag system and gating.
- **SCHEMAS/configuration.schema.json** — JSON Schema for config validation.
- **RUNTIME-OPERATIONS.md** — Config reload behavior at runtime.
- **SECRET-LIFECYCLE.md** — Secret-backed key handling.
- **SECURITY.md** — Security-related key governance.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 0.2.0 | 2026-07-27 | Added full key-by-key reference with reload/restart/validation semantics | Config Team |
| 0.1.0 | 2026-07-27 | Initial stub created | Config Team |
