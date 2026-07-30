---
type: REPORT
owner: Governance Platform
status: Active
version: 1.0.0
purpose: Reviewable mapping table for subsystem names in docs/EVENT-OWNERSHIP-MATRIX.md that do not resolve automatically to a real document, for WS4 (Knowledge Graph) event_graph population.
canonical_source: .governance/programme_2.5/_reconciliation/EVENT-MATRIX-UNRESOLVED-NAMES-REVIEW.md
---

# Event Ownership Matrix -- Unresolved Subsystem Names Review

## Purpose

`tools/governance/references/event_matrix_parser.py` parses
`docs/EVENT-OWNERSHIP-MATRIX.md`'s 47-row event table and resolves each
row's publisher/consumer **subsystem name** (e.g. "Trading Engine") to
a real **document path** (e.g. `docs/TRADING-ENGINE.md`), so that
`event_graph` can be populated with genuine, traceable edges.

Per explicit instruction, resolution is **exact and deterministic
only** -- no fuzzy matching, no inferred aliases, no guessing. A name
resolves only if:
1. A hand-reviewed entry exists in `MANUAL_NAME_OVERRIDES` (6 names,
   listed below, each individually verified against the target
   document's own `## Purpose` text), or
2. Exactly one deterministic filename transformation
   (`NAME.upper().replace(" ", "-")` + `.md` / `-ENGINE.md` /
   `-MANAGER.md`) matches a real file under `docs/`.

Of the 39 distinct subsystem names appearing across all 47 event rows,
**27 resolve** (13 deterministic + 14 manual overrides -- 6 original +
8 approved 2026-07-30), yielding **102 real event_graph edges**. The
remaining **13 names below do NOT resolve** and are correctly excluded from the graph entirely --
present only in this review table and in the live
`.governance/exports/event_graph_resolution_report.json` audit
artefact, never silently wired in.

## Resolved names (for reference -- NOT part of this review)

| Subsystem Name | Resolved Document | Resolution Method |
|---|---|---|
| Trading Engine | `docs/TRADING-ENGINE.md` | deterministic |
| Execution Engine | `docs/EXECUTION-ENGINE.md` | deterministic |
| Risk Engine | `docs/RISK-ENGINE.md` | deterministic |
| Routing Engine | `docs/ROUTING-ENGINE.md` | deterministic |
| AI Pipeline | `docs/AI-PIPELINE.md` | deterministic |
| AI Gateway | `docs/AI-GATEWAY.md` | deterministic |
| Chain Intelligence | `docs/CHAIN-INTELLIGENCE.md` | deterministic |
| Context Builder | `docs/CONTEXT-BUILDER.md` | deterministic |
| Market Data | `docs/MARKET-DATA.md` | deterministic |
| RPC Manager | `docs/RPC-MANAGER.md` | deterministic |
| Security | `docs/SECURITY.md` | deterministic |
| Slippage Model | `docs/SLIPPAGE-MODEL.md` | deterministic |
| Workspace Manager | `docs/WORKSPACE-MANAGER.md` | deterministic |
| Opportunity Detector | `docs/OPPORTUNITY-DETECTION.md` | manual override (reviewed) |
| Opportunity Ranker | `docs/OPPORTUNITY-RANKING.md` | manual override (reviewed) |
| AI Orchestrator | `docs/AI-ORCHESTRATION.md` | manual override (reviewed) |
| Runtime Orchestrator | `docs/ORCHESTRATOR.md` | manual override (reviewed) |
| Wallet Manager | `docs/WALLET-MANAGEMENT.md` | manual override (reviewed) |
| Plugin Manager | `docs/PLUGIN-LIFECYCLE.md` | manual override (reviewed) |
| Chain Adapter | `docs/CHAIN-INTEGRATION.md` | manual override (approved 2026-07-30) |
| Config Manager | `docs/CONFIGURATION.md` | manual override (approved 2026-07-30) |
| DEX Adapter | `docs/DEX-INTEGRATION.md` | manual override (approved 2026-07-30) |
| Health Checker | `docs/HEALTHCHECKS.md` | manual override (approved 2026-07-30) |
| Monitoring | `docs/MONITORING-OBSERVABILITY.md` | manual override (approved 2026-07-30) |
| Notification | `docs/NOTIFICATION-CENTER.md` | manual override (approved 2026-07-30) |
| Secret Manager | `docs/SECRET-LIFECYCLE.md` | manual override (approved 2026-07-30) |
| Widget Manager | `docs/DASHBOARD-WIDGETS.md` | manual override (approved 2026-07-30) |

## Unresolved names (require review before any mapping is approved)

| Subsystem Name | Events (role) | Candidate Document(s) | Confidence | Reason for Ambiguity | Recommended Mapping |
|---|---|---|---|---|---|
| AI Cost Manager | ai.cost.exceeded (publisher) | none | zero_candidates | No document named AI-COST-MANAGER.md exists; likely covered by an AI-COST-* reference doc, not a behavioural root | **Not recommended** -- no single owning document; leave unresolved |
| All Subsystems | runtime.starting, runtime.started, runtime.shutting_down, runtime.failover.started, runtime.failover.completed, runtime.config.reload (all consumer) | none (by definition -- "All Subsystems" is a broadcast target, not one document) | zero_candidates | Deliberately generic broadcast term in the source table, not a specific subsystem | **Not recommended** -- resolving this to any single document would misrepresent a broadcast-to-all relationship as a specific one |
| Any Subsystem | system.error, system.warning (both publisher) | none (same reasoning as "All Subsystems") | zero_candidates | Deliberately generic "could be any subsystem" term | **Not recommended** -- same reasoning as above |
| Audit | trade.opened, trade.executed, trade.failed, trade.settled, ai.tool.invoked, ai.prompt.built, system.error, system.warning, security.violation, secret.rotated (all consumer) | none | zero_candidates | No AUDIT.md or similarly-named document exists; audit trail is a cross-cutting concern described in multiple docs, not owned by one | **Needs human decision**: if an authoritative audit-log document is later added/identified, map it then |
| Dashboard | 25 distinct events (all consumer) | none | zero_candidates | 4 real dashboard documents exist (DASHBOARD-LAYOUT.md, DASHBOARD-RUNTIME.md, DASHBOARD-WIDGETS.md, DASHBOARD-WORKSPACES.md) -- "Dashboard" alone cannot be disambiguated to one of the four without guessing which subsystem actually consumes each specific event | **Not recommended to auto-resolve**: would require per-event review (e.g. does DASHBOARD-RUNTIME.md or DASHBOARD-WIDGETS.md consume `dashboard.widget.updated`?), out of scope for a name-level override |
| Error Handler | system.error (consumer) | none | zero_candidates | No dedicated error-handling document exists as a behavioural root (docs/ERROR-HANDLING-LOGGING.md exists but is a REFERENCE-type catalogue, not itself a subsystem) | **Not recommended** -- ERROR-HANDLING-LOGGING.md is a reference catalogue, not the "Error Handler" runtime subsystem the event table implies |
| Memory | ai.tool.result (consumer) | none | zero_candidates | No MEMORY.md exists as a behavioural root in this corpus | **Not recommended** -- no clear candidate found |
| Plugin Executor | plugin.error (publisher) | none | zero_candidates | Distinct from "Plugin Manager" (already resolved to PLUGIN-LIFECYCLE.md) -- "Plugin Executor" may be a different, more specific runtime component with no dedicated document | **Not recommended** -- risk of conflating with the already-resolved "Plugin Manager" mapping |
| Portfolio | trade.executed, trade.settled, wallet.balance.changed, wallet.transaction.confirmed (all consumer) | none | zero_candidates | docs/PORTFOLIO-MANAGEMENT.md and docs/PORTFOLIO-ANALYTICS.md both exist -- 2 candidates, cannot disambiguate which owns event consumption | **Not recommended to auto-resolve**: genuine 2-way ambiguity |
| Runtime | 6 distinct events (all consumer) | none | zero_candidates | Extremely overloaded generic term; could plausibly mean docs/RUNTIME-OPERATIONS.md, docs/APEX-KERNEL.md, or docs/ORCHESTRATOR.md (already used for "Runtime Orchestrator") -- genuinely ambiguous | **Not recommended to auto-resolve**: 3-way ambiguity, and "Runtime" vs "Runtime Orchestrator" appear intentionally distinct in the source table |
| Security Enforcer | security.violation (publisher) | none | zero_candidates | Distinct from "Security" (already resolved to SECURITY.md) -- "Security Enforcer" may name a specific runtime component within the broader Security subsystem | **Not recommended** -- risk of conflating with the already-resolved "Security" mapping; if truly the same subsystem, the source table should use one consistent name |
| Self-Healer | runtime.health.failed, runtime.health.restored (both consumer) | none | zero_candidates | No SELF-HEALER.md or similarly named document exists in this corpus | **Not recommended** -- no clear candidate found |
| Wallet | trade.executed, trade.rollback (both consumer) | none | zero_candidates | Distinct from "Wallet Manager" (already resolved to WALLET-MANAGEMENT.md) -- ambiguous whether "Wallet" the consumer role is the same subsystem or a different one (e.g. docs/WALLET-COMMAND-CENTER.md also exists) | **Not recommended to auto-resolve**: 2-way ambiguity between WALLET-MANAGEMENT.md and WALLET-COMMAND-CENTER.md |

## Approval Decision (2026-07-30)

The user explicitly reviewed and **approved all 8** "pending decision"
candidates below. They have been added to `MANUAL_NAME_OVERRIDES` in
`tools/governance/references/event_matrix_parser.py` and are now wired
into `event_graph`. This table is retained as the permanent audit
record of that decision (per the traceability requirement) even though
these 8 names have moved from "unresolved" to "resolved (manual
override, approved 2026-07-30)".

