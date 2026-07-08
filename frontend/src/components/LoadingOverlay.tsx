type Props = {
    visible: boolean;
};

export default function LoadingOverlay({
    visible,
}: Props) {

    if (!visible) return null;

    return (

        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm">

            <div className="w-[500px] rounded-2xl bg-slate-900 p-8 shadow-2xl border border-slate-700">

                <h2 className="text-3xl font-bold text-white">
                    OpenRisk AI
                </h2>

                <p className="mt-3 text-slate-300">
                    Analyzing Smart Contract Repository...
                </p>

                <div className="mt-8 h-3 overflow-hidden rounded-full bg-slate-800">

                    <div className="h-full w-full animate-pulse bg-blue-500"></div>

                </div>

                <div className="mt-8 space-y-2 text-slate-400">

                    <p>✓ Cloning repository</p>
                    <p>✓ Parsing Solidity contracts</p>
                    <p>✓ Calculating repository risk</p>
                    <p className="animate-pulse">
                        ⏳ Generating AI Security Report...
                    </p>

                </div>

            </div>

        </div>

    );

}