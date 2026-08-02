---
metadata_schema_version: 1.0
document_id: DOC-0315
title: Gas Optimisation
plane: Product Specification
domain: Market
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/market/routing/gas-optimisation.md
related_concepts:
  - CONCEPT-0315
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Market
type: REFERENCE
purpose: Gas Optimisation documentation.
scope: Reference documentation.
---

# Gas Optimisation

## Document type
This document is an overview, reference, or index as noted below.

# Gas Optimisation

## Purpose
Defines gas estimation, repricing, replacement, batching, and submission timing rules.

## Ownership
- Owns gas estimation, fee policy, replacement thresholds, and submission timing.
- Feeds routing, execution, and transaction lifecycle.

## Responsibilities
- Estimate source and destination gas costs.
- Select fee caps, priority fees, and replacement thresholds.
- Decide when batching or single-shot execution is preferred.
- Expose gas safety data to routing and execution.

## Rules
- Gas policy must be bounded by operator configuration.
- Repricing must preserve nonce safety and idempotency.
- Fee bumps must not violate slippage or edge thresholds.
- Gas estimates must be refreshed when fee markets move materially.

## Outputs
- Gas estimate.
- Fee cap.
- Priority fee.
- Replacement threshold.
- Batching decision.

## Persistence
- Persist gas model version, estimate inputs, selected fees, replacement decisions, and route fingerprint.

## Monitoring
- Gas estimate error.
- Replacement count.
- Over-budget rejection count.

## Governance
- Gas policy is bounded by operator configuration; a policy change is validated before use.
- Fee caps and priority fees are selected within policy limits.
- Persisted gas decisions carry the gas model version and route fingerprint for audit.
- A gas decision that would breach slippage or edge thresholds is rejected before submission.
- Submission timing respects the arbitrage window of the opportunity.

## Cross-references
- `../../execution/transactions/execution-engine.md`
- `../../execution/transactions/transaction-lifecycle.md`
- `./mev-protection.md`

## Operational Contract
This document owns gas estimation, fee policy, replacement thresholds, and submission timing. Execution mechanics are owned by the execution engine; this document supplies the gas decisions it uses.

## Example
A route is repriced with a bounded fee bump that preserves nonce safety and respects the edge threshold; the decision is persisted with the gas model version and route fingerprint.
