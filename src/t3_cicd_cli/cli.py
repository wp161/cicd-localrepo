"""
CLI program using Click to greet a user by name.
"""

import click


@click.command()
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(name):
    """Simple template that greets NAME."""
    click.echo(f"Hello, {name}!")


if __name__ == "__main__":
    hello()
