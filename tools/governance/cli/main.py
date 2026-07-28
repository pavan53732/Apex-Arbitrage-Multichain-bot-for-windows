from __future__ import annotations
import json
import os
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

def sanitize_attrs(attrs: dict) -> dict:
    out = {}
    for k, v in attrs.items():
        if v is None:
            out[k] = ""
        elif isinstance(v, list):
            out[k] = ",".join(str(x) for x in v)
        else:
            out[k] = str(v)
    return out

@app.command()
def run(
    config_path: str = typer.Option("tools/governance/config/governance.yaml"),
    dry_run: bool = typer.Option(False),
):
    cfg = load_config(config_path)
    repo_root = Path(cfg["repo_root"]).resolve()
    if not repo_root.exists() or not (repo_root / "docs").exists():
        cfg_path = Path(config_path)
        for parent in [cfg_path] + list(cfg_path.parents):
            candidate = (parent.parent.parent.parent if "tools" in str(parent) else parent).resolve()
            if (candidate / "docs").exists():
                repo_root = candidate
                break
    docs_globs = cfg["docs_globs"]
    behavioural_signals = cfg["behavioural_root_signals"]
    db_path = repo_root / cfg["storage"]["db_path"]
    export_dir = repo_root / cfg["storage"]["export_dir"]
    progress_path = repo_root / cfg["storage"]["progress_path"]
    graphs_dir = repo_root / cfg["storage"]["graphs_dir"]

    indexer = RepoIndexer(str(repo_root), docs_globs)
    md_parser = MarkdownParser(str(repo_root))
    meta_parser = MetadataParser()
    graph_builder = GraphBuilder()
    root_detector = BehaviouralRootDetector(behavioural_signals)
    store = SqliteStore(str(db_path))
    progress = ProgressTracker(progress_path)

    inventory = indexer.build_inventory()
    docs = []
    for item in inventory:
        parsed = md_parser.parse_file(item["path"])
        meta = meta_parser.parse_document(parsed["raw_text"], item["path"])
        docs.append(meta)
        graph_builder.add_document(meta)

    store.upsert_documents(docs)
    export_documents_json(docs, str(export_dir / "documents.json"))

    roots = root_detector.detect_roots(docs)
    closure_engine = ClosureEngine(graph_builder.dependency_graph)
    all_closures = {r.path: closure_engine.compute_closure(r.path) for r in roots}

    validator = GovernanceValidator(docs, graph_builder.dependency_graph)
    findings = validator.validate_all()

    completeness = CompletenessEngine()
    scores = {d.path: completeness.score_document(d) for d in docs}

    # Sanitize and export graphs
    graphs_dir.mkdir(parents=True, exist_ok=True)
    import networkx as nx
    for g_name, g in [("document_graph", graph_builder.doc_graph), ("dependency_graph", graph_builder.dependency_graph), ("ownership_graph", graph_builder.ownership_graph), ("event_graph", graph_builder.event_graph), ("config_graph", graph_builder.config_graph), ("schema_graph", graph_builder.schema_graph), ("interface_graph", graph_builder.interface_graph), ("state_machine_graph", graph_builder.state_machine_graph)]:
        g_copy = g.__class__()
        for n, data in g.nodes(data=True):
            g_copy.add_node(n, **sanitize_attrs(data))
        for u, v, data in g.edges(data=True):
            g_copy.add_edge(u, v, **sanitize_attrs(data))
        nx.write_graphml(g_copy, str(graphs_dir / f"{g_name}.graphml"))

    progress.update_programme(
        programme="Programme 1",
        phase="Documentation Intelligence Platform",
        completed=True,
        notes=[f"Indexed {len(docs)} documents", f"Detected {len(roots)} behavioural roots", f"Generated {len(findings)} validation findings", f"Computed {len(all_closures)} closures", f"Exported {8} graphs"],
    )

    output = {
        "documents_indexed": len(docs),
        "behavioural_roots": len(roots),
        "validation_findings": len(findings),
        "closures_computed": len(all_closures),
        "avg_completeness": sum(scores.values()) / len(scores) if scores else 0.0,
        "graph_nodes": graph_builder.doc_graph.number_of_nodes(),
        "graph_edges": graph_builder.dependency_graph.number_of_edges(),
    }
    console.print(json.dumps(output, indent=2))

@app.command()
def index(config_path: str = typer.Option("tools/governance/config/governance.yaml")):
    cfg = load_config(config_path)
    repo_root = Path(cfg["repo_root"]).resolve()
    indexer = RepoIndexer(str(repo_root), cfg["docs_globs"])
    console.print(f"Indexed {len(indexer.list_documents())} documents")

@app.command()
def validate(config_path: str = typer.Option("tools/governance/config/governance.yaml")):
    cfg = load_config(config_path)
    repo_root = Path(cfg["repo_root"]).resolve()
    indexer = RepoIndexer(str(repo_root), cfg["docs_globs"])
    md_parser = MarkdownParser(str(repo_root))
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
    repo_root = Path(cfg["repo_root"]).resolve()
    indexer = RepoIndexer(str(repo_root), cfg["docs_globs"])
    md_parser = MarkdownParser(str(repo_root))
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
    repo_root = Path(cfg["repo_root"]).resolve()
    indexer = RepoIndexer(str(repo_root), cfg["docs_globs"])
    md_parser = MarkdownParser(str(repo_root))
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
    repo_root = Path(cfg["repo_root"]).resolve()
    indexer = RepoIndexer(str(repo_root), cfg["docs_globs"])
    md_parser = MarkdownParser(str(repo_root))
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
def graphs(config_path: str = typer.Option("tools/governance/config/governance.yaml")):
    cfg = load_config(config_path)
    repo_root = Path(cfg["repo_root"]).resolve()
    graphs_dir = repo_root / cfg["storage"]["graphs_dir"]
    console.print(f"Graphs directory: {graphs_dir}")
    if graphs_dir.exists():
        for g in graphs_dir.glob("*.graphml"):
            console.print(f"- {g.name}")

@app.command()
def progress(config_path: str = typer.Option("tools/governance/config/governance.yaml")):
    cfg = load_config(config_path)
    repo_root = Path(cfg["repo_root"]).resolve()
    progress = ProgressTracker(repo_root / cfg["storage"]["progress_path"])
    console.print(progress.data)

if __name__ == "__main__":
    app()