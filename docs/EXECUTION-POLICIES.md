# Execution Policies

## Purpose
Defines the policy layer for gas, exposure, trading windows, profit thresholds, retry policy, emergency stop, and pause policy.

## State machine
```mermaid
stateDiagram-v2
  [*] --> EVALUATING
  EVALUATING --> APPROVED
  EVALUATING --> BLOCKED
  APPROVED --> ACTIVE
  ACTIVE --> PAUSED
  PAUSED --> ACTIVE
  ACTIVE --> EMERGENCY_STOPPED
```

## Failure modes
Threshold breach, policy conflict, emergency stop, invalid pause state.

## Recovery
Stop execution, notify operators, and require approval to resume.

## Cross-references
- `RISK-ENGINE.md`
- `POLICY-ENGINE.md`
- `TRADING-LIFECYCLE.md`
- `EXECUTION-LIFECYCLE.md`
