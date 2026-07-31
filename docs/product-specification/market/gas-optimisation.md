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
canonical_source: docs/product-specification/market/gas-optimisation.md
related_concepts:
  - CONCEPT-0315
dependencies:
  - DOC-0280
  - DOC-0299
  - DOC-0322
consumers:
  - DOC-0049
  - DOC-0299
  - DOC-0302
  - DOC-0304
  - DOC-0306
  - DOC-0310
  - DOC-0321
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
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

## Cross-references
- `../execution/execution-engine.md`
- `../execution/transaction-lifecycle.md`
- `./mev-protection.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
