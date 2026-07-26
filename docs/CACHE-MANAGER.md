# Cache Manager

## Purpose
Authoritative owner for cache manager.

## Scope
Cross-cutting platform governance.

## Responsibilities
Define ownership, contracts, lifecycle, validation, and cross-references.

## Cross-references
- `APEX-OS.md`
- `ARCHITECTURE.md`

## Operational Contract
Defines cache ownership, TTL, invalidation, compression, and recovery for price, pool, ABI, token, AI, and RPC caches.

## Example
A stale price cache entry is invalidated after a new market tick arrives.

## Cache contract
- Cache keys must be deterministic and namespaced by domain, chain, provider, and version.
- Invalidation occurs on chain updates, provider changes, schema changes, and TTL expiry.
- Eviction must prefer stale, low-value, or least-recently-used entries under pressure.
- Consistency checks must fail closed when cache freshness is uncertain.

## Cache limits
- Must define TTL, eviction, and freshness windows by domain.

## Required details
- Define TTL, eviction, and freshness values.
