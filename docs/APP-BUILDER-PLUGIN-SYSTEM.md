# App Builder Plugin System

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.1.0 | **Status:** Canonical | **Last Updated:** 2026-07-27 | **Owner:** Plugin Team

## Purpose
Defines how the desktop app discovers, registers, sandboxes, versions, loads, unloads, and updates plugins — with plugin manifest contract, signature requirements, version compatibility, hot reload behavior, failure isolation, uninstall behavior, and API stability policy.

---

## 1. Plugin Manifest Contract

Every plugin must include a `plugin.yaml` manifest (see `PLUGIN-SDK.md` §1 for format). This document adds governance rules:

| Manifest Field | Required | Validation | Governance Rule |
|---------------|----------|------------|----------------|
| `id` | Yes | Globally unique; must match `[a-z0-9-]+` pattern | Cannot conflict with any existing plugin ID in registry |
| `version` | Yes | Semver (MAJOR.MINOR.PATCH) | Major version bump requires operator re-approval; minor/patch auto-updated |
| `api_version` | Yes | Must be >= host minimum supported API version | Incompatible api_version → load rejected with API_VERSION_MISMATCH |
| `capabilities` | Yes | Each capability must exist in SYSTEM-CAPABILITY-REGISTRY | Requesting undeclared capability → security.violation event |
| `sandbox.memory_limit_mb` | Yes | 16–4096 | Cannot exceed `plugin.sandbox.memory_limit_mb` global setting |
| `sandbox.cpu_quota_percent` | Yes | 1–100 | Cannot exceed `plugin.sandbox.cpu_quota_percent` global setting |
| `sandbox.network_allowed_endpoints` | No (default: none) | URL patterns with wildcard | If `plugin.allow_network: false`, this field is ignored (network blocked) |

---

## 2. Signature Requirements

| Requirement | Description | Enforcement |
|-------------|-------------|-------------|
| All marketplace plugins must be signed | Ed25519 signature over manifest + content hash | Plugin store verifies signature before listing; host verifies before loading |
| Unsigned plugins blocked in production mode | `plugin.allow_unsigned: false` (default) | Unsigned plugins fail VALIDATING → REJECTED |
| Unsigned plugins allowed in developer mode only | `plugin.allow_unsigned: true` (dev override) | Dashboard shows "Developer Mode" warning banner |
| Developer public key registered on marketplace | Key stored in marketplace database; verified on each download | Signature mismatch → load rejected |

---

## 3. Version Compatibility

| Compatibility Rule | Description |
|--------------------|-------------|
| api_version must be >= minimum supported | Host defines minimum API version; older API versions cannot load |
| Major version bump → re-approval | Plugin major update may change capabilities; operator must review and re-approve |
| Minor/patch → auto-update | If `plugin.auto_update: true`, minor/patch updates auto-install without operator approval |
| Breaking API changes → migration window | 2 release cycles for consumers to migrate; old API version still supported during window |
| Plugin version independent of host version | Plugin `version` (semver) tracks independently; `api_version` tracks host compatibility |

---

## 4. Hot Reload Behavior

| Scenario | Behavior |
|----------|----------|
| Plugin code updated (minor/patch) | If auto_update enabled: SUSPENDED → UPDATING → ACTIVE (new version loaded in sandbox) |
| Plugin config changed | Hot-reloadable config keys applied via config.updated event to sandbox IPC |
| Plugin manifest updated | Requires full reload: ACTIVE → SUSPENDED → UNLOADING → LOADING → ACTIVE |
| Host config affects plugins (e.g., sandbox limits changed) | All active plugins receive config.updated; sandbox limits applied on next tick |

---

## 5. Failure Isolation

