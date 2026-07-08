export interface Summary {
    total_contracts: number;
    total_functions: number;
    total_external_functions: number;
    total_privileged_functions: number;
    dangerous_operations: number;
}

export interface Risk {
    score: number;
    level: string;
}

export interface AIReport {
    executive_summary: string;
    overall_security_posture: string;
    priority_review_areas: string[];
    recommended_next_steps: string[];
}

export interface RepositoryAnalysis {
    repository: string;
    summary: Summary;
    risk: Risk;
    contracts: any[];
}

export interface AnalysisResponse {
    analysis: RepositoryAnalysis;
    ai_report: AIReport;
}