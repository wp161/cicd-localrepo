# tests/test_cli.py

from click.testing import CliRunner
from t3_cicd_cli.cli import hello


def test_hello():
    runner = CliRunner()
    result = runner.invoke(hello, ["--name", "World"])
    assert result.exit_code == 0
    assert "Hello, World!" in result.output
