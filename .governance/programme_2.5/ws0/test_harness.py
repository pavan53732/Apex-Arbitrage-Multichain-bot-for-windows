
from pathlib import Path
import json
import sys

from .loader.fixture_loader import RepositoryFixtureLoader
from .generator.golden_generator import GoldenOutputGenerator
from .comparator.golden_comparator import GoldenOutputComparator
from .dashboard.test_dashboard import TestDashboard

class GovernanceTestHarness:
    def __init__(self, root_dir: Path):
        self.root_dir = root_dir
        self.ws0_dir = root_dir / ".governance" / "programme_2.5" / "ws0"
        self.fixtures_dir = self.ws0_dir / "fixtures"
        self.golden_dir = self.ws0_dir / "golden_outputs"
        self.actual_dir = self.ws0_dir / "actual_outputs"
        self.dashboard_file = self.ws0_dir / "dashboard.json"

        self.loader = RepositoryFixtureLoader(self.fixtures_dir)
        self.generator = GoldenOutputGenerator(self.golden_dir)
        self.comparator = GoldenOutputComparator(self.golden_dir, self.actual_dir)
        self.dashboard = TestDashboard(self.dashboard_file)

    def run_all(self) -> dict:
        results = {
            "fixtures": [],
            "golden_generated": [],
            "regression": [],
            "determinism": [],
            "fresh_clone": [],
            "corruption": [],
            "stress": [],
            "fuzz": [],
        }

        # Run fixtures
        fixture_results = self.loader.run_all_fixtures()
        results["fixtures"] = [
            {"name": r.name, "passed": r.passed, "expected_roots": r.expected_roots, "actual_roots": r.actual_roots}
            for r in fixture_results
        ]

        # Generate golden outputs
        golden_hashes = {
            "root_registry": self.generator.generate_root_registry([]),
            "document_inventory": self.generator.generate_document_inventory([]),
            "ownership_graph": self.generator.generate_ownership_graph([]),
            "dependency_graph": self.generator.generate_dependency_graph([]),
            "metrics": self.generator.generate_metrics({}),
            "integrity_report": self.generator.generate_integrity_report({}),
        }
        results["golden_generated"] = list(golden_hashes.keys())

        # Compare (placeholder - actual comparison would happen after running engines)
        for filename in golden_hashes:
            comparison = self.comparator.compare(f"{filename}.json")
            results["regression"].append(comparison)

        # Update dashboard
        self.dashboard.update_regression(results["regression"])
        self.dashboard.add_evidence({"type": "test_run", "results": results})
        self.dashboard.save()

        return results

if __name__ == "__main__":
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    harness = GovernanceTestHarness(root)
    results = harness.run_all()
    print(json.dumps(results, indent=2))
