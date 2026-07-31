---
metadata_schema_version: 1.0
document_id: DOC-0294
title: Position Management
plane: Product Specification
domain: Execution
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/execution/position-management.md
related_concepts:
  - CONCEPT-0294
dependencies:
  - DOC-0282
  - DOC-0291
  - DOC-0293
consumers:
  - DOC-0049
  - DOC-0285
  - DOC-0293
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: Position Management documentation.
scope: Reference documentation.
---

# Position Management

## Document type
This document is an overview, reference, or index as noted below.

# Position Management

## Purpose
Tracks active positions, exposure, cost basis, unrealized and realized PnL, and position risk.

## Responsibilities
- Maintain position open, scale, reduce, close, and reconcile lifecycle.
- Tie positions to orders and transactions.
- Publish position risk and accounting state.

## Cross-references
- `./order-management.md`
- `./portfolio-management.md`
- `./risk-engine.md`

## Operational Contract
Defines position creation, sizing, adjustment, risk limits, and closure handling.

## Example
A position is reduced when exposure breaches policy.
