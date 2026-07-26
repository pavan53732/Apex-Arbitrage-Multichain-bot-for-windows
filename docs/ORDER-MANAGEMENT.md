# Order Management

## Purpose
Owns order creation, validation, lifecycle tracking, amendment, cancellation, and reconciliation.

## State machine
Created -> Validated -> Routed -> Submitted -> PartFilled | Filled | CancelRequested | Cancelled | Failed.

## Interfaces
- IPC: order.create, order.update, order.cancel, order.status.
- Persists orders and fills.

## Testing
- Partial-fill reconciliation tests.
- Duplicate-order prevention tests.

