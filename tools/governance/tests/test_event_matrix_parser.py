"""Tests for the Event Ownership Matrix parser (WS4: closing the
event_graph data-completeness gap). Per explicit instruction: parse all
unambiguous mappings automatically; for ambiguous/unmatched subsystem
names, never guess -- produce a documented, reviewable mapping table
instead."""
from pathlib import Path

from governance.references.event_matrix_parser import (
    MANUAL_NAME_OVERRIDES,
    build_event_graph_edges,
    build_unresolved_names_report,
    parse_event_ownership_matrix,
    resolve_subsystem_name,
)

_SAMPLE_TABLE = """
## Event Ownership Matrix

| Event | Publisher | Consumer(s) | Delivery | Ordering | Priority | Retention | Payload Schema |
|-------|-----------|-------------|----------|----------|----------|-----------|----------------|
| `trade.opened` | Trading Engine | Execution Engine, Risk Engine, Dashboard | Exactly-once | Key (trade_id) | Critical | 90 days | `TradeOpened` |
| `trade.failed` | Execution Engine | Trading Engine, Dashboard | Exactly-once | Key (trade_id) | Critical | 365 days | `TradeFailed` |
"""


def test_parse_event_ownership_matrix_extracts_all_rows():
    rows = parse_event_ownership_matrix(_SAMPLE_TABLE)
    assert len(rows) == 2
    assert rows[0].event_name == "trade.opened"
    assert rows[0].publisher_name == "Trading Engine"
    assert rows[0].consumer_names == ["Execution Engine", "Risk Engine", "Dashboard"]
    assert rows[0].payload_schema == "TradeOpened"


def test_parse_ignores_header_and_separator_rows():
    rows = parse_event_ownership_matrix(_SAMPLE_TABLE)
    event_names = [r.event_name for r in rows]
    assert "Event" not in event_names  # header row must not be captured


def test_resolve_subsystem_name_exact_deterministic_match(tmp_path):
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    (docs_dir / "TRADING-ENGINE.md").write_text("# Trading Engine")
    result = resolve_subsystem_name("Trading Engine", docs_dir)
    assert result == "docs/TRADING-ENGINE.md"


def test_resolve_subsystem_name_returns_none_when_zero_candidates(tmp_path):
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    (docs_dir / "TRADING-ENGINE.md").write_text("# Trading Engine")
    result = resolve_subsystem_name("Dashboard", docs_dir)
    assert result is None, "must never guess when there is no deterministic candidate"


def test_resolve_subsystem_name_uses_manual_override_when_present(tmp_path):
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    (docs_dir / "OPPORTUNITY-DETECTION.md").write_text("# Opportunity Detection")
    assert "Opportunity Detector" in MANUAL_NAME_OVERRIDES
    result = resolve_subsystem_name("Opportunity Detector", docs_dir)
    assert result == "docs/OPPORTUNITY-DETECTION.md"


def test_resolve_subsystem_name_manual_override_returns_none_if_target_missing(tmp_path):
    """Even a reviewed manual override must not silently resolve to a
    non-existent path -- if the target document doesn't exist in this
    checkout, treat it as unresolved rather than fabricating an edge to
    a missing node."""
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()  # empty -- OPPORTUNITY-DETECTION.md does not exist here
    result = resolve_subsystem_name("Opportunity Detector", docs_dir)
    assert result is None


def test_build_event_graph_edges_resolves_and_builds_edges(tmp_path):
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    (docs_dir / "TRADING-ENGINE.md").write_text("x")
    (docs_dir / "EXECUTION-ENGINE.md").write_text("x")
    (docs_dir / "RISK-ENGINE.md").write_text("x")
    # "Dashboard" deliberately has no document here -- must be excluded, not guessed.

    rows = parse_event_ownership_matrix(_SAMPLE_TABLE)
    result = build_event_graph_edges(rows, docs_dir)

    edge_docs = {e["source_document"] for e in result["edges"]}
    assert "docs/TRADING-ENGINE.md" in edge_docs
    assert "docs/EXECUTION-ENGINE.md" in edge_docs
    assert "docs/RISK-ENGINE.md" in edge_docs
    # Dashboard must never appear as a resolved edge source.
    assert all("DASHBOARD" not in d.upper() for d in edge_docs)
    assert result["unresolved_name_count"] >= 1
    assert any(u["name"] == "Dashboard" for u in result["unresolved_events"])


