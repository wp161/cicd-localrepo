# tests/test_cli.py

from click.testing import CliRunner
from t3_cicd_cli.cli import cli


class TestPipelineCommands:

    def test_run_dry_run(self):
        """Test the 'run' command with the --dry-run option."""
        runner = CliRunner()
        result = runner.invoke(cli, ["run", "--dry-run"])
        assert result.exit_code == 0
        assert "Performing a dry run of the pipeline..." in result.output
        assert "Dry run complete. No jobs were executed." in result.output

    def test_run_with_override(self):
        """Test the 'run' command with override options."""
        runner = CliRunner()
        result = runner.invoke(
            cli, ["run", "--override", "key1=value1", "--override", "key2=value2"]
        )
        assert result.exit_code == 0
        assert (
            "Overriding the following config values: {'key1': 'value1', "
            + "'key2': 'value2'}"
            in result.output
        )
        assert "Executing the pipeline..." in result.output

    def test_run_without_dry_run_or_override(self):
        """Test the 'run' command without --dry-run or --override options."""
        runner = CliRunner()
        result = runner.invoke(cli, ["run"])
        assert result.exit_code == 0
        assert "Executing the pipeline..." in result.output
