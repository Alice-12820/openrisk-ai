from dataclasses import dataclass

@dataclass
class ContractInfo:
    file: str
    contract_name: str

    functions: list
    modifiers: list

    inherits: list

    roles: list

    external_calls: list

    dangerous_operations: list