import { useState } from "react";

import Header from "./components/Header";
import SearchBar from "./components/SearchBar";

import api from "./services/api";

import type { AnalysisResponse } from "./types/report";

function App() {

    const [loading, setLoading] = useState(false);

    const [report, setReport] =
        useState<AnalysisResponse | null>(null);

    async function analyze(url: string) {

        if (!url) return;

        setLoading(true);

        try {

            const response = await api.post(
                "/analyze",
                {
                    github_url: url,
                }
            );

            setReport(response.data);

        } catch (err) {

            console.error(err);

            alert("Analysis failed.");

        }

        setLoading(false);

    }

    return (

        <div className="min-h-screen bg-slate-950 text-white">

            <div className="mx-auto max-w-6xl p-10">

                <Header />

                <SearchBar
                    loading={loading}
                    onAnalyze={analyze}
                />

                {report && (

                    <pre className="mt-10 overflow-auto rounded-xl bg-slate-900 p-6">

                        {JSON.stringify(
                            report,
                            null,
                            2
                        )}

                    </pre>

                )}

            </div>

        </div>

    );

}

export default App;