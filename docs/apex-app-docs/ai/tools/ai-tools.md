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
canonical_source: docs/apex-app-docs/ai/tools/ai-tools.md
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

# AI Tools

## Document type
Document type: [CONTRACT]

## Purpose
Defines every tool available to AI agents and the rules governing their use.

## Tool surface
- Market search.
- Risk query.
- Wallet query.
- Simulation.
- Logs.
- Configuration.
- Notifications.
- Charts.
- Reports.

## Tool rules
- Every tool has a canonical name, argument shape, output shape, and permission boundary declared in its schema.
- Tools are versioned; a tool version bump must preserve backward compatibility or require agent revalidation.
- A tool call is validated against its schema before execution; an invalid call is rejected.
- Tool execution is bounded by timeout, and permission checks run before every invocation.
- Tools never mutate financial state directly; they return data and validated proposals to the orchestrator.
- A tool failure returns a normalized error through the tool-call contract, never a fabricated result.

## Permission model
- Tool access is granted per agent role by the permission model.
- A tool outside the agent's granted surface is denied with an explicit reason.

## Tool governance
- New tools are approved by the tool governance process and versioned before exposure to agents.
- Tool removal follows deprecation: a deprecated tool remains callable with a warning until retired.
- Tool logs are retained for audit and replay.

## Failure handling
- A tool that exceeds its timeout returns a normalized timeout error.
- A permission-denied tool returns the denial reason; it is never silently skipped.
- A tool that crashes returns a runtime error through the tool-call contract.

## Cross-references
- `../../interfaces/messages/interface-tool-call.md`
- `../orchestration/ai-agent-specification.md`
- `../../interfaces/api/api-reference.md`

## Governance Rules
Defines the complete tool surface available to AI agents, including permissions, argument shapes, and result expectations.

## Example
The risk agent uses a tool to query exposure before consensus; the call is schema-validated, permission-checked, and timed out if it exceeds its budget.
