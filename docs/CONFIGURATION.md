---
last_updated: 2026-07-29
type: CONTRACT
owner: Config Team
status: Canonical
version: 1.1.0
purpose: Defines configuration management, schema, and lifecycle.
scope: Configuration schema, validation, hot-reload, and versioning.
canonical_source: docs/CONFIGURATION.md
---

# Configuration

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.1.0 | **Status:** Canonical | **Last Updated:** 2026-07-29 | **Owner:** Config Team

## Purpose
Defines runtime and operational configuration — precedence, validation, secret handling, profile management, hot-reload semantics, restart-required semantics, conflict resolution, Windows-specific config, and cross-system config ownership wiring.

---

## 1. Configuration Precedence (Highest to Lowest)

| Priority | Source | Example | Override Scope | Persistence |
|----------|--------|---------|----------------|-------------|
| 1 | Encrypted user overrides | `~/.apex/config/user.enc.yaml` | Per-user, permanent | Encrypted file + OS keychain |
| 2 | Session-only runtime overrides | `--set runtime.log.level=debug` | Per-session, ephemeral | In-memory only; lost on shutdown |
| 3 | Environment variables | `APEX_RISK_MAX_POSITION_USD=50000` | Per-process, ephemeral | OS environment; not persisted |
| 4 | Profile-based overrides | `config/profiles/aggressive.yaml` | Per-profile, semi-permanent | Profile file |
| 5 | Installation profile defaults | `config/profiles/install.yaml` | Per-installation | Installed profile |
| 6 | Bundled application defaults | `config/default.yaml` | Per-version, bundled | Application defaults |
| 7 | Secure hardcoded fallbacks | Source code defaults | Per-version, immutable | Hardcoded; not configurable |

### Merge Behavior
- **Scalar values**: Higher-precedence source fully overrides lower.
- **Arrays**: Higher-precedence source **replaces entire array** (no element-level merge).
- **Objects / nested keys**: Deep merge at the leaf level — keys present only in a lower-precedence source are retained unless explicitly set to `null` in a higher source.

---

## 2. Key Reference Authority

`CONFIGURATION-REFERENCE.md` is the **canonical key-by-key configuration reference**. It defines:
- Every configuration key, type, default, owner, validation rule.
- Reload vs Restart semantics per key.
- Conflict resolution rules.
- Environment variable mapping.

This document (`CONFIGURATION.md`) owns **precedence, profiles, secrets, and governance**. `CONFIGURATION-REFERENCE.md` owns **key definitions**.

---

## 3. Hot-Reload vs Restart-Required Semantics

| Category | Hot-Reloadable? | Behavior | Examples |
|----------|----------------|----------|----------|
| **Critical toggles** | No (restart required) | Changing value has no effect until restart; dashboard shows "Restart Required" | `ai.enabled`, `trade.enabled`, `runtime.startup_timeout_ms`, `security.secret.storage_backend` |
| **Operational thresholds** | Yes (hot-reload) | Value applied immediately via config.updated event; subsystem applies atomically | `risk.max_position_usd`, `trade.slippage_max_bps`, `ai.providers.timeout_ms`, `runtime.worker.max_workers` |
| **Secret-backed keys** | No (restart or re-auth) | Requires secret re-fetch; may need re-authentication | `providers.<name>.api_key_env`, `wallet.*.network` |
| **Structural keys** | No (restart required) | Changing config structure (new subsections, schema changes) requires restart | `chains.<id>.rpc_url`, `wallet.<address>.enabled` |

### Hot-Reload Process
1. Config Manager detects change → validates ALL values in batch.
2. If any single value fails → entire batch rejected (all-or-nothing).
3. On success → identify affected subsystems → send config.updated event in dependency order.
4. Each subsystem applies value atomically.
5. Log change to config_history table.

### Restart-Required Process
1. Config Manager detects change → validates.
2. Value queued for next restart (not applied immediately).
3. Dashboard shows "Restart Required" banner with pending key list.
4. On next startup: queued changes applied during Phase 1 (Kernel Bootstrap).

---

## 4. Secret-Backed Configuration

| Rule | Description |
|------|-------------|
| API keys referenced via env vars | `providers.<name>.api_key_env: "APEX_OPENAI_KEY"` — never stored in config file |
| Wallet keys stored in OS keychain | Never in config; accessed via Secret Manager |
| Secret rotation triggers config refresh | When a secret rotates, all subsystems using that secret are notified to refresh their handle |
| Secrets redacted in config dump | `GET /api/admin/config/dump` redacts all secret-backed values as `[SECRET]` |

