# Interface Tool Call

## Document type
This document is an overview, reference, or index as noted below.

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
- `AI-AGENT-SPECIFICATION.md`
- `AI-ORCHESTRATION.md`

## Interface Contract
Defines AI tool invocation shape, permissions, arguments, result handling, and error normalization.

## Example
The AI asks the risk tool for exposure metrics before recommending execution.

## Required details
- Define tool arguments, outputs, permissions, and sandbox constraints.

## Interface model
- Producer: defined by the owning system.
- Consumer: defined by the owning system.
- Payload: defined by the owning system.
- Schema: defined by the owning system.
- Validation: defined by the owning system.
- Versioning: defined by the owning system.
- Failure behavior: defined by the owning system.
