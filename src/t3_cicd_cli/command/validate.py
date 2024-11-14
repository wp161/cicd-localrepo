"""
Class for Configuration Validation Commands
"""

import os
import click
import requests
from t3_cicd_cli.constant.api import LOCAL_ENDPOINT, VALIDATE_URI
from t3_cicd_cli.constant.default import DEFAULT_CONFIG_PATH, DEFAULT_GITHUB_URL
from t3_cicd_cli.command.config import configuration
from t3_cicd_cli.utils.api import assemble_request
from t3_cicd_cli.utils.git_operations import check_file_exists, push
from t3_cicd_cli.utils.path import absolute_to_relative, get_project_root


@click.command(name="validate")
@click.option(
    "--file",
    type=str,
    required=False,
    help="The path to the configuration file you want to validate. "
    + "if not provided, the path will be defaulted to that specified "
    + "in the CLI config file.",
)
def validate(file: str):
    config_path = DEFAULT_CONFIG_PATH

    if configuration.is_repo_remote:
        repo_url = configuration.repo
        branch = configuration.branch

    else:  # upload to our Git cicd-localrepo
        if not os.path.exists(configuration.repo):
            click.echo(
                "Error: The path of the repo does not exist in the local file system. Please check again."
            )
            return
        repo_url = DEFAULT_GITHUB_URL
        branch = push(configuration.repo)

    if file:
        if configuration.is_repo_remote:
            is_file_exist = check_file_exists(repo_url, branch, file)
            if not is_file_exist:
                click.echo(
                    f"Error: Cannot verify file {file} in given repo {repo_url}."
                )
                return
            config_path = file
        else:
            if not os.path.exists(file):
                click.echo(
                    f"Error: The file '{file}' does not exist in the local file system. Please check again."
                )
                return
            project_dir = get_project_root(repo_url)
            if file.find(project_dir) == -1:
                click.echo(
                    f"Error: Project root name '{project_dir}' not found in the file path {file}. Please check again."
                )
                return
            config_path = absolute_to_relative(file, project_dir)

    endpoint = f"{LOCAL_ENDPOINT}{VALIDATE_URI}"
    param = assemble_request(repo_url=repo_url, branch=branch, config_path=config_path)

    try:
        response = requests.post(endpoint, json=param)
        if response.status_code == 200:
            click.echo("The Config File is successfully validated.")
        else:
            click.echo(
                f"{response.status_code} {response.text} " + "Validation failed."
            )
    except requests.exceptions.RequestException as e:
        click.echo(f"Error: An error occurred during the request - {e}")
