type Props = {
    title: string;
    children: React.ReactNode;
};

export default function ReportCard({
    title,
    children,
}: Props) {

    return (
        <div className="rounded-xl bg-slate-900 p-6 shadow-lg">

            <h2 className="mb-4 text-xl font-semibold">
                {title}
            </h2>

            {children}

        </div>
    );

}