def test_build_event_graph_edges_produces_and_consumes_relations(tmp_path):
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    (docs_dir / "TRADING-ENGINE.md").write_text("x")
    (docs_dir / "EXECUTION-ENGINE.md").write_text("x")
    (docs_dir / "RISK-ENGINE.md").write_text("x")

    rows = parse_event_ownership_matrix(_SAMPLE_TABLE)
    result = build_event_graph_edges(rows, docs_dir)

    produces = [e for e in result["edges"] if e["relation"] == "produces"]
    consumes = [e for e in result["edges"] if e["relation"] == "consumes"]
    assert any(e["source_document"] == "docs/TRADING-ENGINE.md" and e["event_name"] == "trade.opened" for e in produces)
    assert any(e["source_document"] == "docs/RISK-ENGINE.md" and e["event_name"] == "trade.opened" for e in consumes)


def test_build_unresolved_names_report_excludes_resolved_names(tmp_path):
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    (docs_dir / "TRADING-ENGINE.md").write_text("x")
    (docs_dir / "EXECUTION-ENGINE.md").write_text("x")
    (docs_dir / "RISK-ENGINE.md").write_text("x")

    rows = parse_event_ownership_matrix(_SAMPLE_TABLE)
    report = build_unresolved_names_report(rows, docs_dir)

    unresolved_names = {e["subsystem_name"] for e in report["unresolved_names"]}
    assert "Dashboard" in unresolved_names
    assert "Trading Engine" not in unresolved_names  # resolves automatically, must be excluded
    assert "Execution Engine" not in unresolved_names


def test_build_unresolved_names_report_includes_traceability_to_events(tmp_path):
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    rows = parse_event_ownership_matrix(_SAMPLE_TABLE)
    report = build_unresolved_names_report(rows, docs_dir)
    dashboard_entry = next(e for e in report["unresolved_names"] if e["subsystem_name"] == "Dashboard")
    assert "trade.opened (consumer)" in dashboard_entry["events"]
    assert "trade.failed (consumer)" in dashboard_entry["events"]


def test_manual_overrides_all_resolve_against_real_repository():
    """Sanity check: every entry in MANUAL_NAME_OVERRIDES must resolve
    to a document that genuinely exists in the real repository (not
    just in a synthetic test fixture) -- these were hand-reviewed
    against the actual corpus and must not silently go stale."""
    import pytest
    repo_root = Path(__file__).resolve().parents[3]
    docs_dir = repo_root / "docs"
    if not docs_dir.exists():
        pytest.skip("real docs/ directory not present in this checkout")
    for name, path in MANUAL_NAME_OVERRIDES.items():
        full_path = repo_root / path
        assert full_path.exists(), f"MANUAL_NAME_OVERRIDES[{name!r}] = {path!r} does not exist"


def test_real_repository_event_ownership_matrix_parses_all_47_rows():
    import pytest
    repo_root = Path(__file__).resolve().parents[3]
    matrix_path = repo_root / "docs" / "EVENT-OWNERSHIP-MATRIX.md"
    if not matrix_path.exists():
        pytest.skip("real EVENT-OWNERSHIP-MATRIX.md not present in this checkout")
    rows = parse_event_ownership_matrix(matrix_path.read_text(encoding="utf-8"))
    assert len(rows) == 47


