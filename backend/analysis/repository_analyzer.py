from ingestion.github_parser import (
    clone_repository,
    find_solidity_files,
)

from analysis.analyzer import analyze_contract
from analysis.repository_summary import RepositorySummary
from analysis.risk_score import RiskScorer


class RepositoryAnalyzer:

    def analyze(self, github_url):

        repo = clone_repository(github_url)

        files = find_solidity_files(repo)

        results = []

        for file in files:

            analysis = analyze_contract(file)

            # Only include files that actually contain contracts
            if analysis["contracts"]:
                results.append(analysis)

        summary = RepositorySummary().summarize(results)

        risk = RiskScorer().score(summary)

        return {
            "repository": github_url,
            "summary": summary,
            "risk": risk,
            "contracts": results,
        }