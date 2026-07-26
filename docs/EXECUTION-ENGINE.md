# Execution Engine

## Purpose
Converts validated trading intents into executable plans and coordinates submission, monitoring, and recovery.

## Responsibilities
- Normalize strategy outputs into executable actions.
- Select execution route and timing.
- Track submission, confirmation, replacement, cancellation, and reconciliation states.

## State machine
Draft -> Validated -> Routed -> Submitted -> Confirming -> Filled | Replaced | Cancelled | Failed -> Reconciled.

## Interfaces
- IPC: execution.plan.create, execution.plan.submit, execution.plan.status, execution.plan.cancel.
- Depends on risk, market data, wallet, and transaction lifecycle.

## Testing
- Route selection tests.
- Reconciliation tests.
- Failure injection for RPC timeout and slippage breach.

