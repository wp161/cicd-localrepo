"""
Class for Configuration Commands
"""
import click


class ConfigurationCommands:

    def __init__(self):
        self.is_repo_remote = False
        self.is_config_remote = False
        self.is_run_remote = False
        self.repo = None
        self.config = None
        self.server = None
        self.format = "plain"

    def display(self):
        """Helper method that displays the current CLI configuration"""
        click.echo("Displaying current configuration")
        click.echo(f"is-repo-remote: {self.is_repo_remote}")
        click.echo(f"is-config-remote: {self.is_config_remote}")
        click.echo(f"is-run-remote: {self.is_run_remote}")
        click.echo(f"repo: {self.repo}")
        click.echo(f"config: {self.config}")
        click.echo(f"server: {self.server}")
        click.echo(f"format: {self.format}")

    def update(
        self,
        is_repo_remote: bool,
        is_config_remote: bool,
        is_run_remote: bool,
        repo: str,
        config: str,
        server: str,
        format: str,
    ):
        """
        Helper method to update configuration variables and display the updated
        configuration
        """
        if is_repo_remote is not None:
            self.is_repo_remote = is_repo_remote
        if is_config_remote is not None:
            self.is_config_remote = is_config_remote
        if is_run_remote is not None:
            self.is_run_remote = is_run_remote
        if repo is not None:
            if repo == "reset":
                self.repo = None
            else:
                self.repo = repo
        if config is not None:
            if config == "reset":
                self.config = None
            else:
                self.config = config
        if server is not None:
            if server == "reset":
                self.server = None
            else:
                self.server = server
        if format is not None:
            self.format = format
        click.echo("Settings updated.")
        configuration.display()


configuration = ConfigurationCommands()


@click.group()
def config():
    """Manage the configuration settings."""
    pass


@config.command(name="show")
def show():
    """The show command will display the current CLI configuration"""
    configuration.display()


@config.command(name="set")
@click.option(
    "--is-repo-remote",
    type=bool,
    default=None,
    help="If the repo is a remote repo, set as True else False",
)
@click.option(
    "--is-config-remote",
    type=bool,
    default=None,
    help="If the config is a remote config, set as True else False",
)
@click.option(
    "--is-run-remote",
    type=bool,
    default=None,
    help="If the run is a remote run, set as True else False",
)
@click.option(
    "--repo",
    default=None,
    help="URL or path to repo, " +
    "set as null if using default",
)
@click.option(
    "--config",
    default=None,
    help="URL or path to config file, set as null if using default",
)
@click.option(
    "--server",
    default=None,
    help="Endpoint for the remote server if is-run-remote is True, " +
    "else set to null as default",
)
@click.option(
    "--format", default=None, help="Output format can be in plain, " +
    "json, or yaml"
)
def set(
    is_repo_remote: bool,
    is_config_remote: bool,
    is_run_remote: bool,
    repo: str,
    config: str,
    server: str,
    format: str,
):
    """
    The user can change the settings and once the command runs, it will
    display the updated configuration
    """
    configuration.update(
        is_repo_remote, is_config_remote, is_run_remote, repo,
        config, server, format
    )


@config.command(name="reset")
def reset():
    """
    The user can change the settings back to its default configuration and
    will display the updated configuration
    """
    click.echo("Configuration has been reset to default.")
    configuration.update(False, False, False, "reset", "reset", "reset",
                         "plain")