---

## 5. Profile Management

See `CONFIGURATION-PROFILES.md` for full profile governance. This document establishes:

| Profile | Purpose | Override Level | Switch Method |
|---------|---------|----------------|---------------|
| `default` | Bundled defaults; baseline | Level 6 (bundled) | Auto (always available) |
| `aggressive` | Higher risk tolerance; more trades | Level 4 (profile) | Dashboard settings or CLI |
| `conservative` | Lower risk; fewer trades; more safety | Level 4 (profile) | Dashboard settings or CLI |
| `simulation` | No real trades; test mode | Level 4 (profile) | Dashboard settings or CLI |
| `install` | Per-platform defaults (Windows, Linux, macOS) | Level 5 (installation) | Auto-detect on install |

### Profile Inheritance
```yaml
# aggressive profile inherits default, overrides specific keys
profile: aggressive
extends: default
trade:
  slippage_max_bps: 100      # overrides default 50
  min_profit_bps: 5           # overrides default 10
risk:
  max_per_trade_usd: 20000    # overrides default 10000
```

---

## 6. Windows Configuration

| Aspect | Rule |
|--------|------|
| **Config file location** | `%APPDATA%/Apex/config/default.yaml` (user scope); `%PROGRAMDATA%/Apex/config/default.yaml` (system scope for service mode) |
| **Environment overrides** | Standard `APEX_` prefix; e.g., `APEX_RISK_MAX_POSITION_USD` |
| **Proxy configuration** | System proxy respected: `HTTP_PROXY`, `HTTPS_PROXY`; can override per-provider in config |
| **Update channel** | `build.update_channel: canary|beta|production`; stored in install profile |
| **Service config** | `service.start_type: auto|manual|disabled`; stored in Windows SCM |
| **UAC elevation** | Config mutations in `%PROGRAMDATA%` require admin; `%APPDATA%` does not |

---

## 7. Cross-System Configuration Ownership Wiring

| Config Section | Primary Owner | Authority Doc | Secondary Consumers |
|---------------|--------------|---------------|--------------------|
| `ai.*` | AI Team | AI-PIPELINE.md | AI-ORCHESTRATION.md, AI-PROVIDER-MANAGER.md, AI-COST-MANAGEMENT.md |
| `trade.*` | Trading Team | TRADING-ENGINE.md | EXECUTION-ENGINE.md, RISK-ENGINE.md |
| `risk.*` | Risk Team | RISK-ENGINE.md | TRADING-ENGINE.md, EXECUTION-ENGINE.md |
| `execution.*` | Execution Team | EXECUTION-ENGINE.md | TRADING-ENGINE.md |
| `runtime.*` | Runtime Team | RUNTIME-OPERATIONS.md | ORCHESTRATOR.md, HEALTHCHECKS.md |
| `event.*` | Runtime Team | EVENT-BUS.md | EVENT-CATALOG.md, EVENT-OWNERSHIP-MATRIX.md |
| `security.*` | Security Team | SECURITY.md | SECRET-LIFECYCLE.md, TRUST-BOUNDARIES.md |
| `plugin.*` | Plugin Team | PLUGIN-SDK.md | PLUGIN-SANDBOX-CONTRACT.md, PLUGIN-LIFECYCLE.md |
| `dashboard.*` | Dashboard Team | DASHBOARD-RUNTIME.md | DASHBOARD-WORKSPACES.md, DASHBOARD-WIDGETS.md |
| `resource.*` | Ops Team | RESOURCE-BUDGET-SPECIFICATION.md | CAPACITY-PLANNING.md, MONITORING-OBSERVABILITY.md |
| `service.*` | Windows Team | SERVICE-STATE-MACHINE.md | WINDOWS-DESKTOP.md |

---

## Cross-References

- **CONFIGURATION-REFERENCE.md** — Canonical key-by-key reference (authoritative for key definitions).
- **CONFIGURATION-PROFILES.md** — Profile inheritance and switching.
- **FEATURE-FLAGS.md** — Feature flag system.
- **FEATURE-FLAG-GOVERNANCE-AND-ROLLOUT-MATRIX.md** — Feature flag governance and rollout.
- **SECRET-LIFECYCLE.md** — Secret-backed configuration handling.
- **TRACEABILITY-MATRIX.md** — REQ-CONFIG-001 through REQ-CONFIG-004.
- **SECURITY.md** — Security-related key governance.
- **RUNTIME-OPERATIONS.md** — Config reload behavior at runtime.
- **WINDOWS-DESKTOP.md** — Windows config locations.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.1.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Config Team |