| Subsystem Name | Candidate | Decision |
|---|---|---|
| Chain Adapter | `docs/CHAIN-INTEGRATION.md` | **APPROVED** |
| Config Manager | `docs/CONFIGURATION.md` | **APPROVED** |
| DEX Adapter | `docs/DEX-INTEGRATION.md` | **APPROVED** |
| Health Checker | `docs/HEALTHCHECKS.md` | **APPROVED** |
| Monitoring | `docs/MONITORING-OBSERVABILITY.md` | **APPROVED** |
| Notification | `docs/NOTIFICATION-CENTER.md` | **APPROVED** |
| Secret Manager | `docs/SECRET-LIFECYCLE.md` | **APPROVED** |
| Widget Manager | `docs/DASHBOARD-WIDGETS.md` | **APPROVED** |

Post-approval resolved-name count: **27 of 39** (19 previous + 8 newly
approved). The remaining **13 names below remain permanently
unresolved** -- they have no plausible single-document candidate
(zero-candidate names) or are genuinely multi-way ambiguous
(Dashboard, Portfolio, Runtime, Wallet) or are deliberate broadcast
terms (All Subsystems, Any Subsystem) -- and are disclosed limitations,
not pending work.

## Original Recommendation (2026-07-30, historical -- 8 items resolved by the Approval Decision above)

