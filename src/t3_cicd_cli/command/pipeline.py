"""
Class for Pipeline Commands
"""

import click
from t3_cicd_cli.command.configuration import configuration


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
    multiple=True,
    type=str,
    help="Override configuration values. Format: key=value.",
)
def run(dry_run, commit, override):
    """
    Run the pipeline. Optionally perform a dry run or override
    configuration values.
    """
    if dry_run:
        click.echo("Performing a dry run of the pipeline...")

    if override:
        overrides = dict(item.split("=") for item in override)
        click.echo(f"Overriding the following config values: {overrides}")

    # Simulate running the pipeline
    if not dry_run:
        click.echo("Executing the pipeline...")
        if configuration.is_config_remote:
            click.echo("Send git repo URL and branch name and optional commit hash")
        else:
            click.echo(
                "Upload the repo to localrepo, obtain git repo URL and branch name, and send"
            )

    else:
        click.echo("Dry run complete. No jobs were executed.")
