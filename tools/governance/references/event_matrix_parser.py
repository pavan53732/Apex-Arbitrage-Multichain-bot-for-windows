"""Event Ownership Matrix parser (Programme 2.5 Phase-0, WS4 Knowledge
Graph -- closing the event_graph data-completeness gap).

`event_graph` was confirmed genuinely empty (0 nodes / 0 edges) because
no document populates `events_produced`/`events_consumed` via the `##
Events Produced`/`## Events Consumed` section pattern MetadataParser
looks for. However, `docs/EVENT-OWNERSHIP-MATRIX.md` contains a single,
canonical, already-structured table (47 rows) mapping every event to
its publisher and consumer(s) BY SUBSYSTEM NAME (e.g. "Trading
Engine", "Opportunity Detector") -- not by document path.

This module parses that table and resolves each subsystem name to a
real document path using ONLY exact, deterministic filename
transformations (name -> SLUG.md / SLUG-ENGINE.md / SLUG-MANAGER.md,
where SLUG is the name uppercased with spaces replaced by hyphens) --
never fuzzy matching, scoring, or inference. A name that does not
resolve to exactly one real file under `docs/` is left UNRESOLVED,
never guessed. Per explicit instruction, unresolved names are surfaced
in a reviewable mapping table (see `build_unresolved_names_report()`)
rather than silently wired in or silently dropped -- they are NOT
auto-applied to the graph until a human explicitly approves a mapping
via `MANUAL_NAME_OVERRIDES` below.

Confirmed via direct extraction against the real corpus (2026-07-30
review): of the 39 distinct subsystem names appearing across all 47
event rows, exactly 11 resolve unambiguously under the deterministic
transformation rules above (AI Gateway, AI Pipeline, Chain
Intelligence, Context Builder, Execution Engine, Market Data, RPC
Manager, Risk Engine, Routing Engine, Security, Slippage Model, Trading
Engine, Workspace Manager -- note: 13 resolve, not 11; see
MANUAL_NAME_OVERRIDES for the review table of the remaining 26+
names that had zero deterministic candidates, e.g. "Opportunity
Detector" (candidate OPPORTUNITY-DETECTOR.md does not exist; the real
document is OPPORTUNITY-DETECTION.md, a genuine naming mismatch, not
an ambiguity -- corrected explicitly below after review, not guessed
by the resolver).
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

# Reviewed, explicit, human-approved name -> document path overrides.
# Each entry here was checked by opening the candidate document and
# confirming its ## Purpose / ## Scope text genuinely describes owning
# the named subsystem's behaviour -- this is NOT a fuzzy-matching
# fallback; it is a hand-reviewed correction for cases where the
# subsystem's prose name in EVENT-OWNERSHIP-MATRIX.md differs from its
# document's filename by more than a mechanical slug transform (e.g.
# "Opportunity Detector" the subsystem vs. "OPPORTUNITY-DETECTION.md"
# the document name -- same subsystem, different word form).
#
# Names NOT in this dict and without a deterministic candidate remain
# UNRESOLVED and are excluded from the graph -- see
# build_unresolved_names_report().
MANUAL_NAME_OVERRIDES: dict[str, str] = {
    "Opportunity Detector": "docs/OPPORTUNITY-DETECTION.md",
    "Opportunity Ranker": "docs/OPPORTUNITY-RANKING.md",
    "AI Orchestrator": "docs/AI-ORCHESTRATION.md",
    "Runtime Orchestrator": "docs/ORCHESTRATOR.md",
    "Wallet Manager": "docs/WALLET-MANAGEMENT.md",
    "Plugin Manager": "docs/PLUGIN-LIFECYCLE.md",
    # --- Approved 2026-07-30 by explicit user sign-off on the 8 "pending
    # decision" candidates documented in
    # .governance/programme_2.5/_reconciliation/EVENT-MATRIX-UNRESOLVED-NAMES-REVIEW.md.
    # Each candidate document was re-verified to exist and to have a
    # `purpose:` front-matter statement plausibly describing the named
    # subsystem's responsibility before being added here -- see the
    # review document's "pending decision" table for the full reasoning
    # per entry. This is a human decision recorded in code, not an
    # automatic/fuzzy resolution.
    "Chain Adapter": "docs/CHAIN-INTEGRATION.md",
    "Config Manager": "docs/CONFIGURATION.md",
    "DEX Adapter": "docs/DEX-INTEGRATION.md",
    "Health Checker": "docs/HEALTHCHECKS.md",
    "Monitoring": "docs/MONITORING-OBSERVABILITY.md",
    "Notification": "docs/NOTIFICATION-CENTER.md",
    "Secret Manager": "docs/SECRET-LIFECYCLE.md",
    "Widget Manager": "docs/DASHBOARD-WIDGETS.md",
}

_ROW_PATTERN = re.compile(
    r"^\| `([^`]+)` \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| `([^`]+)` \|\s*$",
    re.MULTILINE,
)


@dataclass(frozen=True)
class EventOwnershipRow:
    event_name: str
    publisher_name: str
    consumer_names: list[str]
    delivery: str
    ordering: str
    priority: str
    retention: str
    payload_schema: str


def parse_event_ownership_matrix(raw_text: str) -> list[EventOwnershipRow]:
    """Parse every data row of the Event Ownership Matrix table. Header/
    separator rows are not matched by `_ROW_PATTERN` (they contain no
    backtick-quoted event name in the first column)."""
    rows = []
    for match in _ROW_PATTERN.finditer(raw_text):
        event, publisher, consumers, delivery, ordering, priority, retention, schema = match.groups()
        rows.append(
            EventOwnershipRow(
                event_name=event.strip(),
                publisher_name=publisher.strip(),
                consumer_names=[c.strip() for c in consumers.split(",")],
                delivery=delivery.strip(),
                ordering=ordering.strip(),
                priority=priority.strip(),
                retention=retention.strip(),
                payload_schema=schema.strip(),
            )
        )
    return rows


def _deterministic_candidates(name: str, known_doc_files: set[str]) -> list[str]:
    """Exact, deterministic filename transformations only -- no fuzzy
    scoring. Returns the subset that actually exist in
    `known_doc_files`, so a name resolves only when exactly one
    transformation produces a real file."""
    slug = name.strip().upper().replace(" ", "-").replace("'", "")
    candidates = {
        f"{slug}.md",
        f"{slug}-ENGINE.md",
        f"{slug}-MANAGER.md",
    }
    if slug.endswith("-MANAGER"):
        candidates.add(f"{slug[: -len('-MANAGER')]}.md")
    if slug.endswith("-ENGINE"):
        candidates.add(f"{slug[: -len('-ENGINE')]}.md")
    return sorted(c for c in candidates if c in known_doc_files)


def resolve_subsystem_name(name: str, docs_dir: Path) -> Optional[str]:
    """Resolve a subsystem name to a document path (relative, e.g.
    'docs/TRADING-ENGINE.md'), or None if unresolved.

    Resolution order:
    1. `MANUAL_NAME_OVERRIDES` (human-reviewed, exact corrections).
    2. Exactly one deterministic filename-transform candidate exists.
    3. Otherwise: unresolved (never guessed).
    """
    if name in MANUAL_NAME_OVERRIDES:
        candidate_path = Path(MANUAL_NAME_OVERRIDES[name])
        full_path = docs_dir.parent / candidate_path if not candidate_path.is_absolute() else candidate_path
        if full_path.exists():
            return str(candidate_path)
        return None

    known_doc_files = {p.name for p in docs_dir.glob("*.md")} if docs_dir.exists() else set()
    candidates = _deterministic_candidates(name, known_doc_files)
    if len(candidates) == 1:
        return f"docs/{candidates[0]}"
    return None


def build_event_graph_edges(
    rows: list[EventOwnershipRow], docs_dir: Path
) -> dict:
    """Resolve every row's publisher/consumer names to document paths
    and build the edge list for event_graph, plus a full audit trail of
    every resolution decision (resolved or not) for traceability back
    to the source table."""
    resolutions: dict[str, Optional[str]] = {}
    all_names: set[str] = set()
    for row in rows:
        all_names.add(row.publisher_name)
        all_names.update(row.consumer_names)
    for name in sorted(all_names):
        resolutions[name] = resolve_subsystem_name(name, docs_dir)

    edges = []
    unresolved_events = []
    for row in rows:
        publisher_doc = resolutions.get(row.publisher_name)
        consumer_docs = [resolutions.get(c) for c in row.consumer_names]
        if publisher_doc:
            edges.append({
                "source_document": publisher_doc,
                "event_name": row.event_name,
                "relation": "produces",
                "publisher_subsystem_name": row.publisher_name,
            })
        else:
            unresolved_events.append({"event": row.event_name, "role": "publisher", "name": row.publisher_name})
        for consumer_name, consumer_doc in zip(row.consumer_names, consumer_docs):
            if consumer_doc:
                edges.append({
                    "source_document": consumer_doc,
                    "event_name": row.event_name,
                    "relation": "consumes",
                    "consumer_subsystem_name": consumer_name,
                })
            else:
                unresolved_events.append({"event": row.event_name, "role": "consumer", "name": consumer_name})

    return {
        "edges": edges,
        "name_resolutions": resolutions,
        "resolved_name_count": sum(1 for v in resolutions.values() if v),
        "unresolved_name_count": sum(1 for v in resolutions.values() if not v),
        "unresolved_events": unresolved_events,
        "source_document": "docs/EVENT-OWNERSHIP-MATRIX.md",
    }


def build_unresolved_names_report(rows: list[EventOwnershipRow], docs_dir: Path) -> dict:
    """Build the reviewable mapping table for every subsystem name that
    does NOT resolve automatically -- for human review before any
    MANUAL_NAME_OVERRIDES entry is added. Includes every event each
    unresolved name appears on, and why it's ambiguous/unmatched."""
    all_names: set[str] = set()
    name_events: dict[str, list[str]] = {}
    for row in rows:
        for name, role in [(row.publisher_name, "publisher")] + [(c, "consumer") for c in row.consumer_names]:
            all_names.add(name)
            name_events.setdefault(name, []).append(f"{row.event_name} ({role})")

    known_doc_files = {p.name for p in docs_dir.glob("*.md")} if docs_dir.exists() else set()
    entries = []
    for name in sorted(all_names):
        if name in MANUAL_NAME_OVERRIDES:
            continue
        candidates = _deterministic_candidates(name, known_doc_files)
        if len(candidates) == 1:
            continue  # already resolves automatically
        entries.append({
            "subsystem_name": name,
            "events": name_events[name],
            "candidate_documents": candidates,
            "confidence": "zero_candidates" if not candidates else "multiple_candidates",
            "reason": (
                "no document filename matches the deterministic slug transform "
                "(name.upper().replace(' ','-') + .md/.{-ENGINE,-MANAGER}.md)"
                if not candidates
                else f"{len(candidates)} candidate documents matched, cannot disambiguate automatically"
            ),
            "recommended_mapping": None,
        })
    return {"unresolved_names": entries, "total_unresolved": len(entries)}
