"""
CLI program using Click to greet a user by name.
"""

import click
from t3_cicd_cli.pipeline_commands import run
from t3_cicd_cli.configuration_commands import config as config_group
from t3_cicd_cli.job_commands import rerun, stop
from t3_cicd_cli.log_commands import log
from t3_cicd_cli.info_commands import info


@click.group()
def cli():
    """Main entry point for the cicd CLI."""
    pass


cli.add_command(run)
cli.add_command(config_group)
cli.add_command(rerun)
cli.add_command(stop)
cli.add_command(log)
cli.add_command(info)


if __name__ == "__main__":
    cli()
