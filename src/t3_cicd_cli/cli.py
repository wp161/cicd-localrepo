"""
CLI program using Click to greet a user by name.
"""

import click
import importlib
import pkgutil
from t3_cicd_cli import command


@click.group()
def cli():
    """Main entry point for the cicd CLI."""
    pass


# Dynamically import all modules from the command folder
for module_info in pkgutil.iter_modules(command.__path__):
    module = importlib.import_module(f't3_cicd_cli.command.{module_info.name}')

    for attr_name in dir(module):
        attr = getattr(module, attr_name)
        if isinstance(attr, click.Command):
            cli.add_command(attr)
if __name__ == "__main__":
    cli()
