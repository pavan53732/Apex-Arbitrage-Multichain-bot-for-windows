---
last_updated: 2026-07-29
type: CONTRACT
owner: Trading Team
status: Canonical
version: 1.0.0
purpose: Defines DEX registry.
scope: DEX listing and metadata.
canonical_source: docs/DEX-REGISTRY.md
---

# Dex Registry

## Purpose
Defines the authoritative registry of supported DEXs and their capabilities.

## Scope
This registry is descriptive and feeds routing, liquidity, execution, and market data decisions.

## Fields
- DEX name.
- Chain id.
- Router address.
- Factory address.
- Pool types.
- Fee tiers.
- Version.
- Capability flags.

## Cross-references
- `DEX-INTEGRATION.md`
- `ROUTING-ENGINE.md`
- `LIQUIDITY-ANALYSIS.md`
- `MARKET-DATA.md`
- `DATABASE-SCHEMA.md`

## Registry boundary
This is a pure data registry. All runtime behaviour, routing decisions, and validation rules are defined by the market/data/routing authority.

## Interface Contract
Defines DEX identity, pool coverage, supported routes, status, and versioned metadata.

## Example
A DEX entry includes router address, supported features, and chain associations.
