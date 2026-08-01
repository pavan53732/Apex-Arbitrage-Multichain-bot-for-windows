---
metadata_schema_version: 1.0
document_id: DOC-0407
title: AI Runtime README
plane: Product Specification
domain: AI
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/ai/runtime/ai-pipeline.md
related_concepts:
  - CONCEPT-0103
dependencies:
  - DOC-0103
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# AI Runtime

## Purpose and scope

AI pipeline, runtime gateway, and context-window behavior.

## What belongs here

Pipeline, context window, and gateway runtime documents.

## What does not belong here

Provider inventory, prompt design, memory persistence, or product execution engines.

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
| [AI Context Window Management](ai-context-window-management.md) | Reference |
| [AI Gateway](ai-gateway.md) | Reference |
| [AI Pipeline](ai-pipeline.md) | Specification |

## Adjacent domains

Adjacent AI subdomains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
