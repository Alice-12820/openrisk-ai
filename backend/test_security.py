from ingestion.github_parser import clone_repository, find_solidity_files
from analysis.solidity_parser import SolidityParser
from analysis.security_analyzer import SecurityAnalyzer

repo = clone_repository(
    "https://github.com/Uniswap/v4-core"
)

files = find_solidity_files(repo)

parser = SolidityParser(files[0])

functions = parser.extract_functions()

for function in functions:

    findings = SecurityAnalyzer.analyze_function(function)

    if findings:

        print(function.name)

        print(findings)

        print("-" * 40)