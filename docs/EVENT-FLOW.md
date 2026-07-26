# Event Flow

## Purpose
Defines event emission, propagation, ordering, and consumption semantics.

## Ownership
- Owns event semantics only.
- Does not define IPC payload contracts.

## Cross-references
- `DATA-FLOW.md`
- `IPC-PROTOCOL.md`
- `STATE-MANAGEMENT.md`

## Operational Contract
Defines event production, routing, consumption, correlation, and lifecycle across the platform.

## Example
OpportunityDiscovered leads to RiskCalculated, SimulationPassed, and ExecutionSubmitted.

## Arbitrage events
- Must define opportunity, spread, execution, fill, failure, and expiry events.
- Must define Windows Event Log integration for critical events.

## Required details
- Define opportunity, execution, fill, failure, and expiry events.
