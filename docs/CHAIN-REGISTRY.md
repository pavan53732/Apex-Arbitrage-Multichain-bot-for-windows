---
last_updated: 2026-07-29
type: CONTRACT
owner: Trading Team
status: Canonical
version: 1.0.0
purpose: Defines chain registry.
scope: Chain listing and metadata.
canonical_source: docs/CHAIN-REGISTRY.md
---

# Chain Registry

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-29 | **Owner:** Trading Team

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

## Interface Contract
Defines chain identity, metadata, status, endpoints, capabilities, and versioned chain configuration.

## Example
A chain entry lists chain id, name, RPCs, explorers, and active status.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Trading Team |
