---
metadata_schema_version: 1.0
document_id: DOC-0300
title: Wallet Command Center
plane: Product Specification
domain: Execution
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/execution/wallet-portfolio/wallet-command-center.md
related_concepts:
  - CONCEPT-0300
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Execution
type: REFERENCE
purpose: Wallet Command Center documentation.
scope: Reference documentation.
---

# Wallet Command Center

## Document type
Document type: [CONTRACT]

## Purpose
Defines wallet balances, approvals, positions, PnL, gas spent, assets, transaction history, allowance checking, and security alerts.

## Surface
- Balances and assets per chain.
- Approvals and allowance checking.
- Positions and PnL.
- Gas spent and transaction history.
- Security alerts.

## State Machine
- UNINITIALIZED -> LOCKED -> UNLOCKED -> APPROVING -> SIGNING -> ERROR.
- ERROR -> LOCKED on recovery.
- Signing requires desktop approval.

## Action rules
- A transfer request requires explicit confirmation before signing.
- Signing requires desktop approval; headless auto-sign is forbidden by the security contracts.
- Approvals and allowances are checked before any transfer; a missing approval blocks the action.
- Wallet actions are routed through the execution safety layer and recorded for audit.
- A wallet error locks the wallet and requires operator recovery before further actions.

## Security alerts
- Suspicious activity raises a security alert in the command center.
- Alerts route to the notification center for escalation.

## History
- Transaction history is queryable and exportable.
- Gas spent is tracked per wallet and chain.
- Approvals are listed with their current status.
- History is searchable by wallet, chain, and time range.
- Security alerts link to the notification center for escalation.
- Wallet state is revalidated on reconnect; stale balances are labeled.
- Every wallet action records its approval path for audit.
- The command center reflects live wallet state from wallet management, never a cached assumption.

## Cross-references
- `../../interfaces/api/domain-model.md`
- `../../operations/monitoring/health-checks.md`
- `./wallet-management.md`
- `../../security/security-contracts.md`

## Operational Contract

Defines wallet actions, approvals, routing, execution safety, and operational visibility. Wallet keys and custody are owned by wallet management; this command center is the operator surface over them.

## Example
A transfer request requires explicit confirmation before signing; the allowance is checked and approved on chain first.
