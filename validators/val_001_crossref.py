"""
VAL-001: Cross-Reference Validator
Verifies all links and references resolve to valid targets.
"""

from __future__ import annotations
from pathlib import Path
from validator_sdk import (
    BaseValidator,
    ValidationContext,
    ValidationError,
    ValidationWarning,
    ErrorCode,
    format_error,
    LinkResolver,
    MetadataParser,
)


class Validator(BaseValidator):
    VALIDATOR_ID = "VAL-001"
    NAME = "Cross-Reference Validator"
    VERSION = "1.0.0"
    DESCRIPTION = "Verifies all links and references resolve to valid targets"
    CATEGORY = "crossref"
    SEVERITY = "ERROR"
    SUPPORTED_METADATA_SCHEMA_VERSIONS = ["1.0"]
    SUPPORTED_REPOSITORY_SPEC_VERSIONS = ["1.0"]

    def validate(self, context: ValidationContext) -> ValidationError:
        self._start_timer()
        errors = []
        warnings = []
        checked = 0

        vc = context.config.validator_configs.get("VAL-001", {})
        check_anchors = vc.get("check_anchors", True)
        check_external = vc.get("check_external_urls", False)

        # Build lookup sets for fast resolution
        doc_registry = context.document_registry
        concept_registry = context.concept_registry

        doc_ids = set(doc_registry.keys())
        concept_ids = set(concept_registry.keys())

        for md_file in context.all_markdown_files:
            checked += 1
            rel_path = md_file.relative_to(context.repository_root)
            rel_str = str(rel_path).replace("\\", "/")

            # Read full content for link checking
            content = md_file.read_text(encoding="utf-8")
            metadata, body = MetadataParser.parse(md_file)

            # 1. Check markdown links
            links = LinkResolver.find_markdown_links(content)
            for link_text, link_target in links:
                # Skip external URLs unless configured
                if link_target.startswith(("http://", "https://", "mailto:")):
                    if not check_external:
                        continue
                    # Could add HTTP check here but local-first means no network
                    continue

                # Resolve link
                resolved = LinkResolver.resolve_markdown_link(link_target, md_file, context.repository_root)

                if resolved is None:
                    # Check if it's an anchor-only link
                    if link_target.startswith("#"):
                        # Anchor in same file - check if anchor exists
                        anchor = link_target[1:]
                        if not self._anchor_exists(body, anchor):
                            errors.append(ValidationError(
                                code=ErrorCode.BROKEN_ANCHOR_LINK,
                                file=rel_str,
                                line=self._find_link_line(content, link_target),
                                message=format_error(ErrorCode.BROKEN_ANCHOR_LINK, anchor=anchor),
                                severity="ERROR",
                                rule="Anchor links must exist in target file",
                                suggestion=f"Add anchor #{anchor} to target file or fix link"
                            ))
                    else:
                        errors.append(ValidationError(
                            code=ErrorCode.UNRESOLVED_MARKDOWN_LINK,
                            file=rel_str,
                            line=self._find_link_line(content, link_target),
                            message=format_error(ErrorCode.UNRESOLVED_MARKDOWN_LINK, target=link_target, file=rel_str),
                            severity="ERROR",
                            rule="All markdown links must resolve to existing files",
                            suggestion=f"Fix link target or create missing file: {link_target}"
                        ))

            # 2. Check DOC-ID references in body
            doc_refs = LinkResolver.find_doc_ids(content)
            for doc_id in doc_refs:
                if doc_id not in doc_ids:
                    errors.append(ValidationError(
                        code=ErrorCode.UNRESOLVED_DOC_REF,
                        file=rel_str,
                        line=self._find_ref_line(content, doc_id),
                        message=format_error(ErrorCode.UNRESOLVED_DOC_REF, doc_id=doc_id),
                        severity="ERROR",
                        rule="All DOC-ID references must resolve to registered document",
                        suggestion=f"Add {doc_id} to Document Registry or fix reference"
                    ))

            # 3. Check CONCEPT-ID references in body
            concept_refs = LinkResolver.find_concept_ids(content)
            for concept_id in concept_refs:
                if concept_id not in concept_ids:
                    errors.append(ValidationError(
                        code=ErrorCode.UNRESOLVED_CONCEPT_REF,
                        file=rel_str,
                        line=self._find_ref_line(content, concept_id),
                        message=format_error(ErrorCode.UNRESOLVED_CONCEPT_REF, concept_id=concept_id),
                        severity="ERROR",
                        rule="All CONCEPT-ID references must resolve to registered concept",
                        suggestion=f"Add {concept_id} to Concept Registry or fix reference"
                    ))

            # 4. Check metadata references
            # related_concepts
            for concept_id in metadata.get("related_concepts", []):
                if concept_id not in concept_ids:
                    errors.append(ValidationError(
                        code=ErrorCode.UNRESOLVED_CONCEPT_REF,
                        file=rel_str,
                        line=1,
                        message=format_error(ErrorCode.UNRESOLVED_CONCEPT_REF, concept_id=concept_id),
                        severity="ERROR",
                        rule="related_concepts must reference registered concepts",
                        suggestion=f"Add {concept_id} to Concept Registry or fix reference"
                    ))

            # dependencies
            for dep_id in metadata.get("dependencies", []):
                if dep_id not in doc_ids:
                    errors.append(ValidationError(
                        code=ErrorCode.UNRESOLVED_DOC_REF,
                        file=rel_str,
                        line=1,
                        message=format_error(ErrorCode.UNRESOLVED_DOC_REF, doc_id=dep_id),
                        severity="ERROR",
                        rule="dependencies must reference registered documents",
                        suggestion=f"Add {dep_id} to Document Registry or fix reference"
                    ))

            # supersedes / superseded_by
            for field in ("supersedes", "superseded_by"):
                for item in metadata.get(field, []):
                    if item not in doc_ids:
                        errors.append(ValidationError(
                            code=ErrorCode.UNRESOLVED_DOC_REF,
                            file=rel_str,
                            line=1,
                            message=format_error(ErrorCode.UNRESOLVED_DOC_REF, doc_id=item),
                            severity="ERROR",
                            rule=f"{field} must reference registered documents",
                            suggestion=f"Add {item} to Document Registry or fix reference"
                        ))

            # consumers
            for consumer in metadata.get("consumers", []):
                if consumer not in doc_ids:
                    warnings.append(ValidationWarning(
                        code=ErrorCode.UNRESOLVED_DOC_REF,
                        file=rel_str,
                        line=1,
                        message=f"Consumer {consumer} not found in Document Registry",
                        severity="WARNING",
                        rule="consumers should reference registered documents",
                        suggestion=f"Verify consumer {consumer} is registered"
                    ))

        if errors:
            return self._result_fail(checked, errors)
        return self._result_pass(checked, warnings)

    def _find_link_line(self, content: str, target: str) -> int:
        """Find line number of a markdown link."""
        lines = content.split("\n")
        for i, line in enumerate(lines, 1):
            if f"]({target})" in line or f"]({target} " in line:
                return i
        return 1

    def _find_ref_line(self, content: str, ref: str) -> int:
        """Find line number of a reference."""
        lines = content.split("\n")
        for i, line in enumerate(lines, 1):
            if ref in line:
                return i
        return 1

    def _anchor_exists(self, body: str, anchor: str) -> bool:
        """Check if anchor exists in markdown body."""
        # Check for heading anchors
        import re
        # ## Heading -> #heading
        headings = re.findall(r"^#{1,6}\s+(.+)$", body, re.MULTILINE)
        for heading in headings:
            # GitHub-style anchor generation
            slug = heading.lower().replace(" ", "-")
            slug = re.sub(r"[^\w\-]", "", slug)
            if slug == anchor:
                return True

        # Check for explicit anchor tags
        if f'<a id="{anchor}">' in body or f'<a name="{anchor}">' in body:
            return True

        return False