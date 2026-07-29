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
