import { useState } from "react";

type Props = {
    onAnalyze: (url: string) => void;
    loading: boolean;
};

export default function SearchBar({
    onAnalyze,
    loading,
}: Props) {

    const [url, setUrl] = useState("");

    return (

        <div className="bg-slate-900 rounded-xl p-6 shadow-lg">

            <label className="block mb-3 text-slate-300">

                GitHub Repository

            </label>

            <div className="flex gap-4">

                <input
                    className="flex-1 rounded-lg bg-slate-800 border border-slate-700 p-4 text-white"
                    placeholder="https://github.com/Uniswap/v4-core"
                    value={url}
                    onChange={(e) => setUrl(e.target.value)}
                />

                <button
                    onClick={() => onAnalyze(url)}
                    disabled={loading}
                    className="rounded-lg bg-blue-600 px-8 hover:bg-blue-500 disabled:opacity-50"
                >
                    {loading ? "Analyzing..." : "Analyze"}
                </button>

            </div>

        </div>

    );
}