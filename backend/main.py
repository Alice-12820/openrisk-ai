from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from analysis.repository_analyzer import RepositoryAnalyzer
from ai.report_generator import ReportGenerator

app = FastAPI(
    title="OpenRisk AI",
    version="0.1.0",
)

# Allow requests from the frontend during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://potential-dollop-4p9jgj4v9fj7rr-5173.app.github.dev"],  # We'll tighten this later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
    repository_analysis = RepositoryAnalyzer().analyze(
        request.github_url
    )

    ai_report = ReportGenerator().generate(
        repository_analysis
    )

    return {
        "analysis": repository_analysis,
        "ai_report": ai_report,
    }