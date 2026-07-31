---
metadata_schema_version: 1.0
document_id: DOC-0405
title: AI Prompts README
plane: Product Specification
domain: AI
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/ai/prompts/prompt-engineering.md
related_concepts:
  - CONCEPT-0109
dependencies:
  - DOC-0109
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# AI Prompts

## Purpose and scope

Prompt engineering and prompt lifecycle documentation.

## What belongs here

Prompt construction, lifecycle, and prompt governance documents.

## What does not belong here

Provider selection, memory persistence, or orchestration mode selection.

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
| [Prompt Engineering](./prompt-engineering.md) | Specification |
| [Prompt Lifecycle](./prompt-lifecycle.md) | Reference |

## Adjacent domains

Adjacent AI subdomains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
