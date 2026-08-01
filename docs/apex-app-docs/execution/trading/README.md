---
metadata_schema_version: 1.0
document_id: DOC-0419
title: Execution Trading README
plane: Product Specification
domain: Execution
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/execution/trading/trading-engine.md
related_concepts:
  - CONCEPT-0284
dependencies:
  - DOC-0284
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Execution Trading

## Purpose and scope

Trading engine, trading lifecycle, strategies, arbitrage, and trade explanation documentation.

## What belongs here

Trading orchestration, strategy catalog, arbitrage references, and trading lifecycle documents.

## What does not belong here

Transaction submission internals, wallet portfolio state, and market data ownership.

## Expected document classes

- Index
- Specification
- Reference
- Policy where this subdomain owns execution constraints

## Canonical boundaries

This folder indexes execution documents in this subdomain and defers behavior to canonical owner documents identified by metadata and registry entries.

## Documents

| Document | Class |
| --- | --- |
| [Arbitrage Window Manager](arbitrage-window-manager.md) | Specification |
| [Cross Exchange Arbitrage](cross-exchange-arbitrage.md) | Reference |
| [Strategies](strategies.md) | Reference |
| [Strategy Rotation](strategy-rotation.md) | Reference |
| [Trade Explainer](trade-explainer.md) | Reference |
| [Trading Engine](trading-engine.md) | Specification |
| [Trading Lifecycle](trading-lifecycle.md) | Reference |

## Adjacent domains

Adjacent domains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
