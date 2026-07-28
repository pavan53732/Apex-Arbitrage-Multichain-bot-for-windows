
from __future__ import annotations
import re
from typing import Optional
from .models import DocumentMetadata
from ..parser.section_parser import SectionParser
from ..references.reference_parser import ReferenceParser

class MetadataParser:
    REQUIRED_FIELDS = ["type", "owner", "status", "version"]

    def __init__(self, repo_root: str = "."):
        self.repo_root = repo_root
        self.ref_parser = ReferenceParser(repo_root)

    def extract_field(self, text: str, field: str, patterns: list[str]) -> Optional[str]:
        for pattern in patterns:
            try:
                match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
                if match:
                    return match.group(1).strip()
            except Exception:
                continue
        return None

    def extract_list_field(self, text: str, field: str, patterns: list[str]) -> list[str]:
        content = self.extract_field(text, field, patterns)
        if not content:
            return []
        items = []
        for line in content.split("\n"):
            line = line.strip()
            if line.startswith("-"):
                line = line[1:].strip()
            if line and not line.startswith("```") and not line.startswith("```mermaid"):
                items.append(line)
        return items[:10]

    def parse_document(self, text: str, path: str) -> DocumentMetadata:
        front = SectionParser.extract_front_matter(text) or {}

        meta_dict = {"path": path, "raw_text": text}

        # Type patterns
        meta_dict["type"] = self.extract_field(text, "type", [
            r"Document type:\s*\[([A-Z]+)\]",
            r"Document type:\s*([A-Z]+)",
            r"Type:\s*([A-Z]+)",
        ]) or front.get("type")

        # Owner patterns
        meta_dict["owner"] = self.extract_field(text, "owner", [
            r"\*\*Owner:\*\*\s*([^\n|]+)",
            r"Owner:\s*([^\n|]+)",
            r"Canonical Owner:\s*([^\n|]+)",
        ]) or front.get("owner")

        # Status patterns
        meta_dict["status"] = self.extract_field(text, "status", [
            r"\*\*Status:\*\*\s*([A-Za-z]+)",
            r"Status:\s*([A-Z]+)",
        ]) or front.get("status")

        # Version patterns
        meta_dict["version"] = self.extract_field(text, "version", [
            r"\*\*Version:\*\*\s*([0-9.]+)",
            r"Version:\s*([0-9.]+)",
        ]) or front.get("version")

        # Purpose
        meta_dict["purpose"] = self.extract_field(text, "purpose", [
            r"## Purpose\n+(.+?)(?=\n##|\n---|$)",
        ]) or front.get("purpose")

        # Scope
        meta_dict["scope"] = self.extract_field(text, "scope", [
            r"## Scope\n+(.+?)(?=\n##|\n---|$)",
        ]) or front.get("scope")

        # Use reference parser for cross_references and depends_on
        meta_dict["cross_references"] = self.ref_parser.extract_cross_references(text, path)
        meta_dict["depends_on"] = self.ref_parser.extract_depends_on(text, path)

        # If no explicit depends_on, use cross_references as dependencies
        if not meta_dict["depends_on"] and meta_dict["cross_references"]:
            meta_dict["depends_on"] = meta_dict["cross_references"][:5]

        # Responsibilities
        meta_dict["responsibilities"] = self.extract_list_field(text, "responsibilities", [
            r"## Responsibilities\n+(.+?)(?=\n##|\n---|$)",
        ]) or (front.get("responsibilities") or [])

        # Owns
        meta_dict["owns"] = self.extract_list_field(text, "owns", [
            r"## Owns\n+(.+?)(?=\n##|\n---|$)",
            r"## Ownership\n+(.+?)(?=\n##|\n---|$)",
        ]) or (front.get("owns") or [])

        # Does not own
        meta_dict["does_not_own"] = self.extract_list_field(text, "does_not_own", [
            r"## Does Not Own\n+(.+?)(?=\n##|\n---|$)",
            r"## Does not own\n+(.+?)(?=\n##|\n---|$)",
        ]) or (front.get("does_not_own") or [])

        # Inputs
        meta_dict["inputs"] = self.extract_list_field(text, "inputs", [
            r"## Inputs\n+(.+?)(?=\n##|\n---|$)",
        ]) or (front.get("inputs") or [])

        # Outputs
        meta_dict["outputs"] = self.extract_list_field(text, "outputs", [
            r"## Outputs\n+(.+?)(?=\n##|\n---|$)",
        ]) or (front.get("outputs") or [])

        # Required by
        meta_dict["required_by"] = self.extract_list_field(text, "required_by", [
            r"## Required By\n+(.+?)(?=\n##|\n---|$)",
        ]) or (front.get("required_by") or [])

        # Interfaces
        meta_dict["interfaces"] = self.extract_list_field(text, "interfaces", [
            r"## Interfaces\n+(.+?)(?=\n##|\n---|$)",
        ]) or (front.get("interfaces") or [])

        # Events produced
        meta_dict["events_produced"] = self.extract_list_field(text, "events_produced", [
            r"## Events Produced\n+(.+?)(?=\n##|\n---|$)",
        ]) or (front.get("events_produced") or [])

        # Events consumed
        meta_dict["events_consumed"] = self.extract_list_field(text, "events_consumed", [
            r"## Events Consumed\n+(.+?)(?=\n##|\n---|$)",
        ]) or (front.get("events_consumed") or [])

        # Configuration
        meta_dict["configuration"] = self.extract_list_field(text, "configuration", [
            r"## Configuration\n+(.+?)(?=\n##|\n---|$)",
        ]) or (front.get("configuration") or [])

        # Schemas
        meta_dict["schemas"] = self.extract_list_field(text, "schemas", [
            r"## Schemas\n+(.+?)(?=\n##|\n---|$)",
        ]) or (front.get("schemas") or [])

        # State machines
        meta_dict["state_machines"] = self.extract_list_field(text, "state_machines", [
            r"## State Machines\n+(.+?)(?=\n##|\n---|$)",
            r"## State machine\n+(.+?)(?=\n##|\n---|$)",
        ]) or (front.get("state_machines") or [])

        # Security
        meta_dict["security"] = self.extract_list_field(text, "security", [
            r"## Security\n+(.+?)(?=\n##|\n---|$)",
        ]) or (front.get("security") or [])

        # Recovery
        meta_dict["recovery"] = self.extract_list_field(text, "recovery", [
            r"## Recovery\n+(.+?)(?=\n##|\n---|$)",
        ]) or (front.get("recovery") or [])

        # Failure behaviour
        meta_dict["failure_behaviour"] = self.extract_list_field(text, "failure_behaviour", [
            r"## Failure Behaviour\n+(.+?)(?=\n##|\n---|$)",
            r"## Failure modes\n+(.+?)(?=\n##|\n---|$)",
        ]) or (front.get("failure_behaviour") or [])

        # Performance
        meta_dict["performance"] = self.extract_list_field(text, "performance", [
            r"## Performance\n+(.+?)(?=\n##|\n---|$)",
        ]) or (front.get("performance") or [])

        # Validation
        meta_dict["validation"] = self.extract_list_field(text, "validation", [
            r"## Validation\n+(.+?)(?=\n##|\n---|$)",
        ]) or (front.get("validation") or [])

        # Testing
        meta_dict["testing"] = self.extract_list_field(text, "testing", [
            r"## Testing\n+(.+?)(?=\n##|\n---|$)",
        ]) or (front.get("testing") or [])

        # Version history
        meta_dict["version_history"] = self.extract_list_field(text, "version_history", [
            r"## Version History\n+(.+?)(?=\n##|\n---|$)",
            r"## Changelog\n+(.+?)(?=\n##|\n---|$)",
        ]) or (front.get("version_history") or [])

        # Canonical source
        meta_dict["canonical_source"] = self.extract_field(text, "canonical_source", [
            r"## Canonical Source\n+(.+?)(?=\n##|\n---|$)",
        ]) or front.get("canonical_source")

        return DocumentMetadata(**meta_dict)

    def validate_required(self, meta: DocumentMetadata) -> list[str]:
        missing = []
        for f in self.REQUIRED_FIELDS:
            if getattr(meta, f, None) in (None, ""):
                missing.append(f)
        return missing
