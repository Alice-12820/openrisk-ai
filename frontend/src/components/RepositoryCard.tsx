type Props = {
    repository: string;
};

export default function RepositoryCard({
    repository,
}: Props) {

    return (

        <div className="rounded-2xl bg-slate-900 border border-slate-800 p-6 shadow-lg">

            <h2 className="text-xl font-bold">

                Repository

            </h2>

            <p className="mt-3 break-all text-blue-400">

                {repository}

            </p>

        </div>

    );

}