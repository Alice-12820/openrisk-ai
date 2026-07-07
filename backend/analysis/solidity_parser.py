import re
from pathlib import Path

from models.function_model import FunctionInfo

SECURITY_KEYWORDS = [
    "delegatecall",
    "call",
    "staticcall",
    "assembly",
    "selfdestruct",
    "tx.origin",
    "block.timestamp",
    "transfer",
    "send",
]

ROLE_KEYWORDS = [
    "owner",
    "admin",
    "governance",
    "guardian",
    "operator",
]

FUNCTION_REGEX = re.compile(
    r"function\s+(\w+)\s*\([^)]*\)\s*([^{;]*)",
    re.MULTILINE,
)


class SolidityParser:
    def __init__(self, filepath):
        self.filepath = Path(filepath)

        self.content = self.filepath.read_text(
            encoding="utf-8",
            errors="ignore",
        )

    def extract_contracts(self):
        return re.findall(
            r"contract\s+([A-Za-z0-9_]+)",
            self.content,
        )

    def extract_functions(self):
        functions = []

        matches = FUNCTION_REGEX.findall(self.content)

        for name, signature in matches:

            visibility = "internal"

            for v in [
                "public",
                "external",
                "internal",
                "private",
            ]:
                if v in signature:
                    visibility = v
                    break

            state = "nonpayable"

            for s in [
                "view",
                "pure",
                "payable",
            ]:
                if s in signature:
                    state = s
                    break

            modifiers = []

            words = signature.split()

            for word in words:
                if word not in [
                    visibility,
                    state,
                    "returns",
                ]:
                    modifiers.append(word)

            functions.append(
                FunctionInfo(
                    name=name,
                    visibility=visibility,
                    state_mutability=state,
                    modifiers=modifiers,
                )
            )

        return functions

    def extract_modifiers(self):
        return re.findall(
            r"modifier\s+([A-Za-z0-9_]+)",
            self.content,
        )

    def find_security_keywords(self):
        found = []

        for keyword in SECURITY_KEYWORDS:
            if keyword in self.content:
                found.append(keyword)

        return found

    def find_roles(self):
        found = []

        lower = self.content.lower()

        for role in ROLE_KEYWORDS:
            if role in lower:
                found.append(role)

        return found

    def extract_inheritance(self):
        matches = re.findall(
            r"contract\s+\w+\s+is\s+([^{]+)",
            self.content,
        )

        if not matches:
            return []

        parents = []

        for m in matches:
            parents.extend(
                [x.strip() for x in m.split(",")]
            )

        return parents