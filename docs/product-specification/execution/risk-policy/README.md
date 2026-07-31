---
metadata_schema_version: 1.0
document_id: DOC-0417
title: Execution Risk Policy README
plane: Product Specification
domain: Execution
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/execution/risk-policy/risk-engine.md
related_concepts:
  - CONCEPT-0282
dependencies:
  - DOC-0282
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Execution Risk Policy

## Purpose and scope

Risk engine, decision engine, and policy engine documentation for execution approval and policy boundaries.

## What belongs here

Risk checks, decision gates, execution policy authority, and risk/policy references.

## What does not belong here

Market discovery, wallet portfolio management, and low-level transaction submission unless risk-policy ownership is explicit.

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
| [Decision Engine](./decision-engine.md) | Specification |
| [Policy Engine](./policy-engine.md) | Specification |
| [Risk Engine](./risk-engine.md) | Specification |

## Adjacent domains

Adjacent domains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
