from click.testing import CliRunner
from t3_cicd_cli.cli import cli
import unittest
from unittest.mock import patch, mock_open, MagicMock
from t3_cicd_cli.constant.default import DEFAULT_CONFIG_PATH


class TestValidationCommands(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="config content")
    @patch("requests.post")
    def test_good_config(self, mock_post, mock_file):
        runner = CliRunner()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = 'Success'
        mock_post.return_value = mock_response

        result = runner.invoke(
            cli,
            [
                "validate",
                "--config",
                "tests/t3_cicd_cli/test_files/good_config.yaml",
            ]
        )
        file_path = "tests/t3_cicd_cli/test_files/good_config.yaml"
        mock_file.assert_called_once_with(file_path, "rb")
        mock_post.assert_called_once()
        self.assertIn("The Config File is " +
                      "successfully validated.", result.output)

    @patch("builtins.open", new_callable=mock_open, read_data="config content")
    @patch("requests.post")
    def test_default_config(self, mock_post, mock_file):
        runner = CliRunner()

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "Success"
        mock_post.return_value = mock_response

        result = runner.invoke(
            cli,
            [
                "validate",
            ]
        )

        mock_file.assert_called_once_with(DEFAULT_CONFIG_PATH, "rb")
        mock_post.assert_called_once()
        self.assertIn("The Config File is " +
                      "successfully validated.", result.output)

    @patch("builtins.open", new_callable=mock_open, read_data="config content")
    @patch("requests.post")
    def test_bad_config(self, mock_post, mock_file):
        runner = CliRunner()

        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Validation error"
        mock_post.return_value = mock_response

        result = runner.invoke(
            cli,
            [
                "validate",
                "--config",
                "tests/t3_cicd_cli/test_files/bad_config.yaml"
            ]
        )

        file_path = "tests/t3_cicd_cli/test_files/bad_config.yaml"
        mock_file.assert_called_once_with(file_path, "rb")
        mock_post.assert_called_once()
        message = "400 Validation error Validation failed"
        self.assertIn(message, result.output)

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_file_not_found(self, mock_file):
        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "validate",
                "--config",
                "tests/t3_cicd_cli/test_files/unfound_config.yaml"
            ]
        )
        file_path = 'tests/t3_cicd_cli/test_files/unfound_config.yaml'
        self.assertIn(f"Error: The file '{file_path}' was " +
                      "not found.", result.output)
