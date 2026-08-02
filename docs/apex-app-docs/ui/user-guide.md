---
metadata_schema_version: 1.0
document_id: DOC-0392
title: User Guide
plane: Product Specification
domain: UI
class: Guide
authority: Canonical
status: Active
owner: UI Team
version: 1.1.0
canonical_source: docs/apex-app-docs/ui/user-guide.md
related_concepts:
  - CONCEPT-0392
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - UI
type: GUIDE
purpose: User Guide documentation.
scope: Reference documentation.
---

# User Guide

## Document type
Document type: [GUIDE]

## Purpose
Provides operator-facing usage guidance for the application.

## Ownership
- User guidance only; behavior is owned by the canonical contracts.

## Installation and first run
- Install the signed package from the release channel.
- On first run, complete configuration, workspace creation, and wallet connection.
- Review the simulation-mode default before enabling any execution.

## Tray and updates
- The tray shows runtime status and notification state.
- Updates are applied per the update channel and roll back on failure.

## Safe operating procedure
- Review trade status before approving any action.
- Understand the trade explainer before relying on autonomous recommendations.
- Use the emergency stop only for immediate risk; it locks wallets until recovery.
- Start in simulation mode and graduate to live execution only with approval.

## Day-to-day operations
- Open the command centers to review chains, wallets, and opportunities before acting.
- Read notifications for critical alerts; quiet hours suppress noncritical updates only.
- Export reports and logs from the diagnostics and analytics surfaces for review.
- Keep the application updated; updates are integrity-checked and roll back on failure.

## Troubleshooting basics
- Check the tray status first; an unexpected tray state indicates a service issue.
- Read error codes from the diagnostics surface before escalating.
- Restart the application only outside active trading windows when possible.

## Account and security
- Wallet keys live in the OS keychain; signing always requires desktop approval.
- Configuration changes under `%PROGRAMDATA%` require elevation.
- Report suspected incidents through the escalation path in the operations contracts.

## Getting help
- Consult the FAQ for common questions.
- Follow the troubleshooting guide for connectivity and runtime issues.
- The user guide summarizes; canonical contracts remain authoritative.

## Governance Rules
Defines how end users navigate features, interpret statuses, and follow safe operating procedures.

## Cross-references
- `./user-flows.md`
- `../operations/diagnostics/troubleshooting.md`
- `../reference/faq.md`

## Operational Contract

This document owns operator-facing usage guidance. Feature behavior is owned by the canonical contracts; this guide describes how to operate them safely.

## Example
The guide explains how to review trade status before approving an action, and how to interpret the trade explainer.
