# PROJECT-STRUCTURE.md

## Purpose
This document defines the canonical repository layout for APEX. It is the authoritative specification for where code lives, which package owns which responsibility, and which modules may import or call one another.

## Scope
This document covers repository structure, package boundaries, file ownership, import rules, and naming of implementation surfaces. It works together with [`ARCHITECTURE.md`](./ARCHITECTURE.md), [`CODING-STANDARDS.md`](./CODING-STANDARDS.md), [`IPC-PROTOCOL.md`](./IPC-PROTOCOL.md), and [`DATABASE-SCHEMA.md`](./DATABASE-SCHEMA.md).

## Ownership
- Architecture owners maintain package boundaries.
- Feature contributors must place code only in the directories defined here.
- AI agents must not invent alternate top-level structures unless this document is updated first.

## Canonical Repository Layout
```text
/
├─ APEX-ARCHITECTURE.md
├─ .gitignore
├─ docs/
├─ package.json
├─ pnpm-workspace.yaml
├─ tsconfig.base.json
├─ .eslintrc.cjs
├─ .prettierrc
├─ .github/
│  └─ workflows/
├─ apps/
│  └─ desktop/
│     ├─ package.json
│     ├─ electron-builder.yml
│     ├─ src/
│     │  ├─ main/
│     │  ├─ preload/
│     │  └─ renderer/
│     └─ assets/
├─ packages/
│  ├─ core/
│  │  ├─ domain/
│  │  ├─ services/
│  │  ├─ events/
│  │  └─ index.ts
│  ├─ strategy-engine/
│  ├─ risk-engine/
│  ├─ chain-clients/
│  ├─ dex-clients/
│  ├─ ai-orchestrator/
│  ├─ config/
│  ├─ db/
│  ├─ shared-types/
│  ├─ ipc-contracts/
│  ├─ logging/
│  └─ test-utils/
├─ scripts/
├─ tests/
│  ├─ integration/
│  ├─ e2e/
│  └─ fixtures/
└─ storage/
   ├─ dev/
   └─ test/
```

## Top-Level Directory Responsibilities
| Path | Responsibility |
|---|---|
| `/docs` | Single source of truth for architecture, contracts, standards, and operational guidance |
| `/apps/desktop` | Electron application, including main process, preload, and renderer UI |
| `/packages/core` | Domain models, business rules, orchestration primitives, and non-UI application services |
| `/packages/strategy-engine` | Strategy lifecycle, execution framework, signal evaluation, and coordination with risk engine |
| `/packages/risk-engine` | Exposure control, policy enforcement, circuit breakers, and position sizing |
| `/packages/chain-clients` | Blockchain RPC adapters, gas estimation, mempool/state reads |
| `/packages/dex-clients` | DEX-specific quoting, route evaluation, calldata building |
| `/packages/ai-orchestrator` | Cloud AI provider abstraction, tool routing, prompt assembly, structured output validation |
| `/packages/config` | Config schema, parsing, environment variable resolution, defaults |
| `/packages/db` | SQLite schema, migrations, repositories, query helpers |
| `/packages/shared-types` | DTOs, enums, validation schemas, cross-package shared contracts |
| `/packages/ipc-contracts` | IPC message types and request/response schemas used by preload and renderer |
| `/packages/logging` | Logger factory, redaction, sinks, diagnostics serialization |
| `/tests` | Integration and E2E tests that cross package boundaries |
| `/storage` | Local developer data, temp runtime state, mock DBs (never committed except fixtures) |

## Electron App Internal Layout
```text
apps/desktop/src/
├─ main/
│  ├─ bootstrap/
│  ├─ windows/
│  ├─ tray/
│  ├─ ipc/
│  ├─ services/
│  └─ security/
├─ preload/
│  ├─ api/
│  └─ bridge/
└─ renderer/
   ├─ app/
   ├─ pages/
   ├─ components/
   ├─ features/
   ├─ stores/
   ├─ hooks/
   ├─ services/
   ├─ styles/
   └─ utils/
```

## Package Boundary Rules
1. Renderer code must never import directly from Electron, Node built-ins, filesystem, wallet secrets, or raw SQLite adapters.
2. Renderer communicates only through preload-exposed APIs defined in [`IPC-PROTOCOL.md`](./IPC-PROTOCOL.md) and [`API-REFERENCE.md`](./API-REFERENCE.md).
3. `main` process may import package services, but package code must not import from renderer.
4. `shared-types` is dependency-safe and may be imported anywhere.
5. `config` and `logging` may be imported by all runtime packages.
6. `db` may be used by main process services and test utilities, not directly by renderer.
7. Strategy modules depend on shared types, config, logging, chain clients, dex clients, and risk engine interfaces; they must not depend on renderer UI concerns.

## Import Direction
Preferred dependency direction:
```text
renderer -> preload bridge -> ipc contracts -> main services -> core/domain -> adapters
                                               -> db / ai / chain / dex / risk
```

Forbidden dependency direction:
```text
renderer -> db
renderer -> chain clients
renderer -> secret storage
strategy-engine -> renderer
shared-types -> app-specific packages
```

## File Ownership Rules
- One feature owns one directory under `renderer/features`.
- Shared UI primitives belong in `renderer/components` only if reused by at least two features.
- IPC handlers belong in `main/ipc`; handler business logic belongs in package services.
- SQL migrations belong only in `packages/db/migrations`.
- Strategy definitions belong only in `packages/strategy-engine/strategies`.

## Naming Rules
- Packages: kebab-case.
- TypeScript files: kebab-case, except React components in PascalCase when stored as component modules.
- Schemas: `*.schema.ts`.
- Types: `*.types.ts` or exported from package barrel.
- Tests: `*.spec.ts`, `*.test.ts`, E2E files `*.e2e.ts`.

## Generated and Runtime Files
- Build artifacts go to `dist/` or package-local build folders and are ignored by Git.
- Logs, cache, DB, and user state live outside source directories.
- Secrets must never be written into repository paths.

## Cross-References
- [`ARCHITECTURE.md`](./ARCHITECTURE.md)
- [`MODULE-DEPENDENCY.md`](./MODULE-DEPENDENCY.md)
- [`DATA-FLOW.md`](./DATA-FLOW.md)
- [`STATE-MANAGEMENT.md`](./STATE-MANAGEMENT.md)
- [`IPC-PROTOCOL.md`](./IPC-PROTOCOL.md)
- [`BUILD-RELEASE-CICD.md`](./BUILD-RELEASE-CICD.md)
