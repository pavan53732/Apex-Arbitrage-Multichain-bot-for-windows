---
metadata_schema_version: 1.0
document_id: DOC-0247
title: Plugin SDK
plane: Product Specification
domain: Plugins
class: Specification
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/plugins/plugin-sdk.md
related_concepts:
  - CONCEPT-0247
dependencies: []
consumers:
  - DOC-0248
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Plugins
type: CONTRACT
purpose: Defines plugin SDK.
scope: Plugin development.
---

# Plugin SDK

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-29 | **Owner:** Runtime Team

## Purpose
Defines the Plugin SDK — manifest format, lifecycle hooks, versioning rules, sandbox and security constraints, API stability, and extension patterns.

---

## 1. Plugin Manifest Format

Every plugin must include a `plugin.yaml` manifest at its root:

```yaml
id: my-strategy-plugin
name: My Strategy Plugin
version: 1.0.0
api_version: 2.0
author: Developer Name
license: MIT

description: A strategy plugin that detects triangular arbitrage.

capabilities:
  - core.trade.signal
  - core.ohlc.data

hooks:
  on_install: scripts/install.js
  on_uninstall: scripts/uninstall.js
  on_init: index.js
  on_tick: index.js
  on_shutdown: index.js

sandbox:
  memory_limit_mb: 64
  cpu_quota_percent: 10
  network_allowed_endpoints:
    - https://api.example.com/*

settings:
  threshold:
    type: number
    default: 0.5
    description: Minimum arbitrage spread (%)
    constraints:
      min: 0.1
      max: 5.0
```

---

## 2. Lifecycle Hooks

| Hook | Trigger | Expected Return | Timeout | Failure Handling |
|------|---------|-----------------|---------|------------------|
| `onInstall` | Plugin installed | `{success: bool}` | 30s | Uninstall plugin |
| `onUninstall` | Plugin removed | `{success: bool}` | 10s | Force uninstall |
| `onInit` | Plugin loaded | `{ready: bool}` | 10s | Plugin disabled |
| `onTick` | Every trading tick (configurable) | `{signals: [...]}` or `null` | 5s | Skip tick, log warning |
| `onShutdown` | Runtime shutdown | `{success: bool}` | 5s | Force terminate |

### Hook Signatures

```
// JavaScript/TypeScript SDK
interface PluginHooks {
  onInstall(ctx: InstallContext): InstallResult;
  onUninstall(ctx: UninstallContext): UninstallResult;
  onInit(ctx: InitContext): InitResult;
  onTick(ctx: TickContext): TickResult | null;
  onShutdown(ctx: ShutdownContext): ShutdownResult;
}
```

---

## 3. SDK API Surface

| API | Category | Stability | Available Since |
|-----|----------|-----------|-----------------|
| `ctx.market.getOHLC(pair, interval, limit)` | Market data | `stable` | 1.0.0 |
| `ctx.market.getPrice(pair)` | Market data | `stable` | 1.0.0 |
| `ctx.trading.getOpenTrades()` | Trading | `stable` | 1.0.0 |
| `ctx.wallet.getBalance(chain)` | Wallet | `beta` | 2.0.0 |
| `ctx.storage.get(key)` | Storage | `stable` | 1.0.0 |
| `ctx.storage.set(key, value)` | Storage | `stable` | 1.0.0 |
| `ctx.network.fetch(url, options)` | Network | `beta` | 2.0.0 |
| `ctx.notify.send(message, level)` | Notification | `stable` | 1.0.0 |
| `ctx.log.info/warn/error(message)` | Logging | `stable` | 1.0.0 |

---

## 4. Versioning Rules

- Plugin `version` follows semver independently of host version.
- Plugin `api_version` must be >= host's minimum supported API version.
- If `api_version` is incompatible, plugin fails to load with `API_VERSION_MISMATCH`.
- Plugin minor/patch updates are backward-compatible and auto-update.
- Plugin major updates require operator re-approval (capabilities may change).

---

## 5. Distribution & Signing

- Plugins are distributed as `.aplx` (Apex Plugin Archive) — a signed ZIP archive.
- Signing: Ed25519 signature over the manifest + content hash.
- Plugin store verifies signature against the developer's public key on the marketplace.
- Unsigned plugins can load in developer mode only (`plugin.allow_unsigned: true`).

---

## Cross-References

- **PLUGIN-LIFECYCLE.md** — Full plugin lifecycle state machine.
- **PLUGIN-SANDBOX-CONTRACT.md** — Sandbox isolation and capability system.
- **PLUGIN-MARKETPLACE.md** — Distribution marketplace.
- **TRUST-BOUNDARIES.md** — Plugin trust domain T4.
- **CONFIGURATION-REFERENCE.md** — Plugin config keys (`plugin.*`).

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Runtime Team |
