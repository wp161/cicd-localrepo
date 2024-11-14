import os
import re


def absolute_path_to_relative(abs_path, repo):
    """
    Converts an absolute path to a relative path within the specified project directory or repository.

    Parameters:
    - abs_path (str): The absolute path to the file or directory.
                      Example: "/Users/JaneDoe/Desktop/project_dir/file.txt"
    - repo (str): The URL or local path of the project directory. This can be:
                  - A local directory path. Example: "/Users/JaneDoe/Desktop/project_dir"
                  - A Git URL. Example: "https://github.com/example.git"

    Returns:
    - str: The relative path from the project root to the specified file or directory.
           Example: "file.txt" if abs_path is inside the project root.

    Behavior:
    - If `repo` is a Git URL, the method extracts the repository name and calculates the relative path accordingly.
    - If `repo` is a local directory path, the method calculates the relative path using that directory as the root.

    Raises:
    - ValueError: If the `repo` is neither a valid URL nor a local path.
    """
    url_pattern = re.compile(
        r"^(https?://)?"  # Optional scheme (http or https)
        r"([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}"  # Domain name
        r"(:\d+)?"  # Optional port
        r"(/.*)?$",  # Optional path
        re.IGNORECASE,
    )

    if re.match(url_pattern, repo):
        repo_name = repo.rstrip("/").split("/")[-1].replace(".git", "")
        root_index = abs_path.find(repo_name)
        project_root_path = abs_path[: root_index + len(repo_name)]
        relative_path = os.path.relpath(abs_path, start=project_root_path)
        return relative_path
    else:
        return os.path.relpath(abs_path, start=repo)
