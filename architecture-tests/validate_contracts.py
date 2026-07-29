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
    # A contract body may be expressed as a numbered section ("## 1. ..."),
    # or as a heading that contains one of the canonical contract-body
    # keywords anywhere in its text (e.g. "## Operational Contract",
    # "## Interface Contract", "## Cache contract", "## Window contract",
    # "## Mandated Controls", "## Governance Rules", "## Enterprise
    # Contract - Simulation Engine"). The previous pattern only matched
    # headings that literally *started* with "Contract"/"Terms"/etc,
    # which produced false FAILs on 19 real [CONTRACT] documents whose
    # body section is legitimately named e.g. "## Operational Contract".
    ("Terms / Contract body", r"(^## \d+\.|^##.*\b(Terms|Contract|Clauses|Mandate[ds]?)\b)"),
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
        if re.search(pattern, content, re.IGNORECASE | re.MULTILINE):
            found.append(label)
        else:
            missing.append(label)

    return found, missing


def get_front_matter_type(content):
    """Extract the `type:` field from YAML front matter, if present.

    Returns the front-matter type value (e.g. "CONTRACT", "REFERENCE"),
    or None if there is no front matter / no type field.
    """
    fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not fm_match:
        return None
    type_match = re.search(r"^type:\s*(\S+)", fm_match.group(1), re.MULTILINE)
    return type_match.group(1) if type_match else None


def is_self_declared_contract(content):
    """Determine whether a document declares itself as [CONTRACT] type.

    A document is only a self-declared CONTRACT when either:
      1. Its YAML front-matter `type:` field is exactly `CONTRACT`, or
      2. It contains an explicit "Document type: [CONTRACT]" declaration
         (the canonical inline declaration used by non-front-matter docs).

    Merely mentioning the string "[CONTRACT]" in prose (e.g. a document
    that discusses "the 51 [CONTRACT] documents") must NOT be treated as
    a self-declaration. The previous substring-only check produced a false
    positive on FINAL-READINESS-AUDIT.md, which is `type: REFERENCE` but
    references other contracts by name in its executive summary.
    """
    if get_front_matter_type(content) == "CONTRACT":
        return True
    if re.search(r"Document type:\s*\[CONTRACT\]", content, re.IGNORECASE):
        return True
    return False


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
            content = fh.read()
        if is_self_declared_contract(content):
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