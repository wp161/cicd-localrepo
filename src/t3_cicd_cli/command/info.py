"""
Class for Environment Info Commands
"""

import click


@click.command(name="info")
@click.option(
    "--stage",
    type=str,
    help="Specify the stage you want to view the env info for.",
)
@click.option(
    "--job",
    type=str,
    help="Specify the job you want to view the env info for.",
)
@click.pass_context
def info(context, stage: str, job: str):
    """
    Shows the environment info for a stage or job
    """
    if stage and job:
        raise click.BadParameter("Specify either --job " + "or --stage, but not both.")
    if not stage and not job:
        raise click.BadParameter("Either --job or --stage is required.")

    if stage:
        click.echo(f"Environment info of stage {stage}.")
    if job:
        click.echo(f"Environment info of job {job}.")
