import {
    CircularProgressbar,
    buildStyles,
} from "react-circular-progressbar";

import "react-circular-progressbar/dist/styles.css";

type Props = {
    score: number;
    level: string;
};

export default function RiskGauge({
    score,
    level,
}: Props) {

    const color =
        level === "Critical"
            ? "#ef4444"
            : level === "High"
            ? "#f97316"
            : level === "Medium"
            ? "#eab308"
            : "#22c55e";

    return (

        <div className="rounded-2xl border border-slate-800 bg-slate-900 p-8 shadow-xl">

            <h2 className="mb-8 text-2xl font-bold">

                Overall Repository Risk

            </h2>

            <div className="mx-auto h-64 w-64">

                <CircularProgressbar
                    value={score}
                    maxValue={1000}
                    text={`${score}`}
                    styles={buildStyles({
                        pathColor: color,
                        textColor: "#ffffff",
                        trailColor: "#1e293b",
                    })}
                />

            </div>

            <h3
                className="mt-8 text-center text-3xl font-bold"
                style={{
                    color,
                }}
            >
                {level}
            </h3>

        </div>

    );

}