# Domain Model

## Purpose
Defines the canonical platform entities and their relationships.

## Entities
- User.
- Wallet.
- Strategy.
- Order.
- Position.
- Token.
- Chain.
- DEX.
- Oracle.
- SimulationRun.
- Transaction.

## Cross-references
- `ARCHITECTURE.md`
- `DATABASE-SCHEMA.md`
- `STATE-MANAGEMENT.md`
- `CONFIGURATION.md`

## Governance Rules
Defines core entities, relationships, invariants, and vocabulary for the system domain.

## Example
A portfolio always belongs to a single wallet owner.

## Windows entities
- Must define Windows app/session/service entities where applicable.

## Required details
- Define Windows entities where needed.

## Domain entities
- Define the core trading, wallet, service, and Windows desktop entities.
- Define identifiers and relationships clearly.
