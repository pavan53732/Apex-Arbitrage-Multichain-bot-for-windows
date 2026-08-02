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
version: 2.1.0
canonical_source: docs/apex-app-docs/market/connectivity/rpc-manager.md
related_concepts:
  - CONCEPT-0305
dependencies: []
consumers:
  - DOC-0411
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
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
**Version:** 2.1.0 | **Status:** Canonical | **Last Updated:** 2026-08-02 | **Owner:** Runtime Team

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

## Failure Handling

RPC providers are connectivity only, so a provider failure is a routing problem
rather than a trading signal. The manager fails over between endpoints and never
allows a single provider's response to stand as authoritative.

| Failure | Detection | Outcome |
| --- | --- | --- |
| Endpoint latency breach | Latency exceeds threshold across repeated samples | The endpoint is rotated out of the active pool and health-scored down |
| Endpoint returns errors | Error rate exceeds threshold | Automatic failover to the next healthy endpoint in tier order |
| Rate limit reached | HTTP 429 or provider-specific limit response | Requests back off and shift to another endpoint; the limited endpoint is rested rather than retried immediately |
| WebSocket disconnect | Subscription drops | Reconnect with backoff; missed state is re-queried rather than assumed unchanged |
| RPC disagreement | Responses conflict across endpoints | Resolved by consensus per the trust boundary rules; a single endpoint never decides |
| Fewer than two healthy RPCs | Health monitor reports pool below minimum | Phase 3 autonomous execution is blocked, as the redundancy invariant is unmet |
| All endpoints unhealthy for a chain | No endpoint passes health checks | The chain is reported unavailable to consumers; the manager does not fabricate a response |
| Transaction submission fails | Submission rejected by the endpoint | Resubmission is attempted through a different endpoint; submission is never treated as successful without confirmation |

Because the RPC layer holds no pricing, validation, or execution authority, a
failover never changes a trade decision — it only changes which endpoint served
the query.

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
| 2.1.0 | 2026-08-02 | Added Failure Handling section defining failover, rate-limit, disconnect, disagreement, and redundancy-floor behaviour. | Runtime Team |
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Runtime Team |
