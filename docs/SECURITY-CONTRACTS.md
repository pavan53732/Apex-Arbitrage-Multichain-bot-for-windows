---
last_updated: 2026-07-29
type: CONTRACT
owner: Security Team
status: Canonical
version: 1.0.0
purpose: Security Contracts documentation.
scope: Reference documentation.
canonical_source: docs/SECURITY-CONTRACTS.md if filename.startswith('docs/') else SECURITY-CONTRACTS.md
---

# Security Contracts

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-29 | **Owner:** Security Team

## Document type
Document type: [REFERENCE]

## Purpose
Declares high-level security policy for the platform.

## Authority
Detailed security architecture, trust boundaries, secret lifecycle, permission model, incident response, and monitoring are owned by `SECURITY.md`.

Policy mandates from this document are enforced by `SECURITY.md` and `SECURITY.md` §7 (Monitoring Events).

## Mandated Controls
- **Secret storage**: Secrets must use the OS keychain; never stored in `.env` files.
- **Wallet signing**: Wallet signing requires explicit user approval via desktop UI; headless auto-sign forbidden.
- **Plugin sandbox**: Plugins run in a separate process with CPU and RAM limits.
- **Emergency stop**: `/admin/emergency-stop` terminates active orders and locks wallets.
- **Audit log**: Every state transition logs user ID, timestamp, and immutable hash.

## Cross-References
- `SECURITY.md` — Full security architecture.
- `PERMISSION-MODEL.md` — Role/action permission matrix.
- `TRUST-BOUNDARIES.md` — Trust domain definitions.
- `SECRET-LIFECYCLE.md` — Secret lifecycle details.
- `TRACEABILITY-MATRIX.md`

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Security Team |
