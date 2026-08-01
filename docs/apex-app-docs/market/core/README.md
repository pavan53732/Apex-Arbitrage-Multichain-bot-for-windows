---
metadata_schema_version: 1.0
document_id: DOC-0412
title: Market Core README
plane: Product Specification
domain: Market
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/market/core/market-data.md
related_concepts:
  - CONCEPT-0317
dependencies:
  - DOC-0317
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Market Core

## Purpose and scope

Market data, market intelligence, market sessions, and regime detection documentation.

## What belongs here

Market data and intelligence owner documents and references.

## What does not belong here

Routing, token registry, chain registry, and execution behavior unless referenced by market core concepts.

## Expected document classes

- Index
- Specification
- Reference
- Registry where this subdomain owns domain records

## Canonical boundaries

This folder indexes market documents in this subdomain and defers behavior to canonical owner documents identified by metadata and registry entries.

## Documents

| Document | Class |
| --- | --- |
| [Market Data](market-data.md) | Reference |
| [Market Intelligence](market-intelligence.md) | Reference |
| [Market Regime Detection](market-regime-detection.md) | Reference |
| [Market Session](market-session.md) | Reference |

## Adjacent domains

Adjacent domains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
