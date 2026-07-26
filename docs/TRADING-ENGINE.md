# Trading Engine

## Purpose
The trading engine is the top-level coordinator for live, paper, and simulated trading sessions. It owns the trading session state machine and delegates pricing, strategy selection, execution, risk gating, portfolio updates, and telemetry to specialized owner subsystems.

## Responsibilities
- Start, pause, resume, and stop trading sessions.
- Select strategy candidates from market, AI, and configuration inputs.
- Route validated opportunities to execution.
- Maintain session-level reconciliation and emergency stop behavior.
- Emit canonical trading events for UI, AI, monitoring, and audit consumers.

## Business rules
- No execution may begin unless the active mode is ready and the risk engine approves the candidate.
- Live trading must respect configured chain, wallet, liquidity, and stop conditions.
- Paper trading and simulation use the same decision model as live trading but must never broadcast to production chains.
- Emergency stop has priority over all other session commands.

## State machine
Stopped -> Starting -> Ready -> Monitoring -> Planning -> Executing -> Reconciling -> Monitoring.
EmergencyStop is a terminal state until operator reset.

## Inputs
- Market data snapshots.
- Opportunity detections.
- AI recommendations.
- Strategy configuration.
- Risk thresholds.
- Wallet and chain health.

## Outputs
- Execution requests.
- Session lifecycle events.
- Portfolio and position updates.
- Alert and audit events.

## Interfaces
- IPC: trading.start, trading.stop, trading.pause, trading.resume, trading.emergencyStop.
- Depends on: AI pipeline, strategy engine, risk engine, execution engine, portfolio manager, market data.

## Recovery
- On process restart, reload persisted session state and reconcile in-flight work before resuming.
- On unresolved execution state, force reconciliation and block new planning until the session is consistent.

## Monitoring
- Session latency.
- Opportunity-to-execution latency.
- Emergency stop count.
- Reconciliation backlog.
- Session recovery time.

## Testing
- Session lifecycle coverage.
- Emergency stop coverage.
- Crash recovery coverage.

