# Event Catalog

## Document type
This document is an overview, reference, or index as noted below.

# Event Catalog

## Purpose
Authoritative owner for event catalog.

## Scope
Cross-cutting platform governance.

## Responsibilities
Define ownership, contracts, lifecycle, validation, and cross-references.

## Cross-references
- `APEX-OS.md`
- `ARCHITECTURE.md`

## Operational Contract
Defines the canonical registry of events, payload fields, producers, consumers, and versioning rules.

## Example
TradeStarted includes trade id, wallet id, strategy id, chain id, and timestamp.

## Event ownership
- Publisher, consumer, retention, ordering, and priority are defined in `EVENT-OWNERSHIP-MATRIX.md`.
- Delivery guarantees must defer to the owner of the event stream.
