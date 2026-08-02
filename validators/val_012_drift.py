"""
VAL-012: Semantic Drift Validator
Detects semantic drift between related documents through content hash comparison,
section drift detection, version inconsistency, and stale dependency analysis.
"""

from __future__ import annotations
import hashlib
from pathlib import Path
from collections import defaultdict
from datetime import datetime, timezone
from validator_sdk import (
    BaseValidator,
    ValidationContext,
    ValidationError,
    ValidationWarning,
    ErrorCode,
    format_error,
    MetadataParser,
)


class Validator(BaseValidator):
    VALIDATOR_ID = "VAL-012"
    NAME = "Semantic Drift Validator"
    VERSION = "1.0.0"
    DESCRIPTION = "Detects semantic drift between related documents through content hashing, section comparison, and staleness analysis"
    CATEGORY = "drift"
    SEVERITY = "WARNING"
    SUPPORTED_METADATA_SCHEMA_VERSIONS = ["1.0"]
    SUPPORTED_REPOSITORY_SPEC_VERSIONS = ["1.0"]

    STALE_THRESHOLD_DAYS = 90

    def validate(self, context: ValidationContext) -> ValidationResult:
        self._start_timer()
        errors = []
        warnings = []
        checked = 0

        # Phase 1: Compute content hashes for all documents
        doc_hashes: dict[str, str] = {}
        doc_metadata: dict[str, dict] = {}
        doc_headings: dict[str, list[str]] = {}

        for md_file in context.all_markdown_files:
            rel_path = md_file.relative_to(context.repository_root)
            rel_str = str(rel_path).replace("\\", "/")

            metadata, body = MetadataParser.parse(md_file)
            if not metadata:
                continue

            doc_id = metadata.get("document_id", "unknown")
            if doc_id == "unknown":
                continue

            # Content hash (SHA-256 of body only, not frontmatter)
            body_hash = hashlib.sha256(body.encode("utf-8")).hexdigest()
            doc_hashes[doc_id] = body_hash
            doc_metadata[doc_id] = metadata

            # Extract all headings as section markers
            headings = []
            for line in body.split("\n"):
                stripped = line.strip()
                if stripped.startswith("#"):
                    text = stripped.lstrip("#").strip().lower()
                    headings.append(text)
            doc_headings[doc_id] = headings

        # Phase 2: Detect drift in dependency chains
        for doc_id, entry in context.document_registry.items():
            checked += 1

            # Skip historical/superseded docs
            if entry.status in ("Superseded", "Deprecated", "Archived"):
                continue

            # A) Staleness check: last_updated older than threshold
            last_updated = doc_metadata.get(doc_id, {}).get("last_updated", "")
            if last_updated:
                try:
                    if isinstance(last_updated, str):
                        lu_date = datetime.fromisoformat(last_updated)
                    else:
                        lu_date = last_updated
                    days_since = (datetime.now(timezone.utc) - lu_date.replace(tzinfo=timezone.utc)).days
                    if days_since > self.STALE_THRESHOLD_DAYS and entry.status == "Active":
                        warnings.append(ValidationWarning(
                            code="DOCUMENT_STALE",
                            file=entry.path,
                            line=1,
                            message=f"Document {doc_id} last updated {days_since} days ago (> {self.STALE_THRESHOLD_DAYS}d threshold)",
                            severity="WARNING",
                            rule="Active documents should be reviewed at least every 90 days.",
                            suggestion=f"Review {entry.path} for staleness or update last_updated.",
                        ))
                except (ValueError, TypeError):
                    pass

            # B) Dependency drift: consumer newer than its dependency
            if entry.dependencies:
                consumer_updated = doc_metadata.get(doc_id, {}).get("last_updated", "")
                for dep_id in entry.dependencies:
                    dep_id = dep_id.strip()
                    if not dep_id or dep_id not in context.document_registry:
                        continue

                    dep_entry = context.document_registry[dep_id]
                    dep_updated = doc_metadata.get(dep_id, {}).get("last_updated", "")

                    if consumer_updated and dep_updated:
                        try:
                            cu = datetime.fromisoformat(str(consumer_updated))
                            du = datetime.fromisoformat(str(dep_updated))
                            if cu > du:
                                warnings.append(ValidationWarning(
                                    code="DEPENDENCY_DRIFT",
                                    file=entry.path,
                                    line=1,
                                    message=f"Consumer {doc_id} (updated {consumer_updated}) is newer than "
                                            f"its dependency {dep_id} (updated {dep_updated}). "
                                            f"Dependency may be stale relative to consumer.",
                                    severity="WARNING",
                                    rule="Consumers should not be updated more recently than their dependencies "
                                          "without the dependency also being updated.",
                                    suggestion=f"Review {dep_entry.path} — it may need updating to match {entry.path}.",
                                ))
                        except (ValueError, TypeError):
                            pass

            # C) Section drift: compare section headings between related docs
            if entry.dependencies:
                consumer_sections = set(doc_headings.get(doc_id, []))
                for dep_id in entry.dependencies:
                    dep_id = dep_id.strip()
                    if not dep_id or dep_id not in doc_headings:
                        continue
                    dep_sections = set(doc_headings[dep_id])

                    # Check for sections referenced by consumer but missing in dependency
                    for section in consumer_sections:
                        if len(section.split()) >= 3 and section not in dep_sections:
                            warnings.append(ValidationWarning(
                                code="SECTION_DRIFT",
                                file=entry.path, line=1,
                                message=f"Consumer {doc_id} has section '{section}' absent from dependency {dep_id}",
                                severity="WARNING",
                                rule="Sections in consumer should be mirrored in dependency.",
                                suggestion=f"Verify '{section}' is present in {dep_id}.",
                            ))

        # Phase 3: Detect duplicate content via hash collision
        hash_to_docs = defaultdict(list)
        for doc_id, h in doc_hashes.items():
            hash_to_docs[h].append(doc_id)

        for h, docs in hash_to_docs.items():
            if len(docs) > 1:
                # Same body hash = identical content
                errors.append(ValidationError(
                    code="DUPLICATE_CONTENT",
                    file=context.document_registry[docs[0]].path if docs[0] in context.document_registry else "",
                    line=1,
                    message=f"Documents {', '.join(docs)} have identical body content (hash: {h[:12]}...)",
                    severity="ERROR",
                    rule="No two active documents should have identical content.",
                    suggestion="Consolidate duplicate documents or differentiate their content.",
                ))

        # Phase 4: Version inconsistency — related docs should have correlated versions
        for doc_id, entry in context.document_registry.items():
            if entry.status != "Active":
                continue
            version = doc_metadata.get(doc_id, {}).get("version", "1.0.0")
            if entry.dependencies:
                for dep_id in entry.dependencies:
                    dep_id = dep_id.strip()
                    if dep_id not in doc_metadata:
                        continue
                    dep_version = doc_metadata[dep_id].get("version", "1.0.0")
                    # Major version mismatch: consumer v2.x depends on dep v1.x
                    try:
                        v_parts = str(version).split(".")
                        d_parts = str(dep_version).split(".")
                        if len(v_parts) >= 1 and len(d_parts) >= 1:
                            if int(v_parts[0]) > int(d_parts[0]):
                                warnings.append(ValidationWarning(
                                    code="VERSION_DRIFT",
                                    file=entry.path,
                                    line=1,
                                    message=f"Document {doc_id} v{version} depends on {dep_id} v{dep_version} "
                                            f"— major version mismatch may indicate drift",
                                    severity="WARNING",
                                    rule="Major version of consumer should not exceed major version of dependency "
                                          "without explicit justification.",
                                    suggestion=f"Verify {dep_id} is up to date or update its version.",
                                ))
                    except (ValueError, IndexError):
                        pass

        if errors:
            return self._result_fail(checked, errors)
        return self._result_pass(checked, warnings)
