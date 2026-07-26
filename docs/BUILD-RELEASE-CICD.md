# BUILD-RELEASE-CICD.md

## Purpose
Defines the end-to-end build, release, CI, and rollback workflow for APEX.

## Scope
Local builds, CI validation, packaging, code signing, artifact publishing, auto-update channels, and release recovery.

## Branch Workflow
- Default workflow operates directly on `main` unless the owner requests otherwise.
- Always checkout `main`, pull latest changes, commit, push, verify remote state, and end with a clean working tree.

## CI Stages
1. Install dependencies.
2. Typecheck all packages.
3. Lint.
4. Unit tests.
5. Integration tests.
6. E2E smoke tests for desktop shell.
7. Build desktop artifacts.
8. Optional publish step for signed release artifacts.

## Release Versioning
- Semantic versioning for app releases.
- Changelog updated for user-visible changes.
- Schema or IPC breaking changes must bump compatibility metadata.

## Packaging Outputs
- Windows NSIS installer
- optional portable build
- update manifest
- checksum/signature artifacts

## Required Release Checks
- tests green,
- DB migrations verified,
- IPC compatibility verified,
- docs updated for spec changes,
- code signing successful,
- updater metadata published.

## Rollback Strategy
- keep previous stable artifact and update manifest,
- allow channel pinning to stable,
- if migration is non-reversible, document recovery/export path before release.

## Cross-References
- [`WINDOWS-DESKTOP.md`](./WINDOWS-DESKTOP.md)
- [`TESTING-GUIDE.md`](./TESTING-GUIDE.md)
- [`DATABASE-SCHEMA.md`](./DATABASE-SCHEMA.md)
- [`IPC-PROTOCOL.md`](./IPC-PROTOCOL.md)
