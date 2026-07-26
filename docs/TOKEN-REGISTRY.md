# Token Registry

## Document type
This document is an overview, reference, or index as noted below.

# Token Registry

## Purpose
Defines the authoritative registry of tracked tokens and token metadata.

## Scope
This registry is descriptive and feeds market data, routing, wallet, portfolio, and risk workflows.

## Fields
- Token symbol.
- Contract address.
- Chain id.
- Decimals.
- Asset type.
- Wrapped/native relationship.
- Stablecoin flag.
- Display name.

## Cross-references
- `MARKET-DATA.md`
- `ASSET-MANAGEMENT.md`
- `PORTFOLIO-MANAGEMENT.md`
- `WALLET-MANAGEMENT.md`
- `DATABASE-SCHEMA.md`

## Registry boundary
This is a pure data registry. All runtime behaviour, routing decisions, and validation rules are defined by the market/data/routing authority.

## Interface Contract
Defines token metadata, chain association, address validation, status, and versioned token records.

## Example
A token entry stores symbol, decimals, chain id, and active status.
