from __future__ import annotations
import re
FRONT_MATTER_PATTERN = re.compile(r"^---\s*\n(?P<yaml>.*?)\n---\s*\n", re.DOTALL)

class SectionParser:
    @staticmethod
    def extract_front_matter(text: str) -> dict | None:
        import yaml
        m = FRONT_MATTER_PATTERN.match(text)
        if not m:
            return None
        try:
            return yaml.safe_load(m.group("yaml"))
        except Exception:
            return None