def test_real_repository_resolves_expected_count_of_names():
    """Sanity check against the real corpus: exactly 27 of 39 distinct
    subsystem names resolve (13 deterministic + 14 manual overrides --
    6 original + 8 approved 2026-07-30, see
    EVENT-MATRIX-UNRESOLVED-NAMES-REVIEW.md's "Approval Decision"
    section), yielding real event_graph edges; 13 remain genuinely
    unresolved (no safe single-document candidate, or deliberately
    generic/multi-way-ambiguous terms) and must be reflected in the
    unresolved-names report, never guessed."""
    import pytest
    repo_root = Path(__file__).resolve().parents[3]
    matrix_path = repo_root / "docs" / "EVENT-OWNERSHIP-MATRIX.md"
    docs_dir = repo_root / "docs"
    if not matrix_path.exists():
        pytest.skip("real EVENT-OWNERSHIP-MATRIX.md not present in this checkout")

    rows = parse_event_ownership_matrix(matrix_path.read_text(encoding="utf-8"))
    result = build_event_graph_edges(rows, docs_dir)
    assert result["resolved_name_count"] == 27
    assert result["unresolved_name_count"] == 13
    assert len(result["edges"]) == 102


def test_approved_2026_07_30_overrides_all_present_and_resolve():
    """Regression test for the 2026-07-30 user-approved batch of 8
    previously-"pending decision" subsystem name mappings (see
    EVENT-MATRIX-UNRESOLVED-NAMES-REVIEW.md's "Approval Decision"
    section for the full traceable reasoning per entry). Each must be
    present in MANUAL_NAME_OVERRIDES and resolve to a real, existing
    document in the actual repository -- this pins the approval so a
    future accidental revert would be caught immediately."""
    import pytest
    repo_root = Path(__file__).resolve().parents[3]
    docs_dir = repo_root / "docs"
    if not docs_dir.exists():
        pytest.skip("real docs/ directory not present in this checkout")

    approved = {
        "Chain Adapter": "docs/CHAIN-INTEGRATION.md",
        "Config Manager": "docs/CONFIGURATION.md",
        "DEX Adapter": "docs/DEX-INTEGRATION.md",
        "Health Checker": "docs/HEALTHCHECKS.md",
        "Monitoring": "docs/MONITORING-OBSERVABILITY.md",
        "Notification": "docs/NOTIFICATION-CENTER.md",
        "Secret Manager": "docs/SECRET-LIFECYCLE.md",
        "Widget Manager": "docs/DASHBOARD-WIDGETS.md",
    }
    for name, expected_path in approved.items():
        assert name in MANUAL_NAME_OVERRIDES, f"{name!r} missing from MANUAL_NAME_OVERRIDES"
        assert MANUAL_NAME_OVERRIDES[name] == expected_path
        assert (repo_root / expected_path).exists(), f"{expected_path} does not exist"
        resolved = resolve_subsystem_name(name, docs_dir)
        assert resolved == expected_path, f"{name!r} did not resolve to {expected_path!r} (got {resolved!r})"


def test_remaining_13_names_stay_permanently_unresolved():
    """The 13 names that were never recommended for approval (either
    zero plausible candidates, or genuine multi-way ambiguity, or
    deliberate broadcast/generic terms) must remain unresolved -- this
    guards against a future change accidentally guessing a mapping for
    one of them."""
    import pytest
    repo_root = Path(__file__).resolve().parents[3]
    matrix_path = repo_root / "docs" / "EVENT-OWNERSHIP-MATRIX.md"
    docs_dir = repo_root / "docs"
    if not matrix_path.exists():
        pytest.skip("real EVENT-OWNERSHIP-MATRIX.md not present in this checkout")

    rows = parse_event_ownership_matrix(matrix_path.read_text(encoding="utf-8"))
    result = build_event_graph_edges(rows, docs_dir)
    still_unresolved = {name for name, doc in result["name_resolutions"].items() if doc is None}
    expected_unresolved = {
        "AI Cost Manager", "All Subsystems", "Any Subsystem", "Audit",
        "Dashboard", "Error Handler", "Memory", "Plugin Executor",
        "Portfolio", "Runtime", "Security Enforcer", "Self-Healer", "Wallet",
    }
    assert still_unresolved == expected_unresolved
