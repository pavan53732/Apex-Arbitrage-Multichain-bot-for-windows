"""Regression tests for the _check_cycles() performance fix.

Discovered while verifying Remediation Item 1: once phantom graph nodes
were eliminated, a genuine 165-node strongly-connected component in the
real documentation corpus reconnected, and the previous
`nx.simple_cycles()`-based implementation hung indefinitely (did not
return within 25 seconds) because simple-cycle enumeration is
combinatorially expensive at that graph scale. The fix uses
`nx.strongly_connected_components()` (Tarjan's algorithm, O(V+E)) to
detect cycle EXISTENCE without enumerating every individual cycle.
"""
import time
import networkx as nx

from governance.validator.governance_validator import GovernanceValidator
from governance.metadata.models import DocumentMetadata


def test_check_cycles_detects_a_simple_cycle():
    """Severity is INFO, not CRITICAL -- verified empirically (not
    assumed) against the real corpus: this repository has zero documents
    with an explicit '## Depends On' section, so every cycle in the
    'dependency' graph is, in its current form, indistinguishable from
    documentation mutual cross-referencing (benign, expected practice),
    not a verified structural/build-order dependency defect. See the
    detailed rationale in GovernanceValidator._check_cycles()'s
    docstring."""
    docs = [
        DocumentMetadata(path="docs/A.md", owner="Team A"),
        DocumentMetadata(path="docs/B.md", owner="Team B"),
    ]
    g = nx.DiGraph()
    g.add_edge("docs/A.md", "docs/B.md")
    g.add_edge("docs/B.md", "docs/A.md")
    v = GovernanceValidator(docs, g)
    findings = v.validate_all()
    cycle_findings = [f for f in findings if f.rule == "NO_CYCLES"]
    assert len(cycle_findings) == 1
    assert cycle_findings[0].severity.value == "INFO"
    # INFO severity must not cause validate_all()'s findings to trip the
    # failure threshold (docs have distinct owners and no broken
    # references, so the only finding present is the INFO-level cycle).
    assert not GovernanceValidator.has_failing_findings(findings)


def test_check_cycles_reports_nothing_for_an_acyclic_graph():
    docs = [DocumentMetadata(path="docs/A.md"), DocumentMetadata(path="docs/B.md")]
    g = nx.DiGraph()
    g.add_edge("docs/A.md", "docs/B.md")
    v = GovernanceValidator(docs, g)
    findings = v.validate_all()
    cycle_findings = [f for f in findings if f.rule == "NO_CYCLES"]
    assert cycle_findings == []


def test_check_cycles_completes_quickly_on_a_large_densely_connected_graph():
    """Reproduces the exact failure mode found in this repository's real
    dependency graph: a single large strongly-connected component with
    many edges. Must complete in well under the 25-second timeout that
    the old nx.simple_cycles()-based implementation could not clear."""
    docs = [DocumentMetadata(path=f"docs/D{i}.md") for i in range(200)]
    g = nx.DiGraph()
    paths = [d.path for d in docs]
    # Build a densely-connected strongly-connected component: a ring plus
    # extra cross edges, similar in density to the real corpus's ~165-node
    # SCC with ~800+ edges.
    for i in range(len(paths)):
        g.add_edge(paths[i], paths[(i + 1) % len(paths)])
    import random
    random.seed(42)
    for _ in range(600):
        a, b = random.sample(paths, 2)
        g.add_edge(a, b)

    v = GovernanceValidator(docs, g)
    start = time.monotonic()
    findings = v.validate_all()
    duration = time.monotonic() - start
    assert duration < 5.0, f"_check_cycles took {duration:.2f}s, expected well under 5s"
    cycle_findings = [f for f in findings if f.rule == "NO_CYCLES"]
    assert len(cycle_findings) >= 1
