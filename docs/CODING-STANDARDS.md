# CODING-STANDARDS.md

## Purpose
Defines mandatory coding conventions for all code generated for APEX so humans and AI agents produce uniform, reviewable, and maintainable code.

## Scope
Covers TypeScript standards, naming conventions, file naming, architecture rules, dependency rules, formatting, linting, testing expectations, comments, and commit conventions.

## Related Documents
- [PROJECT-STRUCTURE.md](./PROJECT-STRUCTURE.md)
- [ARCHITECTURE.md](./ARCHITECTURE.md)
- [TESTING-GUIDE.md](./TESTING-GUIDE.md)
- [BUILD-RELEASE-CICD.md](./BUILD-RELEASE-CICD.md)

## Language and Tooling Standards
- TypeScript is required for application code.
- Use strict mode, `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`, and path aliases only when defined centrally.
- ESLint and Prettier are mandatory.
- Avoid `any`; prefer `unknown` with explicit narrowing.
- Prefer Zod schemas for runtime validation.

## Naming Rules
- Files: kebab-case, except React components may use `PascalCase.tsx` if enforced consistently.
- Types, interfaces, classes: PascalCase.
- Functions and variables: camelCase.
- Constants: UPPER_SNAKE_CASE only for true constants and env keys.
- IPC channels: `<domain>:<action>` format, for example `wallet:get-balance`.
- Feature folders: singular nouns unless the domain is inherently plural.

## Architectural Rules
- No renderer access to Node or Electron internals except through preload-exposed APIs.
- No direct SQL from UI code.
- No side effects inside pure domain mappers or validators.
- Domain logic must be package-local and testable without Electron.
- Shared contracts must be typed and versioned.

## Dependency Rules
- Import only from package public entry points.
- UI kit must not depend on feature modules.
- Risk engine must not depend on renderer UI.
- Strategy implementations must depend on interfaces and adapters, not concrete window or UI services.
- Cyclic dependencies are forbidden.

## Error and Logging Rules
- Throw typed errors, not string literals.
- Log structured objects, not free-form multiline text as the primary signal.
- Never log secrets, raw API keys, or decrypted credentials.

## Formatting Rules
- One exported symbol family per file when practical.
- Prefer small modules with focused responsibility.
- Keep functions under roughly 60 lines unless orchestration logic genuinely requires more.
- Use early returns to reduce nesting.
- Document non-obvious invariants with concise comments.

## Testability Rules
- Every package must be unit-testable in isolation.
- Business rules must have deterministic tests.
- IPC handlers require contract tests.
- Critical flows require integration coverage.

## Commit Conventions
Use conventional-style commit prefixes:
- `feat:` new functionality
- `fix:` bug fix
- `docs:` documentation only
- `refactor:` internal structural changes
- `test:` test-only changes
- `chore:` tooling or maintenance

Commit bodies must explain:
- what changed,
- why it changed,
- which docs or architecture decisions it aligns with.

## AI Agent Rules
- Do not invent local conventions; follow this document.
- If a generated implementation conflicts with this file, this file wins unless explicitly superseded.
- If a needed convention is missing, update this document before broad code generation continues.
