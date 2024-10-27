# Week 5

# Completed tasks

| Task                                                                                                                                                                         | Weight |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| [Backend Service: Create a service to make Docker containers for each job and pass the script to the container](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/25) | 3      |
| [Backend Database: Connect SpringBoot backend to PostgreSQL and save job run history to a table](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/26)                | 3      |
| [CLI: Implement the pipeline run command with git push](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/34)                                                             | 3      |
| [[ConfigService] Refactor current parsing & validation checks to capture new requirements](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/34)                      | 5      |

# Carry over tasks

| Task                                                                                                                                    | Status          | Weight | Assignee |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------|--------|----------|
| [Create an API and controller to handle pipeline run request from the CLI](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/24) | Reassigning     | 3      | TBD      |
| [[ConfigService] Add line and col in error message](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/33)                        | Dev in progress | 3      | Kelvin   |
| [[CLI] Refactor CLI options to capture new requirements](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/49)                       | Dev pending     | 2      | Yuanyuan |
| [[Config File] Decide how to get the config file in the backend](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/32)           | In review       | 2      | Yuhan    |

# New tasks

| Task                                                                                                                                           | Weight | Assignee |
|------------------------------------------------------------------------------------------------------------------------------------------------|--------|----------|
| [[DockerService] Add Docker registry](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/36)                                             | TBD    | TBD      |
| [[CLI] Allow overriding the default ~/.cicd_config.json location for CLI Config File](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/50) | TBD    | TBD      |
| [[DockerService] Use jobs in jobOrder to create Docker containers](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/38)                | TBD    | TBD      |

# What worked this week?

- Most of the carried-over tickets from last week were successfully reviewed and merged in to the `main` branch.
- We introduced an "Expectation" section in this week's tickets ([example](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/33)), which the team found helpful for clarifying the specific requirements and goals of each task.
- The team agreed on several best practices to improve collaboration, including:
  - Seeking early clarification (and the logistics) when unsure about a task.
  - Taking full ownership of assigned tickets.
  - Preparing adequately for discussions to enhance productivity.
  - Avoiding pressure on individuals during code walk-through by not requiring solo demos.
- We escalated a carry-over ticket ([Create an API and controller to handle pipeline run request from the CLI](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/24)) from the previous sprint that is at risk of delayed delivery again this week. 
We consulted with the professor promptly to ensure the right action is taken in respond to the risk.

# What did not work this week?
- As we transitioned into the implementation phase, the number of pull requests (PRs) increased, but the 24-hour review time frame was not consistently followed.
- The ticket [Create an API and controller to handle pipeline run request from the CLI](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/24) was delayed due to challenges perceived by the original assignee. 
We are reassigning this ticket for the remainder of the sprint, but it may carry over again due to limited resources.
- Some PRs were submitted for review despite not being fully ready for integration into the main branch. This led to unnecessary time spent on reviewing incomplete code.
- We encountered issues with internal communication, particularly in reaching consensus on code standards, code quality expectations, and providing help.

