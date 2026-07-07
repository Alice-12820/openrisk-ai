import re
from pathlib import Path


class SolidityParser:
    def __init__(self, filepath):
        self.filepath = Path(filepath)
        self.content = self.filepath.read_text(
            encoding="utf-8",
            errors="ignore"
        )

    def extract_contracts(self):
        return re.findall(
            r'contract\s+([A-Za-z0-9_]+)',
            self.content
        )

    def extract_functions(self):
        return re.findall(
            r'function\s+([A-Za-z0-9_]+)',
            self.content
        )

    def extract_modifiers(self):
        return re.findall(
            r'modifier\s+([A-Za-z0-9_]+)',
            self.content
        )