# CODING-STANDARDS.md

## Purpose
This document defines the implementation standards for all APEX source code. It is intended to remove stylistic and architectural ambiguity for both human contributors and AI agents.

## Scope
TypeScript rules, naming conventions, formatting, dependency rules, linting, testing expectations, and commit conventions.

## Ownership
Engineering maintainers own this document. Any automated or AI-generated code must conform before merge.

## Language Standards
- Primary language: TypeScript.
- Use `strict` mode across all packages.
- Disallow `any` unless accompanied by a documented justification comment and a tracked cleanup issue.
- Prefer discriminated unions over boolean mode flags.
- Prefer explicit return types on exported functions, public methods, IPC handlers, service boundaries, and hooks.

## Naming Conventions
| Item | Convention |
|---|---|
| Variables/functions | `camelCase` |
| Types/interfaces/classes | `PascalCase` |
| Constants | `SCREAMING_SNAKE_CASE` for true constants; otherwise `camelCase` |
| Files | `kebab-case` |
| React components | `PascalCase.tsx` |
| Hooks | `useXxx.ts` |
| Stores | `*.store.ts` |
| Schemas | `*.schema.ts` |
| Tests | `*.spec.ts` / `*.e2e.ts` |

## Architectural Coding Rules
- Keep domain logic outside React components.
- Keep IPC handlers thin; delegate to services.
- Prefer pure functions in `packages/core`.
- Side effects must be isolated in adapter/service layers.
- No hidden singleton state except explicitly documented infrastructure services.
- Do not parse environment variables outside the config package.
- Do not perform direct SQL in UI, strategy, or renderer layers.

## Dependency Rules
- UI components may depend on hooks, stores, shared types, and API clients.
- UI components must not depend on database or chain adapters.
- Strategy modules may not import Electron-specific APIs.
- Shared types may not import runtime packages.
- Circular dependencies are prohibited.

## Error and Logging Rules
- Throw typed errors from service boundaries.
- Never swallow errors silently.
- Log with structured fields, not concatenated prose, following [`ERROR-HANDLING-LOGGING.md`](./ERROR-HANDLING-LOGGING.md).
- Never log secrets, tokens, private keys, mnemonic phrases, or full provider responses containing user-sensitive fields.

## React / Renderer Rules
- Prefer feature folders over type-based sprawl.
- One component should have one clear responsibility.
- Derived state should stay derived; do not duplicate server/main-process state unnecessarily.
- Use memoization only when profiling or data volume justifies it.

## TypeScript Patterns
- Use `zod` schemas at all external boundaries.
- Prefer readonly types for immutable DTOs.
- Prefer small service interfaces over monolithic god-services.
- Use exhaustive `switch` statements with `never` checks for enums/unions.

## Formatting and Tooling
- ESLint and Prettier are mandatory.
- Max line length: 100-120 depending on formatter settings, but readability takes priority over forced wrapping.
- Use import ordering: built-in -> external -> workspace packages -> relative imports.
- Avoid default exports except for framework-required entrypoints.

## Testing Minimums
- Every package must have unit tests for critical business logic.
- IPC and config validation require explicit boundary tests.
- Bugs fixed in production should add a regression test whenever practical.
- See [`TESTING-GUIDE.md`](./TESTING-GUIDE.md).

## Git and Commit Conventions
- Work directly on `main` unless the repo owner instructs otherwise.
- Pull latest `main` before making changes.
- Use descriptive commit subjects that state the area and intent.
- Multi-paragraph commit bodies are preferred for large documentation or architecture updates.

## AI Agent Constraints
- AI agents must not invent unapproved libraries or folders.
- AI agents must check this document and [`PROJECT-STRUCTURE.md`](./PROJECT-STRUCTURE.md) before writing code.
- Where ambiguity exists, the AI agent must resolve it by updating documentation first rather than improvising architecture.

## Cross-References
- [`PROJECT-STRUCTURE.md`](./PROJECT-STRUCTURE.md)
- [`CONFIGURATION.md`](./CONFIGURATION.md)
- [`ERROR-HANDLING-LOGGING.md`](./ERROR-HANDLING-LOGGING.md)
- [`TESTING-GUIDE.md`](./TESTING-GUIDE.md)
- [`NON-FUNCTIONAL-REQUIREMENTS.md`](./NON-FUNCTIONAL-REQUIREMENTS.md)
