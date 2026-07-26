# Opportunity Lifecycle

## Purpose
Defines the lifecycle from detection to archival.

## State machine
```mermaid
stateDiagram-v2
  [*] --> DETECTED
  DETECTED --> VALIDATED
  VALIDATED --> SCORED
  SCORED --> SIMULATED
  SIMULATED --> APPROVED
  APPROVED --> EXECUTED
  EXECUTED --> CLOSED
  CLOSED --> ARCHIVED
```

## Cross-references
- `OPPORTUNITY-DETECTION.md`
- `OPPORTUNITY-RANKING.md`
- `TRADING-LIFECYCLE.md`
