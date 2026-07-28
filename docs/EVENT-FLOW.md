---
last_updated: 2026-07-29
type: REFERENCE
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Event Flow documentation.
scope: Reference documentation.
canonical_source: docs/EVENT-FLOW.md
---

# Event Flow

## Document type
This document is an overview, reference, or index as noted below.

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

## Event set
- Must define opportunity, execution, fill, failure, recovery, and expiry events.
