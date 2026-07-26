# Windows Deployment

## Document type
This document is an overview, reference, or index as noted below.

# Windows Deployment

## Purpose
Defines how the Windows desktop trading app is packaged, signed, installed, updated, and rolled back.

## Ownership
- Owns Windows installer formats, code signing, update channels, and deployment validation.
- Does not own runtime trading behavior, which belongs to trading and execution owners.

## Windows packaging
- Supported package formats: MSIX, NSIS, and portable zip.
- Installer must preserve user configuration under `%APPDATA%` or `%LOCALAPPDATA%` depending on data sensitivity.
- Code signing is required for public distribution and SmartScreen trust.

## Update and rollback
- Updates must support silent install and rollback.
- Critical update failures must preserve the previous working version.

## Cross-references
- `DEPLOYMENT.md`
- `BUILD-RELEASE-CICD.md`
- `CONFIGURATION.md`
- `SECURITY-CONTRACTS.md`
