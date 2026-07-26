# Risk Engine

## Purpose
Authoritative risk evaluation, limits, halts, and approval gating.

## Ownership
- Owns risk limits, approval gates, emergency stop triggers, and reject reasons.
- Applies to strategies, AI actions, order placement, and execution.

## Responsibilities
- Score opportunities and active positions.
- Enforce exposure, drawdown, concentration, liquidity, and execution risk.
- Gate strategy and AI actions.
- Trigger emergency stop on policy breaches.
- Produce deterministic accept/reject decisions from immutable inputs.

## Risk lifecycle
Candidate -> Evaluated -> Approved -> Monitored -> Breached -> Halted -> Reset.

### Transition rules
- Candidate -> Evaluated on receipt of the latest market, wallet, and position snapshot.
- Evaluated -> Approved only when all hard limits pass.
- Evaluated -> Breached when any hard limit fails.
- Approved -> Monitored while active exposure exists.
- Monitored -> Breached when live values exceed thresholds.
- Breached -> Halted when emergency-stop policy or halt policy is triggered.
- Halted -> Reset only after operator action and state normalization.

## Inputs
- Market data.
- Portfolio and position state.
- Wallet state.
- Strategy metadata.
- Execution plan details.
- AI confidence and explanation metadata.

## Outputs
- Risk scores.
- Approval decisions.
- Reject reasons.
- Halt or emergency-stop recommendations.

## Rules
- Safety, wallet, signing, and liquidity checks are hard gates.
- AI confidence may inform ranking but cannot override risk rejection.
- Risk evaluation must be deterministic for the same snapshot.
- A breached hard limit must produce a stable reject code.

## Idempotency and retry
- Re-evaluating the same snapshot must return the same decision and code set.
- Retry is only for transient data-fetch failures, never for a risk rejection.

## Persistence
- Persist risk snapshot hashes, limit sets, scores, approvals, rejects, breach reasons, and halt timestamps.
- Persist the operator reset decision and recovery notes.

## Monitoring
- Approval rate.
- Breach rate.
- Emergency stop count.
- Risk score drift.
- Evaluation latency.

## Cross-references
- `STRATEGIES.md`
- `EXECUTION-ENGINE.md`
- `MONITORING-OBSERVABILITY.md`
- `SECURITY.md`
