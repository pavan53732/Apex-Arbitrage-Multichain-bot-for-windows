# Architecture Tests

## Document type
Document type: [REFERENCE]

## Version
**Version:** 0.2.0 | **Status:** Draft | **Last Updated:** 2026-07-27 | **Owner:** Runtime Team

## Purpose
Architecture governance tests that validate documentation traceability, cross-reference integrity, contract compliance, and dependency enforcement.

---

## Current automated checks
- `scripts/validate_markdown_refs.sh` validates local markdown links.
- `.github/workflows/validate-doc-governance.yml` runs the validator on every push and pull request.

---

## 1. Traceability Validation

### 1.1 Requirement → Document Mapping
Each row in `TRACEABILITY-MATRIX.md` must have a corresponding document listed in the `Implementation Document` column. The `validate_traceability.py` script checks:

```python
# Pseudo-code
for row in traceability_matrix.rows:
    doc = row["Implementation Document"]
    if doc and not os.path.exists(f"docs/{doc}"):
        fail(f"Traceability matrix references missing document: {doc}")
    test_case = row["Test Case"]
    if test_case and test_case not in architecture_tests:
        fail(f"Traceability matrix references missing test case: {test_case}")
```

### 1.2 Document → Requirement Back-Link
Each document listed in the traceability matrix must contain a cross-reference back to the traceability matrix:

```
## Cross-References
- TRACEABILITY-MATRIX.md  ← Required back-link
```

### 1.3 Reference Integrity
The `validate_markdown_refs.sh` script verifies:
- All `[text](internal-link)` references point to existing files.
- No broken cross-references (404-style broken links).
- All `docs/*.md` files are reachable from `DOCUMENTATION-MAP.md`.

---

## 2. Contract Compliance Check

Every document with type `[CONTRACT]` must include:

```python
contract_fields = ["Purpose", "Scope (for contracts)", "Governance Rules", "Example"]
for doc in contract_docs:
    content = read_file(doc)
    for field in contract_fields:
        if field not in content:
            fail(f"Contract doc {doc} missing required section: {field}")
```

---

## 3. Dependency Graph Enforcement

The `dependency-cruiser` tool checks module-level rules:

| Rule | Description |
|------|-------------|
| No plugin → kernel dependency | Plugins must not import/require kernel modules directly |
| No dashboard → trading direct call | Dashboard must use IPC, not direct imports |
| No circular dependencies | No A → B → A dependency cycles |
| Registry isolation | Registry modules must not depend on trading logic |

---

## 4. Duplicate Detection

The `audit_duplicates.py` script checks:
- Files with same or similar names (e.g., `README.md` and `docs/README.md`)
- Overlapping document purpose statements (80%+ similarity)
- Conflicting governance claims (two docs claiming authority on same topic)

---

## 5. Test Runner

```bash
# Run all architecture tests
$ python3 architecture-tests/validate_traceability.py
$ python3 architecture-tests/audit_duplicates.py
$ scripts/validate_markdown_refs.sh
```

Expected exit code: 0 (all tests pass).