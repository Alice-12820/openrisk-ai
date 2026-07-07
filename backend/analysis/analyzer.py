from analysis.solidity_parser import SolidityParser


def analyze_contract(filepath):
    parser = SolidityParser(filepath)

    return {
        "file": filepath,
        "contracts": parser.extract_contracts(),
        "functions": len(parser.extract_functions()),
        "modifiers": parser.extract_modifiers(),
        "roles": parser.find_roles(),
        "security_keywords": parser.find_security_keywords(),
    }