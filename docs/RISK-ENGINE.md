# Risk Engine

## Purpose
Defines deterministic risk checks for liquidity, oracle deviation, gas spikes, protocol health, wallet risk, and execution confidence.

## Cross-references
- `ORCHESTRATOR.md`
- `DOMAIN-MODEL.md`
- `HEALTHCHECKS.md`

## Example
A route fails the risk gate when exposure, gas, slippage, or confidence breach policy limits.

## Future compatibility notes
Additional risk models may be introduced through configuration.
