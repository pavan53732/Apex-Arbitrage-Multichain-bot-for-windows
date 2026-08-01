---
metadata_schema_version: 1.0
document_id: DOC-0305
title: RPC Manager
plane: Product Specification
domain: Market
class: Specification
authority: Canonical
status: Active
owner: Runtime Team
version: 2.0.0
canonical_source: docs/apex-app-docs/market/connectivity/rpc-manager.md
related_concepts:
  - CONCEPT-0305
dependencies: []
consumers:
  - DOC-0411
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-01
concept_role: Owner
owned_domains:
  - Market
type: CONTRACT
purpose: "Defines RPC management, rate limiting, and RPC lifecycle."
scope: RPC management for runtime components.
---

# Rpc Manager

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-29 | **Owner:** Runtime Team

## 0. Provider Trust Boundaries

### RPC Authority Classification
**Trust Level:** MEDIUM | **Authority:** CONNECTIVITY_AUTHORITY

**RPC Role:**
- ✅ Provide blockchain connectivity
- ✅ Submit transactions to mempool
- ✅ Query chain state and balances
- ✅ Provide gas estimates
- ❌ NOT pricing authority
- ❌ NOT validation authority
- ❌ NOT execution authority

### Critical Invariants
- **RPC providers are connectivity only** — they don't determine trade outcomes
- **Multi-RPC redundancy required** — never rely on single RPC provider
- **RPC disagreement handled by consensus** — use fastest healthy RPC for queries

### RPC Provider Tiers
**Tier 1 (HIGH RELIABILITY):**
- Alchemy
- Infura
- QuickNode
- Ankr

**Tier 2 (MEDIUM RELIABILITY):**
- Cloudflare
- Public RPC endpoints
- Self-hosted nodes

**Tier 3 (LOW RELIABILITY - Fallback Only):**
- Free public RPCs
- Untrusted third-party RPCs

### RPC Health Monitoring
- Track latency, success rate, and error rate
- Automatic failover on health degradation
- Minimum 2 healthy RPCs required for Phase 3

---

## Purpose
Authoritative owner for rpc manager.

## Scope
Cross-cutting platform governance.

## Responsibilities
Define ownership, contracts, lifecycle, validation, and cross-references.

## Cross-references
- `../../architecture/apex-os.md`
- `../../architecture/architecture.md`

## Operational Contract
Defines provider pool management, health, rotation, failover, latency, routing, and rate-limit handling.

## Example
A slow RPC endpoint is rotated out after repeated latency breaches.

## Required details
- Define endpoint config, websocket support, retry, and proxy handling.
- Define failover and custom RPC registration.

## RPC contract
- Define endpoint registration, websocket support, retry policy, and proxy handling.
- Define failover, health scoring, and custom endpoint validation.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Runtime Team |
