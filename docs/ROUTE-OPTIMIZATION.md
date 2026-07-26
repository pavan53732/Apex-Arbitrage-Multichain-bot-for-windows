# Route Optimization

## Purpose
Defines route gathering, simulation, scoring, selection, execution, and verification.

## State machine
```mermaid
stateDiagram-v2
  [*] --> GATHER_ROUTES
  GATHER_ROUTES --> SIMULATE_EACH
  SIMULATE_EACH --> SCORE
  SCORE --> SELECT_BEST
  SELECT_BEST --> EXECUTE
  EXECUTE --> VERIFY
  VERIFY --> [*]
```

## Scoring
Multi-objective scoring uses profit, gas, slippage, historical success, confidence, and complexity with configurable weights.

## Configuration
- ROUTE_SCORE_WEIGHTS.
- MAX_ROUTES_TO_EVALUATE.
- MIN_PROFIT_THRESHOLD.

## Failure modes
If the best route fails simulation, fallback to the second best and log the failure.

## Cross-references
- `SIMULATION-ENGINE.md`
- `EXECUTION-LIFECYCLE.md`
- `TRADING-LIFECYCLE.md`

## Operational Contract
Defines optimization objectives, constraints, scoring, and route comparison logic.

## Example
The optimizer prefers the route with the best net expected return.
