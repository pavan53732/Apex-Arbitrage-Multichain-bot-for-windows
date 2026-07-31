---
metadata_schema_version: 1.0
document_id: DOC-0320
title: Market Session
plane: Product Specification
domain: Market
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/market/market-session.md
related_concepts:
  - CONCEPT-0320
dependencies:
  - DOC-0296
  - DOC-0318
  - DOC-0319
consumers:
  - DOC-0049
  - DOC-0310
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: Market Session documentation.
scope: Reference documentation.
---

# Market Session

## Document type
This document is an overview, reference, or index as noted below.

# Market Session

## Purpose
Defines the market condition labels used to guide strategy selection and scheduling.

## Regimes
Trending, volatile, quiet, congested, recovery, high MEV.

## Cross-references
- `./market-regime-detection.md`
- `./market-intelligence.md`
- `../execution/strategy-rotation.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
