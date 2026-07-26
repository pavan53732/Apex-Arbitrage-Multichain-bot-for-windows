# PROJECT-STRUCTURE.md

## Purpose
Defines the canonical repository layout for the APEX Windows desktop application. This file is the single source of truth for folder ownership, package boundaries, import direction rules, and placement of new code.

## Scope
Covers repository structure, package responsibilities, module boundaries, import constraints, ownership rules, and placement conventions for application code, shared libraries, contracts, tests, generated artifacts, and documentation.

## Related Documents
- [ARCHITECTURE.md](./ARCHITECTURE.md)
- [MODULE-DEPENDENCY.md](./MODULE-DEPENDENCY.md)
- [DATA-FLOW.md](./DATA-FLOW.md)
- [IPC-PROTOCOL.md](./IPC-PROTOCOL.md)
- [STATE-MANAGEMENT.md](./STATE-MANAGEMENT.md)
- [CODING-STANDARDS.md](./CODING-STANDARDS.md)

## Canonical Repository Layout
```text
/
├── .github/
│   └── workflows/
├── apps/
│   └── desktop/
│       ├── src/
│       │   ├── main/
│       │   ├── preload/
│       │   ├── renderer/
│       │   └── shared/
│       ├── assets/
│       ├── electron-builder.yml
│       └── package.json
├── packages/
│   ├── ai-core/
│   ├── strategy-engine/
│   ├── risk-engine/
│   ├── chain-adapters/
│   ├── dex-adapters/
│   ├── ipc-contracts/
│   ├── config/
│   ├── db/
│   ├── observability/
│   ├── ui-kit/
│   └── test-utils/
├── contracts/
│   ├── evm/
│   └── abi/
├── scripts/
├── tests/
│   ├── e2e/
│   ├── integration/
│   └── fixtures/
├── docs/
├── output/
└── APEX-ARCHITECTURE.md
```

## Package Ownership
- `apps/desktop`: Electron shell, desktop lifecycle, window management, preload bridge, renderer composition.
- `packages/ai-core`: provider abstraction, prompts, tool registration, parsing, fallback routing.
- `packages/strategy-engine`: strategy interfaces, orchestration, opportunity evaluation, trade plan generation.
- `packages/risk-engine`: guards, limits, exposure control, kill switch logic.
- `packages/chain-adapters`: RPC abstractions, chain metadata, gas, nonce, balances.
- `packages/dex-adapters`: quote/swap adapters, liquidity route normalization.
- `packages/ipc-contracts`: typed IPC schemas shared by main, preload, renderer.
- `packages/config`: environment parsing, schema validation, runtime defaults, feature flags.
- `packages/db`: SQLite schema, migrations, repositories, retention jobs.
- `packages/observability`: logs, metrics, tracing, diagnostics.
- `packages/ui-kit`: reusable renderer components and design primitives.
- `packages/test-utils`: mocks, fixtures, harness helpers.

## Import Direction Rules
1. Renderer code must never import Electron main-process modules directly.
2. Preload is the only bridge between renderer and privileged APIs.
3. UI components may import `ui-kit`, `ipc-contracts`, and renderer-local modules only.
4. Main process may import any shared package except renderer-only UI modules.
5. Adapters must not depend on UI, Electron, or persistence implementations.
6. `strategy-engine` may depend on adapters and risk abstractions, but not renderer code.
7. `db` is infrastructure and must not import feature/UI modules.
8. Cross-package imports must use public package entry points only.

## Directory Rules
- New business logic belongs in `packages/`, not under `apps/desktop/src/renderer`.
- Renderer feature screens live under `apps/desktop/src/renderer/features/<feature-name>/`.
- IPC channel declarations belong only in `packages/ipc-contracts`.
- SQL migrations belong only in `packages/db/migrations`.
- Static assets used by UI belong in `apps/desktop/assets`.
- Generated reports, exports, or runtime files must never be committed unless explicitly designated fixtures.

## Ownership Conventions
- Each package must expose a README or package-level overview once implemented.
- Each package must define a single public entry point.
- Each feature must have one owning module and one owning doc section.
- If two packages need the same utility, move it into a lower-level shared package rather than duplicating it.

## Implementation Guidance for AI Agents
- Create missing folders exactly as defined here unless a later authoritative doc revises this layout.
- Do not invent new top-level directories without updating this file first.
- Prefer package extraction over large feature folders in the Electron app.
- When uncertain where code belongs, choose the lowest layer that does not depend on UI or Electron.
