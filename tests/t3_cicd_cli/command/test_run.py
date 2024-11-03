from click.testing import CliRunner
from unittest.mock import patch
from t3_cicd_cli.cli import cli


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
