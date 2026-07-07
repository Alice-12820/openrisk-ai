from fastapi import FastAPI
from pydantic import BaseModel

from analysis.repository_analyzer import RepositoryAnalyzer

app = FastAPI(
    title="OpenRisk AI",
    version="0.1.0",
)


class AnalyzeRequest(BaseModel):
    github_url: str


@app.get("/")
def root():
    return {
        "status": "healthy",
        "service": "OpenRisk AI",
        "version": "0.1.0",
    }


@app.post("/analyze")
def analyze(request: AnalyzeRequest):

    analyzer = RepositoryAnalyzer()

    return analyzer.analyze(
        request.github_url
    )