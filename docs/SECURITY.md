# Security

## Document type
This document is an overview, reference, or index as noted below.

# Security

## Purpose
Defines threat model, secret handling, signing boundaries, permission model, and security response behavior.

## Cross-references
- `WALLET-MANAGEMENT.md`
- `PERMISSION-MODEL.md`
- `RUNTIME-OPERATIONS.md`


## Governance Rules
Defines the platform security baseline for secrets, access control, wallet handling, sandboxing, and emergency response.

## Example
A plugin without sandbox approval is blocked from loading.

## Windows security baseline
- Must define DPAPI, Credential Manager, Defender, and signing expectations.
- Must define Windows-specific threat model and secure storage requirements.

## Required details
- Define DPAPI, Credential Manager, Defender, AppContainer, and signing baseline.

## Security rules
- Define secrets handling, least privilege, and safe deployment expectations.
- Define incident reporting and key rotation guidance.

## Final rules
- Define secrets handling, least privilege, and incident reporting.
- Define key rotation and safe deployment guidance.

## Canonical ownership
This document defers to the canonical owners for implementation, policy, and schema details.

## Trust and secrets
- Trust boundaries are defined in `TRUST-BOUNDARIES.md`.
- Secret handling is defined in `SECRET-LIFECYCLE.md`.
