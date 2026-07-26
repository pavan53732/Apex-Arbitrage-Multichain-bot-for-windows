# Order Management

## Purpose
The order manager owns order creation, validation, amendment, cancellation, and reconciliation across live, paper, and simulated modes.

## Responsibilities
- Validate incoming order requests.
- Assign canonical order identifiers.
- Track status transitions and partial fills.
- Correlate orders with transactions, fills, and positions.
- Persist audit history.

## Business rules
- Orders must be rejected when risk, balance, or validation constraints fail.
- A single strategy request may create multiple child orders when routing requires it.
- Duplicate active orders for the same unique intent must be prevented.

## State machine
Created -> Validated -> Routed -> Submitted -> PartFilled | Filled | CancelRequested | Cancelled | Failed -> Reconciled.

## Inputs
- Strategy intent.
- Execution plan.
- Wallet and balance state.
- Quote and route details.

## Outputs
- Order records.
- Fill records.
- Status updates.
- Audit events.

## Interfaces
- IPC: order.create, order.update, order.cancel, order.status.
- Database: order, fill, and order-status history tables.

## Recovery
- Rehydrate open orders on startup.
- Reconcile orders with chain receipts and transaction statuses.
- Mark stale orders for operator review if reconciliation cannot resolve them.

## Testing
- Partial-fill reconciliation.
- Duplicate-order prevention.
- Amend/cancel race conditions.

