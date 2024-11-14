"""
Class for Configuration Commands
"""

import click
from t3_cicd_cli.constant.default import (
    DEFAULT_BRANCH_NAME,
    DEFAULT_CLI_CONFIG_PATH,
    DEFAULT_NULL_INPUTS,
    DEFAULT_FORMAT,
    DEFAULT_FORMATS,
)
from t3_cicd_cli.constant.cli_config import (
    CLI_CONFIG_KEY_IS_REPO_REMOTE,
    CLI_CONFIG_KEY_IS_RUN_REMOTE,
    CLI_CONFIG_KEY_REPO,
    CLI_CONFIG_KEY_BRANCH,
    CLI_CONFIG_KEY_SERVER,
    CLI_CONFIG_KEY_FORMAT,
)
import os
import json

config_file_path = os.path.expanduser(DEFAULT_CLI_CONFIG_PATH)


class ConfigurationCommands:

    def __init__(self):
        self.set_default_values()
        self.load()

    def set_default_values(self):
        """Set all configurations to default values"""
        self.is_repo_remote = False
        self.is_run_remote = False
        self.repo = None
        self.branch = DEFAULT_BRANCH_NAME
        self.server = None
        self.format = DEFAULT_FORMAT

    def get_option(self, key):
        """Get the name of CLI option, e.g. --repo"""
        return "--" + key

    def load(self):
        """Load configuration from a JSON file"""
        if os.path.exists(config_file_path):
            with open(config_file_path, "r") as config_file:
                config_data = json.load(config_file)
                self.is_repo_remote = config_data.get(
                    CLI_CONFIG_KEY_IS_REPO_REMOTE, False
                )
                self.is_run_remote = config_data.get(
                    CLI_CONFIG_KEY_IS_RUN_REMOTE, False
                )
                self.repo = config_data.get(CLI_CONFIG_KEY_REPO, None)
                self.branch = config_data.get(
                    CLI_CONFIG_KEY_BRANCH, DEFAULT_BRANCH_NAME
                )
                self.server = config_data.get(CLI_CONFIG_KEY_SERVER, None)
                self.format = config_data.get(CLI_CONFIG_KEY_FORMAT, DEFAULT_FORMAT)
        else:
            self.save()

    def save(self):
        """Save configuration to a JSON file"""
        config_data = {
            CLI_CONFIG_KEY_IS_REPO_REMOTE: self.is_repo_remote,
            CLI_CONFIG_KEY_IS_RUN_REMOTE: self.is_run_remote,
            CLI_CONFIG_KEY_REPO: self.repo,
            CLI_CONFIG_KEY_BRANCH: self.branch,
            CLI_CONFIG_KEY_SERVER: self.server,
            CLI_CONFIG_KEY_FORMAT: self.format,
        }
        with open(config_file_path, "w") as config_file:
            json.dump(config_data, config_file, indent=4)

    def display(self):
        """Helper method that displays the current CLI configuration"""
        click.echo("====Displaying current configuration====\n")
        click.echo(f"{CLI_CONFIG_KEY_IS_REPO_REMOTE}: {self.is_repo_remote}")
        click.echo(f"{CLI_CONFIG_KEY_IS_RUN_REMOTE}: {self.is_run_remote}")
        click.echo(f"{CLI_CONFIG_KEY_REPO}: {self.repo}")
        click.echo(f"{CLI_CONFIG_KEY_BRANCH}: {self.branch}")
        click.echo(f"{CLI_CONFIG_KEY_SERVER}: {self.server}")
        click.echo(f"{CLI_CONFIG_KEY_FORMAT}: {self.format}")

    def update(
        self,
        is_repo_remote: bool,
        is_run_remote: bool,
        repo: str,
        branch: str,
        server: str,
        format: str,
    ):
        """
        Helper method to update configuration variables and display the updated
        configuration
        """
        if is_repo_remote is not None:
            self.is_repo_remote = is_repo_remote
        if is_run_remote is not None:
            self.is_run_remote = is_run_remote
        if repo is not None and repo not in DEFAULT_NULL_INPUTS:
            self.repo = repo
        if branch is not None and branch not in DEFAULT_NULL_INPUTS:
            self.branch = branch
        if server is not None and server not in DEFAULT_NULL_INPUTS:
            self.server = server
        if format is not None and format not in DEFAULT_NULL_INPUTS:
            if format.lower() not in DEFAULT_FORMATS:
                click.echo("Format has to be plain/ json/ yaml.")
                return
            self.format = format
        self.save()
        click.echo("Settings updated.")
        self.display()


configuration = ConfigurationCommands()


@click.group()
def config():
    """Manage CLI configurations"""
    pass


@config.command(name="show")
def show():
    """Display the current CLI configurations."""
    configuration.load()
    configuration.display()


@config.command(name="set")
@click.option(
    configuration.get_option(CLI_CONFIG_KEY_IS_REPO_REMOTE),
    type=bool,
    default=None,
    help="If the repo is a remote repo, default is False",
)
@click.option(
    configuration.get_option(CLI_CONFIG_KEY_IS_RUN_REMOTE),
    type=bool,
    default=None,
    help="If the run is a remote run, default is False",
)
@click.option(
    configuration.get_option(CLI_CONFIG_KEY_REPO),
    default=None,
    help=f"Git URL (if {CLI_CONFIG_KEY_IS_REPO_REMOTE} is true) or absolute path \
    (if {CLI_CONFIG_KEY_IS_REPO_REMOTE} is false) of the repo, " + "default is null",
)
@click.option(
    configuration.get_option(CLI_CONFIG_KEY_BRANCH),
    default=None,
    help="Branch of the remote repo, default is main",
)
@click.option(
    configuration.get_option(CLI_CONFIG_KEY_SERVER),
    default=None,
    help="Endpoint for the remote server, " + "default is null",
)
@click.option(
    configuration.get_option(CLI_CONFIG_KEY_FORMAT),
    default=DEFAULT_FORMAT,
    help="Output format can be in plain, " + "json, or yaml, default is plain",
)
def set(
    is_repo_remote: bool,
    is_run_remote: bool,
    repo: str,
    branch: str,
    server: str,
    format: str,
):
    """
    Update CLI configurations and display new values after the update.
    """
    configuration.update(
        is_repo_remote,
        is_run_remote,
        repo,
        branch,
        server,
        format,
    )


@config.command(name="reset")
def reset():
    """
    Reset all CLI configuration to default values.
    """
    configuration.set_default_values()
    configuration.save()
    click.echo("Configuration has been reset to default.")
    configuration.display()
