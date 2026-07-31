---
metadata_schema_version: 1.0
document_id: DOC-0400
title: AI Explainability README
plane: Product Specification
domain: AI
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/ai/explainability/explainability.md
related_concepts:
  - CONCEPT-0126
dependencies:
  - DOC-0126
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# AI Explainability

## Purpose and scope

AI explainability, audit lineage, and governance explainability documents.

## What belongs here

Explainability specifications and explainability references.

## What does not belong here

Provider, runtime, memory, or prompt behavior unless explainability is the owning concern.

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
| [Explainability](./explainability.md) | Reference |
| [Governance Explainability](./governance-explainability.md) | Specification |

## Adjacent domains

Adjacent AI subdomains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
