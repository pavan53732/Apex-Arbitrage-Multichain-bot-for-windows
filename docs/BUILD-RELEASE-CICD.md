# BUILD RELEASE CICD

## Purpose
Navigation-only document pointing to the authoritative owner(s).

## Cross-references
- `DEPLOYMENT.md`
- `WINDOWS-DESKTOP.md`
- `TESTING-GUIDE.md`
- `RUNTIME-OPERATIONS.md`

## Operational Contract
Defines build stages, release gates, artifact checks, deployment triggers, and rollback conditions.

## Example
A release is blocked until validation and packaging succeed.

## Windows release pipeline
- Must define Windows runners, signing, packaging, and update artifact generation.
- Must define build gates for installer, smoke test, and rollback verification.
