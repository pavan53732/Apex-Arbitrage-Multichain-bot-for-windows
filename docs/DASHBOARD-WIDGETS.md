# Dashboard Widgets

## Document type
This document is an overview, reference, or index as noted below.

# Dashboard Widgets

## Purpose
Defines the reusable dashboard widgets used by the Windows desktop UI.

## Scope
This document covers widget behavior, data bindings, refresh expectations, and display states.

## Widget groups
- AI confidence.
- PnL.
- Gas.
- Wallet.
- Trades.
- Chains.
- Strategies.
- Latency.
- Health.
- Logs.
- Charts.
- Orders.
- Heatmaps.
- Risk.

## Cross-references
- `WINDOWS-DESKTOP.md`
- `UI-COMPONENT-SPEC.md`
- `USER-FLOWS.md`
- `STATE-MANAGEMENT.md`
- `MONITORING-OBSERVABILITY.md`


For interaction logic, data binding, and state transitions, see `UI-DASHBOARD-SPEC.md`.

## Operational Contract
Defines widget responsibilities, inputs, outputs, rendering cadence, and error states.

## Example
A wallet widget shows balance, exposure, and status in one view.

## Trading widgets
- Must define widgets for spread, P&L, order book, MEV, and execution status.

## Required details
- Define widget behavior and live update cadence.

## Widget rules
- Define widget states, update cadence, and error handling.
- Define the core widgets for spread, P&L, health, and execution.
