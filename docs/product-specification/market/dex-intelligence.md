---
metadata_schema_version: 1.0
document_id: DOC-0314
title: DEX Intelligence
plane: Product Specification
domain: Market
class: Reference
authority: Canonical
status: Active
owner: Trading Team
version: 1.0.0
canonical_source: docs/product-specification/market/dex-intelligence.md
related_concepts:
  - CONCEPT-0314
dependencies:
  - DOC-0252
  - DOC-0364
consumers:
  - DOC-0049
  - DOC-0310
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: Dex Intelligence documentation.
scope: Reference documentation.
---

# Dex Intelligence

## Document type
This document is an overview, reference, or index as noted below.

# DEX Intelligence

## Purpose
Defines DEX-level liquidity, TVL, fees, latency, pools, performance, and supported-token views.

## Cross-references
- `../interfaces/domain-model.md`
- `../reference/metrics.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Arbitrage intelligence
- Must define DEX ranking factors, fee sensitivity, and route quality signals.
- Must define how intelligence feeds arbitrage opportunity detection.
