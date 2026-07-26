# Interface Agent Message

## Document type
This document is an overview, reference, or index as noted below.

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
- Producer: defined by the owning system.
- Consumer: defined by the owning system.
- Payload: defined by the owning system.
- Schema: defined by the owning system.
- Validation: defined by the owning system.
- Versioning: defined by the owning system.
- Failure behavior: defined by the owning system.
