---
metadata_schema_version: 1.0
document_id: DOC-0365
title: Troubleshooting
plane: Product Specification
domain: Operations
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/operations/diagnostics/troubleshooting.md
related_concepts:
  - CONCEPT-0365
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Operations
type: REFERENCE
purpose: Troubleshooting documentation.
scope: Reference documentation.
---

# Troubleshooting

## Document type
Document type: [GUIDE]

## Purpose
Provides operator-facing troubleshooting steps for the APEX platform.

## Scope
Covers Windows connectivity, permissions, runtime recovery, and common failure paths. Detailed recovery is owned by the recovery contracts; this guide is the step-by-step surface.

## Windows connectivity
- Verify the service is running and the tray shows the expected status.
- Check proxy settings: `HTTP_PROXY` and `HTTPS_PROXY` are respected per the configuration contract.
- A network reconnect is normal after a drop; repeated reconnects are investigated.

## Permissions
- Configuration mutations under `%PROGRAMDATA%` require admin elevation.
- Wallet and secret access require the OS keychain and desktop approval.

## Runtime recovery
- Follow the recovery playbook for the failing component.
- Use the diagnostics surface to read error codes from the error catalog.
- Escalate when a recovery action fails beyond its retry budget.

## Common symptoms
- **No tray icon**: the service or shell process is not running; verify service status and restart per the shutdown lifecycle.
- **Stale dashboard data**: the data pipeline or cache refresh stalled; check metrics and the cache freshness labels.
- **Wallet locked after error**: wallet recovery requires operator action; see the wallet command center.
- **Updates not applying**: the update channel is unreachable or the integrity check failed; verify connectivity and rollback state.
- **High CPU or memory**: check worker counts and resource limits; the resource manager bounds usage.

## Escalation
- Follow the recovery playbook for the failing component before escalating.
- Escalate with the error code, logs, and the recovery actions already attempted.
- Escalation paths and contact owners are defined in the operations contracts.
- A repeat incident is logged for trend analysis, not handled as a one-off.
- Every resolution is recorded so the playbook improves.
- Operator actions that touch wallets or keys require desktop approval.
- Logs for escalation are exported from the diagnostics surface with the incident window.
- Check the notification center for alerts raised by monitoring before deep-diving.
- After recovery, verify the affected surface returns to normal before closing the incident.

## Cross-references
- `../../ui/user-guide.md`
- `../reliability/runtime-operations.md`
- `../monitoring/monitoring-observability.md`
- `./error-catalog.md`

## Operational Contract

This document owns operator-facing troubleshooting guidance. Diagnosis data is owned by the diagnostics and observability contracts; this guide turns it into steps.

## Example
An operator with no connectivity checks the service status, proxy configuration, and network reconnect metrics before escalating.
