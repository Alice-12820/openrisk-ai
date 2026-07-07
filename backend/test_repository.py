from ingestion.github_parser import clone_repository, find_solidity_files
from analysis.analyzer import analyze_contract

repo = clone_repository(
    "https://github.com/Uniswap/v4-core"
)

files = find_solidity_files(repo)

results = []

for file in files:
    results.append(analyze_contract(file))

print(results)