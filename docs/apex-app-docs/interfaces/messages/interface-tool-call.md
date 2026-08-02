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
canonical_source: docs/apex-app-docs/interfaces/messages/interface-tool-call.md
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

# Interface: Tool Call

## Document type
Document type: [CONTRACT]

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

## Interface model
- Producer: Agent Orchestrator.
- Consumer: Tool Adapter.
- Payload: Tool name, args, timeout, result, and error.
- Schema: name, args, result, error, timeout, permissions.
- Validation: name required, timeout > 0, result xor error, args validated by tool schema.
- Versioning: v1.0 backward compatible with additive tool metadata.
- Failure behavior: unknown tool, invalid args, timeout, permission denied, or tool runtime error.

## Invocation semantics
- Every invocation is validated against the tool schema before dispatch.
- Permission checks run before execution; an unauthorized tool is denied with a reason.
- Tool execution is bounded by `timeout`; a timeout returns a normalized error, never a partial result as success.
- A tool result or error is returned through this contract; results are never fabricated by the agent.

## Result normalization
- Errors are normalized to a canonical error shape before return.
- A timeout is distinguishable from a failure result.
- A permission denial is returned with its reason, never swallowed.

## Cross-references
- `../../ai/orchestration/ai-agent-specification.md`
- `../../ai/orchestration/ai-orchestration.md`
- `../../ai/tools/ai-tools.md`

## Interface Contract
Defines AI tool invocation shape, permissions, arguments, result handling, and error normalization.

## Example
The AI asks the risk tool for exposure metrics before recommending execution; the call is schema-validated and permission-checked before dispatch.
