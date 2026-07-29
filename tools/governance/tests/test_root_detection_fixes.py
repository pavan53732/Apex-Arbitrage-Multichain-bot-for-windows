"""Regression tests for the Phase-0-as-written implementation programme,
WS1 (Root Detection Engine).

Covers three defects confirmed in the Programme 2.5 Final Certification
Audit (commit 3b1240164), all fixed in the same change to
`BehaviouralRootDetector.detect_roots()`:

1. CORE_ROOTS/EXCLUDED_PATTERNS contradictions (SERVICE-REGISTRY.md,
   SIMULATION-ENGINE.md, WORKER-POOL.md were force-included by CORE_ROOTS
   but force-excluded by a filename-substring blocklist, with exclusion
   applied first).
2. 8 false-negative behavioural roots (real CONTRACT subsystem documents
   that a broad prefix-based exclusion blocklist incorrectly filtered
   out before root-detection logic ever ran).
3. Anomalous non-CONTRACT root: PROGRAMME-3-CLOSURE-ORCHESTRATOR.md
   (type: SPECIFICATION) was previously classified as a root purely by
   strong-signal word count, bypassing the CONTRACT-type requirement.
"""
from governance.closure.closure_engine import BehaviouralRootDetector, CORE_ROOTS, EXCLUDED_PATTERNS
from governance.metadata.models import DocumentMetadata

SIGNALS = [
    "CONTRACT", "Engine", "Pipeline", "Runtime", "Kernel", "Orchestrator",
    "Workflow", "Bus", "Lifecycle", "Coordinator", "Manager", "Builder",
]


def test_core_roots_and_excluded_patterns_no_longer_contradict_in_detection():
    """The 3 filenames present in both CORE_ROOTS and matched by an
    EXCLUDED_PATTERNS substring must still be detected as roots when they
    are genuine CONTRACT subsystem documents -- detect_roots() must not
    silently drop them via is_excluded()."""
    contradictions = [
        cr for cr in CORE_ROOTS
        if any(pat in cr for pat in EXCLUDED_PATTERNS)
    ]
    assert set(contradictions) == {
        "SERVICE-REGISTRY.md", "SIMULATION-ENGINE.md", "WORKER-POOL.md",
    }, "If this set changes, CORE_ROOTS or EXCLUDED_PATTERNS content changed -- re-verify detect_roots() still catches every one."

    detector = BehaviouralRootDetector(SIGNALS)
    docs = [
        DocumentMetadata(path=f"docs/{fn}", type="CONTRACT", purpose="Defines runtime behaviour for this subsystem.")
        for fn in contradictions
    ]
    roots = detector.detect_roots(docs)
    root_paths = {r.path for r in roots}
    for fn in contradictions:
        assert f"docs/{fn}" in root_paths, f"{fn} must be detected as a root despite matching an EXCLUDED_PATTERNS substring"


def test_false_negative_roots_now_detected():
    """8 real CONTRACT subsystem documents previously excluded by
    filename-prefix blocklist entries must now be detected as roots."""
    false_negatives = [
        "AI-PROVIDER-MANAGER.md", "DIAGNOSTICS.md", "SERVICE-REGISTRY.md",
        "SIMULATION-ENGINE.md", "UPDATE-MANAGER.md",
        "WINDOWS-SECURITY-INTEGRATION.md", "WINDOWS-SERVICE-INTEGRATION.md",
        "WORKER-POOL.md",
    ]
    detector = BehaviouralRootDetector(SIGNALS)
    docs = [
        DocumentMetadata(path=f"docs/{fn}", type="CONTRACT", purpose="Defines the runtime manager and lifecycle for this subsystem.")
        for fn in false_negatives
    ]
    roots = detector.detect_roots(docs)
    root_paths = {r.path for r in roots}
    for fn in false_negatives:
        assert f"docs/{fn}" in root_paths, f"{fn} must now be detected as a root"


def test_non_contract_document_never_a_root_regardless_of_signal_count():
    """A SPECIFICATION-typed document with >=2 strong signal words must
    NOT be classified as a behavioural root -- CONTRACT type is a hard
    requirement, not a signal-count-overridable one. Regression test for
    PROGRAMME-3-CLOSURE-ORCHESTRATOR.md's prior misclassification."""
    detector = BehaviouralRootDetector(SIGNALS)
    doc = DocumentMetadata(
        path="docs/PROGRAMME-3-CLOSURE-ORCHESTRATOR.md",
        type="SPECIFICATION",
        purpose="Defines the Closure Orchestrator engine for Programme 3.",
    )
    roots = detector.detect_roots([doc])
    assert roots == [], "A non-CONTRACT document must never be classified as a behavioural root, regardless of strong-signal count"


def test_contract_document_with_zero_signals_and_not_core_is_not_a_root():
    """Sanity check: CONTRACT type alone is not sufficient -- a CONTRACT
    document with no strong signals and not in CORE_ROOTS must not be a
    root (guards against an overly permissive fix)."""
    detector = BehaviouralRootDetector(SIGNALS)
    doc = DocumentMetadata(
        path="docs/SOME-UNRELATED-CONTRACT.md",
        type="CONTRACT",
        purpose="Defines an unrelated reference contract with no runtime behaviour words at all.",
    )
    roots = detector.detect_roots([doc])
    assert roots == []
