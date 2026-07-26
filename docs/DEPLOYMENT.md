# APEX Deployment & Release Guide

## Purpose
Defines build pipeline, packaging, testing gates, release promotion, rollback expectations, and operator release workflow.

## Ownership
- Owns packaging, installer flow, release channels, and upgrade/rollback procedures.
- Consumes `RUNTIME-OPERATIONS.md`, `TESTING-GUIDE.md`, and `SECURITY.md`.

## Release stages
- Build.
- Sign.
- Package.
- Publish.
- Verify.
- Promote.
- Roll back.

## Preconditions
- Tests must pass.
- Configuration schema must validate.
- Migration scripts must be reversible or explicitly documented.
- Release artifacts must include checksums and version metadata.

## Cross-references
- `WINDOWS-DESKTOP.md`
- `BUILD-RELEASE-CICD.md`
- `RUNTIME-OPERATIONS.md`
- `SECURITY.md`
