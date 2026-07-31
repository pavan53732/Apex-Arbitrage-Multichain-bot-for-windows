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
canonical_source: docs/product-specification/execution/cross-exchange-arbitrage.md
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

# Cross Exchange Arbitrage

## Document type
This document is an overview, reference, or index as noted below.

# Cross-Exchange Arbitrage

## Purpose
Defines how arbitrage opportunities are coordinated across multiple exchanges or venues.

## Ownership
- Owns multi-venue arbitrage coordination, leg ordering, and atomicity expectations.
- Does not own provider selection, which belongs to routing and execution owners.

## Execution contract
- Must define opportunity detection, quote comparison, leg sequencing, and failure rollback.
- Must specify partial fill handling and reconciliation rules.

## Cross-references
- `../market/dex/dex-integration.md`
- `./execution-lifecycle.md`
- `./trading-lifecycle.md`
- `./risk-engine.md`

## Canonical ownership
This document defers to the canonical owners for implementation, policy, and schema details.
