# Week 1

# Completed tasks

| Task                                                                                 | Weight | 
|--------------------------------------------------------------------------------------|--------| 
| [Create a Second Repository](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/3) | 1     |


# Carry over tasks

| Task                                                                                                                               | Weight | Assignee          |
|------------------------------------------------------------------------------------------------------------------------------------|--------|-------------------|
| [Configure the backend repo](https://github.com/orgs/CS6510-SEA-F24/projects/11?pane=issue&itemId=81421828)                        | 5      | Wenbo |
| [Investigate Git Repo Integration for Local/Remote](https://github.com/orgs/CS6510-SEA-F24/projects/11?pane=issue&itemId=81411091) | 3      | Wenbo, Yuhan      |

# New tasks

| Task | Weight | Assignee |
|------|--------|----------|
|      |        |          |


# What worked this week?
- Aligned the team rituals, e.g. sprint meeting schedule, git repo management, PR rules, weekly scrum master rotation, etc.
- Had initial discussion on the high-level system design, and figured next steps (2 spikes)
- Configured both Java and Python repo
- GitHub Actions CI/CD is added to both repo - a good learning experience
- Aligned the team rituals, e.g. sprint meeting schedule, git repo management, PR rules, weekly scrum master rotation, etc.
- Had initial discussion on the high-level system design, and figured next steps (2 spikes)
- Configured both Java and Python repo
- GitHub Actions CI/CD is added to both repo - a good learning experience


# What did not work this week?
- PR review takes time
- We could have more discussion on some initial product backlog tickets

# Design updates 
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