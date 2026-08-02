---
metadata_schema_version: 1.0
document_id: DOC-0368
title: FAQ
plane: Product Specification
domain: Reference
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/reference/faq.md
related_concepts:
  - CONCEPT-0368
dependencies: []
consumers:
  - DOC-0361
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Reference
type: REFERENCE
purpose: Faq documentation.
scope: Reference documentation.
---

# FAQ

## Document type
Document type: [REFERENCE]

## Purpose
Answers common operator questions about installing, updating, and operating the APEX platform.

## Installation
- **How do I install the app?** Installers are signed and distributed through the release channels; see the deployment guide.
- **What are the Windows requirements?** See the Windows desktop contract for platform requirements.
- **Does it run as a service?** Yes, service mode is supported and managed via the Service Control Manager.

## Updates
- **How do updates work?** Updates flow through the configured channel and are integrity-checked before application.
- **What happens if an update fails?** It rolls back to the last known good version.

## Trading
- **Is live trading enabled by default?** No. Phase 1 defaults to simulation; live execution requires operator approval.
- **Why was an opportunity skipped?** Use the trade explainer, which records the reason for every skip.
- **Are my wallet keys stored on disk?** No; keys are held in the OS keychain and signing requires desktop approval.

## Troubleshooting
- **No connectivity?** Check service status, proxy configuration, and network reconnect metrics; see troubleshooting.
- **Where do I see errors?** The diagnostics surface shows codes from the error catalog.

## Security and keys
- **Where are my keys stored?** Wallet keys are held in the OS keychain; signing requires desktop approval.
- **Can the service sign transactions?** No; headless auto-sign is forbidden by the security contracts.
- **How are updates verified?** Updates are integrity-checked and signature-verified before application.

## Recovery
- **What happens after a crash?** State is rehydrated from persistence; pending transactions resume per the transaction lifecycle.
- **How do I restore a configuration?** Restore a snapshot from version history; restores are validated and audited.
- **When should I use the emergency stop?** Only for immediate risk; it locks wallets until recovery.

## Scope
- **Which chains are supported?** See the chain registry and the roadmap for the phased expansion.
- **Is autonomous trading available?** No; execution is operator-approved, with autonomous modes phased.
- **Where do I report issues?** The diagnostics surface and the operations contracts define the escalation path.

## Governance
- **Who owns the answer to my question?** Each answer points to its canonical owner; the FAQ never defines behavior itself.
- **Can I rely on the FAQ alone?** No; the FAQ summarizes; the canonical contracts are authoritative.
- **How is the FAQ kept current?** Answers are updated in the same change as the contracts they summarize.
- **What if an answer conflicts with a contract?** The contract wins; the FAQ is corrected in the same change.
- Platform requirements questions point to the Windows desktop contract.

## Cross-references
- `../ui/user-guide.md`
- `../operations/diagnostics/troubleshooting.md`
- `../deployment/app-builder-deployment-guide.md`

## Operational Contract

This document owns the operator FAQ. Each answer points to a canonical owner; this document never defines behavior itself.

## Example
An operator asks why trading is not live and is directed to the phased-execution model in the strategy and risk contracts.
