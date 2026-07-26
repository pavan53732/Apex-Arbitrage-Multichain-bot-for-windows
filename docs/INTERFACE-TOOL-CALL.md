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
