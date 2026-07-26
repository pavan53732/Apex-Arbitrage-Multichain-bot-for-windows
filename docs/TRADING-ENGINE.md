# Trading Engine

## Purpose
The trading engine is the top-level coordinator for live, paper, and simulated trading sessions. It owns the session lifecycle and routes validated opportunity work to the execution engine and portfolio subsystems.

## Ownership
- Owns session state, session commands, emergency stop, and reconciliation policy.
- Depends on strategy, AI, risk, execution, portfolio, market data, and monitoring owners.

## Responsibilities
- Start, pause, resume, and stop trading sessions.
- Convert market and AI inputs into session-level plans.
- Enforce mode-specific behavior for live, paper, and simulation sessions.
- Emit canonical session events for UI, automation, and auditing.
- Block planning while reconciliation is incomplete.
- Maintain authoritative session state that can be reconstructed from persisted records after restart.

## Session lifecycle
Stopped -> Starting -> Ready -> Monitoring -> Planning -> Executing -> Reconciling -> Monitoring.
EmergencyStop is terminal until operator reset; Recovering is permitted only after crash restart.

### Transition rules
- Stopped -> Starting after configuration, runtime, and dependency validation pass.
- Starting -> Ready only after state restoration and warmup complete.
- Ready -> Monitoring when the engine is idle and healthy.
- Monitoring -> Planning when validated opportunity work is admitted.
- Planning -> Executing after risk, wallet, route, and execution checks pass.
- Executing -> Reconciling after a terminal execution event or failure event.
- Reconciling -> Monitoring only after durable state is consistent.
- Any active state -> EmergencyStop when the operator or risk engine triggers a halt.
- EmergencyStop -> Stopped or Recovering only after explicit operator reset.

## Session contract
A session must include session id, mode, strategy reference, active universe, emergency-stop flag, recovery state, last reconciliation point, and current operator control state.

## Inputs
- Market data snapshots.
- Opportunity detections and rankings.
- AI recommendations.
- Strategy configuration.
- Risk thresholds.
- Wallet and chain health.
- Runtime diagnostics.
- Persisted session snapshots.

## Outputs
- Execution requests.
- Session lifecycle events.
- Portfolio and position updates.
- Alerts and audit events.
- Recovery tasks after restart.

## Idempotency and retry
- Session commands must be idempotent when invoked with the same correlation id and command payload.
- Restart recovery must reconstruct the same session state from durable records.
- Planning retries must not create duplicate execution work.
- Emergency stop must always win over in-flight planning or execution.

## Failure and recovery
- On process restart, reload persisted session state and reconcile in-flight work before resuming.
- On unresolved execution state, force reconciliation and block new planning until the session is consistent.
- If reconciliation cannot complete, degrade to stopped state and surface a blocking diagnostic.
- If durable state is inconsistent with live state, durable state is authoritative and live work must be reconciled to it.

## Persistence
- Persist session id, mode, lifecycle state, current strategy, halt reason, emergency-stop state, and active work references.
- Persist start, stop, pause, resume, and recovery timestamps.
- Persist the last known consistent snapshot before resuming work.

## Monitoring
- Session latency.
- Opportunity-to-execution latency.
- Emergency stop count.
- Reconciliation backlog.
- Session recovery time.
- State restoration success rate.

## Testing
- Session lifecycle coverage.
- Emergency stop coverage.
- Crash recovery coverage.
- Reconciliation gate coverage.
- Restart replay coverage.

## Cross-references
- `EXECUTION-ENGINE.md`
- `RISK-ENGINE.md`
- `STATE-MANAGEMENT.md`
- `DATABASE-SCHEMA.md`
- `MONITORING-OBSERVABILITY.md`
