from click.testing import CliRunner
from unittest.mock import patch, MagicMock, call
from t3_cicd_cli.cli import cli
from t3_cicd_cli.constant.default import DEFAULT_GITHUB_URL


class TestPipelineCommands:

    @patch("t3_cicd_cli.command.run.is_git_repo", return_value=True)
    @patch("t3_cicd_cli.command.run.is_repo_dirty", return_value=False)
    @patch("t3_cicd_cli.command.run.push", return_value="main")
    @patch("t3_cicd_cli.command.run.requests.post")
    @patch("t3_cicd_cli.command.run.configuration")
    def test_run_dry_run(
        self, mock_config, mock_post, mock_push, mock_is_repo_dirty, mock_is_git_repo
    ):
        """Test the 'run' command with the --dry-run option."""
        runner = CliRunner()
        result = runner.invoke(cli, ["run", "--dry-run"])
        assert result.exit_code == 0
        assert "Performing a dry run of the pipeline..." in result.output
        assert "Dry run complete. No jobs were executed." in result.output

    @patch("t3_cicd_cli.command.run.is_git_repo", return_value=True)
    @patch("t3_cicd_cli.command.run.is_repo_dirty", return_value=False)
    @patch("t3_cicd_cli.command.run.push", return_value="main")
    @patch("t3_cicd_cli.command.run.requests.post")
    @patch("t3_cicd_cli.command.run.configuration")
    def test_run_with_override(
        self, mock_config, mock_post, mock_push, mock_is_repo_dirty, mock_is_git_repo
    ):
        """Test the 'run' command with override options."""
        mock_config.repo = "https://example.com/repo.git"
        mock_config.is_repo_remote = True
        mock_post.return_value.status_code = 200

        runner = CliRunner()
        result = runner.invoke(cli, ["run", "--override", "key1=value1,key2=value2"])

        assert result.exit_code == 0
        assert "Executing the pipeline..." in result.output
        assert mock_post.called
        assert "The Pipeline is successfully started." in result.output

    @patch("t3_cicd_cli.command.run.configuration")
    def test_run_with_file_and_pipeline(self, mock_config):
        """Test error when both --file and --pipeline are specified."""
        runner = CliRunner()
        result = runner.invoke(
            cli, ["run", "--file", "test_file.yml", "--pipeline", "test_pipeline"]
        )

        assert result.exit_code == 0
        assert (
            "Error: Specify either --file or --pipeline, but not both." in result.output
        )

    @patch("t3_cicd_cli.command.run.configuration")
    @patch("t3_cicd_cli.command.run.os.path.exists")
    @patch("t3_cicd_cli.command.run.get_project_root")
    @patch("t3_cicd_cli.command.run.absolute_to_relative")
    @patch("t3_cicd_cli.command.run.requests.post")
    @patch("t3_cicd_cli.command.run.is_git_repo")
    @patch("t3_cicd_cli.command.run.is_repo_dirty")
    @patch("t3_cicd_cli.command.run.push")
    def test_run_with_file_local_repo(
        self,
        mock_push,
        mock_is_repo_dirty,
        mock_is_git_repo,
        mock_post,
        mock_absolute_to_relative,
        mock_get_project_root,
        mock_exists,
        mock_config,
    ):
        """Test the 'run' command when --file is specified on a local repo."""

        mock_config.is_repo_remote = False
        mock_config.repo = "/path/to/local/repo"
        mock_config.branch = "main"
        mock_exists.return_value = True
        mock_get_project_root.return_value = "repo"
        mock_absolute_to_relative.return_value = "relative/path/to/config.yaml"

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "Success"
        mock_post.return_value = mock_response
        mock_is_git_repo.return_value = True
        mock_is_repo_dirty.return_value = False
        mock_push.return_value = "main"
        runner = CliRunner()

        result = runner.invoke(
            cli, ["run", "--file", "/path/to/local/repo/config.yaml"]
        )
        assert result.exit_code == 0
        assert "Executing the pipeline..." in result.output
        assert "The Pipeline is successfully started." in result.output

        mock_post.assert_called_once_with(
            "http://localhost:8080/pipeline/run",
            json={
                "repo_url": "https://github.com/wp161/cicd-localrepo.git",
                "branch": "main",
                "config_path": "relative/path/to/config.yaml",
            },
        )

    @patch("t3_cicd_cli.command.run.configuration")
    @patch("t3_cicd_cli.command.run.requests.post")
    @patch("t3_cicd_cli.command.run.check_file_exists")
    def test_run_with_non_exist_file_remote_repo(
        self, mock_check_file_exists, mock_post, mock_config
    ):
        """Test the 'run' command when --file does not exist on a local repo."""

        mock_config.is_repo_remote = True
        mock_config.repo = "https://github.com/example.git"
        mock_config.branch = "main"

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "Success"
        mock_post.return_value = mock_response
        mock_check_file_exists.return_value = False
        runner = CliRunner()

        result = runner.invoke(cli, ["run", "--file", "config.yaml"])
        assert (
            "Error: Cannot verify file config.yaml in given repo https://github.com/example.git."
            in result.output
        )
        mock_post.assert_not_called()

    @patch("t3_cicd_cli.command.run.is_git_repo", return_value=True)
    @patch("t3_cicd_cli.command.run.is_repo_dirty", return_value=False)
    @patch("t3_cicd_cli.command.run.push", return_value="main")
    @patch("t3_cicd_cli.command.run.requests.post")
    @patch("t3_cicd_cli.command.run.configuration")
    def test_run_without_dry_run_or_override(
        self, mock_config, mock_post, mock_push, mock_is_repo_dirty, mock_is_git_repo
    ):
        """Test the 'run' command without --dry-run or --override options."""
        mock_config.repo = "https://example.com/repo.git"
        mock_config.is_repo_remote = True
        mock_post.return_value.status_code = 200

        runner = CliRunner()
        result = runner.invoke(cli, ["run"])

        assert result.exit_code == 0
        assert "Executing the pipeline..." in result.output
        assert mock_post.called
        assert "The Pipeline is successfully started." in result.output

    @patch("t3_cicd_cli.command.run.configuration")
    def test_run_with_null_local_repo(self, mock_config):
        """Test running the pipeline with an invalid local repository path."""
        mock_config.repo = None
        mock_config.is_repo_remote = False

        runner = CliRunner()
        result = runner.invoke(cli, ["run"])

        assert result.exit_code == 0
        assert "Error: The path/URL of the repo cannot be null." in result.output

    @patch("t3_cicd_cli.command.run.configuration")
    def test_run_with_invalid_local_repo(self, mock_config):
        """Test running the pipeline with an invalid local repository path."""
        mock_config.repo = "/invalid/repo"
        mock_config.is_repo_remote = False

        runner = CliRunner()
        result = runner.invoke(cli, ["run"])

        assert result.exit_code == 0
        assert "Error: The path of the repo does not exist" in result.output

    @patch("t3_cicd_cli.command.run.is_git_repo", return_value=True)
    @patch("os.path.exists", return_value=True)
    @patch("t3_cicd_cli.command.run.is_repo_dirty", return_value=False)
    @patch("t3_cicd_cli.command.run.push", return_value="main")
    @patch("t3_cicd_cli.command.run.configuration")
    def test_run_with_dirty_local_repo(
        self, mock_config, mock_push, mock_is_repo_dirty, mock_exists, mock_is_git_repo
    ):
        """Test running the pipeline with a dirty local repository."""
        mock_config.repo = "/valid/repo/path"
        mock_config.is_repo_remote = False

        runner = CliRunner()
        result = runner.invoke(cli, ["run"])
        assert mock_push.called
        assert result.exit_code == 0

    @patch("t3_cicd_cli.command.run.is_git_repo", return_value=True)
    @patch("t3_cicd_cli.command.run.is_repo_dirty", return_value=False)
    @patch("t3_cicd_cli.command.run.push", return_value="main")
    @patch("t3_cicd_cli.command.run.requests.post")
    @patch("t3_cicd_cli.command.run.configuration")
    def test_run_with_pipeline_failure(
        self, mock_config, mock_post, mock_push, mock_is_repo_dirty, mock_is_git_repo
    ):
        """Test the pipeline when the request to the server fails."""
        mock_config.repo = "https://example.com/repo.git"
        mock_config.is_repo_remote = True
        mock_post.return_value.status_code = 400
        mock_post.return_value.text = "Bad request error"

        runner = CliRunner()
        result = runner.invoke(cli, ["run"])

        assert result.exit_code == 0
        assert "400 Bad request error Validation failed." in result.output
