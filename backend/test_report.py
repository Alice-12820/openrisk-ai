from analysis.repository_analyzer import RepositoryAnalyzer
from ai.report_generator import ReportGenerator

repository = RepositoryAnalyzer().analyze(
    "https://github.com/Uniswap/v4-core"
)

report = ReportGenerator().generate(
    repository
)

print(report)