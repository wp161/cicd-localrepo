"""
Class for Pipeline Commands
"""

import click
import os
import requests
from t3_cicd_cli.command.config import configuration
from t3_cicd_cli.utils.api import assemble_request
from t3_cicd_cli.utils.git_operations import is_git_repo, is_repo_dirty, push
from t3_cicd_cli.constant.default import DEFAULT_GITHUB_URL
from t3_cicd_cli.constant.api import LOCAL_ENDPOINT, RUN_URI


@click.command()
@click.option(
    "--commit",
    type=str,
    required=False,
    help="Optional commit hash of the remote repo to use to run the pipeline.",
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Run the pipeline without executing any jobs (simulation).",
)
@click.option(
    "--override",
    type=str,
    help="Override configuration values. Format: key=value.",
)
def run(commit, dry_run, override):
    """
    Run the pipeline. Optionally perform a dry run or override
    configuration values.
    """
    if not dry_run:
        click.echo("Executing the pipeline...")
        if not configuration.repo:
            click.echo(
                "Error: The path/URL of the repo cannot be null. Please configure it with cicd config --set."
            )
            return

        if configuration.is_repo_remote:  # use user's Git repo
            repo_url = configuration.repo
            branch = configuration.branch
        else:  # upload to our Git cicd-localrepo, user needs to commit any change first
            if not os.path.exists(configuration.repo):
                click.echo(
                    "Error: The path of the repo does not exist in the local file system. Please check again."
                )
                return
            elif is_git_repo(configuration.repo):
                if is_repo_dirty(configuration.repo):
                    return
            repo_url = DEFAULT_GITHUB_URL
            branch = push(configuration.repo)
        if override:
            overrides = dict(item.split("=") for item in override.split(","))
        else:
            overrides = {}
        endpoint = f"{LOCAL_ENDPOINT}{RUN_URI}"
        param = assemble_request(
            repo_url=repo_url,
            branch=branch,
            commit=commit,
            override=overrides,
        )

        try:
            response = requests.post(endpoint, json=param)
            if response.status_code == 200:
                click.echo("The Pipeline is successfully started.")
            else:
                click.echo(
                    f"{response.status_code} {response.text} " + "Validation failed."
                )

        except requests.exceptions.RequestException as e:
            click.echo(f"Error: An error occurred during the request - {e}")

    else:
        click.echo("Performing a dry run of the pipeline...")
        click.echo("Dry run complete. No jobs were executed.")
