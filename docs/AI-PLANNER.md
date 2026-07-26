# AI Planner

## Purpose
Defines the planner agent contract for goal decomposition, dependency ordering, execution sequencing, and failure recovery.

## State machine
```mermaid
stateDiagram-v2
  [*] --> RECEIVED
  RECEIVED --> DECOMPOSING
  DECOMPOSING --> ORDERING
  ORDERING --> SEQUENCING
  SEQUENCING --> READY
  READY --> MONITORING
```

## Cross-references
- `AI-ORCHESTRATION.md`
- `DECISION-ENGINE.md`
- `AI-CONSENSUS.md`

## Operational Contract
Defines goal decomposition, dependency ordering, sequencing, recovery, and plan emission.

## Example
The planner breaks a multi-step execution request into risk, simulation, and trade tasks.
