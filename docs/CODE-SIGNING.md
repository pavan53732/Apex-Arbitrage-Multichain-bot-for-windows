# Code Signing

## Version
**Version:** 0.1.0 | **Status:** Draft | **Last Updated:** 2026-07-27 | **Owner:** DevOps Team

## Purpose
Defines code signing requirements for the Apex platform — signing binaries, plugin archives, configuration files, and release artifacts.

## Scope
All release builds published through the build pipeline must be signed. Developer builds and local testing may skip signing.

## Signing Requirements

| Artifact | Signing Method | Key Type | Verification |
|----------|---------------|----------|--------------|
| Windows executable (.exe) | Authenticode (signtool) | EV Code Signing Certificate | Windows SmartScreen |
| Plugin archive (.aplx) | Ed25519 signature | Developer key pair | Plugin store verification |
| Configuration files | SHA-256 hash | N/A (integrity only) | Checksum comparison |
| Release artifacts (.zip) | GPG signature | Release key | GPG verification |
| Container images | Cosign | OIDC-based key | Container registry |

## Verification
- All signed artifacts are verified before distribution.
- Failed verification blocks the release pipeline.
- Expired certificates trigger an alert 30 days before expiration.

## Cross-References
- **APP-BUILDER-WORKFLOW.md** — Build pipeline.
- **SECURITY.md** — Security policies.
- **RELEASE-PROCESS.md** — Release management.

## Version History
| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 0.1.0 | 2026-07-27 | Initial spec | DevOps Team |