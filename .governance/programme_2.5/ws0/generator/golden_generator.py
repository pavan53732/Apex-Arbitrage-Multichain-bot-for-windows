
from pathlib import Path
import json
import hashlib

class GoldenOutputGenerator:
    def __init__(self, output_dir: Path):
        self.output_dir = output_dir

    def generate_root_registry(self, roots: list) -> str:
        registry = {"roots": roots, "count": len(roots)}
        content = json.dumps(registry, indent=2, sort_keys=True)
        hash_val = hashlib.sha256(content.encode()).hexdigest()[:16]
        output_file = self.output_dir / "golden_root_registry.json"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
        return hash_val

    def generate_document_inventory(self, docs: list) -> str:
        inventory = {"documents": docs, "count": len(docs)}
        content = json.dumps(inventory, indent=2, sort_keys=True)
        hash_val = hashlib.sha256(content.encode()).hexdigest()[:16]
        output_file = self.output_dir / "golden_document_inventory.json"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
        return hash_val

    def generate_ownership_graph(self, edges: list) -> str:
        graph = {"type": "ownership", "edges": edges}
        content = json.dumps(graph, indent=2, sort_keys=True)
        hash_val = hashlib.sha256(content.encode()).hexdigest()[:16]
        output_file = self.output_dir / "golden_ownership_graph.json"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
        return hash_val

    def generate_dependency_graph(self, edges: list) -> str:
        graph = {"type": "dependency", "edges": edges}
        content = json.dumps(graph, indent=2, sort_keys=True)
        hash_val = hashlib.sha256(content.encode()).hexdigest()[:16]
        output_file = self.output_dir / "golden_dependency_graph.json"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
        return hash_val

    def generate_metrics(self, metrics: dict) -> str:
        content = json.dumps(metrics, indent=2, sort_keys=True)
        hash_val = hashlib.sha256(content.encode()).hexdigest()[:16]
        output_file = self.output_dir / "golden_metrics.json"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
        return hash_val

    def generate_integrity_report(self, report: dict) -> str:
        content = json.dumps(report, indent=2, sort_keys=True)
        hash_val = hashlib.sha256(content.encode()).hexdigest()[:16]
        output_file = self.output_dir / "golden_integrity_report.json"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
        return hash_val
