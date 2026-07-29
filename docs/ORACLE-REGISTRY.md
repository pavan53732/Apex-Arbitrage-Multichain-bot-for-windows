---
last_updated: 2026-07-29
type: CONTRACT
owner: Trading Team
status: Canonical
version: 1.0.0
purpose: Defines oracle registry.
scope: Oracle listing and metadata.
canonical_source: docs/ORACLE-REGISTRY.md
---

# Oracle Registry

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-29 | **Owner:** Trading Team

## Purpose
Defines the authoritative registry of supported oracle sources and fallback order.

## Scope
This registry is descriptive and feeds market data, routing, slippage, and risk decisions.

## Fields
- Oracle name.
- Chain id.
- Feed identifiers.
- Supported assets.
- Update cadence.
- Confidence policy.
- Fallback priority.
- Health status.

## Cross-references
- `MARKET-DATA.md`
- `LIQUIDITY-ANALYSIS.md`
- `SLIPPAGE-MODEL.md`
- `RISK-ENGINE.md`
- `DATABASE-SCHEMA.md`

## Registry boundary
This is a pure data registry. All runtime behaviour, routing decisions, and validation rules are defined by the market/data/routing authority.

## Interface Contract
Defines oracle identity, feed metadata, heartbeat expectations, and versioned feed configuration.

## Example
A price oracle entry includes chain, feed id, heartbeat, and status.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Trading Team |
