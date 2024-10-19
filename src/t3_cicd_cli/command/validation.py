"""
Class for Configuration Validation Commands
"""

import click
import requests
from t3_cicd_cli.constant.api import LOCAL_ENDPOINT, VALIDATE_URI
from t3_cicd_cli.constant.default import DEFAULT_CONFIG_PATH


@click.command(name="validate")
@click.option(
    "--config",
    type=str,
    required=False,
    help="The path to the configuration file you want to validate. "
    + "if not provided, the path will be defaulted to that specified "
    + "in the CLI config file.",
)
def validate(config: str):
    # Use default config path if none is provided
    config_path = config if config else DEFAULT_CONFIG_PATH
    validate_url = f"{LOCAL_ENDPOINT}{VALIDATE_URI}"

    try:
        with open(config_path, "rb") as file:
            files = {"file": (config_path, file)}
            response = requests.post(validate_url, files=files)

        if response.status_code == 200:
            click.echo("The Config File is successfully validated.")
        else:
            click.echo(
                f"{response.status_code} {response.text} " + "Validation failed."
            )

    except FileNotFoundError:
        click.echo(f"Error: The file '{config_path}' was not found.")
    except requests.exceptions.RequestException as e:
        click.echo(f"Error: An error occurred during the request - {e}")
