# Chain Registry

## Purpose
Defines the authoritative registry of supported chains and chain-level capabilities.

## Scope
This registry is descriptive and feeds chain integration, routing, wallet, gas, and deployment decisions.

## Fields
- Chain name.
- Chain id.
- RPC endpoints.
- Explorer URL.
- Native token.
- Gas model.
- Supported DEXs.
- Flash loan support.
- Finality profile.
- Feature flags.

## Cross-references
- `CHAIN-INTEGRATION.md`
- `ROUTING-ENGINE.md`
- `WALLET-MANAGEMENT.md`
- `GAS-OPTIMISATION.md`
- `DATABASE-SCHEMA.md`

## Registry boundary
This is a pure data registry. All runtime behaviour, routing decisions, and validation rules are defined by the market/data/routing authority.
