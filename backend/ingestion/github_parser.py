from git import Repo
import tempfile
import os


def clone_repository(repo_url):
    temp_dir = tempfile.mkdtemp()

    Repo.clone_from(
        repo_url, temp_dir
    )

    return temp_dir


def find_solidity_files(repo_path):
    files = []

    for root, dirs, filenames in os.walk(repo_path):
        for f in filenames:
            if f.endswith(".sol"):
                files.append(
                    os.path.join(root, f)
                )

    return files


if __name__ == "__main__":
    repo = clone_repository(
        "https://github.com/Uniswap/v4-core"
    )

    solidity_files = find_solidity_files(repo)

    print(
        f"Found {len(solidity_files)} Solidity files"
    )

    for f in solidity_files[:10]:
        print(f)