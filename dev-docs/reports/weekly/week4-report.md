# Week 4

# Completed tasks

| Task                                                                                                                          | Weight |
| ----------------------------------------------------------------------------------------------------------------------------- | ------ | ----- |
| [CLI: Implement configuration reading/ writing with local JSON file](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/36) | 3      | Wenbo |
| [Update backend design doc based on current comment](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/23)             | 3      | Yuhan |

# Carry over tasks

| Task                                                                                                                                                                         | Weight | Assignee |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | -------- |
| [Create an API and controller to handle pipeline run request from the CLI](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/24)                                      | 3      | Yuanyuan |
| [Backend Service: Create a service to make Docker containers for each job and pass the script to the container](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/25) | 3      | Kelvin   |
| [Backend Database: Connect SpringBoot backend to PostgreSQL and save job run history to a table](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/26)                | 3      | Yuhan    |
| [CLI: Implement the pipeline run command with git push](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/34)                                                             | 3      | Wenbo    |

# New tasks

- Assign new tasks every Tuesday during the sprint meeting
  | Task | Weight | Assignee |
  | ---- | ------ | -------- |

# What worked this week?

- Updated the backend design document, incorporating feedback and requirements.
- Successfully split the run pipeline feature into four parts, with each team member focusing on a specific part.
- CLI: Initialized the local repository and coordinated the configuration. Added CLI configurations and reading/writing. Add Generated the required API and posted it to the backend.
- Controller: Implemented the pipeline controller, which is now capable of handling requests from the CLI client. It’s ready to interact with Docker and Log services.
- Job run and Docker Service: Configured the Docker container and successfully passed scripts into the container to run job, stop job.
- Connection to PostgreSQL and Log Service: Implemented the LogService entity, repository, PostgreSQL connection configuration, and SOP document for local PostgreSQL initial setup.

# What did not work this week?

- CLI: Still working on finalizing tests for the git utility methods and the pipeline run command, will complete once it's done.
- Controller: Testing for the controller is still in progress and needs intergrate with each service after service part finished.
- Docker: Testing for the Docker service is still in progress.
- Connection to PostgreSQL and Log Service: Working on adding tests and potentially updating the Log entity or adding additional entities.

# Design updates

- [Team 3 CI/CD Backend System Design](https://docs.google.com/document/d/1WmzA9xXXay2349NbBVnbmHHtN1dFnkX-mJs9rkf4Dnw/edit?usp=sharing)
- Summaries:
  - We updated the Pipeline/run API by reducing the payload size, removing redundant fields. Previously, optional fields like commit were included in the payload as empty strings (e.g., commit: ""). In the updated API, if a field is optional and not provided, the key itself is omitted from the payload. This reduces the payload size without affecting functionality, as the backend can handle missing keys for optional parameters

# Previous Design updates

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
