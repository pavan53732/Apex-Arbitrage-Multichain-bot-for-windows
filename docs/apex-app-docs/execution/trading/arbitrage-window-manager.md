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
version: 1.1.0
canonical_source: docs/apex-app-docs/execution/trading/arbitrage-window-manager.md
related_concepts:
  - CONCEPT-0278
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - Execution
type: CONTRACT
purpose: Arbitrage Window Manager documentation.
scope: Reference documentation.
---

# Arbitrage Window Manager

## Version
**Version:** 1.1.0 | **Status:** Canonical | **Last Updated:** 2026-08-02 | **Owner:** Runtime Team

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

## Failure Handling

Window failures are time-critical: an arbitrage window that cannot be trusted is
invalidated rather than extended. Extending a window to accommodate a failure
would execute against market state the window no longer describes.

| Failure | Detection | Outcome |
| --- | --- | --- |
| Latency budget exceeded on a leg | Per-leg timing check against the window's budget | The window is invalidated; remaining legs are not dispatched |
| Opportunity becomes stale mid-flow | Price or liquidity revalidation fails before dispatch | The window transitions to expired and the opportunity is withdrawn from ranking |
| Window expires during execution | Expiry timer fires after dispatch | Expiry does not cancel in-flight legs; ownership of the in-flight transaction passes to the execution path, and no further legs are opened |
| Clock or timing desynchronization | Timing synchronization check fails | Window creation is suspended until synchronization is re-established, because expiry cannot be evaluated correctly without it |
| Detection input unavailable | Upstream market data missing or stale | No window is created; an absent input is never treated as an unchanged input |

Invalidated windows are recorded with their invalidation cause so that repeated
staleness in a venue or route is observable rather than appearing as an absence
of opportunities.

## Cross-references
- `./trading-lifecycle.md`
- `../../market/opportunities/opportunity-ranking.md`
- `../risk-policy/risk-engine.md`
- `../../runtime/orchestrator.md`

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.1.0 | 2026-08-02 | Added Failure Handling section defining window invalidation on latency breach, staleness, expiry, desynchronisation, and missing detection input. | Runtime Team |
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Runtime Team |
