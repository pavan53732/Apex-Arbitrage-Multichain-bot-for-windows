---
metadata_schema_version: 1.0
document_id: DOC-0304
title: Routing Engine
plane: Product Specification
domain: Market
class: Specification
authority: Canonical
status: Active
owner: Trading Team
version: 1.0.0
canonical_source: docs/product-specification/market/routing-engine.md
related_concepts:
  - CONCEPT-0304
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
purpose: Defines routing engine.
scope: Order routing logic.
---

# Routing Engine

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-29 | **Owner:** Trading Team

## Purpose
Determines optimal execution paths across DEXs, chains, pools, and bridges.

## Ownership
- Owns route construction, route ranking, and route invalidation rules.
- Produces execution-ready route plans for the execution engine.

## Responsibilities
- Build route candidates from market data and execution constraints.
- Rank routes by edge, gas, slippage, liquidity, finality, and MEV exposure.
- Reject invalid, stale, or unsafe routes.
- Produce route plans with stable fingerprints and validation metadata.

## Route lifecycle
Candidate -> Scored -> Validated -> Approved -> Bound -> Invalidated -> Replaced.

### Transition rules
- Candidate -> Scored after quote and liquidity analysis completes.
- Scored -> Validated after gas, slippage, MEV, and chain checks pass.
- Validated -> Approved only after execution-risk gating passes.
- Approved -> Bound when the route is attached to an execution plan.
- Bound -> Invalidated when market, chain, or wallet state changes materially.
- Any route can move to Replaced only via a new validated route with a new fingerprint.

## Inputs
- Market data.
- Liquidity analysis.
- Gas estimates.
- Slippage model.
- MEV protection signals.
- Chain suitability and wallet readiness.

## Outputs
- Route fingerprints.
- Ranked route candidates.
- Reject reasons.
- Execution-ready route plans.

## Idempotency and retry
- The same input snapshot must yield the same route ranking.
- Re-evaluating a route under unchanged inputs must preserve the same fingerprint.
- Retry of route computation must not mutate state.

## Failure and recovery
- Stale quotes, invalid gas data, or unsafe MEV exposure must reject the route.
- If route validity is lost after binding, execution must revalidate before submission.
- If no safe route exists, return a hard reject rather than a degraded unsafe path.

## Persistence
- Persist route fingerprint, scoring breakdown, reject reasons, chain id, DEX ids, pool ids, and input snapshot hash.
- Persist route invalidation events and replacement lineage.

## Monitoring
- Route compute latency.
- Route rejection rate.
- Route invalidation rate.
- Re-ranking count.
- Fingerprint stability count.

## Cross-references
- `./market-data.md`
- `./liquidity-analysis.md`
- `./slippage-model.md`
- `./gas-optimisation.md`
- `./mev-protection.md`
- `../execution/execution-engine.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Routing behavior
- Must define failover, chain changes, and proxy-aware routing.

## Required details
- Define routing failover and proxy-aware decisions.

## Routing rules
- Define route selection, failover, and proxy-aware decision inputs.
- Define handling for changing network conditions.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Trading Team |
