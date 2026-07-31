---
metadata_schema_version: 1.0
document_id: DOC-0331
title: Token Discovery
plane: Product Specification
domain: Market
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/market/token-discovery.md
related_concepts:
  - CONCEPT-0331
dependencies:
  - DOC-0317
  - DOC-0318
consumers:
  - DOC-0049
  - DOC-0310
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: Token Discovery documentation.
scope: Reference documentation.
---

# Token Discovery

## Document type
This document is an overview, reference, or index as noted below.

# TOKEN DISCOVERY

## Purpose
Navigation-only document pointing to the authoritative owner(s).

## Cross-references
- `./market-data.md`
- `./market-intelligence.md`

## Operational Contract
Defines token lookup, discovery sources, validation, enrichment, and registry synchronization.

## Example
A discovered token is validated before being promoted into the token registry.

## Required details
- Define discovery cadence, caching, and refresh triggers.

## Discovery rules
- Define refresh cadence, cache invalidation, and discovery triggers.
- Define how new tokens are promoted into registries.
