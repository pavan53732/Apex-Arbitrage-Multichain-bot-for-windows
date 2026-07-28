---
type: REFERENCE
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Unified registry contract for chain, DEX, token, oracle, service, plugin, contract, and system capability registries — with common interface, versioning, validation, mutation, ownership, and reconciliation rules.
scope: None
last_updated: 2026-07-29
canonical_source: docs/REGISTRY-SYSTEM.md
---

# Registry System

## Document type
Document type: [REFERENCE]

## Version
**Version:** 0.2.0 | **Status:** Draft | **Last Updated:** 2026-07-27 | **Owner:** Runtime Team

## Purpose
Unified registry contract for chain, DEX, token, oracle, service, plugin, contract, and system capability registries — with common interface, versioning, validation, mutation, ownership, and reconciliation rules.

---

## 1. Registry Contract (`IRegistry`)

All registries implement the `IRegistry` interface:

```typescript
interface IRegistry<T> {
  // Query
  list(filter?: RegistryFilter): T[];
  get(id: string): T | null;
  exists(id: string): boolean;
  count(): number;

  // Mutation
  create(entry: T): RegistryResult;
  update(id: string, changes: Partial<T>): RegistryResult;
  delete(id: string): RegistryResult;

  // Lifecycle
  refresh(): Promise<RegistryRefreshResult>;
  watch(callback: RegistryChangeCallback): UnsubscribeFn;

  // Validation
  validate(entry: T): ValidationResult;
}
```

---

## 2. Registry Inventory

| Registry | Interface Type | Entries | Source of Truth | Refresh Policy | Auto-Import | Approval Required |
|----------|---------------|---------|-----------------|----------------|-------------|-------------------|
| **Chain Registry** | `IRegistry<ChainEntry>` | 20 | Built-in + RPC | On startup + manual | From RPC | Yes (new chains) |
| **DEX Registry** | `IRegistry<DEXEntry>` | 200 | Built-in + user | On startup + manual | From chain | No (auto for known) |
| **Token Registry** | `IRegistry<TokenEntry>` | 5000 | Built-in + user | On startup + manual | From chain/DEX | No (auto for known) |
| **Oracle Registry** | `IRegistry<OracleEntry>` | 50 | User-configured | On startup | No | Yes |
| **Contract Registry** | `IRegistry<ContractEntry>` | 1000 | Built-in + user | On startup | From chain | No (auto for verified) |
| **Service Registry** | `IRegistry<ServiceEntry>` | 20 | Built-in | On startup | No | No |
| **Plugin Registry** | `IRegistry<PluginEntry>` | < 50 | Plugin manager | On load/unload | From plugin store | Yes (marketplace) |
| **Capability Registry** | `IRegistry<CapabilityEntry>` | 30 | Built-in | On startup | No | No |

---

## 3. Versioning Rules

| Rule | Description |
|------|-------------|
| Schema version | Every entry has `schema_version` field. Must be backward-compatible for 2 versions. |
| Entry version | Each entry has `version` field incremented on mutation. |
| Backward compatibility | Adding optional fields is allowed. Removing or renaming fields requires a new API version. |
| Migration | On schema version bump, old entries are lazily migrated on read. |

---

## 4. Validation Rules

| Registry | Validation | Error Action |
|----------|------------|--------------|
| Chain | Chain ID > 0, RPC URL must resolve, chain name unique | Reject entry |
| DEX | Address checksummed, chain ID exists, router version supported | Reject entry |
| Token | Address checksummed, symbol ≤ 10 chars, decimals > 0 | Reject entry |
| Oracle | Feed address valid, heartbeat config present, deviation threshold set | Reject entry |
| Contract | Address checksummed, ABI parseable, chain ID exists | Reject entry |

---

## 5. Mutation Rules

| Operation | Immutable Fields | Audit Event |
|-----------|-----------------|-------------|
| Create | `id`, `schema_version`, `created_at` | `registry.entry.created` |
| Update | `id`, `schema_version` (requires migration), `created_at` | `registry.entry.updated` |
| Delete | — | `registry.entry.deleted` |

- Mutations are blocked if the entry is currently in use (trading, simulation).
- Bulk mutations are atomic (all or nothing).

---

## 6. Ownership Hierarchy

```
Source of Truth: Built-in (canonical) → User-local (overrides)
```

- Built-in entries (shipped with the app) cannot be deleted, but can be overridden.
- User-local entries take precedence over built-in entries of the same ID.
- Override metadata is stored separately (original is preserved).

---

## 7. Consistency & Reconciliation

| Trigger | Reconciliation Action |
|---------|----------------------|
| Startup | Validate all registry entries against schemas. Refresh from configured sources. |
| Manual refresh | Re-pull from external sources, merge with local overrides. |
| Chain RPC reconnect | Re-verify DEX and token entries against on-chain state. |
| Periodic (24h) | Re-verify token addresses against chain state; flag stale entries. |
| On mutation | Validate immediately, reject if invalid. |

---

## Cross-References

- **CHAIN-REGISTRY.md** — Chain-specific registry implementation.
- **DEX-REGISTRY.md** — DEX-specific registry implementation.
- **TOKEN-REGISTRY.md** — Token-specific registry implementation.
- **ORACLE-REGISTRY.md** — Oracle-specific registry implementation.
- **CONTRACT-REGISTRY.md** — Contract-specific registry implementation.
- **SERVICE-REGISTRY.md** — Service-specific registry implementation.
- **SYSTEM-CAPABILITY-REGISTRY.md** — Capability registry.
- **CONTRACT-MANAGEMENT.md** — Contract management policies.
- **CONFIGURATION-REFERENCE.md** — Registry config keys.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 0.2.0 | 2026-07-27 | Unified registry contract with IRegistry interface, 8-registry inventory, validation, mutation, ownership, reconciliation | Runtime Team |
| 0.1.0 | 2026-07-27 | Initial stub | Runtime Team |