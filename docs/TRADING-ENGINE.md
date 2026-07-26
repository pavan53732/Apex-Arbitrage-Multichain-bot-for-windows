# Trading Engine

## Purpose
Owns end-to-end trading lifecycle orchestration across strategy, execution, risk, wallet, portfolio, and market data.

## State machine
Stopped -> Starting -> Ready -> Monitoring -> Planning -> Executing -> Reconciled -> Monitoring.

## Interfaces
- IPC: trading.start, trading.stop, trading.pause, trading.resume, trading.emergencyStop.
- Depends on AI, strategy, risk, execution, portfolio, market-data.

## Testing
- Session lifecycle tests.
- Recovery and emergency stop tests.

