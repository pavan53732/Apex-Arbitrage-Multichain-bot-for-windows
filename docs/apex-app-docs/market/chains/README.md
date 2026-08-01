---
metadata_schema_version: 1.0
document_id: DOC-0410
title: Market Chains README
plane: Product Specification
domain: Market
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/market/chains/chain-integration.md
related_concepts:
  - CONCEPT-0302
dependencies:
  - DOC-0302
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Market Chains

## Purpose and scope

Chain integration, chain registries, chain intelligence, chain rotation, and chain command-center documentation.

## What belongs here

Chain integration, chain metadata, chain registry, and chain selection documents.

## What does not belong here

DEX-specific, token-specific, routing, or execution behavior unless chain ownership is explicit.

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
| [Chain Command Center](chain-command-center.md) | Reference |
| [Chain Integration](chain-integration.md) | Specification |
| [Chain Intelligence](chain-intelligence.md) | Reference |
| [Chain Registry](./chain-registry.md) | Registry |
| [Chain Rotation](chain-rotation.md) | Reference |

## Adjacent domains

Adjacent domains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
