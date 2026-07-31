---
metadata_schema_version: 1.0
document_id: DOC-0411
title: Market Connectivity README
plane: Product Specification
domain: Market
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/market/connectivity/rpc-manager.md
related_concepts:
  - CONCEPT-0305
dependencies:
  - DOC-0305
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Market Connectivity

## Purpose and scope

RPC and market connectivity provider management documentation.

## What belongs here

RPC provider pool, latency, rotation, failover, and connectivity material.

## What does not belong here

AI provider behavior or generic operations provider resilience unless market connectivity is explicit.

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
| [RPC Manager](./rpc-manager.md) | Specification |

## Adjacent domains

Adjacent domains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
