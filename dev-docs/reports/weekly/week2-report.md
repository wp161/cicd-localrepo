# Week 2

# Completed tasks

| Task                                                                                 | Weight | 
|--------------------------------------------------------------------------------------|--------| 
| [Design Reading Configuration for the Backend](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/6) | 5     |
| [Configured the Backend Repo](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/1) | 5     |
| [Designed CLI](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/10) | 3     |
| [Configured CLI Repo](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/4) | 3     |
| [Investigate Git Repo Integration for Local/Remote](https://github.com/orgs/CS6510-SEA-F24/projects/11?pane=issue&itemId=81411091) | 3      |
| [Create Configuration Class and Tests for Configuration Commands](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/15) | 2     |
| [Removed weekly reports from main branch](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/7) | 1     |
| [Moved weekly reports back to main branch](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/7) | 1     |


# Carry over tasks

| Task                                                                                                                               | Weight | Assignee          |
|------------------------------------------------------------------------------------------------------------------------------------|--------|-------------------|
| [Discuss design documentation for Backend MVP Design](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/9)                        | 5      | Kelvin, Wenbo, Yuhan, Yuanyuan |
| [Create Log Class and Tests for Log Commands](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/19)                        | 2      | Kelvin |
| [Create Job Class and Tests for Job Commands](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/18)                        | 2      | Kelvin |


# New tasks

| Task | Weight | Assignee |
|------|--------|----------|
| [Finalize Database Design](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/7)                        | 3      | Wenbo, Kelvin, Yuhan, Yuanyuan |
| [Create Pipeline Class and Tests for Pipeline Commands](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/17)                        | 1      | Kelvin |
| [Create EnvironmentInfo Class and Tests for EnvironmentInfo Commands](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/21)                        | 1      | Kelvin |


# What worked this week?
- Aligned the team rituals, e.g. sprint meeting schedule, git repo management, PR rules, weekly scrum master rotation, etc.
- Had initial discussion on the high-level system design, and figured next steps (2 spikes)
- Successfully tested click commands in Configuration class - further skeleton code implementation and testing can be replicated for other command classes
- Finalized most aspects of the design for the backend, but we still require further discussion on certain areas
- Defining and creating issues has become a lot easier


# What did not work this week?
- PR review takes time
- We had some confusion of when the new sprint started

# Design updates
- [Design doc for backend](https://docs.google.com/document/d/1XcHfwnMC0B63F5Rg29R3JsgyDN8vZ4y84AKfCS_KK0w/edit?usp=sharing)
- Summaries:
  - Configuration Management
  - Pipeline Execution and Management
  - Job Management
  - Log Management
  - Configuration File Management
  - Environment Information Query
  - Database Design - not yet finalized
  - Overall Architecture Diagram

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
      - [GitHub repo](https://github.com/CS6510-SEA-F24/t3-cicd-backend)
      - [GitHub Client integration design update](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/1)
  - Job Execution: Docker container + Kubernetes cluster
    - In order to allow parallelism for jobs, Docker containers should be created per job level (which is different from GitHub Actions where containers are created per stage level)
    - Why not creating a container per stage level, and having multiple processes (jobs) running in parallel? 
      - Docker containers are generally designed to run one process at a time. While theoretically run multiple process within a single container is possible, it's not recommended in practice.
      - Related reading: [Can I run multiple programs in a Docker container?](https://stackoverflow.com/a/48242863multi-service_container/)/ [Docker document](https://docs.docker.com/engine/containers/multi-service_container/)
  - Data store: PostgreSQL (objects, files, metadata, history) + Redis (streaming real-time logs)