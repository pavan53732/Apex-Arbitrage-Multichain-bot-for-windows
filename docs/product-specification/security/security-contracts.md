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
canonical_source: docs/product-specification/security/security-contracts.md
related_concepts:
  - CONCEPT-0227
dependencies:
  - DOC-0051
  - DOC-0226
  - DOC-0228
  - DOC-0230
  - DOC-0231
consumers:
  - DOC-0005
  - DOC-0020
  - DOC-0022
  - DOC-0023
  - DOC-0024
  - DOC-0025
  - DOC-0026
  - DOC-0027
  - DOC-0029
  - DOC-0030
  - DOC-0032
  - DOC-0033
  - DOC-0034
  - DOC-0035
  - DOC-0036
  - DOC-0037
  - DOC-0038
  - DOC-0039
  - DOC-0040
  - DOC-0041
  - DOC-0042
  - DOC-0043
  - DOC-0049
  - DOC-0059
  - DOC-0079
  - DOC-0221
  - DOC-0229
  - DOC-0281
  - DOC-0283
  - DOC-0296
  - DOC-0359
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
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
