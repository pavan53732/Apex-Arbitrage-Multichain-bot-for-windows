---
metadata_schema_version: 1.0
document_id: DOC-0404
title: AI Orchestration README
plane: Product Specification
domain: AI
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/ai/orchestration/ai-orchestration.md
related_concepts:
  - CONCEPT-0102
dependencies:
  - DOC-0102
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# AI Orchestration

## Purpose and scope

AI orchestration, agent coordination, planning, consensus, and reflection documentation.

## What belongs here

Orchestration, agent specification, planner, consensus, and reflection documents.

## What does not belong here

Provider health, low-level runtime pipeline, or memory storage unless orchestration is the owning concern.

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
| [AI Agent Specification](./ai-agent-specification.md) | Specification |
| [AI Consensus](./ai-consensus.md) | Reference |
| [AI Orchestration](./ai-orchestration.md) | Specification |
| [AI Planner](./ai-planner.md) | Reference |
| [AI Reflection](./ai-reflection.md) | Reference |

## Adjacent domains

Adjacent AI subdomains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
