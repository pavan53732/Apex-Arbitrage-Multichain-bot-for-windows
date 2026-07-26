# Position Management

## Purpose
Tracks active positions, exposure, cost basis, unrealized and realized PnL, and position risk.

## State machine
Flat -> Opening -> Open -> Reducing -> Closing -> Closed -> Reconciled.

## Interfaces
- IPC: position.open, position.update, position.close, position.status.
- Persists positions and exposure history.

