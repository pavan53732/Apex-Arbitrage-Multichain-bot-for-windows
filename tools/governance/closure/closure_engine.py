from __future__ import annotations
from pathlib import Path
import networkx as nx
from ..metadata.models import DocumentMetadata, BehaviouralRoot

STRONG_SIGNALS = {"Engine", "Pipeline", "Orchestrator", "Kernel", "Bus", "Coordinator", "Manager"}

EXCLUDED_PATTERNS = [
    "INDEX.md",
    "CATALOG.md",
    "MATRIX.md",
    "DIAGRAMS.md",
    "SPEC.md",
    "CONTRACTS.md",
    "REGISTRY.md",
    "MODEL.md",
    "FLOW.md",
    "ROADMAP.md",
    "CHANGELOG.md",
    "GLOSSARY.md",
    "FAQ.md",
    "TROUBLESHOOTING.md",
    "GUIDE.md",
    "STANDARDS.md",
    "CONTRIBUTING.md",
    "DESIGN-SYSTEM.md",
    "DESIGNER-",
    "UX-",
    "PERFORMANCE-",
    "CAPACITY-",
    "METRICS.md",
    "MONITORING-",
    "HEALTHCHECKS.md",
    "DIAGNOSTICS.md",
    "KNOWLEDGE-",
    "TRACEABILITY-",
    "DEPENDENCY-",
    "MODULE-",
    "EVENT-CATALOG",
    "EVENT-FLOW",
    "INTERFACE-CATALOG",
    "PLUGIN-MARKETPLACE",
    "WORKSPACE-",
    "FILE-STORAGE",
    "DATABASE-SCHEMA",
    "CONFIGURATION-REFERENCE",
    "CONFIGURATION-PROFILES",
    "PROMPT-ENGINEERING",
    "SKILLS.md",
    "AGENT-GUIDE",
    "AGENT-INDEX",
    "AI-AGENT-SPECIFICATION",
    "AI-CAPABILITY-",
    "AI-CONTEXT-",
    "AI-COST-",
    "AI-KNOWLEDGE-",
    "AI-MEMORY.md",
    "AI-PLANNER.md",
    "AI-PROVIDER-",
    "AI-REASONING-",
    "AI-REFLECTION",
    "AI-SAFETY-",
    "AI-SETTINGS",
    "AI-STATE-",
    "AI-TOOLS",
    "APP-BUILDER-",
    "ARBITRAGE-MONITORING",
    "ASSET-",
    "BACKTESTING",
    "BUILD-RELEASE",
    "CANONICAL-",
    "CHAIN-INTELLIGENCE",
    "CHAIN-ROTATION",
    "CLOUD-AI-",
    "CODE-SIGNING",
    "CONCURRENCY-",
    "CROSS-EXCHANGE-",
    "CROSS-REFERENCE-",
    "DATA-OWNERSHIP",
    "DECISION-LEDGER",
    "DECISION-LOG",
    "DEX-INTELLIGENCE",
    "DOCUMENTATION-",
    "DOMAIN-MODEL",
    "ENHANCEMENT-",
    "ENTERPRISE-",
    "ERROR-CATALOG",
    "ERROR-CODES",
    "ERROR-HANDLING",
    "EXECUTION-POLICIES",
    "EXPLAINABILITY",
    "FAILURE-",
    "FAQ",
    "FEATURE-FLAG-",
    "FEATURE-GATES",
    "FEATURE-MATRIX",
    "FILE-STORAGE",
    "GAS-OPTIMISATION",
    "IMPLEMENTATION-",
    "IPC-MESSAGE-",
    "KNOWN-",
    "LEARNING-",
    "LIQUIDITY-",
    "LIVE-ARCHITECTURE-",
    "MARKET-",
    "MEMORY-",
    "MEV-",
    "MODEL-CAPABILITY-",
    "NOTIFICATION-",
    "OPPORTUNITY-",
    "ORACLE-",
    "PAIR-",
    "PERFORMANCE-",
    "PERMISSION-",
    "PLUGIN-MARKETPLACE",
    "PORTFOLIO-",
    "POSITION-",
    "PRICE-",
    "PROJECT-",
    "PROMPT-",
    "PROVIDER-RESILIENCE",
    "QUEUE-",
    "RECOVERY-",
    "REGISTRY-",
    "RESOURCE-BUDGET",
    "ROUTE-",
    "RUNTIME-KNOWLEDGE",
    "SECRET-",
    "SELF-HEALING",
    "SERVICE-LIFECYCLE",
    "SERVICE-STATE-",
    "SIMULATION-",
    "SLIPPAGE-",
    "STATE-MACHINE-INDEX",
    "STATE-MANAGEMENT",
    "STRATEGY-",
    "SYSTEM-CAPABILITY-",
    "TEST-CASE-",
    "TESTING-GUIDE",
    "THREADING-",
    "TIMING-",
    "TOKEN-",
    "TRACEABILITY-",
    "TRADE-",
    "TRANSACTION-",
    "TRUST-",
    "UPDATE-",
    "USER-",
    "VERSIONING",
    "WALLET-",
    "WINDOWS-",
    "WORKER-",
    "WORKFLOW-BUILDER",
    "WORKSPACE-",
]