# Design updates
- [Solution Proposal for Config File Handling in CI/CD Backend Validation](https://docs.google.com/document/d/1KR9USlJs-kzIUOknt-beb1QnXEubE6aH63ZUWvAiBrg/edit?usp=sharing)
  - Summary: TBD (this ticket is still in progress, we are still deciding on the best solution)

# Previous Design updates

## Week 4
- **High-level Design Updates**:
    - **Git Integration Shifted to CLI**:
        - Initially, Git integration was part of the Java backend. In the new design, Git operations (like cloning and pushing code) are handled by the CLI, reducing the load on the backend.
    - **Previous approach**:
        - Per [GitHub Client integration design update](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/1),
          The Java backend was responsible for fetching the code repository using Git commands and passing it to Docker containers for job execution. Local repos were zipped and sent via HTTP to the backend.
    - **Issues with the Previous Approach**:
        - **High Data Transfer**: Multiple transfers between CLI, backend, and services created inefficiencies.
        - **Memory Usage**: Large repos would cause memory issues on the backend, requiring complex file I/O handling.
    - **Solution**:
        - **Shift Git Cloning to Docker Containers**: Each Docker container now clones the required Git repository directly. The CLI retrieves the Git URL and branch name from the CLI configuration and passes it to the backend.
            - **Using existing design**: In CLI design, we save the URL/ path of the repo as one of the CLI Configurations (see this in Week1&Week2 below), and we can leverage on this feature to get the Git URL and the branch name that we need.
              > A key design is the **CLI config** where the user can specify environment variables.
            - **Remote Repos**: The URL and branch name from the user's configuration are passed directly to the backend.
            - **Local Repos**: A dedicated Git repo (**[cicd-localrepo](https://github.com/wp161/cicd-localrepo)**) is used to store local files, mimicking remote repo behavior. The CLI pushes local files to this repo before running CI/CD.
            - **Branch Management**: Users can configure which branch to use for remote repos in the CLI Config, while unique branch names are created for local repos pushed to **[cicd-localrepo](https://github.com/wp161/cicd-localrepo)**.
            - **Using Specific Commit**: By committing and uploading the local repo to **[cicd-localrepo](https://github.com/wp161/cicd-localrepo/tree/main)**, it's guaranteed that when the user specifies a valid commit with `cicd run --commit <commit_hash>`, this commit will exist in **[cicd-localrepo](https://github.com/wp161/cicd-localrepo/tree/main)**.
    - **Edge Case - Mixed Repos**:
        - If a repo is both local and remote (e.g., cloned from a remote Git), the user must specify in the CLI configuration whether to treat it as remote or local. For local repos, the user must commit any changes before running CI/CD.
    - **Alternatives Considered**:
        - Directly pushing changes to the user’s remote repo was ruled out to maintain privacy.
        - Creating "dummy commits" on behalf of the user was also rejected due to risks of corrupting Git history.
    - **Possible optimization**:
        - **Reducing Branch Count**: Instead of creating new branches for each local run, the same branch could be reused with incremental changes. This would reduce the number of branches and avoid redundant code storage. However, it requires saving unique branch names in the user’s local file system, which risks unintentional modification or deletion by the user.
        - **Improving Infrastructure**: **[cicd-localrepo](https://github.com/wp161/cicd-localrepo/tree/main)** is a lazy solution because we don't want to pay for storage and just want a quick way to upload/download local code repo. In a more robust infrastructure, the process for handling local repos could involve object storage (like S3), async job queues, and dedicated CI/CD workers to manage builds more efficiently.
- [Team 3 CI/CD Backend System Design](https://docs.google.com/document/d/1WmzA9xXXay2349NbBVnbmHHtN1dFnkX-mJs9rkf4Dnw/edit?usp=sharing)
    - We updated the Pipeline/run API by reducing the payload size, removing redundant fields. Previously, optional fields like commit were included in the payload as empty strings (e.g., commit: ""). In the updated API, if a field is optional and not provided, the key itself is omitted from the payload. This reduces the payload size without affecting functionality, as the backend can handle missing keys for optional parameters
    - Delete mock code for controller part for reason:
        - There is duplication between the logic and the mock code. The document is already 50 pages long, which isn't a good sign. It's becoming difficult to modify each part consistently, and any lack of clarity could lead to confusion during implementation.
        - The controller's mock code needs to be fully written to avoid misunderstandings. If it's incomplete, it could cause confusion and increase the workload beyond just design.
        - When implementing, the controller can often be designed with a better logic than what’s initially written in the mock code, making the mock version less helpful.
    - Update API by adding CLI configuration information as argument.
    - CLI configurations design: The current CLI configurations are stored in a plain object, causing updates to be lost across multiple calls. To ensure persistent configuration values, implement reading and writing to a local JSON file

## Week3

- Team 3 CI/CD Backend System Design
- Summaries:
    - We used a client-driven approach when designing APIs. Each CLI subcommand will have its own API and unique URI. In this way there's a one-to-one relationship between APIs and CLI subcommands, which reduces the logic on the CLI and keeps it lightweight.
    - We designed our backend services in a way such that the same business logic can be called by different APIs. For example, ConfigService provides logic to validate a Config File, which can be used in both the API for pipeline run subcommand and the API for validate subcommand. The purpose is to create a loosely-coupled backend, and increase modularity and encapsulation. In this way, business logic is decoupled from the API layer, and the API doesn't need to worry about the implementation of the logic as long as it knows what service to call. This will help reducing repetitive logic in the backend, as the same logic can be invoked at different places. It also makes the backend easier to maintain and easier to extend.
    - The details in this design, e.g. the exact URI path/ request entity/ response entity/ scope and methods of each service are hand-wavy and will be subjected to change/ update as we haven't come up with the DB schema and don't have enough experience working with some of the dependencies e.g. Docker/ Redis. However, we believe it's more important to start implementing now and pick up on these things along the way than waiting for a confirmed 100% preparation to start. Upon implementation, we will take a deeper look at these details and make the judgement call.
    - This week we implemented the ConfigService, and the actual implementation is off from what was planned in the design document. For more details and the reasoning, please refer to the PR link:Implement ConfigService and ConfigValidationControlle.

## Week1&Week2

- [Original Design doc](https://github.com/CS6510-SEA-F24/individual-proposal-for-tech-stack-and-initial-design-wp161)
- Summaries:
    - CLI:
        - [GitHub repo](https://github.com/CS6510-SEA-F24/t3-cicd-cli/tree/main)
        - Uses Python with [Click](https://click.palletsprojects.com/en/8.1.x/)
        - [CLI design doc](https://docs.google.com/document/d/1DdQHFntSbfUYHPYVOcu_mPvhTw1j20WMiWfzVuX3bdg/edit?usp=sharing)
            - A key design is the **CLI config** where the user can specifies environment variables
    - Config File: YAML (similar to GitLab CI/CD)
        - [GitLab CI/CD example setup](https://docs.gitlab.com/ee/ci/examples/)
    - Backend: Java Spring Boot
        - [Team 3 CI/CD Backend System Design](https://docs.google.com/document/d/1WmzA9xXXay2349NbBVnbmHHtN1dFnkX-mJs9rkf4Dnw/edit?usp=sharing)
        - [GitHub repo](https://github.com/CS6510-SEA-F24/t3-cicd-backend)
        - [GitHub Client integration design update](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/1)
    - Job Execution: Docker container + Kubernetes cluster
        - In order to allow parallelism for jobs, Docker containers should be created per job level (which is different from GitHub Actions where containers are created per stage level)
        - Why not creating a container per stage level, and having multiple processes (jobs) running in parallel?
            - Docker containers are generally designed to run one process at a time. While theoretically run multiple process within a single container is possible, it's not recommended in practice.
            - Related reading: [Can I run multiple programs in a Docker container?](https://stackoverflow.com/a/48242863multi-service_container/)/ [Docker document](https://docs.docker.com/engine/containers/multi-service_container/)
    - Data store: PostgreSQL (objects, files, metadata, history) + Redis (streaming real-time logs)
    - PostgreSQL Setup:
        - https://docs.google.com/document/d/15iOqlgZsiwzGAgmnN_sBQOZPpmCjgrxgbKVoj-op9rM/edit?usp=sharing
