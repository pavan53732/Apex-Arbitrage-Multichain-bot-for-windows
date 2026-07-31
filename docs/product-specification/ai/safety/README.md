---
metadata_schema_version: 1.0
document_id: DOC-0408
title: AI Safety README
plane: Product Specification
domain: AI
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/ai/safety/ai-safety-boundary.md
related_concepts:
  - CONCEPT-0105
dependencies:
  - DOC-0105
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# AI Safety

## Purpose and scope

AI safety boundary and reasoning policy documentation.

## What belongs here

Safety boundary and reasoning policy documents.

## What does not belong here

Provider routing, prompt lifecycle, memory retention, or product security domain documents.

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
| [AI Reasoning Policy](./ai-reasoning-policy.md) | Policy |
| [AI Safety Boundary](./ai-safety-boundary.md) | Specification |

## Adjacent domains

Adjacent AI subdomains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
