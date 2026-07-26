# Orchestrator

## Purpose
Defines the system coordinator that sequences AI, trading, and runtime actions.

## Ownership
- Owns orchestration flow and priority among subsystems.
- Does not own the internal behavior of trading, execution, or AI contracts.

## Windows concerns
- Must define tray actions, window state coordination, and service restart flow.
- Must define behavior on app startup, sleep/resume, and reconnect.

## Cross-references
- `AI-ORCHESTRATION.md`
- `RUNTIME-OPERATIONS.md`
- `TRADING-LIFECYCLE.md`
- `EXECUTION-LIFECYCLE.md`

## Required details
- Define startup, retry, and cross-subsystem sequencing.
