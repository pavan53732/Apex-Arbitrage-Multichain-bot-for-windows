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
