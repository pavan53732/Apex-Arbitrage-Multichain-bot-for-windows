# Plugin Sandbox Contract

## Document type
Document type: [CONTRACT]

## Version
**Version:** 0.2.0 | **Status:** Draft | **Last Updated:** 2026-07-27 | **Owner:** Plugin Team

## Purpose
Defines the plugin sandbox contract — filesystem, memory, IPC, permissions, resource, network, and AI access boundaries for plugins.

---

## 1. Sandbox Isolation Model

| Isolation Layer | Mechanism | Guarantee |
|-----------------|-----------|-----------|
| Process boundary | Each plugin runs in a separate OS process | No shared memory between plugins |
| Filesystem | Restricted to `plugins/<plugin_id>/data/` | No access outside plugin directory |
| Network | Blocked unless proxied through host | Plugin cannot initiate connections |
| IPC | Typed IPC channel — host → plugin only | Plugin cannot bypass IPC bridge |
| Resource | CPU/memory quotas enforced by OS scheduler | Plugin cannot starve the host |

---

## 2. Plugin Capability System

Each plugin declares required capabilities in its manifest. Capabilities are granted at load time by the operator.

| Capability | Description | Risk Level | Grant Required? |
|------------|-------------|------------|-----------------|
| `core.trade.signal` | Provide trading signals | Low | No |
| `core.ohlc.data` | Access OHLC market data | Low | No |
| `core.wallet.read` | Read wallet balance | Medium | Yes |
| `core.analysis` | Run analysis on trade history | Medium | Yes |
| `core.market.data` | Subscribe to real-time price feeds | Low | No |
| `core.notification` | Send dashboard notifications | Low | No |
| `core.network.http` | Make external HTTP requests | High | Yes (with URL allowlist) |
| `core.network.ws` | Open WebSocket connections | High | Yes (with URL allowlist) |
| `core.storage.read` | Read plugin storage | Low | No |
| `core.storage.write` | Write plugin storage | Low | No |
| `core.trade.execute` | Execute trades | Critical | Yes (operator override) |

---

## 3. API Stability Policy

### Versioning
- Plugin API follows semantic versioning: `MAJOR.MINOR.PATCH`.
- MAJOR: breaking API changes (removed/modified hooks, changed return types).
- MINOR: new API features, backward-compatible.
- PATCH: bug fixes, no API surface change.

### Compatibility Window
- The host guarantees backward compatibility for 2 MAJOR versions.
- Plugins compiled against API v1.x continue to work on host v2.x and v3.x.
- At v4.0, plugins must be recompiled against v3.x API (1-version deprecation window).

### Deprecation Process
1. API element marked `@deprecated` with `since` and `removal` version.
2. Removal version must be at least 2 MAJOR versions after deprecation.
3. Deprecated elements generate a warning at plugin load time.
4. After removal, the plugin fails to load with `API_VERSION_MISMATCH`.

### Stability Labels
| Label | Meaning | Compatibility |
|-------|---------|---------------|
| `stable` | Production-ready | Breaking changes only at MAJOR version |
| `beta` | Feature-complete, may change | MINOR version changes allowed |
| `experimental` | In development | May change at any PATCH version |
| `deprecated` | Scheduled for removal | Use only for migration |

---

## 4. Resource Limits

| Resource | Default Limit | Config Key | Enforcement |
|----------|---------------|------------|-------------|
| Memory (per plugin) | 64 MB | `plugin.sandbox.memory_limit_mb` | Process RSS cap |
| CPU (per plugin) | 10% of 1 core | `plugin.sandbox.cpu_quota_percent` | OS scheduler quota |
| Threads (per plugin) | 4 | — | Thread pool limit |
| File descriptors | 32 | — | OS rlimit |
| IPC message size | 1 MB | — | IPC bridge enforcement |
| Network requests/min | 60 | — | Rate-limited proxy |

---

## 5. Sandbox Violation Response

| Violation | Detection | Response |
|-----------|-----------|----------|
| Memory limit exceeded | RSS monitor > threshold | Kill plugin, emit `plugin.violation` event |
| CPU quota exceeded | CPU monitor > threshold for 10s | Throttle plugin, warn on repeat |
| Filesystem escape | Access outside plugin directory | Block access, emit `security.violation` |
| Unauthorized capability call | Capability check fails | Block call, emit `plugin.violation` |
| Network proxy bypass | Direct socket attempt | Block, emit `security.violation` |
| IPC message too large | Message > 1 MB | Reject message, warn plugin |
| Plugin crash | Process exit with non-zero | Auto-restart once, then disable |

---

## Cross-References

- **PLUGIN-LIFECYCLE.md** — Plugin lifecycle state machine.
- **TRACEABILITY-MATRIX.md** — Requirement-to-document mapping and governance validation.
- **PLUGIN-SDK.md** — Plugin API reference and hooks.
- **PLUGIN-MARKETPLACE.md** — Plugin distribution and signing.
- **TRUST-BOUNDARIES.md** — Trust domain T4 plugin isolation.
- **SECURITY.md** — Security integration for plugins.
- **CONFIGURATION-REFERENCE.md** — Plugin sandbox config keys (`plugin.sandbox.*`).

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 0.2.0 | 2026-07-27 | Complete sandbox contract — isolation, capabilities, API stability policy, resource limits, violation response | Plugin Team |
| 0.1.0 | 2026-07-27 | Initial stub | Plugin Team |