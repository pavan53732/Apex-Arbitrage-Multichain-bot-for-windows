# Configuration

## Purpose
Defines runtime and operational configuration, precedence, validation, and secret handling.

## Ownership
- Owns schema, defaults, override precedence, and validation rules.

## Precedence
1. Secure defaults.
2. Bundled application defaults.
3. Installation profile.
4. Environment variables.
5. Encrypted user overrides.
6. Session-only runtime overrides where allowed.

## Cross-references
- `AI-SETTINGS.md`
- `SECURITY.md`
- `RUNTIME-OPERATIONS.md`
- `DATABASE-SCHEMA.md`
- `AI-COST-MANAGEMENT.md`
- `VERSIONING.md`

- `PLUGIN-SDK.md`

- `HEALTHCHECKS.md`


For provider setup and probe configuration, see `AI-PROVIDER-MANAGER.md` and `HEALTHCHECKS.md`.
