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
version: 1.0.0
canonical_source: docs/product-specification/market/rpc-manager.md
related_concepts:
  - CONCEPT-0305
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
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

## Purpose
Authoritative owner for rpc manager.

## Scope
Cross-cutting platform governance.

## Responsibilities
Define ownership, contracts, lifecycle, validation, and cross-references.

## Cross-references
- `../architecture/apex-os.md`
- `../architecture/architecture.md`

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
