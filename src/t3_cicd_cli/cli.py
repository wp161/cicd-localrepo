"""
CLI program using Click to greet a user by name.
"""

import click
from t3_cicd_cli.configuration import config as config_group


@click.group()
def cli():
    """Main entry point for the cicd CLI."""
    pass


cli.add_command(config_group)


@cli.command()
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
def run(dry_run, override):
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
    else:
        click.echo("Dry run complete. No jobs were executed.")


if __name__ == "__main__":
    cli()