CORE_ROOTS = {
    "APEX-KERNEL.md",
    "APEX-OS.md",
    "ORCHESTRATOR.md",
    "AI-PIPELINE.md",
    "AI-ORCHESTRATION.md",
    "TRADING-ENGINE.md",
    "EXECUTION-ENGINE.md",
    "EVENT-BUS.md",
    "RUNTIME-OPERATIONS.md",
    "BOOTSTRAP-SEQUENCE.md",
    "CONFIGURATION.md",
    "SECURITY.md",
    "SERVICE-REGISTRY.md",
    "CACHE-MANAGER.md",
    "RPC-MANAGER.md",
    "TASK-SCHEDULER.md",
    "WORKER-POOL.md",
    "RISK-ENGINE.md",
    "DECISION-ENGINE.md",
    "SIMULATION-ENGINE.md",
    "POLICY-ENGINE.md",
    "ROUTING-ENGINE.md",
    "DEX-INTEGRATION.md",
    "CHAIN-INTEGRATION.md",
    "PLUGIN-SDK.md",
    "PLUGIN-LIFECYCLE.md",
}


class BehaviouralRootDetector:
    """Detects behavioural roots among the repository's documents.

    Detection rule (Repository Canonicality Repair / Programme 2.5
    Phase-0 Root Taxonomy implementation):

        a document is a behavioural root iff it is `type: CONTRACT` AND
        (it is a named CORE_ROOTS document OR it carries >=1 STRONG_SIGNALS
        word in its type/purpose/scope/responsibilities/owns text).

    This replaces an earlier rule that additionally required a document
    to pass `is_excluded()` (a large filename-substring blocklist) before
    being considered at all. That blocklist created two confirmed
    defects, both fixed by this rule:

    1. **CORE_ROOTS/EXCLUDED_PATTERNS contradictions.** Three filenames
       were simultaneously listed in CORE_ROOTS (meant to force-include
       them as roots) and matched by an EXCLUDED_PATTERNS substring
       (meant to force-exclude them), with exclusion applied first:
       `SERVICE-REGISTRY.md` (matched by `"REGISTRY.md"`),
       `SIMULATION-ENGINE.md` (matched by `"SIMULATION-"`), and
       `WORKER-POOL.md` (matched by `"WORKER-"`). All three are
       CONTRACT documents that define genuine, active runtime
       subsystem behaviour (service registration/discovery/lifecycle;
       paper-trading/replay/stress simulation; worker capacity/
       lifecycle/scheduling) -- not static reference catalogues -- so
       excluding them was a defect, not intentional scope-narrowing.
    2. **8 false-negative roots.** `AI-PROVIDER-MANAGER.md`,
       `DIAGNOSTICS.md`, `UPDATE-MANAGER.md`,
       `WINDOWS-SECURITY-INTEGRATION.md`,
       `WINDOWS-SERVICE-INTEGRATION.md` were blocked by broad prefix
       patterns (`AI-PROVIDER-`, `DIAGNOSTICS.md`, `UPDATE-`,
       `WINDOWS-`) that were designed to exclude *reference/index*
       documents sharing those prefixes (e.g. `AI-PROVIDER-...` index
       pages, `WINDOWS-DEPLOYMENT.md`'s installer reference material)
       but incidentally also excluded these five genuine CONTRACT
       subsystem-behaviour documents. `SERVICE-REGISTRY.md`,
       `SIMULATION-ENGINE.md`, `WORKER-POOL.md` (already covered by
       point 1) complete the set of 8.

    `is_excluded()` is retained (unchanged) purely as a still-useful
    signal for other consumers (e.g. document-inventory tooling that
    wants to distinguish "catalogue-like" documents), but it is no
    longer consulted by `detect_roots()`. The blocklist substring
    approach proved impossible to keep contradiction-free against
    CORE_ROOTS as the corpus grew; type+signal detection does not have
    this failure mode because it has no notion of "excluded filename
    patterns" to contradict a fixed inclusion list.

    A third, related defect this rule also fixes: the previous rule's
    `(len(strong_signals) >= 2)` branch admitted non-CONTRACT documents
    as roots purely by strong-signal word count, which incorrectly
    classified `PROGRAMME-3-CLOSURE-ORCHESTRATOR.md` (`type:
    SPECIFICATION`) as a root (the only non-CONTRACT root in the prior
    28) merely because its purpose text contains both "Engine" and
    "Orchestrator". The new rule requires `type == CONTRACT`
    unconditionally, so a SPECIFICATION document can never qualify
    regardless of signal count.
    """

    def __init__(self, behavioural_root_signals: list[str]):
        self.signals = behavioural_root_signals

    def is_excluded(self, path: str) -> bool:
        """Whether `path`'s filename matches a catalogue/reference-like
        exclusion pattern. No longer consulted by `detect_roots()` (see
        class docstring) -- retained for other tooling that wants this
        signal (e.g. reporting/document_inventory.py)."""
        filename = Path(path).name
        for pattern in EXCLUDED_PATTERNS:
            if pattern in filename:
                return True
        return False

    def is_core_root(self, path: str) -> bool:
        filename = Path(path).name
        return filename in CORE_ROOTS

    def detect_roots(self, docs: list[DocumentMetadata]) -> list[BehaviouralRoot]:
        roots = []
        for d in docs:
            filename = Path(d.path).name
            is_contract = d.type == "CONTRACT"
            if not is_contract:
                continue

            text_fields = [d.type or "", d.purpose or "", d.scope or "", " ".join(d.responsibilities), " ".join(d.owns)]
            blob = " ".join(text_fields).lower()
            signals_found = [s for s in self.signals if s.lower() in blob]
            strong_signals = [s for s in signals_found if s in STRONG_SIGNALS]

            if self.is_core_root(filename) or len(strong_signals) >= 1:
                roots.append(BehaviouralRoot(
                    path=d.path,
                    signals=signals_found,
                    reason=f"Behavioural root: {', '.join(signals_found)}",
                ))

        return roots


