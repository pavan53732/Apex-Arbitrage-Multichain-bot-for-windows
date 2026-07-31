---
metadata_schema_version: 1.0
document_id: DOC-0413
title: Market DEX README
plane: Product Specification
domain: Market
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/market/dex/dex-integration.md
related_concepts:
  - CONCEPT-0303
dependencies:
  - DOC-0303
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Market DEX

## Purpose and scope

DEX integration, DEX registry, and DEX intelligence documentation.

## What belongs here

DEX adapter, DEX metadata, DEX registry, and DEX intelligence documents.

## What does not belong here

Chain, token, route scoring, or execution behavior outside DEX-specific ownership.

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
| [DEX Integration](./dex-integration.md) | Specification |
| [DEX Intelligence](./dex-intelligence.md) | Reference |
| [DEX Registry](./dex-registry.md) | Registry |

## Adjacent domains

Adjacent domains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
