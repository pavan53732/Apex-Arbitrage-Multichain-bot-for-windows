# App Builder Workflow

## Purpose
Defines the workflow for building, testing, packaging, and releasing the Windows app.

## Ownership
- Owns the build-to-release workflow for the desktop app.
- Does not own runtime trading semantics.

## Workflow contract
- Must define source validation, test gates, packaging, signing, and release checks.
- Must define how failures block the pipeline and how rollback is performed.

## Cross-references
- `BUILD-RELEASE-CICD.md`
- `WINDOWS-DEPLOYMENT.md`
- `TESTING-GUIDE.md`
- `DEPLOYMENT.md`
