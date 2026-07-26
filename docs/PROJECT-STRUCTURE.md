# Project Structure

## Purpose
Defines the canonical repository layout and ownership boundaries for implementation.

## Canonical layout
- `apps/desktop/` for Electron desktop shell and renderer.
- `packages/core/` for shared domain contracts.
- `packages/config/` for validated runtime configuration.
- `packages/logging/` for structured logging and redaction.
- `packages/db/` for persistence, migrations, and repositories.
- `packages/ai-orchestrator/` for AI routing and validation.
- `packages/strategy-engine/` for strategy lifecycle and evaluation.
- `packages/risk-engine/` for approvals and limits.
- `packages/chain-clients/` for chain reads and transactions.
- `packages/dex-clients/` for quotes and calldata generation.
- `packages/market-data/` for ingestion and normalization.
- `packages/runtime/` for workers, queues, scheduler, failover.
- `tests/` for unit, integration, e2e, and fork tests.

## Ownership rules
- Shared contracts live in `packages/core`.
- Feature code owns its own interfaces and runtime adapters.
- UI code consumes only stable IPC or adapter contracts.
- No package may import renderer internals.

## Cross-references
- `docs/ARCHITECTURE.md`
- `docs/MODULE-DEPENDENCY.md`
- `docs/BUILD-RELEASE-CICD.md`
