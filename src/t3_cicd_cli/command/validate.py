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
from t3_cicd_cli.utils.path import absolute_path_to_relative


@click.command(name="validate")
@click.option(
    "--file",
    type=str,
    required=False,
    help="Absolute path to the configuration file you want to validate. "
    + "if not provided, the path will be defaulted to {DEFAULT_CONFIG_PATH}",
)
def validate(file: str):
    config_path = DEFAULT_CONFIG_PATH

    if configuration.is_repo_remote:
        repo_url = configuration.repo
        branch = configuration.branch
        if file:
            if configuration.is_repo_remote:
                is_file_exist = check_file_exists(repo_url, branch, file)
                if not is_file_exist:
                    click.echo(
                        f"Error: Cannot verify file {file} in given repo {repo_url}."
                    )
                    return
                config_path = absolute_path_to_relative(file, configuration.repo)
    else:  # upload to our Git cicd-localrepo
        if file:
            if not os.path.exists(file):
                click.echo(
                    f"Error: The file '{file}' does not exist in the local file system. Please check again."
                )
                return
            if not file.startswith(configuration.repo):
                click.echo(
                    f"Error: Project root name '{configuration.repo}' not found in the file path {file}. Please check again."
                )
                return
            config_path = absolute_path_to_relative(file, configuration.repo)
        if not os.path.exists(configuration.repo):
            click.echo(
                "Error: The path of the repo does not exist in the local file system. Please check again."
            )
            return
        repo_url = DEFAULT_GITHUB_URL
        branch = push(configuration.repo)

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
