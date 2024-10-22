from click.testing import CliRunner
from t3_cicd_cli.command.configuration import config, ConfigurationCommands
from unittest.mock import patch, mock_open

mock_config_data = """
{
  "is-repo-remote": false,
  "is-config-remote": false,
  "is-run-remote": false,
  "repo": null,
  "remote-branch": "main",
  "config": null,
  "server": null,
  "format": "plain"
}
"""

MOCK_CONFIG_FILE_PATH = "/mock/path/config.json"


class TestConfigurationCommands:
    @patch(
        "t3_cicd_cli.constant.default.DEFAULT_CLI_CONFIG_PATH", "/mock/path/config.json"
    )
    @patch("builtins.open", new_callable=mock_open, read_data=mock_config_data)
    def test_show_default(self, mock_file):
        runner = CliRunner()
        result = runner.invoke(config, ["reset"])
        result = runner.invoke(config, ["show"])
        assert result.exit_code == 0
        assert "Displaying current configuration" in result.output
        assert "is-repo-remote: False" in result.output
        assert "is-config-remote: False" in result.output
        assert "is-run-remote: False" in result.output
        assert "repo: None" in result.output
        assert "remote-branch: main" in result.output
        assert "config: None" in result.output
        assert "server: None" in result.output
        assert "format: plain" in result.output

    @patch(
        "t3_cicd_cli.constant.default.DEFAULT_CLI_CONFIG_PATH", "/mock/path/config.json"
    )
    @patch("builtins.open", new_callable=mock_open, read_data=mock_config_data)
    def test_set_all_options(self, mock_file):
        runner = CliRunner()
        result = runner.invoke(config, ["reset"])
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
                "--remote-branch",
                "example-branch",
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
        assert "remote-branch: example-branch" in result.output
        assert "config: https://example.com/config.yaml" in result.output
        assert "server: https://example.com/server" in result.output
        assert "format: json" in result.output

        runner = CliRunner()
        result = runner.invoke(config, ["reset"])
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
        assert "remote-branch: main" in result.output
        assert "is-config-remote: False" in result.output
        assert "is-run-remote: False" in result.output
        assert "format: plain" in result.output

        runner = CliRunner()
        result = runner.invoke(config, ["reset"])
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
                "--remote-branch",
                "example-branch",
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
        assert "remote-branch: main" in result.output
        assert "config: None" in result.output
        assert "server: None" in result.output
        assert "format: plain" in result.output

    @patch(
        "t3_cicd_cli.constant.default.DEFAULT_CLI_CONFIG_PATH", "/mock/path/config.json"
    )
    @patch("builtins.open", new_callable=mock_open, read_data=mock_config_data)
    def test_set_null_values(self, mock_file):
        """Test setting values to null and coverage for line 89"""
        runner = CliRunner()
        result = runner.invoke(config, ["reset"])

        result = runner.invoke(
            config,
            [
                "set",
                "--remote-branch",
                "none",
                "--config",
                "none",
                "--server",
                "none",
            ],
        )
        assert result.exit_code == 0
        assert "Settings updated." in result.output
        assert "remote-branch: main" in result.output
        assert "config: None" in result.output
        assert "server: None" in result.output

    @patch(
        "t3_cicd_cli.constant.default.DEFAULT_CLI_CONFIG_PATH", MOCK_CONFIG_FILE_PATH
    )
    @patch(
        "builtins.open", new_callable=mock_open, read_data='{"is-repo-remote": false}'
    )
    def test_invalid_format(self, mock_file):
        """Test that an invalid format results in an error message"""
        configuration = ConfigurationCommands()
        runner = CliRunner()
        result = runner.invoke(config, ["set", "--format", "invalidFormat"])
        assert result.exit_code == 0
        assert "Format has to be plain/ json/ yaml." in result.output
        assert configuration.format == "plain"
