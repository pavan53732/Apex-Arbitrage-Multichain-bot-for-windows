# BUILD-RELEASE-CICD.md

## Purpose
Defines how APEX is built, tested, packaged, versioned, released, and rolled back.

## Scope
Covers CI workflows, branch policy, build steps, artifacts, code signing, release channels, distribution, and rollback procedures.

## Related Documents
- [WINDOWS-DESKTOP.md](./WINDOWS-DESKTOP.md)
- [TESTING-GUIDE.md](./TESTING-GUIDE.md)
- [PROJECT-STRUCTURE.md](./PROJECT-STRUCTURE.md)

## Branch Policy
- Primary branch: `main`.
- Documentation and implementation changes may land directly on `main` when explicitly authorized.
- CI must run on push to `main`.

## CI Stages
1. install dependencies
2. lint
3. typecheck
4. unit tests
5. integration tests
6. contract tests
7. e2e smoke tests
8. package Windows artifacts

## Release Outputs
- NSIS installer
- portable executable package
- checksums
- release notes
- update manifest

## Versioning
- Semantic versioning for app releases.
- Documentation-only changes may skip version bump unless docs materially redefine implementation requirements.

## Rollback
- Preserve prior installer artifacts.
- Auto-update channels must support pinned rollback targets.
- Breaking provider/config migrations require documented downgrade handling.
