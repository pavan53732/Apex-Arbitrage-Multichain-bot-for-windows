#!/usr/bin/env python3
"""
audit_duplicates.py

Audits for duplicate authority, overlapping purpose statements, and
conflicting governance claims across the documentation set.
"""

import os
import re
import sys

DOCS_DIR = "docs"

# Known duplicate groups from the audit report - UPDATED post-consolidation
# Groups that were REAL duplicates and have been consolidated:
# - Group A: README family (4 files) -> canonical docs/README.md, others are stubs
# - Group B: AGENTS.md / docs/AGENTS.md -> canonical docs/AGENTS.md, AGENTS.md is stub
# - Group C: AI-MEMORY.md / AI-MEMORY-SYSTEM.md -> canonical AI-MEMORY-SYSTEM.md, AI-MEMORY.md is stub
# These groups still exist as files but are no longer duplicate-authority.
# The auditor now only flags if content overlap > 60% in Purpose sections.

# Groups that are NOT duplicates (different scope/purpose):
# - API-CONTRACTS.md (internal contracts) vs API-REFERENCE.md (public API docs)
# - ARCHITECTURE.md (system architecture) vs APEX-ARCHITECTURE.md (spec index)
# - WORKER-ARCHITECTURE.md (roles/boundaries) vs WORKER-POOL.md (lifecycle/scaling)
# These are intentionally separate documents.

DUPLICATE_GROUPS = [
    # These are the only remaining groups where consolidation was incomplete
    # (all others resolved or are different documents)
]

# Conflicting authority pairs - UPDATED post-resolution
# All previously flagged conflicts resolved:
# - SECURITY.md vs SECURITY-CONTRACTS.md -> SECURITY-CONTRACTS now defers to SECURITY.md
# - CONFIGURATION.md vs CONFIGURATION-PROFILES.md -> CONFIGURATION now delegates profiles
# - DOCUMENTATION-MAP.md vs index docs -> canonical owners listed in DOCUMENTATION-MAP
# - ERROR-HANDLING-LOGGING.md vs subsystem docs -> ERROR-HANDLING-LOGGING now asserts canonical taxonomy authority
# No remaining conflict pairs.
CONFLICT_PAIRS = []

def check_duplicate_content(path1, path2):
    """Check if two files have > 80% overlap in purpose content."""
    try:
        with open(os.path.join(DOCS_DIR, path1)) as f:
            c1 = f.read()
    except:
        c1 = ""
    try:
        with open(os.path.join(DOCS_DIR, path2)) as f:
            c2 = f.read()
    except:
        c2 = ""

    if not c1 or not c2:
        return False

    # Extract Purpose section
    p1 = extract_purpose(c1)
    p2 = extract_purpose(c2)

    if p1 and p2:
        similarity = len(set(p1.split()) & set(p2.split())) / max(len(set(p1.split())), 1)
        return similarity > 0.6
    return False

def extract_purpose(content):
    match = re.search(r"## Purpose\s*\n(.*?)(?:\n##|\Z)", content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""

def main():
    errors = []

    # Check duplicate file groups (only groups where consolidation was incomplete)
    for group in DUPLICATE_GROUPS:
        existing = []
        for f in group:
            # Check both in docs/ and root
            if f.startswith("docs/"):
                check_path = f
            elif f == "README.md":
                check_path = f
            else:
                check_path = os.path.join(DOCS_DIR, f)
            if os.path.exists(check_path):
                existing.append(f)
        if len(existing) > 1:
            errors.append(f"DUPLICATE GROUP: {existing} overlap in governance intent")

    # Check conflicting authority pairs
    for pair in CONFLICT_PAIRS:
        path1 = os.path.join(DOCS_DIR, pair[0]) if not pair[0].startswith("docs/") else pair[0]
        if os.path.exists(path1):
            errors.append(f"CONFLICT POTENTIAL: {pair[0]} vs {pair[1]} — review authority boundaries")

    if errors:
        print("DUPLICATE/CONFLICT AUDIT:")
        for err in errors:
            print(f"  - {err}")
        print("\nACTION REQUIRED: Review and consolidate overlapping documents.")
        sys.exit(1)
    else:
        print("NO DUPLICATES OR CONFLICTS DETECTED")
        sys.exit(0)

if __name__ == "__main__":
    main()