---
metadata_schema_version: 1.0
document_id: DOC-0414
title: Market Opportunities README
plane: Product Specification
domain: Market
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/market/opportunities/opportunity-detection.md
related_concepts:
  - CONCEPT-0323
dependencies:
  - DOC-0323
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Market Opportunities

## Purpose and scope

Opportunity detection, lifecycle, and ranking documentation.

## What belongs here

Opportunity discovery, ranking, and opportunity-state references.

## What does not belong here

Order execution, transaction lifecycle, or risk approval behavior.

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
| [Opportunity Detection](./opportunity-detection.md) | Reference |
| [Opportunity Lifecycle](./opportunity-lifecycle.md) | Reference |
| [Opportunity Ranking](./opportunity-ranking.md) | Reference |

## Adjacent domains

Adjacent domains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
