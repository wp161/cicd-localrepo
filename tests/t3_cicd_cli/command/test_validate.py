from click.testing import CliRunner
from unittest.mock import patch, MagicMock
from t3_cicd_cli.command.validate import validate
from t3_cicd_cli.constant.default import DEFAULT_CONFIG_PATH


class TestValidateCommand:
    @patch("t3_cicd_cli.command.validate.configuration")
    @patch("t3_cicd_cli.command.validate.requests.post")
    def test_validate_good_config(self, mock_post, mock_config):
        mock_config.is_repo_remote = True
        mock_config.repo = "https://github.com/example/repo.git"
        mock_config.remote_branch = "main"
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "Success"
        mock_post.return_value = mock_response
        runner = CliRunner()
        result = runner.invoke(
            validate, ["--file", "tests/t3_cicd_cli/test_files/good_config.yaml"]
        )
        assert result.exit_code == 0
        assert "The Config File is successfully validated." in result.output
        mock_post.assert_called_once()

    @patch("os.path.exists", return_value=True)
    @patch("t3_cicd_cli.command.validate.push", return_value="mock_branch")
    @patch("t3_cicd_cli.command.validate.configuration")
    @patch("t3_cicd_cli.command.validate.requests.post")
    def test_validate_bad_config(self, mock_post, mock_config, mock_push, mock_exists):
        mock_config.is_repo_remote = False
        mock_config.repo = "https://github.com/example/repo.git"
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Validation error"
        mock_post.return_value = mock_response
        runner = CliRunner()
        result = runner.invoke(
            validate, ["--file", "tests/t3_cicd_cli/test_files/bad_config.yaml"]
        )
        assert result.exit_code == 0
        assert "400 Validation error Validation failed." in result.output
        mock_post.assert_called_once()
        mock_push.assert_called_once_with(mock_config.repo)

    @patch("t3_cicd_cli.command.validate.configuration")
    @patch("t3_cicd_cli.command.validate.requests.post")
    def test_validate_default_config_path(self, mock_post, mock_config):
        mock_config.is_repo_remote = True
        mock_config.repo = "https://github.com/example/repo.git"
        mock_config.remote_branch = "main"
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "Success"
        mock_post.return_value = mock_response
        runner = CliRunner()
        result = runner.invoke(validate)
        assert result.exit_code == 0
        assert "The Config File is successfully validated." in result.output
        mock_post.assert_called_once_with(
            "http://localhost:8080/validate",
            json={
                "repo_url": "https://github.com/example/repo.git",
                "branch": "main",
                "config_path": DEFAULT_CONFIG_PATH,
            },
        )
