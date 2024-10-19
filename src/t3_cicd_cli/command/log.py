"""
Class for Log Commands
"""

import click


@click.command(name="log")
@click.option(
    "--pipeline",
    type=str,
    help="The pipeline name to query the logs for.",
)
@click.option(
    "--stage",
    type=str,
    help="The stage name to query the logs for.",
)
@click.option("--job", type=str, help="The job name to query the logs for.")
def log(pipeline: str, stage: str, job: str):
    """
    Shows the logs for completed stages or jobs
    """
    if pipeline and stage and job:
        click.echo(
            f"Shows logs for job {job} in " + f"pipeline {pipeline}, stage {stage}."
        )
    if pipeline and stage:
        click.echo(
            "Shows all logs for the jobs in " + f"pipeline {pipeline}, stage {stage}."
        )
    if pipeline:
        click.echo(
            "Shows all logs for the jobs and stages in " + f"pipeline {pipeline}."
        )
    if not pipeline and not stage and not job:
        click.echo("Shows all logs for every pipeline")
