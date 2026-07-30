---
last_updated: 2026-07-29
type: REFERENCE
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Interface Agent Message documentation.
scope: Reference documentation.
canonical_source: docs/INTERFACE-AGENT-MESSAGE.md
---

# Interface Agent Message


## AI Guard
Before creating or modifying ANY markdown file, verify it complies with the 5 Prime Directives.
- Lifecycle docs must explicitly define initial state, terminal state, allowed transitions, forbidden transitions, recovery transitions, and failure transitions.
- Interface docs must explicitly define producer, consumer, payload, schema, validation, versioning, and failure behavior.
- Owner docs must explicitly state what they own and do not own.
- Cross-cutting docs must defer to canonical owners.
- Short docs must explicitly declare whether they are an [INDEX], [OVERVIEW], or [REFERENCE].
If a file fails any directive, abort and fix it before proceeding.

## Document type
This document is a reference.

# Interface: Agent Message

## Purpose
Defines the canonical agent message envelope.

## Schema
- sender.
- recipient.
- payload.
- correlationId.
- deadline.

## Validation
- `sender` and `recipient` are required non-empty strings.
- `correlationId` is required and globally unique.
- `deadline` is required and must be an ISO-8601 timestamp.
- `payload` is required and must validate against the registered message type.

## Cross-references
- `ai/orchestration/AI-ORCHESTRATION.md`
- `ai/reference/AI-AGENT-SPECIFICATION.md`

## Interface Contract
Defines message envelope, routing fields, correlation, priority, and validation rules for agent-to-agent messages.

## Example
A planner message includes task id, origin agent, destination agent, priority, and payload type.

## Required details
- Define transport-agnostic payloads and correlation IDs.

## Interface model
- Producer: AI Orchestrator.
- Consumer: Agent Worker.
- Payload: Task routing, correlation, priority, and response context..
- Schema: sender, recipient, payload, correlationId, deadline, priority.
- Validation: sender and recipient required, correlationId unique, deadline ISO-8601, payload validated by message type.
- Versioning: v1.0 backward compatible with additive fields only.
- Failure behavior: missing required fields, invalid payload type, expired deadline, or unknown recipient.
