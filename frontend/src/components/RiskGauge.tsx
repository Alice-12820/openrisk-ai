type Props = {
    score: number;
    level: string;
};

export default function RiskGauge({
    score,
    level,
}: Props) {

    let color = "text-green-400";

    if (level === "Medium")
        color = "text-yellow-400";

    if (level === "High")
        color = "text-orange-400";

    if (level === "Critical")
        color = "text-red-500";

    return (
        <div className="rounded-xl bg-slate-900 p-8 shadow-lg text-center">

            <p className="text-slate-400">
                Risk Score
            </p>

            <h1 className={`mt-4 text-6xl font-bold ${color}`}>
                {score}
            </h1>

            <p className={`mt-2 text-2xl font-semibold ${color}`}>
                {level}
            </p>

        </div>
    );
}