# Oracle Registry

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
