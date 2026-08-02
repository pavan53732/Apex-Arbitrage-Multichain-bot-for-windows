---
metadata_schema_version: 1.0
document_id: DOC-0265
title: Cache Manager
plane: Product Specification
domain: Data
class: Specification
authority: Canonical
status: Active
owner: Runtime Team
version: 1.1.0
canonical_source: docs/apex-app-docs/data/state/cache-manager.md
related_concepts:
  - CONCEPT-0265
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - Data
type: CONTRACT
purpose: "Defines cache management, eviction policies, and cache lifecycle."
scope: Caching for runtime components.
---

# Cache Manager

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.1.0 | **Status:** Canonical | **Last Updated:** 2026-08-02 | **Owner:** Runtime Team

## Purpose
Authoritative owner for cache manager behavior.

## Scope
Cross-cutting platform governance for cache ownership, TTL, invalidation, compression, and recovery.

## Responsibilities
Define ownership, contracts, lifecycle, validation, and cross-references for all cache domains.

## Cache domains
- Price caches.
- Pool caches.
- ABI caches.
- Token metadata caches.
- AI context caches.
- RPC response caches.

## Cache contract
- Cache keys must be deterministic and namespaced by domain, chain, provider, and version.
- Invalidation occurs on chain updates, provider changes, schema changes, and TTL expiry.
- Eviction must prefer stale, low-value, or least-recently-used entries under pressure.
- Consistency checks must fail closed when cache freshness is uncertain.
- TTL and freshness windows are defined per data domain; a stale entry is never served as fresh.
- A stale price cache entry is invalidated after a new market tick arrives.

## Recovery
- A cache that cannot be validated is rebuilt from source rather than served.
- Cache corruption triggers reload from the durable source and logs the event.

## Freshness
- Freshness windows are defined per data domain; a stale entry fails closed on read.
- Cache consistency is verified on read whenever freshness is uncertain.

## Cross-references
- `../../architecture/apex-os.md`
- `../../architecture/architecture.md`
- `./state-management.md`

## Operational Contract

Defines cache ownership, TTL, invalidation, compression, and recovery for price, pool, ABI, token, AI, and RPC caches. Caches are acceleration, never the source of truth; the durable stores and live sources own truth.

## Example
A stale price cache entry is invalidated after a new market tick arrives, and a consistency failure blocks reads rather than serving stale data.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.1.0 | 2026-08-02 | Expanded canonical content: replaced placeholder directives and generic boilerplate with grounded ownership, rules, lifecycle, failure, and cross-reference detail. | Runtime Team |
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Runtime Team |
