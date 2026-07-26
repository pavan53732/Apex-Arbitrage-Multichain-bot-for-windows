# APEX OS

## Purpose
Defines the constitution of the platform: vision, mission, philosophy, design principles, architecture principles, runtime principles, AI principles, security principles, extensibility principles, roadmap, non-goals, and evolution strategy.

## State machine
```mermaid
stateDiagram-v2
  [*] --> DEFINED
  DEFINED --> GOVERNING
  GOVERNING --> EVOLVING
  EVOLVING --> GOVERNING
```

## Cross-references
- `APEX-KERNEL.md`
- `ORCHESTRATOR.md`
- `POLICY-ENGINE.md`
- `PLUGIN-SDK.md`
- `WINDOWS-DESKTOP.md`
- `ENTERPRISE-OPERATIONS.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
