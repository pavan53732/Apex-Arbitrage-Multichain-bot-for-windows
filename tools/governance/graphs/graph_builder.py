from __future__ import annotations
import networkx as nx
from ..metadata.models import DocumentMetadata

class GraphBuilder:
    def __init__(self):
        self.doc_graph = nx.DiGraph()
        self.dependency_graph = nx.DiGraph()
        self.ownership_graph = nx.DiGraph()
        self.event_graph = nx.DiGraph()
        self.config_graph = nx.DiGraph()
        self.schema_graph = nx.DiGraph()
        self.interface_graph = nx.DiGraph()
        self.state_machine_graph = nx.DiGraph()
        # WS4 (Programme 2.5 Phase-0 graph_specification.json): 3 of the
        # remaining 6 required graphs mirror the existing field-to-graph
        # pattern above (document -> declared-item edges), using metadata
        # fields the parser already extracts.
        self.security_graph = nx.DiGraph()
        self.recovery_graph = nx.DiGraph()
        self.validation_graph = nx.DiGraph()

    def add_document(self, meta: DocumentMetadata):
        self.doc_graph.add_node(meta.path, **meta.model_dump())
        # WS4 fix: document_graph previously had nodes only, zero edges
        # (confirmed: 277 nodes / 0 edges even after the initial 14-graph
        # implementation pass), because nothing populated it beyond
        # add_node(). It is meant to represent raw document-to-document
        # relationships -- distinct from dependency_graph, which encodes
        # the narrower depends_on/required_by semantic specifically.
        # cross_references (220/277 documents have at least one) is the
        # correct source for this: every document's '## Cross-references'
        # section names other documents it relates to, independent of
        # formal dependency direction.
        for ref in meta.cross_references:
            self.doc_graph.add_edge(meta.path, ref, relation="references")
        for dep in meta.depends_on:
            self.dependency_graph.add_edge(meta.path, dep, relation="depends_on")
        for req in meta.required_by:
            self.dependency_graph.add_edge(req, meta.path, relation="required_by")
        if meta.owner:
            self.ownership_graph.add_edge(meta.owner, meta.path, relation="owns")
        for ev in meta.events_produced:
            self.event_graph.add_edge(meta.path, ev, relation="produces")
        for ev in meta.events_consumed:
            self.event_graph.add_edge(ev, meta.path, relation="consumes")
        for cfg in meta.configuration:
            self.config_graph.add_edge(meta.path, cfg, relation="configures")
        for sc in meta.schemas:
            self.schema_graph.add_edge(meta.path, sc, relation="uses_schema")
        for iface in meta.interfaces:
            self.interface_graph.add_edge(meta.path, iface, relation="implements")
        for sm in meta.state_machines:
            self.state_machine_graph.add_edge(meta.path, sm, relation="defines")
        for sec in meta.security:
            self.security_graph.add_edge(meta.path, sec, relation="declares_security_control")
        for rec in meta.recovery:
            self.recovery_graph.add_edge(meta.path, rec, relation="declares_recovery_behaviour")
        for val in meta.validation:
            self.validation_graph.add_edge(meta.path, val, relation="declares_validation_rule")

    def add_schema_references(self, scan_results: dict) -> None:
        """Merge resolved schema references into schema_graph, from
        governance.references.schema_reference_scanner.scan_corpus_for_schema_references().

        Like add_event_matrix_edges(), this is not per-document
        structured metadata (no document populates the `schemas` field
        via a `## Schemas` section) -- it comes from scanning every
        document's raw prose text for literal, exact schema filename
        mentions. Only RESOLVED references (exact match against a real
        file under schemas/) become edges; unresolved mentions (e.g.
        docs/TESTING.md's 'config.schema.json', which does not exist)
        are never added to the graph, only to the audit report.
        """
        for document_path, refs in scan_results.items():
            for ref in refs:
                if ref.resolved:
                    self.schema_graph.add_edge(document_path, ref.schema_filename, relation="uses_schema")

    def add_event_matrix_edges(self, edges: list[dict]) -> None:
        """Merge externally-resolved event edges into event_graph, from
        governance.references.event_matrix_parser.build_event_graph_edges().

        This data does NOT come from any single document's own metadata
        (unlike every other edge type in this class, added per-document
        via add_document()) -- it comes from parsing the single,
        canonical docs/EVENT-OWNERSHIP-MATRIX.md table and resolving
        each row's publisher/consumer SUBSYSTEM NAME to a document path.
        It is therefore added via a separate method, called once after
        all documents have been indexed (see cli/main.py's `run`
        command), rather than folded into add_document()'s per-document
        loop.
        """
        for edge in edges:
            doc_path = edge["source_document"]
            event_name = edge["event_name"]
            relation = edge["relation"]  # "produces" or "consumes"
            if relation == "produces":
                self.event_graph.add_edge(doc_path, event_name, relation="produces")
            else:
                self.event_graph.add_edge(event_name, doc_path, relation="consumes")
