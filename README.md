# t3-cicd-cli

A Python CLI for executing and orchestrating CI/CD pipelines. This CLI is built using Python's `Click` framework and supports YAML configuration for defining pipeline stages and jobs.

## Table of Contents

- [Features](#features)
- [Development Setup](#development-setup)
  - [Prerequisites](#prerequisites)
  - [Build Instructions](#build-instructions)
  - [Running Tests](#running-tests)
  - [Other Useful Commands](#other-useful-commands)
- [Pull Request Process](#pull-request-process)
  - [Creating a PR](#creating-a-pr)
  - [Rules for PRs](#rules-for-prs)
- [CI/CD Workflows](#ci-cd-workflows)
- [License](#license)

## Features (WIP)

- **Command-Line Interface (CLI)**: Allows users to trigger and manage CI/CD pipeline execution.
- **YAML Configuration Support**: Define pipeline stages, jobs, and dependencies using YAML.
- **Git Integration**: Handles fetching repositories and metadata via GitPython.
- **Real-Time Log Streaming** (optional): Stream execution logs via Redis.
- **Extensible and Easy to Use**: Python's simplicity for fast prototyping and development.

## Development Setup

### Prerequisites

To use this project, you need:

- Python 3.8 or higher
- Poetry (for dependency management)

### Build Instructions

Clone the repository:

```bash
git clone https://github.com/CS6510-SEA-F24/t3-cicd-cli.git
```

Build the Project:
Using Nox for Automated Builds, Tests, and Linting, file in `noxfile.py`:

We use nox to run automated sessions like testing, linting, and building the project.
Nox allows us to define a "do-all" type script to ensure everything runs in one command.

To run all sessions:

```bash
nox -s all
```

Install the dependencies using Poetry:

```bash
poetry install
```

Build the Project: Build source distribution and wheel files:

```bash
poetry build
```

Running Tests
To run all unit tests:

```bash
poetry run pytest
```

To run tests with coverage reports:

```bash
poetry run pytest --cov=src/ --cov-report=term-missing --cov-fail-under=80
```

Coverage reports can be found in the htmlcov/ directory.
If test coverage is below 80%, the build will fail.

Other Useful Commands:
Auto-format Code(Black): Automatically format the code in src/ and tests/ to follow PEP8 guidelines:

```bash
poetry run black src/ tests
```

Lint Code (Flake8): Check code style against PEP8 guidelines:

```bash
poetry run flake8 src/ tests/
```

## Pull Request Process

### Creating a PR

#### **Always use feature branch to make change**:

```bash
git checkout -b <branch_name> # create a new branch with <branch_name>
```

> Direct push to the main branch is strictly forbidden as this is the Production branch. All change
> should be merged with approved PR.

#### **Ensure your code is up-to-date with the `main` branch**:

```bash
git config pull.rebase true # always use rebase to reconcile divergent branches
git pull
```

> Regularly pull from the main branch avoids conflicts pilling up.
> Please make sure you pull again before creating a PR.

#### **Follow the PR Template**:

- Your PR description should address any relevant context to help the reviewer to understand the
  PR. If this is related to an issue, reference the issue in the description.
- Make sure to use the checklist, and give explanations to any unchecked ones.

#### **Check PR details**:

- Make sure the origin and destination of the PR is correct, as well as everything in the Commits
  and Files changed tabs before clicking "Create Pull Request".

#### **Submit your PR**:

- No need to manually select reviewers. Once the PR is created, 2 reviewers will be automatically
  assigned based on the [Reviewer Lottery](https://github.com/marketplace/actions/reviewer-lottery)
  process.

### Rules for PRs

#### **PR Size Limit**:

- PRs should not exceed 150 lines unless absolutely necessary.
  > To override this, add an `override-size-limit` label in the PR, and provide explanation in the
  > PR description.

#### Testing:

- Ensure all new code is properly tested.

#### Commit Guidelines:

- Use [meaningful commit messages](https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/).
  Squash commits if necessary to clean up the history.

#### Merging:

- When merging PRs, always use **SQUASH AND MERGE** to combine all changes into a single commit.

#### Review Timebox:

- Please post reviews within 24 hours after you received the review request, or ask for others to
  do the review.

## CI/CD Workflows

This project uses **GitHub Actions** for CI/CD automation. The configured CI/CD workflows are:

- **PR Size Check**:

  - This workflow is triggered when a new PR is created, or when a new commit is pushed to an existing PR.
  - It fails if the size of PR is greater than 150 lines, and no override label is provided.

- **Assign Reviewers**:

  - This workflow is triggered when a new PR is created, and PR Size Check completes successfully.
  - It assigns 2 random reviewers to the PR.

- **Pipeline Run**:
  - This workflow is triggered when:
    - "PR Size Check" workflow completes successfully.
    - A PR is merged.
  - This workflow will execute:
    - Build: Ensures the code builds successfully.
    - Run Unit Tests: All tests must pass.
    - Test Coverage Verification: Verifies that test coverage meets minimum requirements.
    - Code Quality Checks: Checkstyle and SpotBugs
    - Artifacts Upload: Build artifacts and generated reports are uploaded after pipeline run

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
