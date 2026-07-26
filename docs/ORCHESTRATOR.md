# Orchestrator

## Purpose
Defines the top-level operational state machine for the autonomous platform.

## State machine
Idle -> Discovery -> Validation -> Risk -> Simulation -> Decision -> Queue -> Execute -> Verify -> Learn -> Idle.

## Sequence
1. Market scanning triggers discovery.
2. AI analysis invokes multi-agent consensus.
3. Risk gating performs deterministic pre-simulation checks.
4. Simulation invokes `SIMULATION-ENGINE.md`.
5. Execution invokes execution workers.
6. Verification confirms post-execution outcomes.
7. Learning feeds the persistent learning database.
8. Recovery handles failover and retry logic.

## Cross-references
- `AI-ORCHESTRATION.md`
- `AI-PIPELINE.md`
- `RUNTIME-OPERATIONS.md`
- `SIMULATION-ENGINE.md`
- `EXECUTION-ENGINE.md`
- `RISK-ENGINE.md`
