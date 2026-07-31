---
metadata_schema_version: 1.0
document_id: DOC-0403
title: AI Memory README
plane: Product Specification
domain: AI
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/ai/memory/ai-memory-system.md
related_concepts:
  - CONCEPT-0120
dependencies:
  - DOC-0120
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# AI Memory

## Purpose and scope

AI memory system, memory lifecycle, and context-priority material.

## What belongs here

Memory, retention, context priority, and retrieval documents.

## What does not belong here

Generic data persistence or provider orchestration unless memory is the owning concern.

## Expected document classes

- Index
- Specification
- Reference
- Policy where the subdomain owns AI behavioral constraints

## Canonical boundaries

This folder indexes AI documents in this subdomain and defers behavior to the canonical owner document identified by metadata and registry entries.

## Documents

| Document | Class |
| --- | --- |
| [AI Memory System](./ai-memory-system.md) | Reference |
| [Context Priority Matrix](./context-priority-matrix.md) | Specification |
| [Memory Lifecycle](./memory-lifecycle.md) | Reference |

## Adjacent domains

Adjacent AI subdomains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
