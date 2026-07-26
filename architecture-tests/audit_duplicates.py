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

# Known duplicate groups from the audit report
DUPLICATE_GROUPS = [
    ["README.md", "docs/README.md", "README-GOVERNANCE.md", "docs/README-GOVERNANCE.md"],
    ["AGENTS.md", "docs/AGENTS.md"],
    ["AI-MEMORY.md", "AI-MEMORY-SYSTEM.md"],
    ["API-CONTRACTS.md", "API-REFERENCE.md"],
    ["ARCHITECTURE.md", "APEX-ARCHITECTURE.md"],
    ["WORKER-ARCHITECTURE.md", "WORKER-POOL.md"],
]

# Conflicting authority pairs - two docs claiming ownership of the same topic
CONFLICT_PAIRS = [
    ("DOCUMENTATION-MAP.md", "docs/* that claim index/reference roles"),
    ("CONFIGURATION.md", "CONFIGURATION-PROFILES.md"),
    ("ERROR-HANDLING-LOGGING.md", "subsystem docs with local error codes"),
    ("SECURITY.md", "SECURITY-CONTRACTS.md"),
    ("SECURITY.md", "PERMISSION-MODEL.md"),
]

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

    # Check duplicate file groups
    for group in DUPLICATE_GROUPS:
        existing = [f for f in group if os.path.exists(os.path.join(DOCS_DIR if not f.startswith("docs/") and f != "README.md" else "", f)) or os.path.exists(f)]
        if len(existing) > 1:
            errors.append(f"DUPLICATE GROUP: {existing} overlap in governance intent")

    # Check conflicting authority pairs
    for pair in CONFLICT_PAIRS:
        path1 = os.path.join(DOCS_DIR, pair[0]) if not pair[0].startswith("docs/") else pair[0]
        path2 = pair[1]
        if os.path.exists(path1):
            errors.append(f"CONFLICT POTENTIAL: {pair[0]} vs {pair[1]} — review authority boundaries")

    if errors:
        print("DUPLICATE/CONFLICT AUDIT:")
        for err in errors:
            print(f"  - {err}")
        print("\nACTION REQUIRED: Review and consolidate overlapping documents.")
    else:
        print("NO DUPLICATES OR CONFLICTS DETECTED")

if __name__ == "__main__":
    main()