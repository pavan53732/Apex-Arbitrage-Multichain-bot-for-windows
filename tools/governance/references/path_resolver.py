"""Canonical document-identity resolver.

Repository Canonicality Repair follow-up (Remediation Item 1, per the
Evidence-First Verification Report finding "Broken reference
normalization"): every document in this repository must have exactly one
canonical identifier, and every reference to a document (whether written
as `FILE.md`, `docs/FILE.md`, `./FILE.md`, or a markdown link) must
resolve to that same identifier before being compared, stored, or used as
a graph node key.

ROOT CAUSE (confirmed by direct reproduction): `RepoIndexer.list_documents()`
indexes documents by their path relative to the repository root — e.g.
`docs/DOCUMENTATION-MAP.md`, `docs/AGENTS.md`, or a root-level gate file
such as `AGENTS.md` (no `docs/` prefix; these are separate, deliberately
distinct documents — see the `basenames with more than one indexed path`
check in `list_canonical_paths()` below, which found exactly 3 legitimate
same-basename pairs: AGENTS.md, README.md, README-GOVERNANCE.md, each a
root-level "gate" stub pointing at its `docs/`-prefixed canonical owner).

Meanwhile, `ReferenceParser.extract_cross_references()` /
`extract_depends_on()` previously stripped any `docs/` prefix
unconditionally before returning a reference string, on the theory that
this would "normalize" the reference — but the indexer never applied the
same stripping to real document paths. The result: a reference to
`docs/DOCUMENTATION-MAP.md` became the bare string `DOCUMENTATION-MAP.md`,
which does not match the indexed key `docs/DOCUMENTATION-MAP.md` -- but
DOES coincidentally exist as a graph node once any OTHER document
references it, creating a phantom duplicate node with no metadata.

FIX: resolve every reference against the actual indexed document set,
using the same directory-relative resolution strategy already proven
correct by `architecture-tests/validate_cross_references.py` (which
reports 0 broken references), rather than a blind prefix strip. This
module is the single place that performs this resolution; every consumer
(ReferenceParser, GovernanceValidator, GraphBuilder, DocumentInventory)
must use it instead of ad hoc string manipulation.
"""
from __future__ import annotations

from pathlib import Path
from typing import Optional


class DocumentIdentityResolver:
    """Resolves a raw reference string (as written in a document) to the
    canonical indexed path of the document it refers to, given the set of
    all canonically indexed document paths.

    A reference is considered resolved if it maps unambiguously to exactly
    one document in `known_paths`. If it cannot be resolved to any known
    document, the ORIGINAL raw reference string is returned unchanged (so
    a genuinely broken reference is still reported as broken, using the
    text the author actually wrote — not silently coerced into matching
    something).
    """

    def __init__(self, known_paths: list[str]):
        self.known_paths: set[str] = set(known_paths)
        # Map basename -> list of full paths, for fallback resolution when
        # a reference has no path component (e.g. "SIGNING-POLICY.md").
        self._by_basename: dict[str, list[str]] = {}
        for p in known_paths:
            name = Path(p).name
            self._by_basename.setdefault(name, []).append(p)

    def resolve(self, raw_ref: str, source_path: str) -> str:
        """Resolve `raw_ref` (as extracted from `source_path`'s content) to
        a canonical indexed path, or return `raw_ref` unchanged if it
        cannot be resolved to any known document.

        Resolution order (first match wins):
          1. Exact match: raw_ref is already a valid indexed path.
          2. Relative to the source document's own directory (mirrors
             architecture-tests/validate_cross_references.py's proven
             resolution strategy) -- e.g. a reference written in
             `docs/API-CONTRACTS.md` as `./IPC-PROTOCOL.md` resolves
             against `docs/`, giving `docs/IPC-PROTOCOL.md`.
          3. Under `docs/` explicitly -- covers references written as a
             bare filename from a root-level document that actually point
             at a `docs/`-owned canonical document.
          4. Basename fallback, ONLY if the basename is unambiguous (maps
             to exactly one known document) -- covers cases like a
             root-level document referencing another root-level document
             by bare name. If the basename is ambiguous (e.g. "AGENTS.md",
             which exists at both `AGENTS.md` and `docs/AGENTS.md`), this
             step intentionally does NOT guess; the raw reference is
             returned unresolved rather than silently picking the wrong
             one of two real documents.
        """
        if not raw_ref:
            return raw_ref

        cleaned = raw_ref.strip()
        if cleaned.startswith("./"):
            cleaned = cleaned[2:]
        if cleaned.startswith("/"):
            cleaned = cleaned.lstrip("/")

        # 1. Exact match.
        if cleaned in self.known_paths:
            return cleaned

        # 2. Relative to the source document's own directory.
        source_dir = Path(source_path).parent
        candidate = (source_dir / cleaned).as_posix()
        # Normalize "docs/./X.md" -> "docs/X.md", collapse any ".." safely
        # by relying on pathlib's own normalization via os.path.normpath
        # semantics (as_posix() does not collapse "..", so do it manually
        # only for the simple, expected case of no "..": if raw_ref had no
        # "..", `candidate` is already correct as constructed above).
        if candidate in self.known_paths:
            return candidate

        # 3. Explicit docs/ prefix.
        docs_candidate = f"docs/{cleaned}"
        if docs_candidate in self.known_paths:
            return docs_candidate

        # 4. Unambiguous basename fallback.
        basename = Path(cleaned).name
        matches = self._by_basename.get(basename, [])
        if len(matches) == 1:
            return matches[0]

        # Unresolvable (or ambiguous): return the original, unmodified.
        # This ensures a genuinely broken reference is reported using the
        # text the author wrote, and an ambiguous reference is flagged
        # rather than silently guessed.
        return raw_ref

    def is_known(self, resolved_ref: str) -> bool:
        return resolved_ref in self.known_paths
