"""Tests for the deterministic schema reference scanner (WS4: closing
the schema_graph data-completeness gap, per explicit instruction to be
conservative -- exact literal filename matches only, no fuzzy matching,
full traceability)."""
from pathlib import Path

from governance.references.schema_reference_scanner import (
    build_schema_reference_report,
    scan_corpus_for_schema_references,
    scan_document_for_schema_references,
)


def test_resolves_exact_match_with_schemas_prefix():
    text = "   a. Validate manifest schema against schemas/plugin.schema.json.\n"
    refs = scan_document_for_schema_references("docs/PLUGIN-LIFECYCLE.md", text, {"plugin.schema.json"})
    assert len(refs) == 1
    assert refs[0].resolved is True
    assert refs[0].schema_filename == "plugin.schema.json"
    assert refs[0].line_number == 1
    assert refs[0].matched_text == "schemas/plugin.schema.json"


def test_resolves_exact_match_case_insensitive_directory_prefix():
    """docs/CONFIGURATION-REFERENCE.md uses 'SCHEMAS/' (uppercase)."""
    text = "- **SCHEMAS/configuration.schema.json** — JSON Schema for config validation.\n"
    refs = scan_document_for_schema_references("docs/CONFIGURATION-REFERENCE.md", text, {"configuration.schema.json"})
    assert len(refs) == 1
    assert refs[0].resolved is True
    assert refs[0].schema_filename == "configuration.schema.json"


def test_does_not_fuzzy_match_similarly_named_nonexistent_file():
    """Regression guard for the exact scenario found in docs/TESTING.md:
    'config.schema.json' is mentioned but does NOT exist (only
    'configuration.schema.json' does) -- must NOT be silently coerced
    to the similarly-named real file. Per explicit instruction: no
    inferred aliases, exact filename matches only."""
    text = "| **Configuration contracts** | ... | Vitest + config.schema.json | Every PR |\n"
    refs = scan_document_for_schema_references("docs/TESTING.md", text, {"configuration.schema.json"})
    assert len(refs) == 1
    assert refs[0].schema_filename == "config.schema.json"
    assert refs[0].resolved is False, "must NOT fuzzy-match to configuration.schema.json"


def test_multiple_references_on_different_lines_all_captured_with_correct_line_numbers():
    text = (
        "line one is irrelevant\n"
        "| `dashboard.trade` | ... | `schemas/event.schema.json` | ... |\n"
        "another irrelevant line\n"
        "| `dashboard.widget` | ... | `schemas/settings.schema.json` | ... |\n"
    )
    known = {"event.schema.json", "settings.schema.json"}
    refs = scan_document_for_schema_references("docs/DASHBOARD-RUNTIME.md", text, known)
    assert len(refs) == 2
    assert refs[0].line_number == 2
    assert refs[0].schema_filename == "event.schema.json"
    assert refs[1].line_number == 4
    assert refs[1].schema_filename == "settings.schema.json"


def test_no_references_found_returns_empty_list():
    refs = scan_document_for_schema_references("docs/UNRELATED.md", "Nothing here mentions any schema file.", {"event.schema.json"})
    assert refs == []


def test_repeated_references_to_same_schema_all_recorded_separately():
    """DASHBOARD-RUNTIME.md references schemas/event.schema.json 5
    times across different table rows -- each must be recorded as a
    distinct, traceable reference (not deduplicated), since each
    represents a genuinely distinct sentence/claim in the source."""
    text = "\n".join([f"| `x.{i}` | ... | `schemas/event.schema.json` | ... |" for i in range(5)])
    refs = scan_document_for_schema_references("docs/DASHBOARD-RUNTIME.md", text, {"event.schema.json"})
    assert len(refs) == 5
    assert all(r.schema_filename == "event.schema.json" for r in refs)
    assert [r.line_number for r in refs] == [1, 2, 3, 4, 5]


