---
metadata_schema_version: 1.0
document_id: DOC-0124
title: AI Tools
plane: Product Specification
domain: AI
class: Reference
authority: Canonical
status: Active
owner: AI Team
version: 1.0.0
canonical_source: docs/product-specification/ai/tools/ai-tools.md
related_concepts:
  - CONCEPT-0124
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - AI
type: REFERENCE
purpose: Ai Tools documentation.
scope: Reference documentation.
---

# Ai Tools

## Document type
This document is an overview, reference, or index as noted below.

# AI Tools

## Purpose
Defines every tool available to AI agents.

## Scope
Market search, risk query, wallet query, simulation, logs, configuration, notifications, charts, reports.

## Cross-references
- `../../interfaces/messages/interface-tool-call.md`
- `../orchestration/ai-agent-specification.md`
- `../../interfaces/api/api-reference.md`

## Governance Rules
Defines the complete tool surface available to AI agents, including permissions, argument shapes, and result expectations.

## Example
The risk agent uses a tool to query exposure before consensus.

## Required details
- Define tool schema and permissions.

## Tool rules
- Define tool names, arguments, outputs, and permission boundaries.
- Define how tools are versioned and validated.

## Tool rules
- Define tool names, arguments, outputs, permissions, and versioning.
- Define tool validation before execution.
