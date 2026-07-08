type Props = {
    title: string;
    value: string | number;
};

export default function StatsCard({
    title,
    value,
}: Props) {
    return (
        <div className="rounded-xl bg-slate-900 p-6 shadow-lg">
            <p className="text-sm text-slate-400">
                {title}
            </p>

            <h2 className="mt-2 text-3xl font-bold text-white">
                {value}
            </h2>
        </div>
    );
}