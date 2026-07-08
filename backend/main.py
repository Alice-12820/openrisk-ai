from fastapi import FastAPI
from pydantic import BaseModel

from analysis.repository_analyzer import RepositoryAnalyzer
from ai.report_generator import ReportGenerator

app = FastAPI(
    title="OpenRisk AI",
    version="0.1.0"
)


class AnalyzeRequest(BaseModel):
    github_url: str


@app.get("/")
def root():
    return {
        "status": "healthy",
        "service": "OpenRisk AI",
        "version": "0.1.0"
    }


@app.post("/analyze")
def analyze(request: AnalyzeRequest):

    # Analyze the GitHub repository
    repository_analysis = RepositoryAnalyzer().analyze(
        request.github_url
    )

    # Generate the AI security report
    ai_report = ReportGenerator().generate(
        repository_analysis
    )

    return {
        "analysis": repository_analysis,
        "ai_report": ai_report
    }