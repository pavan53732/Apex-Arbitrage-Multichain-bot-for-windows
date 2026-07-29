#!/usr/bin/env python3
"""
validate_cross_references.py

Validates all markdown cross-references across the docs directory.
Checks that every `[text](path/to/file.md)` reference points to an existing file.
"""

import os
import re
import sys

DOCS_DIR = "docs"

errors = []
warnings = []

def extract_refs(filepath):
    """Extract all markdown link references from a file."""
    refs = []
    with open(filepath) as f:
        content = f.read()

    # Match [text](path)
    for match in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', content):
        text = match.group(1)
        link = match.group(2)
        refs.append((text, link))

    # Match bare file.md references
    for match in re.finditer(r'`([A-Z][A-Z0-9_.-]+\.md)`', content):
        refs.append((match.group(1), match.group(1)))

    return refs

def resolve_ref(base_dir, link):
    """Resolve a relative markdown link to an absolute path."""
    if link.startswith("http://") or link.startswith("https://") or link.startswith("#"):
        return None  # External or anchor link
    if link.startswith("/"):
        return os.path.join(DOCS_DIR, link.lstrip("/"))
    return os.path.join(base_dir, link)

def main():
    if not os.path.exists(DOCS_DIR):
        print(f"FAIL: {DOCS_DIR} directory not found")
        sys.exit(1)

    # sorted(): os.listdir() order is filesystem-dependent, not guaranteed
    # deterministic across platforms/processes.
    doc_files = sorted(f for f in os.listdir(DOCS_DIR) if f.endswith(".md"))
    
    for doc_file in doc_files:
        doc_path = os.path.join(DOCS_DIR, doc_file)
        refs = extract_refs(doc_path)
        
        for text, link in refs:
            resolved = resolve_ref(os.path.dirname(doc_path), link)
            if resolved is None:
                continue
            if not os.path.exists(resolved):
                # Check if it exists without the DOCS_DIR prefix
                alt_path = resolved.replace("docs/docs/", "docs/")
                if not os.path.exists(alt_path):
                    errors.append(f"{doc_file}: broken ref '{link}' -> {resolved} (text: '{text}')")
                else:
                    warnings.append(f"{doc_file}: ref '{link}' resolves via alt path")

    if errors:
        print("=== CROSS-REFERENCE VALIDATION FAILED ===")
        for err in errors[:20]:
            print(f"  {err}")
        if len(errors) > 20:
            print(f"  ... and {len(errors) - 20} more errors")
        print(f"\nTotal broken references: {len(errors)}")
        sys.exit(1)
    else:
        print("=== CROSS-REFERENCE VALIDATION PASSED ===")
        print(f"All {len(doc_files)} docs checked, 0 broken references")
        if warnings:
            print(f"Warnings: {len(warnings)}")
            for w in warnings[:5]:
                print(f"  {w}")
        sys.exit(0)

if __name__ == "__main__":
    main()