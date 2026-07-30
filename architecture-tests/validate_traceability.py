#!/usr/bin/env python3
"""
validate_traceability.py

Validates traceability matrix integrity:
- All referenced documents exist (handling cross-directory refs)
- All referenced test case IDs exist in TEST-CASE-REGISTRY.md
- All referenced documents back-link to TRACEABILITY-MATRIX.md
"""

import os
import re
import sys

DOCS_DIR = "docs"
TRACEABILITY_FILE = os.path.join(DOCS_DIR, "TRACEABILITY-MATRIX.md")
TEST_CASE_REGISTRY = os.path.join(DOCS_DIR, "TEST-CASE-REGISTRY.md")

errors = []

# Known test case IDs extracted from TEST-CASE-REGISTRY.md
KNOWN_TEST_CASES = []

def load_test_case_registry():
    """Load all test case IDs from the test case registry."""
    global KNOWN_TEST_CASES
    if not os.path.exists(TEST_CASE_REGISTRY):
        errors.append("MISSING REGISTRY: TEST-CASE-REGISTRY.md not found")
        return
    
    with open(TEST_CASE_REGISTRY) as f:
        content = f.read()
    
    # Extract test IDs from table rows
    for match in re.finditer(r'\|\s*(test-[a-z0-9-]+)\s*\|', content):
        KNOWN_TEST_CASES.append(match.group(1))

def resolve_doc_path(doc_ref):
    """Resolve a document reference to an actual file path.
    Handles: 'DOC.md', 'docs/DOC.md', '../APEX-ARCHITECTURE.md', 'subdir/DOC.md'
    Also resolves by basename anywhere under DOCS_DIR (recursive), since
    traceability identifiers are independent of folder location.
    """
    doc_ref = doc_ref.strip().replace("`", "").replace("**", "")

    # Direct path under docs/
    path = os.path.join(DOCS_DIR, doc_ref)
    if os.path.exists(path):
        return path

    # Already has ../ prefix, resolve relative to DOCS_DIR
    if doc_ref.startswith("../"):
        root_path = doc_ref[3:]  # ../APEX-ARCHITECTURE.md → APEX-ARCHITECTURE.md
        if os.path.exists(root_path):
            return root_path

    # Recursive basename search under DOCS_DIR (handles moved/nested docs)
    basename = os.path.basename(doc_ref)
    for root, _dirs, files in os.walk(DOCS_DIR):
        if basename in files:
            return os.path.join(root, basename)

    return None

def check_doc_exists(doc_ref):
    if not doc_ref:
        return
    resolved = resolve_doc_path(doc_ref)
    if resolved is None:
        errors.append(f"MISSING DOC: '{doc_ref}' (referenced in traceability matrix)")

def check_back_link(doc_ref):
    if not doc_ref:
        return
    resolved = resolve_doc_path(doc_ref)
    if resolved is None:
        return
    with open(resolved) as f:
        content = f.read()
    if "TRACEABILITY-MATRIX.md" not in content and "traceability" not in content.lower():
        doc_name = os.path.basename(doc_ref)
        errors.append(f"MISSING BACK-LINK: '{doc_ref}' does not reference TRACEABILITY-MATRIX.md")

def check_test_case(test_id):
    if not test_id:
        return
    if KNOWN_TEST_CASES and test_id not in KNOWN_TEST_CASES:
        errors.append(f"UNKNOWN TEST CASE: '{test_id}' not found in TEST-CASE-REGISTRY.md")

def main():
    load_test_case_registry()
    
    if not os.path.exists(TRACEABILITY_FILE):
        print("FAIL: TRACEABILITY-MATRIX.md not found")
        sys.exit(1)

    with open(TRACEABILITY_FILE) as f:
        content = f.read()

    # Parse table rows
    for line in content.split("\n"):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")]
        if len(cells) < 7:
            continue
        req_id = cells[1]
        if not req_id.startswith("REQ-"):
            continue
        
        doc_col = cells[7] if len(cells) > 7 else ""
        test_col = cells[6] if len(cells) > 6 else ""
        
        # Check documents
        for doc_ref in doc_col.split(","):
            doc_ref = doc_ref.strip().replace("`", "").replace("**", "")
            check_doc_exists(doc_ref)
            check_back_link(doc_ref)
        
        # Check test case
        check_test_case(test_col.strip().replace("`", ""))

    if errors:
        print("TRACEABILITY VALIDATION FAILED:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print(f"TRACEABILITY VALIDATION PASSED — {len(KNOWN_TEST_CASES)} known test cases, all docs verified")
        sys.exit(0)

if __name__ == "__main__":
    main()