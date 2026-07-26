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