| Isolation Mechanism | Description | Enforcement |
|--------------------|-------------|-------------|
| Process isolation | Each plugin runs in separate process (not thread) | OS-level; no shared memory between plugins |
| Sandbox resource limits | Memory and CPU quotas enforced per plugin | OS enforcement (job objects on Windows) |
| IPC typed channels | Plugin can only communicate via typed IPC messages to host | IPC gateway validates every message against manifest capabilities |
| Capability grants | Plugin cannot access resources beyond declared capabilities | Capability enforcer blocks unauthorized IPC calls |
| Network filter | Plugin network calls routed through host proxy with capability check | Sandbox network filter blocks if `plugin.allow_network: false` |
| Filesystem isolation | Plugin can only read/write within its sandbox directory | OS filesystem ACL; no access to host directories |
| No cross-plugin communication | Plugins cannot communicate with each other directly | Process isolation; no shared IPC channels between plugins |

### Failure Handling
| Failure | Isolation | Recovery |
|---------|-----------|----------|
| Plugin crash (process exit) | Only this plugin affected; no cascade | Auto-restart once; second crash → plugin disabled |
| Plugin memory limit exceeded | Sandbox process killed; no host memory impact | Plugin SUSPENDED; operator notified |
| Plugin CPU quota exceeded | Sandbox throttled; host continues normally | Plugin tick rate reduced |
| Plugin security violation | Sandbox process terminated immediately; security.violation event | Plugin REJECTED; operator must re-approve |
| Plugin IPC call exceeds capabilities | IPC gateway blocks call; violation logged | Warning on first; REJECTED on repeated |

---

## 6. Uninstall Behavior

| Step | Action | Persistence |
|------|--------|-------------|
| 1 | Send shutdown signal to sandbox process | — |
| 2 | Wait for graceful exit (unload_timeout_ms: 10s) | — |
| 3 | Force terminate if timeout exceeded | — |
| 4 | Delete sandbox directory and plugin files | Disk cleanup |
| 5 | Remove registry entry from plugin registry | DB delete |
| 6 | Remove capability grants from capability enforcer | In-memory update |
| 7 | Close IPC channels | Process cleanup |
| 8 | Notify dashboard (plugin.removed event) | UI update |
| 9 | Persist uninstall record in audit log | Audit trail |

---

## 7. API Stability Policy

| API Category | Stability Level | Change Policy | Breaking Change Window |
|-------------|----------------|---------------|----------------------|
| `ctx.market.*` | Stable | Additive only; no removals | 2 release cycles |
| `ctx.trading.*` | Stable | Additive only; no removals | 2 release cycles |
| `ctx.storage.*` | Stable | Additive only; no removals | 2 release cycles |
| `ctx.log.*` | Stable | Additive only; no removals | 2 release cycles |
| `ctx.notify.*` | Stable | Additive only | 2 release cycles |
| `ctx.wallet.*` | Beta | May change; backward compat attempted | 1 release cycle |
| `ctx.network.*` | Beta | May change; backward compat attempted | 1 release cycle |
| Internal APIs | Experimental | No stability guarantee | No window |
| Plugin manifest format | Stable (v2) | Additive only; new fields optional | 2 release cycles |

### Deprecation Policy
- Deprecated APIs are marked with `deprecated_since` and `removal_scheduled` in the API surface.
- Deprecated APIs remain functional for 2 release cycles after deprecation.
- Removal requires major API version bump.

---

## Cross-References

- **PLUGIN-SDK.md** — SDK specification, manifest format, hooks.
- **PLUGIN-LIFECYCLE.md** — Plugin lifecycle management.
- **PLUGIN-STATE-MACHINE.md** — State machine for plugin lifecycle.
- **PLUGIN-SANDBOX-CONTRACT.md** — Sandbox isolation details.
- **PLUGIN-MARKETPLACE.md** — Distribution and marketplace.
- **TRUST-BOUNDARIES.md** — Plugin trust domain T4.
- **APP-BUILDER-WORKFLOW.md** — Build pipeline for plugins.
- **CONFIGURATION-REFERENCE.md** — `plugin.*` config keys.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.1.0 | 2026-07-27 | Full plugin system contract: manifest governance, signatures, versioning, hot reload, failure isolation, uninstall, API stability policy | Plugin Team |
| 1.0.0 | 2025-01-15 | Initial stub (6 lines) | Plugin Team |
