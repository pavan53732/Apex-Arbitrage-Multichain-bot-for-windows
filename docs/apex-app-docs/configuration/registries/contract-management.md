---
metadata_schema_version: 1.0
document_id: DOC-0359
title: Contract Management
plane: Product Specification
domain: Configuration
class: Specification
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.1
canonical_source: docs/apex-app-docs/configuration/registries/contract-management.md
related_concepts:
  - CONCEPT-0359
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Configuration
type: CONTRACT
purpose: Contract Management documentation.
scope: Reference documentation.
---

# Contract Management

## Version
**Version:** 1.0.1 | **Status:** Canonical | **Last Updated:** 2026-07-29 | **Owner:** Runtime Team

## Document type
This document is an overview, reference, or index as noted below.

# Contract Management

## Purpose
Defines registry-based contract storage, ABI versioning, governance approval, deployment selection, and retirement.

## State machine
```mermaid
stateDiagram-v2
  [*] --> REGISTER
  REGISTER --> VERSION
  VERSION --> VALIDATE_ABI
  VALIDATE_ABI --> APPROVE
  APPROVE --> DEPLOY
  DEPLOY --> MONITOR
  MONITOR --> RETIRE
```

## Governance
New deployments are selected via configuration and governance approval, not automatic rotation.

## Configuration
- DEPLOYMENT_WHITELIST.
- MIN_APPROVALS.
- ABI_STORAGE_PATH.

## Security
Must be secured with multi-sig and emergency pause controls.

## Cross-references
- `../../security/security-contracts.md`
- `../../market/chains/chain-registry.md`
- `../../runtime/orchestrator.md`

## Governance Rules
Defines contract lifecycle handling, deployment references, upgrades, deprecation, and address safety.

## Operational Contract
Defines the authoritative lifecycle for on-chain contract artefacts owned by APEX: registration in `./contract-registry.md`, semantic ABI versioning, governance-gated approval before deployment selection, monitored deployment, and controlled retirement. No deployment is selected automatically — every transition from `APPROVE` to `DEPLOY` requires the configured `MIN_APPROVALS` governance approvals recorded against the entry in `ABI_STORAGE_PATH`.

## Example
A proxy upgrade is recorded before the implementation address changes.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.1 | 2026-07-29 | Added `## Operational Contract` section (state-machine-consistent authoritative contract body) to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`). All other content unchanged. | Runtime Team |
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Runtime Team |
