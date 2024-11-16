import os

def absolute_to_relative(abs_path, project_dir):
    """
    Converts an absolute path to a relative path within the specified project directory.

    Parameters:
    - abs_path (str): The absolute path to the file or directory (e.g., "/Users/Wenbo/Desktop/project_dir/file.txt").
    - project_dir (str): The name of the project root directory (e.g., "project_dir").

    Returns:
    - str: The relative path from the project root to the specified file or directory
           (e.g., "file.txt").
    """
    root_index = abs_path.find(project_dir)
    project_root_path = abs_path[: root_index + len(project_dir)]
    relative_path = os.path.relpath(abs_path, start=project_root_path)
    return relative_path
