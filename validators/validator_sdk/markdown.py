"""
Markdown utilities: discovery, metadata parsing, link resolution.
"""

from __future__ import annotations
import re
import yaml
from pathlib import Path
from typing import Any
from dataclasses import dataclass

from .config import ValidatorConfig


@dataclass
class ParsedMarkdown:
    """Result of parsing a markdown file."""
    file_path: Path
    metadata: dict[str, Any]
    body: str
    raw_content: str


class MarkdownDiscovery:
    """Discover all markdown files with filtering."""

    @staticmethod
    def find_all(repo_root: Path, config: ValidatorConfig) -> list[Path]:
        """Find all .md files in repository, respecting ignore patterns."""
        all_files = []

        for md_file in repo_root.rglob("*.md"):
            # Skip ignored paths
            relative = md_file.relative_to(repo_root)
            if any(ignored in str(relative) for ignored in config.ignored_paths):
                continue

            # Skip ignored files
            if any(md_file.match(pattern) for pattern in config.ignored_files):
                continue

            # Check file size
            if md_file.stat().st_size > config.max_file_size_mb * 1024 * 1024:
                continue

            all_files.append(md_file)

        return sorted(all_files)

    @staticmethod
    def find_changed(repo_root: Path, since_commit: str) -> list[Path]:
        """Find markdown files changed since a commit (requires git)."""
        import subprocess

        try:
            result = subprocess.run(
                ["git", "diff", "--name-only", since_commit, "HEAD"],
                cwd=repo_root,
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode != 0:
                return []

            changed = []
            for line in result.stdout.strip().split("\n"):
                if line.endswith(".md"):
                    path = repo_root / line
                    if path.exists():
                        changed.append(path)
            return changed
        except Exception:
            return []


class MetadataParser:
    """Parse and validate YAML frontmatter."""

    REQUIRED_FIELDS = [
        "metadata_schema_version",
        "document_id",
        "title",
        "plane",
        "domain",
        "class",
        "authority",
        "status",
        "owner",
        "version",
        "canonical_source",
        "concept_role",
    ]

    VALID_PLANES = ["Repository Operating Model", "Product Specification"]
    VALID_AUTHORITIES = ["Canonical", "Derived", "Reference", "Historical", "Generated"]
    VALID_STATUSES = ["Draft", "Review", "Approved", "Active", "Deprecated", "Archived", "Superseded", "Experimental"]
    VALID_CLASSES = [
        "Specification", "Guide", "Reference", "ADR", "Historical",
        "Certification", "Registry", "Policy", "Workflow", "Manifest", "Index", "Generated"
    ]

    @staticmethod
    def parse(file_path: Path) -> tuple[dict[str, Any], str]:
        """Parse markdown file into (metadata, body). Returns empty dict if no frontmatter."""
        content = file_path.read_text(encoding="utf-8")

        if not content.startswith("---"):
            return {}, content

        parts = content.split("---", 2)
        if len(parts) < 3:
            return {}, content

        try:
            metadata = yaml.safe_load(parts[1]) or {}
        except yaml.YAMLError:
            metadata = {}

        body = parts[2] if len(parts) > 2 else ""
        return metadata, body

    @staticmethod
    def parse_file(file_path: Path) -> ParsedMarkdown:
        """Parse file into structured result."""
        content = file_path.read_text(encoding="utf-8")
        metadata, body = MetadataParser.parse(file_path)
        return ParsedMarkdown(
            file_path=file_path,
            metadata=metadata,
            body=body,
            raw_content=content
        )

    @staticmethod
    def validate(metadata: dict[str, Any], schema_version: str = "1.0") -> list[tuple[str, str, str]]:
        """
        Validate metadata against schema.
        Returns list of (field, expected, actual) for violations.
        """
        errors = []

        # Check required fields
        for field in MetadataParser.REQUIRED_FIELDS:
            if field not in metadata:
                errors.append((field, "required", "missing"))
                continue

            value = metadata[field]

            # Validate specific fields
            if field == "plane" and value not in MetadataParser.VALID_PLANES:
                errors.append((field, f"one of {MetadataParser.VALID_PLANES}", str(value)))

            elif field == "authority" and value not in MetadataParser.VALID_AUTHORITIES:
                errors.append((field, f"one of {MetadataParser.VALID_AUTHORITIES}", str(value)))

            elif field == "status" and value not in MetadataParser.VALID_STATUSES:
                errors.append((field, f"one of {MetadataParser.VALID_STATUSES}", str(value)))

            elif field == "class" and value not in MetadataParser.VALID_CLASSES:
                errors.append((field, f"one of {MetadataParser.VALID_CLASSES}", str(value)))

            elif field == "document_id" and not re.match(r"^DOC-\d{4}$", str(value)):
                errors.append((field, "DOC-XXXX format", str(value)))

            elif field == "metadata_schema_version" and str(value) != schema_version:
                errors.append((field, schema_version, str(value)))

        return errors


class LinkResolver:
    """Resolve internal markdown links and DOC-ID/CONCEPT-ID references."""

    DOC_ID_PATTERN = re.compile(r"DOC-\d{4}")
    CONCEPT_ID_PATTERN = re.compile(r"CONCEPT-\d{4}")
    MARKDOWN_LINK_PATTERN = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")

    @staticmethod
    def find_markdown_links(content: str) -> list[tuple[str, str]]:
        """Find all markdown links in content. Returns [(text, target), ...]."""
        return LinkResolver.MARKDOWN_LINK_PATTERN.findall(content)

    @staticmethod
    def find_doc_ids(content: str) -> list[str]:
        """Find all DOC-ID references in content."""
        return LinkResolver.DOC_ID_PATTERN.findall(content)

    @staticmethod
    def find_concept_ids(content: str) -> list[str]:
        """Find all CONCEPT-ID references in content."""
        return LinkResolver.CONCEPT_ID_PATTERN.findall(content)

    @staticmethod
    def resolve_markdown_link(link: str, from_file: Path, repo_root: Path) -> Path | None:
        """Resolve a markdown link target to an absolute path."""
        # Handle anchor links
        if link.startswith("#"):
            return from_file  # Same file, anchor only

        # Handle relative paths
        link_path = (from_file.parent / link).resolve()

        # Must be within repo
        try:
            link_path.relative_to(repo_root)
        except ValueError:
            return None

        if link_path.exists():
            return link_path

        # Try with .md extension
        if not link_path.suffix:
            md_path = link_path.with_suffix(".md")
            if md_path.exists():
                return md_path

        return None

    @staticmethod
    def resolve_doc_id(doc_id: str, document_registry: dict) -> Path | None:
        """Resolve DOC-ID to file path using Document Registry."""
        entry = document_registry.get(doc_id)
        if entry and entry.path:
            return Path(entry.path)
        return None

    @staticmethod
    def resolve_concept_id(concept_id: str, concept_registry: dict) -> dict | None:
        """Resolve CONCEPT-ID to concept entry using Concept Registry."""
        return concept_registry.get(concept_id)