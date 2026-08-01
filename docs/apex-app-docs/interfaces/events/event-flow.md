---
metadata_schema_version: 1.0
document_id: DOC-0258
title: Event Flow
plane: Product Specification
domain: Interfaces
class: Reference
authority: Reference
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/interfaces/events/event-bus.md
related_concepts:
  - CONCEPT-0253
dependencies:
  - DOC-0253
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Reference
owned_domains: []
type: REFERENCE
purpose: Event Flow documentation.
scope: Reference documentation.
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
- `../../data/knowledge/data-flow.md`
- `../ipc/ipc-protocol.md`
- `../../data/state/state-management.md`

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
