# Architecture

## Purpose
Defines the system architecture, subsystem boundaries, and orchestration model.

## System layers
- Desktop shell and renderer UI.
- Typed IPC and preload bridge.
- Main-process services and orchestrators.
- Domain engines and adapters.
- Persistence, monitoring, and operator tooling.

## Canonical boundaries
- Trading decisions are owned by the trading engine.
- Transaction submission and reconciliation are owned by the execution engine.
- Price, liquidity, and route viability are owned by market data, liquidity analysis, routing, slippage, gas, and MEV subsystems.
- Durable history is owned by the database schema and repository layer.
- Runtime coordination is owned by runtime operations.

## Deterministic orchestration rules
For authoritative runtime flow, see `ORCHESTRATOR.md`.
- Main process is the source of truth for operational state. For authoritative runtime flow, see `ORCHESTRATOR.md`.
- Renderer state is derived and must not bypass typed IPC.
- Risk gates must execute before any live submission.
- For the authoritative runtime state machine and orchestration flow, see `ORCHESTRATOR.md`.
- Recovery must reconcile persisted state before new execution is admitted.

## Cross-references
- `docs/TRADING-ENGINE.md`
- `docs/EXECUTION-ENGINE.md`
- `docs/AI-PIPELINE.md`
- `docs/RUNTIME-OPERATIONS.md`
- `docs/STATE-MANAGEMENT.md`
- `CHAIN-REGISTRY.md`
- `DEX-REGISTRY.md`
- `TOKEN-REGISTRY.md`
- `ORACLE-REGISTRY.md`
- `DASHBOARD-LAYOUT.md`
- `DASHBOARD-WIDGETS.md`
- `UX-GUIDELINES.md`
- `VERSIONING.md`

- `DOMAIN-MODEL.md`


For canonical data contracts, see `DOMAIN-MODEL.md`.


## Enterprise Contract – Architecture
- Interfaces: `INTERFACE-AGENT-MESSAGE.md`, `INTERFACE-TOOL-CALL.md`.
- State machine: `ORCHESTRATOR.md`, `TRADING-LIFECYCLE.md`, `EXECUTION-LIFECYCLE.md`.
- Security boundaries: `SECURITY-CONTRACTS.md`.
- Performance SLOs: `PERFORMANCE-SLOS.md`.
- Failure modes: sequencing failure, ambiguous ownership, runtime drift; recover via authoritative owner docs and orchestrator retry.

For trading lifecycle, see `TRADING-LIFECYCLE.md`.
For execution lifecycle, see `EXECUTION-LIFECYCLE.md`.
For event handling, see `EVENT-BUS.md`.
For worker scheduling, see `WORKER-POOL.md`.
For workspace persistence, see `DASHBOARD-WORKSPACES.md`.
For dependency graph details, see `DEPENDENCY-GRAPH.md`.