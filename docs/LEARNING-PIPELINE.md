# Learning Pipeline

## Purpose
Formalizes how operational history is converted into future model and policy improvements.

## Feature store
Market conditions, strategy parameters, execution latency, gas prices, success and failure flags.

## Reward signal
Reward = Profit - (2 * MaxDrawdown) - (0.001 * Slippage), configurable.

## Pipeline states
```mermaid
stateDiagram-v2
  [*] --> COLLECTING
  COLLECTING --> PREPROCESSING
  PREPROCESSING --> TRAINING
  TRAINING --> EVALUATING
  EVALUATING --> PROMOTING
  EVALUATING --> REJECTING
  PROMOTING --> DEPLOYING
  REJECTING --> COLLECTING
  DEPLOYING --> COLLECTING
```

## Trigger policy
Retrain on daily schedule at 00:00 UTC, after 100 new trades, or after a 5% confidence degradation over 24 hours.

## A/B testing
New models go to a shadow pool for 24 hours. Roll back automatically if shadow performance is 10% below production.

## Configuration
- RETRAIN_TRIGGER_TYPE.
- MIN_TRADES_FOR_RETRAIN.
- SHADOW_DURATION_HOURS.
- ROLLBACK_THRESHOLD.

## Cross-references
- `AI-ORCHESTRATION.md`
- `AI-MEMORY-SYSTEM.md`
- `METRICS.md`
- `SIMULATION-ENGINE.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
