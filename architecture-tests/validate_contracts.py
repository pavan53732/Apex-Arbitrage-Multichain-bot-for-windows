#!/usr/bin/env python3
"""
validate_contracts.py

Validates that all documents declaring themselves as [CONTRACT] type
include the mandatory sections required by the governance rules.

Required sections per contract:
  1. Document type declaration: `Document type: [CONTRACT]` (or `[CONTRACT]` variant)
  2. Version block (with version number, status, date, owner)
  3. Purpose section
  4. Owner / Ownership section (who owns this contract)
  5. Terms / Contract body (the actual clauses)
  6. Cross-references section
  7. Version History section
"""

import os
import re
import sys

DOCS_DIR = "docs"

REQUIRED_SECTIONS = [
    ("Document type (CONTRACT)", r"\[CONTRACT\]"),
    ("Version metadata", r"## Version"),
    ("Purpose section", r"## Purpose"),
    ("Owner / Ownership", r"(Owner:|## Ownership)"),
    ("Terms / Contract body", r"(## Terms|## Contract|## Clauses|## Mandates|## \d+\.)"),
    ("Cross-references", r"## Cross-?references"),
    ("Version History", r"## Version History"),
]

def check_contract(filepath):
    """Check a single file for all required contract sections."""
    with open(filepath) as f:
        content = f.read()

    missing = []
    found = []

    for label, pattern in REQUIRED_SECTIONS:
        if re.search(pattern, content, re.IGNORECASE):
            found.append(label)
        else:
            missing.append(label)

    return found, missing

def main():
    if not os.path.exists(DOCS_DIR):
        print(f"FAIL: {DOCS_DIR} directory not found")
        sys.exit(1)

    contract_files = []
    doc_files = sorted(os.listdir(DOCS_DIR))

    for f in doc_files:
        if not f.endswith(".md"):
            continue
        filepath = os.path.join(DOCS_DIR, f)
        with open(filepath) as fh:
            first_30 = fh.read(3000)
        if re.search(r"\[CONTRACT\]", first_30):
            contract_files.append(filepath)

    if not contract_files:
        print("No [CONTRACT] documents found.")
        sys.exit(0)

    print(f"Found {len(contract_files)} [CONTRACT] document(s):\n")
    
    all_pass = True
    for filepath in contract_files:
        filename = os.path.basename(filepath)
        found, missing = check_contract(filepath)

        status = "PASS" if not missing else "FAIL"
        if missing:
            all_pass = False

        print(f"  [{status}] {filename}")
        print(f"         Found ({len(found)}/7): {', '.join(found)}")
        if missing:
            print(f"         MISSING ({len(missing)}/7): {', '.join(missing)}")
        print()

    if all_pass:
        print("All [CONTRACT] documents pass compliance validation.")
        sys.exit(0)
    else:
        print("Some [CONTRACT] documents have compliance gaps — see above.")
        sys.exit(1)

if __name__ == "__main__":
    main()