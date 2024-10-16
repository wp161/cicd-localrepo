"""
Class for Run Commands for Stages and Jobs
"""
import click


@click.command(name="rerun")
@click.option(
    "--job",
    type=str,
    required=True,
    help="The name of the job to rerun",
)
@click.option(
    "--override",
    multiple=True,
    default=None,
    help="Override configuration values. Format: key=value",
)
def rerun(job: str, override: str):
    """
    The rerun command will run the job with default
    or overriden configuration settings
    """
    if override:
        overrides = dict(item.split("=") for item in override)
        click.echo("Temporarily overriding the following config values: " +
                   f"{overrides}")
    click.echo(f"Rerunning job {job}")


@click.command(name="stop")
@click.option(
    "--stage",
    type=str,
    help="Specify the stage you want to stop.",
)
@click.option(
    "--job",
    type=str,
    help="Specific the name of the job you want to stop.",
)
@click.pass_context
def stop(context, stage: str, job: str):
    """
    The user can stop a stage or a job. If the stage or job cannot be
    stopped (e.g. the stage is completed, the job does not exist),
    return an error message to the user.
    """
    if stage and job:
        raise click.BadParameter('Specify either --job ' +
                                 'or --stage, but not both.')
    if not stage and not job:
        raise click.BadParameter('Either --job or --stage is required.')

    if stage:
        click.echo(f"Stage {stage} has stopped.")
    elif job:
        click.echo(f"Job {job} has stopped.")
