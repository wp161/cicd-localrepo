from click.testing import CliRunner
from t3_cicd_cli.command.configuration import config


class TestConfigurationCommands:

    def test_show_default(self):
        runner = CliRunner()
        result = runner.invoke(config, ["show"])
        assert result.exit_code == 0
        assert "Displaying current configuration" in result.output
        assert "is-repo-remote: False" in result.output
        assert "is-config-remote: False" in result.output
        assert "is-run-remote: False" in result.output
        assert "repo: None" in result.output
        assert "config: None" in result.output
        assert "server: None" in result.output
        assert "format: plain" in result.output

    def test_set_all_options(self):
        runner = CliRunner()
        result = runner.invoke(
            config,
            [
                "set",
                "--is-repo-remote",
                "True",
                "--is-config-remote",
                "True",
                "--is-run-remote",
                "True",
                "--repo",
                "https://example.com/repo.git",
                "--config",
                "https://example.com/config.yaml",
                "--server",
                "https://example.com/server",
                "--format",
                "json",
            ],
        )
        assert result.exit_code == 0
        assert "Settings updated." in result.output
        assert "is-repo-remote: True" in result.output
        assert "is-config-remote: True" in result.output
        assert "is-run-remote: True" in result.output
        assert "repo: https://example.com/repo.git" in result.output
        assert "config: https://example.com/config.yaml" in result.output
        assert "server: https://example.com/server" in result.output
        assert "format: json" in result.output

    def test_set_partial_options(self):
        runner = CliRunner()
        runner.invoke(config, ["reset"])
        result = runner.invoke(
            config,
            [
                "set",
                "--repo",
                "https://example.com/repo.git",
                "--server",
                "https://example.com/server",
            ],
        )
        assert result.exit_code == 0
        assert "Settings updated." in result.output
        assert "repo: https://example.com/repo.git" in result.output
        assert "server: https://example.com/server" in result.output
        assert "is-repo-remote: False" in result.output
        assert "is-config-remote: False" in result.output
        assert "is-run-remote: False" in result.output
        assert "format: plain" in result.output

    def test_reset(self):
        # First set some values to non-default
        runner = CliRunner()
        result = runner.invoke(
            config,
            [
                "set",
                "--is-repo-remote",
                "True",
                "--is-config-remote",
                "True",
                "--is-run-remote",
                "True",
                "--repo",
                "https://example.com/repo.git",
                "--config",
                "https://example.com/config.yaml",
                "--server",
                "https://example.com/server",
                "--format",
                "json",
            ],
        )
        assert result.exit_code == 0  # Ensure the settings were updated

        # Now reset the configuration
        result = runner.invoke(config, ["reset"])
        assert result.exit_code == 0
        assert "Configuration has been reset to default." in result.output
        assert "is-repo-remote: False" in result.output
        assert "is-config-remote: False" in result.output
        assert "is-run-remote: False" in result.output
        assert "repo: None" in result.output
        assert "config: None" in result.output
        assert "server: None" in result.output
        assert "format: plain" in result.output
