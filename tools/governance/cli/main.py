from __future__ import annotations
import json
from pathlib import Path
import typer
import yaml
from rich.console import Console

from ..config.config_loader import load_config
from ..indexer.repo_indexer import RepoIndexer
from ..parser.markdown_parser import MarkdownParser
from ..metadata.metadata_parser import MetadataParser
from ..references.reference_parser import ReferenceParser
from ..graphs.graph_builder import GraphBuilder
from ..closure.closure_engine import BehaviouralRootDetector, ClosureEngine
from ..validator.governance_validator import GovernanceValidator
from ..metrics.metrics_engine import CompletenessEngine
from ..storage.sqlite_store import SqliteStore
from ..storage.json_export import export_documents_json
from ..progress.progress_tracker import ProgressTracker

console = Console()
app = typer.Typer()

@app.command()
def run(
    config_path: str = typer.Option("tools/governance/config/governance.yaml"),
    dry_run: bool = typer.Option(False),
):
    cfg = load_config(config_path)
    repo_root = cfg["repo_root"]
    docs_globs = cfg["docs_globs"]
    behavioural_signals = cfg["behavioural_root_signals"]
    db_path = cfg["storage"]["db_path"]
    export_dir = cfg["storage"]["export_dir"]
    progress_path = cfg["storage"]["progress_path"]

    indexer = RepoIndexer(repo_root, docs_globs)
    md_parser = MarkdownParser(repo_root)
    meta_parser = MetadataParser()
    graph_builder = GraphBuilder()
    root_detector = BehaviouralRootDetector(behavioural_signals)
    store = SqliteStore(db_path)
    progress = ProgressTracker(Path(repo_root) / progress_path)

    inventory = indexer.build_inventory()
    docs = []
    for item in inventory:
        parsed = md_parser.parse_file(item["path"])
        meta = meta_parser.parse_document(parsed["raw_text"], item["path"])
        docs.append(meta)
        graph_builder.add_document(meta)

    store.upsert_documents(docs)
    export_documents_json(docs, str(Path(repo_root) / export_dir / "documents.json"))

    roots = root_detector.detect_roots(docs)
    closure_engine = ClosureEngine(graph_builder.dependency_graph)
    all_closures = {r.path: closure_engine.compute_closure(r.path) for r in roots}

    validator = GovernanceValidator(docs, graph_builder.dependency_graph)
    findings = validator.validate_all()

    completeness = CompletenessEngine()
    scores = {d.path: completeness.score_document(d) for d in docs}

    progress.update_programme(
        programme="Programme 1",
        phase="Documentation Intelligence Platform",
        completed=True,
        notes=[f"Indexed {len(docs)} documents", f"Detected {len(roots)} behavioural roots", f"Generated {len(findings)} validation findings"],
    )

    output = {"documents_indexed": len(docs), "behavioural_roots": len(roots), "validation_findings": len(findings), "avg_completeness": sum(scores.values()) / len(scores) if scores else 0.0}
    console.print(json.dumps(output, indent=2))

@app.command()
def index(config_path: str = typer.Option("tools/governance/config/governance.yaml")):
    cfg = load_config(config_path)
    indexer = RepoIndexer(cfg["repo_root"], cfg["docs_globs"])
    console.print(f"Indexed {len(indexer.list_documents())} documents")

@app.command()
def validate(config_path: str = typer.Option("tools/governance/config/governance.yaml")):
    cfg = load_config(config_path)
    from ..indexer.repo_indexer import RepoIndexer
    from ..parser.markdown_parser import MarkdownParser
    from ..metadata.metadata_parser import MetadataParser
    from ..graphs.graph_builder import GraphBuilder
    from ..validator.governance_validator import GovernanceValidator
    indexer = RepoIndexer(cfg["repo_root"], cfg["docs_globs"])
    md_parser = MarkdownParser(cfg["repo_root"])
    meta_parser = MetadataParser()
    graph_builder = GraphBuilder()
    docs = []
    for item in indexer.build_inventory():
        parsed = md_parser.parse_file(item["path"])
        meta = meta_parser.parse_document(parsed["raw_text"], item["path"])
        docs.append(meta)
        graph_builder.add_document(meta)
    validator = GovernanceValidator(docs, graph_builder.dependency_graph)
    findings = validator.validate_all()
    console.print(f"Findings: {len(findings)}")
    for f in findings[:20]:
        console.print(f"- [{f.severity.value}] {f.path}: {f.message}")

