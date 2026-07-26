# AI Consensus

## Purpose
Defines multi-model decision thresholds, quorum rules, disagreement handling, and fallback behavior.

## Rules
- Execution requires configurable quorum.
- Risk decisions have veto authority over planner recommendations.
- Large disagreement forces no-op or simulation-only mode.
- Provider/model disagreement beyond threshold triggers alerting and fallback.

## Cross-references
- `AI-PIPELINE.md`
- `AI-COST-MANAGEMENT.md`
- `RISK-ENGINE.md`
- `ORCHESTRATOR.md`
