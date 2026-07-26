# Trading Engine

## Purpose
Defines the end-to-end trading decision and execution coordination layer.

## Ownership
- Owns trade orchestration from opportunity to settlement.
- Does not own UI rendering or low-level chain submission details.

## Windows concerns
- Must define service behavior, crash recovery, and desktop visibility.
- Must define how trade state is surfaced in the Windows app.

## Cross-references
- `TRADING-LIFECYCLE.md`
- `EXECUTION-ENGINE.md`
- `ORCHESTRATOR.md`
- `RISK-ENGINE.md`

## Required details
- Define service mode, crash recovery, and desktop state surfaces.
