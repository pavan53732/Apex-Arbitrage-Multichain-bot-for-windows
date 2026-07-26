# MEV Protection

## Purpose
Defines protection behavior against sandwiching, front-running, and route exposure.

## Inputs
Route visibility, mempool exposure, transaction size, and execution path.

## Outputs
Protection decision, route change, or execution rejection.

## Algorithm
- Detect exposed routes.
- Prefer safer submission paths where available.
- Reject execution if exposure cannot be reduced below policy.

## Cross-references
- `ROUTING-ENGINE.md`
- `EXECUTION-ENGINE.md`
- `RISK-ENGINE.md`
