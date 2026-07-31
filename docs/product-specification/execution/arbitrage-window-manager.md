---
metadata_schema_version: 1.0
document_id: DOC-0278
title: Arbitrage Window Manager
plane: Product Specification
domain: Execution
class: Specification
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/execution/arbitrage-window-manager.md
related_concepts:
  - CONCEPT-0278
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Execution
type: CONTRACT
purpose: Arbitrage Window Manager documentation.
scope: Reference documentation.
---

# Arbitrage Window Manager

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-29 | **Owner:** Runtime Team

## Document type
This document is an overview, reference, or index as noted below.

# Arbitrage Window Manager

## Purpose
Defines the lifecycle of arbitrage windows from detection through expiry or execution.

## Ownership
- Owns window creation, timing budgets, expiry, and stale-opportunity invalidation.
- Does not own trade execution or route scoring.

## Window contract
- Must define latency budget per leg, expiry conditions, and timing synchronization.
- Must define what happens when the opportunity becomes stale mid-flow.

## Cross-references
- `./trading-lifecycle.md`
- `../market/opportunity-ranking.md`
- `./risk-engine.md`
- `../runtime/orchestrator.md`

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Runtime Team |
