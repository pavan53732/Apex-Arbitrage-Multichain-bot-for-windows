---
type: ADR
owner: Governance Platform
status: Accepted
version: 1.0.0
purpose: Governance Platform as standalone product.
canonical_source: .governance/programme_2.5/phase_0.75/adr_0010_governance_platform_product.md
---

# ADR-0010: Governance Platform as Standalone Product

## Decision

The Apex Governance Platform is treated as a standalone product inside the repository rather than just a supporting tool.

## Rationale

The governance platform has evolved into a comprehensive framework with:
- Architecture versioning
- Semantic versioning
- ADRs
- Changelog
- Test suite
- Release process
- Migration strategy
- Compatibility policy

## Consequences

- The platform has its own version (0.1.0)
- Separate changelog and release process
- Independent migration strategy
- Compatibility policy for future versions
- Easier maintenance as repository grows
- Future AI agents can depend on it as a product

