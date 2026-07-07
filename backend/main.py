from fastapi import FastAPI
from pydantic import BaseModel

from ingestion.github_parser import (
    clone_repository,
    find_solidity_files,
)

from analysis.analyzer import analyze_contract

app = FastAPI()


class AnalyzeRequest(BaseModel):
    github_url: str


@app.post("/analyze")
def analyze(request: AnalyzeRequest):

    repo = clone_repository(
        request.github_url
    )

    files = find_solidity_files(repo)

    output = []

    for file in files:
        output.append(
            analyze_contract(file)
        )

    return {
        "contracts": output
    }
    @app.get("/")
    def root():
        return {
        "status": "healthy",
        "service": "OpenRisk AI",
        "version": "0.1.0"
    }