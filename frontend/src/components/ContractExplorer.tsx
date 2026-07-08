import { useMemo, useState } from "react";

type Contract = {
    file: string;
    contracts: string[];
    functions: string[];
    external_functions: string[];
    privileged_functions: string[];
    dangerous_operations: string[];
};

type Props = {
    contracts: Contract[];
};

export default function ContractExplorer({
    contracts,
}: Props) {

    const [search, setSearch] = useState("");

    const filtered = useMemo(() => {

        return contracts.filter((contract) =>
            contract.file
                .toLowerCase()
                .includes(search.toLowerCase())
        );

    }, [contracts, search]);

    return (

        <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6">

            <h2 className="mb-6 text-2xl font-bold">
                Contract Explorer
            </h2>

            <input
                className="mb-6 w-full rounded-lg border border-slate-700 bg-slate-800 p-3 text-white"
                placeholder="Search contract..."
                value={search}
                onChange={(e) =>
                    setSearch(e.target.value)
                }
            />

            <div className="space-y-4">

                {filtered.map((contract, index) => (

                    <details
                        key={index}
                        className="rounded-xl bg-slate-800 p-4"
                    >

                        <summary className="cursor-pointer text-lg font-semibold">

                            {contract.file}

                        </summary>

                        <div className="mt-4 space-y-2 text-slate-300">

                            <p>
                                <strong>Contracts:</strong>{" "}
                                {contract.contracts.join(", ")}
                            </p>

                            <p>
                                <strong>Functions:</strong>{" "}
                                {contract.functions.length}
                            </p>

                            <p>
                                <strong>External:</strong>{" "}
                                {contract.external_functions.length}
                            </p>

                            <p>
                                <strong>Privileged:</strong>{" "}
                                {contract.privileged_functions.length}
                            </p>

                            <p>
                                <strong>Dangerous Operations:</strong>{" "}
                                {contract.dangerous_operations.length}
                            </p>

                        </div>

                    </details>

                ))}

            </div>

        </div>

    );

}