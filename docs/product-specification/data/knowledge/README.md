---
metadata_schema_version: 1.0
document_id: DOC-0432
title: Data Knowledge README
plane: Product Specification
domain: Data
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/data/knowledge/knowledge-graph.md
related_concepts:
  - CONCEPT-0275
dependencies:
  - DOC-0275
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# Data Knowledge

## Purpose and scope

Knowledge graph, context builder, data flow, data governance, and data ownership documentation.

## What belongs here

Knowledge graph, context assembly, data flow, data governance, and data ownership documents.

## What does not belong here

Physical persistence, runtime state, or product configuration unless knowledge/data semantics own the concern.

## Expected document classes

- Index
- Specification
- Reference
- Policy or Registry where this subdomain owns the concern

## Canonical boundaries

This folder indexes Data documents in this subdomain and defers behavior to canonical owner documents identified by metadata and registry entries.

## Documents

| Document | Class |
| --- | --- |
| [Context Builder](./context-builder.md) | Reference |
| [Data Flow](./data-flow.md) | Reference |
| [Data Governance](./data-governance.md) | Reference |
| [Data Ownership](./data-ownership.md) | Policy |
| [Knowledge Graph](./knowledge-graph.md) | Reference |

## Adjacent domains

Adjacent domains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
