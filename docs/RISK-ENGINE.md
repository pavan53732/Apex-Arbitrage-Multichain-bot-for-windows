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

## Risk inputs
- Market data freshness and quality.
- Portfolio and position state.
- Wallet state.
- Strategy metadata.
- Execution plan details.
- AI confidence and explanation metadata.

## Hard gates
- Freshness gate.
- Liquidity gate.
- Concentration gate.
- Exposure gate.
- Volatility gate.
- Chain health gate.
- Wallet readiness gate.
- Security and authorization gate.

## Risk outputs
- Risk score.
- Approval state.
- Reject code.
- Halt recommendation.
- Emergency stop flag.
- Recovery instructions.

## Determinism rules
- Re-evaluating the same snapshot must return the same decision and code set.
- Risk decisions must not depend on non-versioned mutable state.
- AI may contribute a score, but the deterministic hard gates control the final answer.

## Failure and recovery
- A breached hard limit must produce a stable reject code.
- If any required input is missing, fail closed.
- If state becomes inconsistent, halt new execution until reconciliation completes.
- Retry is allowed only for transient data-fetch failures, never for a risk rejection.

## Persistence
- Persist risk snapshot hashes, limit sets, scores, approvals, rejects, breach reasons, and halt timestamps.
- Persist operator reset decisions and recovery notes.
- Persist the exact input snapshot that produced the decision.

## Monitoring
- Approval rate.
- Breach rate.
- Emergency stop count.
- Risk score drift.
- Evaluation latency.
- Hard-gate failure counts by category.

## Cross-references
- `STRATEGIES.md`
- `EXECUTION-ENGINE.md`
- `MONITORING-OBSERVABILITY.md`
- `SECURITY.md`
