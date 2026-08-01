---
metadata_schema_version: 1.0
document_id: DOC-0409
title: AI Tools README
plane: Product Specification
domain: AI
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/ai/tools/ai-tool-invocation-contract.md
related_concepts:
  - CONCEPT-0107
dependencies:
  - DOC-0107
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# AI Tools

## Purpose and scope

AI tool invocation and tool surface documentation.

## What belongs here

Tool invocation contracts and AI tool references.

## What does not belong here

External plugin SDK behavior or product interface catalogs unless explicitly tool-related.

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
| [AI Tool Invocation Contract](ai-tool-invocation-contract.md) | Specification |
| [AI Tools](ai-tools.md) | Reference |

## Adjacent domains

Adjacent AI subdomains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
