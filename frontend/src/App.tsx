import { useState } from "react";

import Header from "./components/Header";
import SearchBar from "./components/SearchBar";
import RiskGauge from "./components/RiskGauge";
import StatsCard from "./components/StatsCard";
import ReportCard from "./components/ReportCard";
import RepositoryCard from "./components/RepositoryCard";
import LoadingOverlay from "./components/LoadingOverlay";

import api from "./services/api";

import type { AnalysisResponse } from "./types/report";

function App() {

    const [loading, setLoading] =
        useState(false);

    const [report, setReport] =
        useState<AnalysisResponse | null>(null);

    async function analyze(url: string) {

        if (!url) return;

        setLoading(true);

        try {

            const response =
                await api.post(
                    "/analyze",
                    {
                        github_url: url,
                    }
                );

            setReport(response.data);

        } catch (err) {

            console.error(err);

            alert("Analysis failed.");

        } finally {

            setLoading(false);

        }

    }

    return (

        <div className="min-h-screen bg-slate-950 text-white">

            <LoadingOverlay
                visible={loading}
            />

            <div className="mx-auto max-w-7xl p-10">

                <Header />

                <SearchBar
                    loading={loading}
                    onAnalyze={analyze}
                />

                {report && (

                    <div className="mt-10 space-y-8">

                        <RepositoryCard
                            repository={
                                report.analysis.repository
                            }
                        />

                        <RiskGauge
                            score={
                                report.analysis.risk.score
                            }
                            level={
                                report.analysis.risk.level
                            }
                        />

                        <div className="grid grid-cols-2 gap-6 md:grid-cols-4">

                            <StatsCard
                                title="Contracts"
                                value={
                                    report.analysis.summary.total_contracts
                                }
                            />

                            <StatsCard
                                title="Functions"
                                value={
                                    report.analysis.summary.total_functions
                                }
                            />

                            <StatsCard
                                title="External"
                                value={
                                    report.analysis.summary.total_external_functions
                                }
                            />

                            <StatsCard
                                title="Dangerous Ops"
                                value={
                                    report.analysis.summary.dangerous_operations
                                }
                            />

                        </div>

                        <ReportCard
                            title="Executive Summary"
                        >

                            <p className="leading-8 text-slate-300">

                                {
                                    report.ai_report.executive_summary
                                }

                            </p>

                        </ReportCard>

                        <ReportCard
                            title="Priority Review Areas"
                        >

                            <ul className="space-y-3">

                                {report.ai_report.priority_review_areas.map(
                                    (
                                        item,
                                        index
                                    ) => (

                                        <li
                                            key={index}
                                        >
                                            ✅ {item}
                                        </li>

                                    )
                                )}

                            </ul>

                        </ReportCard>

                        <ReportCard
                            title="Recommended Next Steps"
                        >

                            <ul className="space-y-3">

                                {report.ai_report.recommended_next_steps.map(
                                    (
                                        item,
                                        index
                                    ) => (

                                        <li
                                            key={index}
                                        >
                                            🚀 {item}
                                        </li>

                                    )
                                )}

                            </ul>

                        </ReportCard>

                    </div>

                )}

            </div>

        </div>

    );

}

export default App;