def test_scan_corpus_uses_real_schemas_directory(tmp_path):
    schemas_dir = tmp_path / "schemas"
    schemas_dir.mkdir()
    (schemas_dir / "plugin.schema.json").write_text("{}")
    (schemas_dir / "event.schema.json").write_text("{}")

    class FakeDoc:
        def __init__(self, path, raw_text):
            self.path = path
            self.raw_text = raw_text

    docs = [
        FakeDoc("docs/A.md", "See schemas/plugin.schema.json for details."),
        FakeDoc("docs/B.md", "No schema mention here at all."),
        FakeDoc("docs/C.md", "References schemas/nonexistent.schema.json."),
    ]
    result = scan_corpus_for_schema_references(docs, schemas_dir)
    assert set(result.keys()) == {"docs/A.md", "docs/C.md"}  # B has no matches, excluded
    assert result["docs/A.md"][0].resolved is True
    assert result["docs/C.md"][0].resolved is False


def test_scan_corpus_empty_when_schemas_dir_missing(tmp_path):
    class FakeDoc:
        path = "docs/A.md"
        raw_text = "schemas/plugin.schema.json"

    result = scan_corpus_for_schema_references([FakeDoc()], tmp_path / "does_not_exist")
    # schemas_dir doesn't exist -> known_filenames is empty -> reference
    # found but unresolved (not silently dropped).
    assert "docs/A.md" in result
    assert result["docs/A.md"][0].resolved is False


def test_build_schema_reference_report_separates_resolved_and_unresolved():
    from governance.references.schema_reference_scanner import SchemaReference
    scan_results = {
        "docs/A.md": [
            SchemaReference("docs/A.md", 1, "schemas/plugin.schema.json", "plugin.schema.json", True),
            SchemaReference("docs/A.md", 5, "config.schema.json", "config.schema.json", False),
        ],
    }
    report = build_schema_reference_report(scan_results)
    assert report["total_references_found"] == 2
    assert report["resolved_count"] == 1
    assert report["unresolved_count"] == 1
    assert report["resolved_references"][0]["schema_filename"] == "plugin.schema.json"
    assert report["unresolved_references"][0]["schema_filename"] == "config.schema.json"
    assert "reason" in report["unresolved_references"][0]


def test_real_repository_corpus_finds_expected_resolved_references():
    """Sanity check against the ACTUAL repository corpus, confirming
    the scanner correctly resolves the 8 real references identified
    during manual investigation (PLUGIN-LIFECYCLE.md x1,
    CONFIGURATION-REFERENCE.md x1, DASHBOARD-RUNTIME.md x7) and
    correctly leaves docs/TESTING.md's 'config.schema.json' /
    'event.schema.json' mentions unresolved-if-nonexistent or
    resolved-if-real (event.schema.json IS real; config.schema.json is
    NOT)."""
    import pytest
    repo_root = Path(__file__).resolve().parents[3]
    schemas_dir = repo_root / "schemas"
    if not schemas_dir.exists():
        pytest.skip("real schemas/ directory not present in this checkout")

    class FakeDoc:
        def __init__(self, path):
            self.path = path
            self.raw_text = (repo_root / path).read_text(encoding="utf-8")

    candidate_paths = [
        "docs/PLUGIN-LIFECYCLE.md",
        "docs/CONFIGURATION-REFERENCE.md",
        "docs/DASHBOARD-RUNTIME.md",
        "docs/TESTING.md",
    ]
    docs = [FakeDoc(p) for p in candidate_paths if (repo_root / p).exists()]
    if not docs:
        pytest.skip("expected real documents not present in this checkout")

    result = scan_corpus_for_schema_references(docs, schemas_dir)
    all_refs = [r for refs in result.values() for r in refs]
    resolved = [r for r in all_refs if r.resolved]
    unresolved = [r for r in all_refs if not r.resolved]

    # docs/TESTING.md's "config.schema.json" must be unresolved (real
    # file is "configuration.schema.json", not "config.schema.json").
    testing_unresolved = [r for r in unresolved if r.document_path == "docs/TESTING.md"]
    assert any(r.schema_filename == "config.schema.json" for r in testing_unresolved)

    # docs/PLUGIN-LIFECYCLE.md's plugin.schema.json mention must resolve.
    plugin_resolved = [r for r in resolved if r.document_path == "docs/PLUGIN-LIFECYCLE.md"]
    assert any(r.schema_filename == "plugin.schema.json" for r in plugin_resolved)
