from analysis.solidity_parser import SolidityParser
from analysis.security_analyzer import SecurityAnalyzer


def analyze_contract(filepath):
    parser = SolidityParser(filepath)

    functions = parser.extract_functions()

    analyzed_functions = []

    for function in functions:

        analyzed_functions.append(
            {
                "name": function.name,
                "visibility": function.visibility,
                "state_mutability": function.state_mutability,
                "modifiers": function.modifiers,
                "security_findings": SecurityAnalyzer.analyze_function(
                    function
                ),
            }
        )

    return {
        "file": filepath,
        "contracts": parser.extract_contracts(),
        "inherits": parser.extract_inheritance(),
        "functions": analyzed_functions,
        "modifiers": parser.extract_modifiers(),
        "roles": parser.find_roles(),
        "security_keywords": parser.find_security_keywords(),
    }