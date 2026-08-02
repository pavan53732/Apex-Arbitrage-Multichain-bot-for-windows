---
metadata_schema_version: 1.0
document_id: DOC-0223
title: Code Signing
plane: Product Specification
domain: Deployment
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/deployment/code-signing.md
related_concepts:
  - CONCEPT-0223
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Deployment
type: REFERENCE
purpose: Code Signing documentation.
scope: Reference documentation.
---

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

## Key management
- Signing keys are held in the key store and never embedded in source or configuration.
- Certificate renewal is tracked; an alert is raised 30 days before expiration.
- Compromised or revoked keys invalidate affected artifacts, which must be re-signed or withdrawn.
- Key access is restricted to the release pipeline identity; no developer credential can sign a release artifact.
- Every signature records its signer, certificate, and timestamp for audit.
- Key rotation produces a signed transition record so artifact verification remains continuous.

## Policy
- Developer builds and local testing may skip signing; release builds may not.
- A release artifact that fails verification is blocked from distribution.
- Plugins are verified against the developer public key on the marketplace before activation.

## Compliance
- Signing policy is enforced at the release gate; an unsigned release is blocked.
- A signed artifact's signature is verified before distribution.
- Signing logs are retained for audit.

## Cross-References
- **APP-BUILDER-WORKFLOW.md** — Build pipeline.
- **SECURITY.md** — Security policies.
- **RELEASE-PROCESS.md** (future) — Release management. Not yet authored; tracked as a known forward reference, not a broken link, per the Repository Canonicality Repair's identifier-normalization remediation.

## Version History
| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 0.1.0 | 2026-07-27 | Initial spec | DevOps Team |
