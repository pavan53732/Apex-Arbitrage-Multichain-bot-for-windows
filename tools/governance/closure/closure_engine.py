from __future__ import annotations
import networkx as nx
from ..metadata.models import DocumentMetadata, BehaviouralRoot

class BehaviouralRootDetector:
    def __init__(self, behavioural_root_signals: list[str]):
        self.signals = behavioural_root_signals

    def detect_roots(self, docs: list[DocumentMetadata]) -> list[BehaviouralRoot]:
        roots = []
        for d in docs:
            signals_found = []
            text_fields = [d.type or "", d.purpose or "", d.scope or "", " ".join(d.responsibilities), " ".join(d.owns)]
            blob = " ".join(text_fields).lower()
            for s in self.signals:
                if s.lower() in blob:
                    signals_found.append(s)
            if not signals_found:
                continue
            roots.append(BehaviouralRoot(path=d.path, signals=signals_found, reason=f"Detected signals: {', '.join(signals_found)}"))
        return roots

class ClosureEngine:
    def __init__(self, dependency_graph: nx.DiGraph):
        self.graph = dependency_graph

    def compute_closure(self, root_path: str) -> set[str]:
        try:
            closure = set(nx.descendants(self.graph, root_path))
        except nx.NetworkXError:
            closure = set()
        closure.add(root_path)
        return closure
