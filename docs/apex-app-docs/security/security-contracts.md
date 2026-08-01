---
metadata_schema_version: 1.0
document_id: DOC-0227
title: Security Contracts
plane: Product Specification
domain: Security
class: Specification
authority: Canonical
status: Active
owner: Security Team
version: 1.0.0
canonical_source: docs/apex-app-docs/security/security-contracts.md
related_concepts:
  - CONCEPT-0227
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Security
type: CONTRACT
purpose: Security Contracts documentation.
scope: Reference documentation.
---

# Security Contracts

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-29 | **Owner:** Security Team

## Document type
Document type: [REFERENCE]

## Purpose
Declares high-level security policy for the platform.

## Authority
Detailed security architecture, trust boundaries, secret lifecycle, permission model, incident response, and monitoring are owned by `./security.md`.

Policy mandates from this document are enforced by `./security.md` and `./security.md` §7 (Monitoring Events).

## Mandated Controls
- **Secret storage**: Secrets must use the OS keychain; never stored in `.env` files.
- **Wallet signing**: Wallet signing requires explicit user approval via desktop UI; headless auto-sign forbidden.
- **Plugin sandbox**: Plugins run in a separate process with CPU and RAM limits.
- **Emergency stop**: `/admin/emergency-stop` terminates active orders and locks wallets.
- **Audit log**: Every state transition logs user ID, timestamp, and immutable hash.

## Cross-References
- `./security.md` — Full security architecture.
- `./permission-model.md` — Role/action permission matrix.
- `./trust-boundaries.md` — Trust domain definitions.
- `./secret-lifecycle.md` — Secret lifecycle details.
- `../../historical/traceability-matrix.md`

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Security Team |
