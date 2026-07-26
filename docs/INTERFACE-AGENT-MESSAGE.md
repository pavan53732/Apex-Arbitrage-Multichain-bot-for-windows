# Interface Agent Message

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
- `AI-ORCHESTRATION.md`
- `AI-AGENT-SPECIFICATION.md`

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
