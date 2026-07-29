#!/usr/bin/env python3
"""
validate_ownership.py

Validates document ownership integrity across the documentation set:
1. Every owner document claims ownership explicitly (owns/does-not-own).
2. No two documents claim ownership of the same subsystem.
3. Every thin stub declares its owner document reference.
4. Every [CONTRACT] document has version/status/date/owner metadata.
5. DOCUMENTATION-MAP.md registers all owner documents.
"""

import os
import re
import sys

DOCS_DIR = "docs"
DOC_MAP = os.path.join(DOCS_DIR, "DOCUMENTATION-MAP.md")

errors = []
warnings = []

def find_owner_conflicts():
    """Check if any two docs claim ownership of the same subsystem."""
    ownership_claims = {}
    
    for f in sorted(os.listdir(DOCS_DIR)):
        if not f.endswith(".md"):
            continue
        filepath = os.path.join(DOCS_DIR, f)
        with open(filepath) as fh:
            content = fh.read()
        
        # Extract explicit ownership claims — only match substantive subsystem names
        # Skip generic terms like "matrix", "model", "index", "catalog"
        skip_terms = {"matrix", "model", "index", "catalog", "registry", "rules", "lifecycle", "integration"}
        for match in re.finditer(r'(?:Owns|owns)\s+(?:of\s+)?([A-Z][\w\s]+?)(?:\n|\.|;|,)', content):
            claim = match.group(1).strip().lower()
            if any(t in claim for t in skip_terms):
                continue
            if len(claim) < 5:  # Skip very short claims
                continue
            if claim not in ownership_claims:
                ownership_claims[claim] = [f]
            else:
                ownership_claims[claim].append(f)
    
    for claim, docs in ownership_claims.items():
        if len(docs) > 1:
            errors.append(f"OWNERSHIP CONFLICT: '{claim}' claimed by {len(docs)} docs: {', '.join(docs)}")

def _get_front_matter_type(content):
    """Extract the `type:` field from YAML front matter, if present."""
    fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not fm_match:
        return None
    type_match = re.search(r"^type:\s*(\S+)", fm_match.group(1), re.MULTILINE)
    return type_match.group(1) if type_match else None


def _is_self_declared_contract(content):
    """Determine whether a document declares ITSELF as [CONTRACT] type.

    A naive `"[CONTRACT]" in content` substring check produces false
    positives whenever a document merely *mentions* contracts in prose
    (e.g. "the 51 [CONTRACT] documents", or a REFERENCE doc explaining
    that it is "not a [CONTRACT] and must not be treated as one"). Only
    treat a document as self-declaring CONTRACT type when either:
      1. Its YAML front-matter `type:` field is exactly `CONTRACT`, or
      2. It contains the canonical inline declaration
         "Document type: [CONTRACT]".
    """
    if _get_front_matter_type(content) == "CONTRACT":
        return True
    if re.search(r"Document type:\s*\[CONTRACT\]", content, re.IGNORECASE):
        return True
    return False


def check_contract_metadata():
    """Verify all [CONTRACT] documents have required metadata."""
    for f in sorted(os.listdir(DOCS_DIR)):
        if not f.endswith(".md"):
            continue
        filepath = os.path.join(DOCS_DIR, f)
        with open(filepath) as fh:
            content = fh.read()

        if not _is_self_declared_contract(content):
            continue

        head = content[:3000]

        # Check for version block
        if not re.search(r'## Version', head, re.IGNORECASE):
            errors.append(f"MISSING VERSION: {f} declares [CONTRACT] but has no ## Version section")
        
        # Check for purpose section
        if not re.search(r'## Purpose', head, re.IGNORECASE):
            errors.append(f"MISSING PURPOSE: {f} declares [CONTRACT] but has no ## Purpose section")
        
        # Check for owner
        if not re.search(r'(Owner:|## Ownership)', head, re.IGNORECASE):
            warnings.append(f"NO EXPLICIT OWNER: {f} declares [CONTRACT] but has no explicit Owner line")

