import git
from git import Repo
from t3_cicd_cli.constant.default import (
    DEFAULT_GITHUB_URL,
    DEFAULT_GITHUB_REMOTE_NAME,
    MAX_UNSIGNED_64_BIT_INT,
)
import requests
import time


def is_git_repo(path):
    """
    Check if the given path is a valid Git repository.
    """
    try:
        Repo(path)
        return True
    except git.exc.InvalidGitRepositoryError:
        return False


def is_repo_dirty(path):
    """
    Check if the repository has uncommitted changes or untracked files.
    """
    repo = Repo(path)
    dirty = repo.is_dirty(untracked_files=True)

    if dirty:
        print(
            "You have the following uncommitted changes. Please commit them before proceeding."
        )
        print("Changes not staged for commit: ")
        for diff in repo.index.diff(None):
            print(f"      Modified:     {diff.a_path}")
        print("\nChanges staged for commit:")
        for diff in repo.index.diff("HEAD"):
            print(f"      Staged:       {diff.a_path}")
        if repo.untracked_files:
            print("\nUntracked files:")
            for untracked in repo.untracked_files:
                print(f"      Untracked:    {untracked}")
        return True
    return False


def setup_repo(path):
    """
    Ensure that the given folder is a Git repository.
    If it's not, initialize a new Git repository.
    """
    if not is_git_repo(path):
        repo = Repo.init(path)
    else:
        repo = Repo(path)
    return repo


def setup_remote(repo, remote_name, remote_url):
    """
    Ensure that the specified remote exists in the repository.
    If it doesn't, add the remote.
    """
    for remote in repo.remotes:
        if remote.name == remote_name:
            return remote
    return repo.create_remote(remote_name, remote_url)


def set_up_branch(repo, branch_name):
    """
    Ensure that the specified branch exists in the repository.
    If it doesn't, create the branch.
    """
    if branch_name in repo.branches:
        return repo.branches[branch_name]
    else:
        return repo.create_head(branch_name)


def push(path):
    """
    Push the current state of the repository to the remote on a newly created branch.
    """
    branch_name = str(hash(path + str(time.time())) & MAX_UNSIGNED_64_BIT_INT)
    repo = setup_repo(path)
    remote = setup_remote(repo, DEFAULT_GITHUB_REMOTE_NAME, DEFAULT_GITHUB_URL)
    branch = repo.create_head(branch_name)
    repo.git.checkout(branch)
    remote.push(refspec=f"{branch_name}:{branch_name}")
    return branch_name


def check_file_exists(git_url, branch, file_path):
    """
    Checks if a file exists in a GitHub repository.

    Parameters:
    - git_url (str): The Git repository URL.
    - branch (str): The branch name (e.g., 'main', 'master').
    - file_path (str): The relative path to the file in the repository.

    Returns:
    - bool: True if the file exists, False otherwise.
    """
    parts = git_url.rstrip("/").replace(".git", "").split("/")
    owner, repo = parts[-2], parts[-1]

    api_url = (
        f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}?ref={branch}"
    )

    response = requests.get(api_url)

    if response.status_code == 200:
        return True
    else:
        return False


def is_github_repo(url):
    """
    Checks if a given GitHub URL is a valid public repository using the GitHub API.

    Parameters:
    - url (str): The URL of the GitHub repository.

    Returns:
    - bool: True if the URL is a valid GitHub repository, False otherwise.
    """
    if not url.startswith("https://github.com/"):
        return False

    try:
        parts = url.replace("https://github.com/", "").rstrip("/").split("/")
        if len(parts) < 2:
            return False
        owner, repo = parts[:2]
        repo = repo.replace(".git", "")
        api_url = f"https://api.github.com/repos/{owner}/{repo}"
        response = requests.get(api_url, timeout=10)
        return response.status_code == 200

    except requests.RequestException:
        return False