@app.command()
def roots(config_path: str = typer.Option("tools/governance/config/governance.yaml")):
    cfg = load_config(config_path)
    from ..indexer.repo_indexer import RepoIndexer
    from ..parser.markdown_parser import MarkdownParser
    from ..metadata.metadata_parser import MetadataParser
    from ..closure.closure_engine import BehaviouralRootDetector
    indexer = RepoIndexer(cfg["repo_root"], cfg["docs_globs"])
    md_parser = MarkdownParser(cfg["repo_root"])
    meta_parser = MetadataParser()
    docs = []
    for item in indexer.build_inventory():
        parsed = md_parser.parse_file(item["path"])
        meta = meta_parser.parse_document(parsed["raw_text"], item["path"])
        docs.append(meta)
    detector = BehaviouralRootDetector(cfg["behavioural_root_signals"])
    roots = detector.detect_roots(docs)
    console.print(f"Behavioural roots: {len(roots)}")
    for r in roots:
        console.print(f"- {r.path}: {r.reason}")

@app.command()
def closure(root_path: str, config_path: str = typer.Option("tools/governance/config/governance.yaml")):
    cfg = load_config(config_path)
    from ..indexer.repo_indexer import RepoIndexer
    from ..parser.markdown_parser import MarkdownParser
    from ..metadata.metadata_parser import MetadataParser
    from ..graphs.graph_builder import GraphBuilder
    from ..closure.closure_engine import ClosureEngine
    indexer = RepoIndexer(cfg["repo_root"], cfg["docs_globs"])
    md_parser = MarkdownParser(cfg["repo_root"])
    meta_parser = MetadataParser()
    graph_builder = GraphBuilder()
    docs = []
    for item in indexer.build_inventory():
        parsed = md_parser.parse_file(item["path"])
        meta = meta_parser.parse_document(parsed["raw_text"], item["path"])
        docs.append(meta)
        graph_builder.add_document(meta)
    closure_engine = ClosureEngine(graph_builder.dependency_graph)
    closure = closure_engine.compute_closure(root_path)
    console.print(f"Closure for {root_path}: {len(closure)} documents")
    for p in sorted(closure):
        console.print(f"  - {p}")

@app.command()
def completeness(config_path: str = typer.Option("tools/governance/config/governance.yaml")):
    cfg = load_config(config_path)
    from ..indexer.repo_indexer import RepoIndexer
    from ..parser.markdown_parser import MarkdownParser
    from ..metadata.metadata_parser import MetadataParser
    from ..metrics.metrics_engine import CompletenessEngine
    indexer = RepoIndexer(cfg["repo_root"], cfg["docs_globs"])
    md_parser = MarkdownParser(cfg["repo_root"])
    meta_parser = MetadataParser()
    engine = CompletenessEngine()
    scores = []
    for item in indexer.build_inventory():
        parsed = md_parser.parse_file(item["path"])
        meta = meta_parser.parse_document(parsed["raw_text"], item["path"])
        scores.append(engine.score_document(meta))
    avg = sum(scores) / len(scores) if scores else 0.0
    console.print(f"Average completeness: {avg:.2f}")

@app.command()
def standardise(config_path: str = typer.Option("tools/governance/config/governance.yaml")):
    console.print("Programme 2: Documentation Standardisation not yet implemented in this pass.")

@app.command()
def graphs(config_path: str = typer.Option("tools/governance/config/governance.yaml")):
    console.print("Programme 4: Graph generation stub; graphs built internally during run.")

@app.command()
def context(root_path: str, config_path: str = typer.Option("tools/governance/config/governance.yaml")):
    console.print("Programme 5: Context builder stub; use closure for now.")

@app.command()
def metrics(config_path: str = typer.Option("tools/governance/config/governance.yaml")):
    console.print("Programme 8: Metrics stub; run completeness and validate for metrics.")

@app.command()
def progress(config_path: str = typer.Option("tools/governance/config/governance.yaml")):
    cfg = load_config(config_path)
    progress = ProgressTracker(Path(cfg["repo_root"]) / cfg["storage"]["progress_path"])
    console.print(progress.data)

if __name__ == "__main__":
    app()
