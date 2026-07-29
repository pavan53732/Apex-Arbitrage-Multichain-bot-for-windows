"""Derived knowledge graphs (Programme 2.5 Phase-0, WS4 Knowledge
Graph): service_graph, plugin_graph, runtime_graph, algorithm_graph.

`graph_specification.json` freezes 14 graphs. 7 of them
(document/dependency/ownership/interface/event/schema/configuration)
were already implemented in `GraphBuilder`, and 3 more
(security/recovery/validation) were added directly to `GraphBuilder`
alongside them (see graph_builder.py) because they follow the exact
same "declared metadata list -> per-item edge" pattern the existing 7
already use.

The remaining 4 (service, plugin, runtime, algorithm) have no
corresponding single metadata field to iterate the same way -- there is
no `services:`/`plugins:`/`runtime:`/`algorithms:` front-matter field
anywhere in the 277-document corpus. Rather than inventing a new
metadata field the corpus doesn't populate (which would produce another
all-zero graph, the exact defect already found and disclosed for
event_graph/schema_graph), these 4 are built as REAL, non-trivial
induced subgraphs of the single canonical dependency graph, filtered by
criteria the pipeline already computes:

- `service_graph`: the dependency graph induced on documents tiered as
  Tier D (Subsystem Root) or Tier E (Integration Root) -- i.e. the
  "service" concept in this platform's own architecture documents
  (docs/API-CONTRACTS.md's "Core Service Interfaces" table) maps
  directly onto subsystem/integration-level behavioural roots, not UI
  or kernel-level ones.
- `plugin_graph`: the dependency graph induced on every document whose
  path or purpose text mentions "plugin" (PLUGIN-SDK.md,
  PLUGIN-LIFECYCLE.md, PLUGIN-SANDBOX-CONTRACT.md, PLUGIN-STATE-MACHINE.md,
  PLUGIN-MARKETPLACE.md, APP-BUILDER-PLUGIN-SYSTEM.md, plus their
  immediate dependency-graph neighbours).
- `runtime_graph`: the dependency graph induced on documents tiered as
  Tier A (Platform Root), Tier B (Kernel Root), or Tier C (Runtime
  Root) -- the platform's own runtime-lifecycle-owning layer.
- `algorithm_graph`: the dependency graph induced on documents whose
  purpose/scope text matches the same ALGORITHM_KEYWORDS used by the
  ALGORITHM-001 category validator (validator/algorithm/checks.py) --
  reusing that keyword list rather than defining a second, potentially
  inconsistent one.

Each of these is a genuine, populated (non-empty on the current corpus)
graph -- not a placeholder -- and each is fully reproducible from data
the canonical pipeline already computed (tier_report, dependency_graph,
docs), preserving the single-canonical-computation invariant.
"""
from __future__ import annotations

import networkx as nx

from ..metadata.models import DocumentMetadata
from ..validator.algorithm.checks import _claims_algorithm_content

SERVICE_TIERS = {"Tier D: Subsystem Root", "Tier E: Integration Root"}
RUNTIME_TIERS = {"Tier A: Platform Root", "Tier B: Kernel Root", "Tier C: Runtime Root"}


def _deterministic_induced_subgraph(graph: nx.DiGraph, node_set: set[str]) -> nx.DiGraph:
    """Build the induced subgraph of `graph` on `node_set`, with fully
    deterministic node and edge insertion order.

    IMPORTANT (determinism): `nx.DiGraph.subgraph(nodes)` does NOT
    preserve the order of whatever iterable is passed to it, even a
    pre-sorted list -- internally, `subgraph()` wraps the node filter in
    `networkx.classes.filters.show_nodes`, whose `__init__` immediately
    does `self.nodes = set(nodes)` (see
    site-packages/networkx/classes/filters.py). The resulting view's
    `FilterAtlas.__iter__` (networkx/classes/coreviews.py) then iterates
    that internal `set` directly whenever it is smaller than the parent
    graph's node count -- which is exactly the case for every derived
    graph here (a small subset of the 277-document corpus) -- so the
    final node/edge order depends on Python's per-process string hash
    randomisation (PYTHONHASHSEED) regardless of what order was
    originally passed in. This was confirmed by direct reproduction:
    `graph.subgraph(sorted(node_set))` still produced 3 different
    GraphML byte sequences across 3 fresh processes with the exact same
    logical node/edge content.

    Fixed by NOT using `subgraph()`'s node view at all: construct a
    fresh `nx.DiGraph` and add nodes/edges directly, iterating our own
    explicitly `sorted()` collections throughout, so no networkx
    internal set-iteration is ever involved in determining output
    order. This is the same non-determinism defect CLASS already found
    and fixed elsewhere in this codebase (see
    references/reference_parser.py's `_dedupe_preserve_order()` and
    storage/sqlite_store.py's `fresh=True` rebuild) -- fixed here by
    avoiding the offending API entirely rather than trying to out-sort
    it.
    """
    result = nx.DiGraph()
    for n in sorted(node_set):
        if n in graph:
            result.add_node(n, **graph.nodes[n])
        else:
            result.add_node(n)
    for u, v, data in sorted(
        ((u, v, d) for u, v, d in graph.edges(data=True) if u in node_set and v in node_set),
        key=lambda t: (t[0], t[1]),
    ):
        result.add_edge(u, v, **data)
    return result


def _induced_subgraph_with_neighbours(graph: nx.DiGraph, seed_paths: set[str]) -> nx.DiGraph:
    """Induced subgraph on `seed_paths` plus their immediate dependency
    neighbours (both directions), so the derived graph captures not just
    the seed documents but what they connect to. See
    `_deterministic_induced_subgraph` for why this does not use
    `nx.DiGraph.subgraph()` directly."""
    nodes = set(seed_paths)
    for p in sorted(seed_paths):
        if p in graph:
            nodes.update(graph.predecessors(p))
            nodes.update(graph.successors(p))
    return _deterministic_induced_subgraph(graph, nodes)


def build_service_graph(graph: nx.DiGraph, root_tiers: dict[str, str]) -> nx.DiGraph:
    service_paths = {p for p, tier in root_tiers.items() if tier in SERVICE_TIERS}
    return _deterministic_induced_subgraph(graph, service_paths & set(graph.nodes()))


def build_runtime_graph(graph: nx.DiGraph, root_tiers: dict[str, str]) -> nx.DiGraph:
    runtime_paths = {p for p, tier in root_tiers.items() if tier in RUNTIME_TIERS}
    return _deterministic_induced_subgraph(graph, runtime_paths & set(graph.nodes()))


def build_plugin_graph(graph: nx.DiGraph, docs: list[DocumentMetadata]) -> nx.DiGraph:
    plugin_paths = {
        d.path for d in docs
        if "plugin" in d.path.lower() or "plugin" in (d.purpose or "").lower()
    }
    return _induced_subgraph_with_neighbours(graph, plugin_paths)


def build_algorithm_graph(graph: nx.DiGraph, docs: list[DocumentMetadata]) -> nx.DiGraph:
    algorithm_paths = {d.path for d in docs if _claims_algorithm_content(d)}
    return _induced_subgraph_with_neighbours(graph, algorithm_paths)
