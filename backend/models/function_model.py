from dataclasses import dataclass
from typing import List


@dataclass
class FunctionInfo:
    name: str
    visibility: str
    state_mutability: str
    modifiers: List[str]