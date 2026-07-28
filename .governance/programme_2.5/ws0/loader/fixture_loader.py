
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Optional
import json

@dataclass
class FixtureResult:
    name: str
    expected_roots: int
    expected_docs: int
    expected_errors: List[str]
    actual_roots: int = 0
    actual_docs: int = 0
    actual_errors: List[str] = None
    passed: bool = False

    def __post_init__(self):
        if self.actual_errors is None:
            self.actual_errors = []

class RepositoryFixtureLoader:
    def __init__(self, fixtures_dir: Path):
        self.fixtures_dir = fixtures_dir
        self.fixtures = {
            "minimal_valid": {"expected_roots": 1, "expected_docs": 1, "expected_errors": []},
            "medium": {"expected_roots": 10, "expected_docs": 50, "expected_errors": []},
            "full_apex": {"expected_roots": 22, "expected_docs": 360, "expected_errors": []},
            "corrupted": {"expected_roots": 0, "expected_docs": 0, "expected_errors": ["missing_owners"]},
            "duplicate_ownership": {"expected_roots": 0, "expected_docs": 0, "expected_errors": ["duplicate_ownership"]},
            "broken_references": {"expected_roots": 0, "expected_docs": 0, "expected_errors": ["broken_references"]},
            "cyclic_dependency": {"expected_roots": 0, "expected_docs": 0, "expected_errors": ["cycles"]},
            "missing_metadata": {"expected_roots": 0, "expected_docs": 0, "expected_errors": ["missing_metadata"]},
            "invalid_graph": {"expected_roots": 0, "expected_docs": 0, "expected_errors": ["invalid_graph"]},
            "invalid_closure": {"expected_roots": 0, "expected_docs": 0, "expected_errors": ["invalid_closure"]},
        }

    def load_fixture(self, fixture_name: str) -> FixtureResult:
        if fixture_name not in self.fixtures:
            raise ValueError(f"Unknown fixture: {fixture_name}")

        fixture_config = self.fixtures[fixture_name]
        result = FixtureResult(
            name=fixture_name,
            expected_roots=fixture_config["expected_roots"],
            expected_docs=fixture_config["expected_docs"],
            expected_errors=fixture_config["expected_errors"],
        )

        # Load fixture repository
        fixture_path = self.fixtures_dir / fixture_name
        if not fixture_path.exists():
            result.actual_errors.append("fixture_not_found")
            return result

        # Count documents
        docs = list(fixture_path.glob("*.md"))
        result.actual_docs = len(docs)

        # Count roots (simplified - would use actual root detection in production)
        roots = [d for d in docs if "BEHAVIOURAL" in d.read_text(encoding="utf-8", errors="ignore")]
        result.actual_roots = len(roots)

        # Validate
        result.passed = (
            result.actual_roots == result.expected_roots and
            result.actual_docs == result.expected_docs and
            set(result.actual_errors) == set(result.expected_errors)
        )

        return result

    def run_all_fixtures(self) -> List[FixtureResult]:
        results = []
        for fixture_name in self.fixtures:
            result = self.load_fixture(fixture_name)
            results.append(result)
        return results
