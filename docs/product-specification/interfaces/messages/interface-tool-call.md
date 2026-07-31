---
metadata_schema_version: 1.0
document_id: DOC-0263
title: Interface Tool Call
plane: Product Specification
domain: Interfaces
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/interfaces/messages/interface-tool-call.md
related_concepts:
  - CONCEPT-0263
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Interfaces
type: REFERENCE
purpose: Interface Tool Call documentation.
scope: Reference documentation.
---

# Interface Tool Call

## Document type
This document is a reference.

# Interface: Tool Call

## Purpose
Defines canonical tool invocation and result contracts.

## Schema
- name.
- args.
- result.
- error.
- timeout.

## Validation
- `name` is required and non-empty.
- `args` is required.
- `timeout` is required and must be greater than zero.
- `result` and `error` are mutually exclusive.

## Cross-references
- `../../ai/orchestration/ai-agent-specification.md`
- `../../ai/orchestration/ai-orchestration.md`

## Interface Contract
Defines AI tool invocation shape, permissions, arguments, result handling, and error normalization.

## Example
The AI asks the risk tool for exposure metrics before recommending execution.

## Required details
- Define tool arguments, outputs, permissions, and sandbox constraints.

## Interface model
- Producer: Agent Orchestrator.
- Consumer: Tool Adapter.
- Payload: Tool name, args, timeout, result, and error..
- Schema: name, args, result, error, timeout, permissions.
- Validation: name required, timeout > 0, result xor error, args validated by tool schema.
- Versioning: v1.0 backward compatible with additive tool metadata.
- Failure behavior: unknown tool, invalid args, timeout, permission denied, or tool runtime error.