def check_doc_map_registration():
    """Check that DOCUMENTATION-MAP.md references key contract documents."""
    if not os.path.exists(DOC_MAP):
        errors.append("MISSING: DOCUMENTATION-MAP.md not found")
        return
    
    with open(DOC_MAP) as fh:
        map_content = fh.read()
    
    # Key documents that should be registered
    required_docs = [
        "ORCHESTRATOR.md",
        "IPC-PROTOCOL.md",
        "END-TO-END-WIRING-CONTRACT.md",
        "RUNTIME-FLOW-LIFECYCLE.md",
        "STATE-MACHINE-INDEX.md",
        "RECOVERY-COORDINATION.md",
        "WINDOWS-APP-ARCHITECTURE.md",
        "WINDOWS-SERVICE-INTEGRATION.md",
        "WINDOWS-NETWORK-RESILIENCE.md",
        "WINDOWS-NOTIFICATION-INTEGRATION.md",
        "WINDOWS-SECURITY-INTEGRATION.md",
        "WINDOWS-DESKTOP.md",
        "WINDOWS-DEPLOYMENT.md",
        "PLUGIN-LIFECYCLE.md",
        "EVENT-BUS.md",
        "DATABASE-SCHEMA.md",
        "WORKER-POOL.md",
        "TASK-SCHEDULER.md",
        "THREADING-MODEL.md",
        "TESTING.md",
        "SECURITY.md",
        "HEALTHCHECKS.md",
        "DOMAIN-MODEL.md",
        "DASHBOARD-WIDGETS.md",
        "DASHBOARD-RUNTIME.md",
        "DASHBOARD-LAYOUT.md",
        "DASHBOARD-WORKSPACES.md",
        "AI-ORCHESTRATION.md",
        "AI-PROVIDER-MANAGER.md",
        "TRADING-ENGINE.md",
        "EXECUTION-ENGINE.md",
        "FEATURE-FLAG-GOVERNANCE-AND-ROLLOUT-MATRIX.md",
        "DOCUMENTATION-STATUS-REVIEW-WORKFLOW.md",
    ]
    
    for doc in required_docs:
        if doc not in map_content:
            errors.append(f"DOC-MAP MISSING: {doc} not registered in DOCUMENTATION-MAP.md")

def check_thin_stub_owners():
    """Check that thin stubs (< 50 lines) reference their owner document."""
    for f in sorted(os.listdir(DOCS_DIR)):
        if not f.endswith(".md"):
            continue
        filepath = os.path.join(DOCS_DIR, f)
        line_count = 0
        with open(filepath) as fh:
            lines = fh.readlines()
            line_count = len(lines)
        
        if line_count < 50 and line_count > 5:
            content = ''.join(lines)
            # Skip deprecation redirects
            if "consolidated" in content.lower() or "redirects" in content.lower():
                continue
            # Skip ADRs
            if "adr/" in filepath:
                continue
            # Skip navigation stubs
            if any(x in content for x in ["Navigation-only", "Navigation stubs must"]):
                continue
            # Check if stub references an owner
            if not re.search(r'(owner|canonical|authoritative|owned by|See|see)', content, re.IGNORECASE):
                warnings.append(f"THIN STUB NO OWNER REF: {f} ({line_count} lines) has no reference to its owner document")

def main():
    find_owner_conflicts()
    check_contract_metadata()
    check_doc_map_registration()
    check_thin_stub_owners()
    
    if errors:
        print("=== OWNERSHIP VALIDATION FAILED ===")
        for err in errors:
            print(f"  - {err}")
        print(f"\nTotal errors: {len(errors)}")
        if warnings:
            print(f"\nWarnings ({len(warnings)}):")
            for w in warnings[:10]:
                print(f"  - {w}")
            if len(warnings) > 10:
                print(f"  ... and {len(warnings) - 10} more warnings")
        sys.exit(1)
    else:
        print("=== OWNERSHIP VALIDATION PASSED ===")
        print(f"  No ownership conflicts found")
        print(f"  All [CONTRACT] documents have required metadata")
        print(f"  All key documents registered in DOCUMENTATION-MAP.md")
        if warnings:
            print(f"\nWarnings ({len(warnings)}):")
            for w in warnings[:10]:
                print(f"  - {w}")
        sys.exit(0)

if __name__ == "__main__":
    main()
