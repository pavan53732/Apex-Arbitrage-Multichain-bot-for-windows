---
metadata_schema_version: 1.0
document_id: DOC-0401
title: AI Knowledge README
plane: Product Specification
domain: AI
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/ai/knowledge/ai-knowledge-index.md
related_concepts:
  - CONCEPT-0111
dependencies:
  - DOC-0111
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# AI Knowledge

## Purpose and scope

AI knowledge indexing and retrieval surfaces.

## What belongs here

Knowledge index specifications and references.

## What does not belong here

Memory persistence, prompt construction, or provider selection behavior.

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
| [AI Knowledge Index](./ai-knowledge-index.md) | Index |

## Adjacent domains

Adjacent AI subdomains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
