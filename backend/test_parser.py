from ingestion.github_parser import clone_repository, find_solidity_files
from analysis.solidity_parser import SolidityParser

repo = clone_repository(
    "https://github.com/Uniswap/v4-core"
)

files = find_solidity_files(repo)

parser = SolidityParser(files[0])

print(parser.extract_contracts())
print(parser.extract_functions())
print(parser.extract_modifiers())