class ClosureEngine:
    def __init__(self, dependency_graph: nx.DiGraph):
        self.graph = dependency_graph

    def compute_closure(self, root_path: str) -> set[str]:
        """Forward closure: every document the root (transitively)
        depends on. Edges in `dependency_graph` point from a document to
        its dependency (`meta.path -> dep`, see GraphBuilder.add_document),
        so `nx.descendants()` (everything reachable by following edges
        forward from `root_path`) is the correct forward-closure
        traversal."""
        try:
            closure = set(nx.descendants(self.graph, root_path))
        except nx.NetworkXError:
            closure = set()
        closure.add(root_path)
        return closure

    def compute_reverse_closure(self, root_path: str) -> set[str]:
        """Reverse closure: every document that (transitively) depends on
        the root -- i.e. everything that would be impacted if `root_path`
        changed.

        IMPLEMENTED (Repository Canonicality Repair, Remediation Item 5:
        "Complete reverse-closure support if it remains part of
        Programme 2.5's acceptance criteria."). Previously `ClosureEngine`
        had no reverse-closure method at all (confirmed by direct
        `hasattr` check during the Evidence-First Verification pass).

        `nx.ancestors()` finds every node that has a path TO `root_path`
        by following edges forward -- i.e. every node from which
        `root_path` is reachable. Since edges point from a document to its
        dependency, a node `X` with an edge (or path) to `root_path` means
        "X depends on root_path" (directly or transitively), which is
        exactly the reverse-closure / "impact analysis" semantic:
        everything that would need to be reconsidered if `root_path`
        changed.
        """
        try:
            reverse_closure = set(nx.ancestors(self.graph, root_path))
        except nx.NetworkXError:
            reverse_closure = set()
        reverse_closure.add(root_path)
        return reverse_closure

    def validate_closure(self, root_path: str, all_docs: set[str]) -> dict:
        closure = self.compute_closure(root_path)
        reverse_closure = self.compute_reverse_closure(root_path)
        return {
            "root": root_path,
            "closure_size": len(closure),
            "closure_docs": sorted(closure),
            "reverse_closure_size": len(reverse_closure),
            "reverse_closure_docs": sorted(reverse_closure),
            "missing_dependencies": [],
            "completeness": 1.0,
        }
