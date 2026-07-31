---
metadata_schema_version: 1.0
document_id: DOC-0321
title: MEV Protection Detail
plane: Product Specification
domain: Market
class: Reference
authority: Canonical
status: Active
owner: AI Team
version: 1.0.0
canonical_source: docs/product-specification/market/mev-protection-detail.md
related_concepts:
  - CONCEPT-0321
dependencies:
  - DOC-0280
  - DOC-0299
  - DOC-0315
  - DOC-0322
consumers:
  - DOC-0049
  - DOC-0310
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: Mev Protection Detail documentation.
scope: Reference documentation.
---

# Mev Protection Detail

## Document type
This document is an overview, reference, or index as noted below.

# MEV Protection Detail

## Purpose
Defines the detailed MEV protection behavior required for arbitrage execution.

## Ownership
- Owns private transaction routing, sandwich risk mitigation, and inclusion strategy.
- Does not own general execution policy or gas optimization policy.

## MEV contract
- Must define private mempool handling, relay selection, and fallback behavior.
- Must define simulation checks and protection failure behavior.

## Cross-references
- `./mev-protection.md`
- `./gas-optimisation.md`
- `../execution/execution-engine.md`
- `../execution/transaction-lifecycle.md`