Of the original 21 unresolved names identified before the 2026-07-30
approval, this review identified:
- **8 names with zero plausible candidate at all** (AI Cost Manager,
  All Subsystems, Any Subsystem, Audit, Error Handler, Memory,
  Plugin Executor, Self-Healer) -- no action possible without either
  authoring new documents or restructuring the event table itself.
- **2 names that are intentional broadcast/generic terms**, not real
  subsystems (All Subsystems, Any Subsystem) -- these should likely
  remain unresolved permanently, as mapping them to any single
  document would misrepresent a one-to-many relationship.
- **4 names with a genuine multi-way ambiguity** (Dashboard: 4
  candidates; Portfolio: 2 candidates; Runtime: 3 candidates; Wallet: 2
  candidates) -- resolving these requires either per-event review (not
  a name-level decision) or a source-table edit to use more specific
  subsystem names.
- **7 names with exactly one plausible candidate identified during
  this review**, but deliberately NOT auto-applied to
  `MANUAL_NAME_OVERRIDES` without explicit approval, since each
  candidate's name differs from the event-table subsystem name by more
  than a simple word-order/suffix change (Chain Adapter/Chain
  Integration, Config Manager/Configuration, DEX Adapter/DEX
  Integration, Health Checker/Healthchecks, Monitoring/Monitoring
  Observability, Notification/Notification Center, Secret
  Manager/Secret Lifecycle, Widget Manager/Dashboard Widgets):

  | Subsystem Name | Candidate | Approve? |
  |---|---|---|
  | Chain Adapter | `docs/CHAIN-INTEGRATION.md` | **APPROVED 2026-07-30** |
  | Config Manager | `docs/CONFIGURATION.md` | **APPROVED 2026-07-30** |
  | DEX Adapter | `docs/DEX-INTEGRATION.md` | **APPROVED 2026-07-30** |
  | Health Checker | `docs/HEALTHCHECKS.md` | **APPROVED 2026-07-30** |
  | Monitoring | `docs/MONITORING-OBSERVABILITY.md` | **APPROVED 2026-07-30** |
  | Notification | `docs/NOTIFICATION-CENTER.md` | **APPROVED 2026-07-30** |
  | Secret Manager | `docs/SECRET-LIFECYCLE.md` | **APPROVED 2026-07-30** |
  | Widget Manager | `docs/DASHBOARD-WIDGETS.md` | **APPROVED 2026-07-30** |

  All 8 were added to `MANUAL_NAME_OVERRIDES` in
  `tools/governance/references/event_matrix_parser.py` on 2026-07-30.
  Confirmed by live `apex-gov run`: resolved-name count rose from
  19/39 to **27/39**, and `event_graph_edges_resolved` rose from 78 to
  **102** (24 new edges, not the earlier ~20-30 estimate -- exact count
  confirmed by execution, not assumed).

## Traceability

This table was generated by directly running
`build_unresolved_names_report()` from
`tools/governance/references/event_matrix_parser.py` against the live
`docs/EVENT-OWNERSHIP-MATRIX.md`, cross-checked against
`.governance/exports/event_graph_resolution_report.json` (regenerated
on every `apex-gov run`). No entry in this table was fabricated or
inferred beyond what is stated -- every "possible candidate" was found
by manually inspecting the real `docs/` directory listing, not guessed
by the resolver itself (which, by design, never proposes candidates
that differ from the source name by more than the fixed deterministic
transform).
