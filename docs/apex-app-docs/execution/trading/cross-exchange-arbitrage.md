---
metadata_schema_version: 1.0
document_id: DOC-0287
title: Cross Exchange Arbitrage
plane: Product Specification
domain: Execution
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/execution/trading/cross-exchange-arbitrage.md
related_concepts:
  - CONCEPT-0287
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Execution
type: REFERENCE
purpose: Cross Exchange Arbitrage documentation.
scope: Reference documentation.
---

# Cross-Exchange Arbitrage

## Document type
Document type: [CONTRACT]

## Purpose
Defines how arbitrage opportunities are coordinated across multiple exchanges or venues.

## Ownership
- Owns multi-venue arbitrage coordination, leg ordering, and atomicity expectations.
- Does not own provider selection, which belongs to routing and execution owners.

## Execution contract
- Opportunity detection compares quotes across venues and rejects stale or non-arbitrageable sets.
- Leg sequencing is deterministic and derived from route scoring; legs are dispatched in order.
- Atomicity is best-effort with explicit expectations: a leg that cannot fill is handled per the partial-fill rules.
- Failure rollback reverses completed legs where possible and reconciles the remainder.

## Partial fill and reconciliation
- A partial fill is recorded against the order and reconciled after execution.
- Reconciliation compares executed legs against the plan; drift is surfaced to the execution lifecycle.
- An unexecutable leg does not silently cancel the opportunity; it is reported with its reason.

## Leg ordering
- Leg order is derived from route scoring and declared in the plan.
- Each leg carries its own validation gates before dispatch.
- A leg is dispatched only while the arbitrage window is valid.

## Atomicity expectations
- Cross-venue atomicity is best effort; the contract defines what is guaranteed.
- Partial fills are reconciled after execution.
- A failed leg does not cancel the opportunity silently; it is reported with its reason.

## Monitoring
- Leg fills and reconciliation are monitored per the operations contracts.

## Safety controls
- No leg is dispatched without a valid arbitrage window and passing risk gates.
- Total exposure across legs is bounded by the risk engine before dispatch.
- A venue that becomes unreliable is excluded from future leg selection until revalidated.
- Partial fills are reconciled before a follow-up leg is opened.
- Every multi-venue execution is recorded with its leg plan for audit.
- A cross-venue imbalance that cannot be reconciled is escalated rather than absorbed.

## Cross-references
- `../../market/dex/dex-integration.md`
- `../transactions/execution-lifecycle.md`
- `./trading-lifecycle.md`
- `../risk-policy/risk-engine.md`
- `./arbitrage-window-manager.md`

## Operational Contract

This document owns multi-venue arbitrage coordination, leg ordering, and atomicity expectations. Venue data is owned by market/DEX owners; route selection is owned by routing; execution mechanics are owned by the execution lifecycle. This document coordinates across them.

## Example
A two-leg opportunity dispatches leg one, records a partial fill, reconciles it, and either completes leg two or reports the shortfall.
