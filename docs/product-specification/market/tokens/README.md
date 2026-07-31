---
metadata_schema_version: 1.0
document_id: DOC-0416
title: Market Tokens README
plane: Product Specification
domain: Market
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/market/tokens/token-registry.md
related_concepts:
  - CONCEPT-0309
dependencies:
  - DOC-0309
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Market Tokens

## Purpose and scope

Token registry, token discovery, token intelligence, oracle registry, pair discovery, and price discovery documentation.

## What belongs here

Token, oracle, pair, and price discovery documents.

## What does not belong here

DEX adapter behavior, route execution, or wallet asset management.

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
| [Oracle Registry](./oracle-registry.md) | Registry |
| [Pair Discovery](./pair-discovery.md) | Reference |
| [Price Discovery](./price-discovery.md) | Reference |
| [Token Discovery](./token-discovery.md) | Reference |
| [Token Intelligence](./token-intelligence.md) | Reference |
| [Token Registry](./token-registry.md) | Registry |

## Adjacent domains

Adjacent domains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
