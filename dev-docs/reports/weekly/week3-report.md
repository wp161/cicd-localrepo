# Week 3

# Completed tasks

| Task                                                                                                                              | Weight | 
|-----------------------------------------------------------------------------------------------------------------------------------|--------| 
| [Implement ConfigService and ConfigValidationController](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/22)             | 5      |      |
| [Created Pipeline Commands, Log Commands, Info Commands Classes and Tests](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/21) | 5      |
| [Added Rerun and Stop commands in CLI (skeleton methods)](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/18)                  | 3      |
| [Draft MVP Design doc for Backend](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/8)                                    | 3      |    |
| [Discuss about blocker of backend design](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/6)                             | 1      |    |
| [Finish finalize backend design doc](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/26)      | 3      |    |




# Carry over tasks

| Task                                                                                                                                                   | Weight | Assignee          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-------------------|
| [[Parent Ticket] Create a skeleton for the Commands and Subcommands from Finalized CLI Design](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/11) | 3      | Kelvin | | 3      | Yuhan, Yuanyuan |
| [Create and test the Validation class for configuration validation commands](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/20)                  | 2      | Kelvin |



# New tasks

| Task | Weight | Assignee |
|------|--------|----------|
| [Finalize Database Design](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/7)                        | 3      | Wenbo, Kelvin, Yuhan, Yuanyuan |



# What worked this week?
- Aligned the team rituals, e.g. sprint meeting schedule, git repo management, PR rules, weekly scrum master rotation, etc.
- Conducted multiple discussions on the advanced CI/CD backend system design, and the documentation is now almost complete and has entered the review phase.
- Completed the development and testing of Pipeline Commands, Log Commands, and Info Commands classes.
- Implemented ConfigService and ConfigValidationController.
- Defining and creating issues has become a lot easier.


# What did not work this week?
- PR review takes time
- Discussions require more time and effort due to the diverse knowledge backgrounds of team members.

# Design updates
- [Team 3 CI/CD Backend System Design](https://docs.google.com/document/d/1WmzA9xXXay2349NbBVnbmHHtN1dFnkX-mJs9rkf4Dnw/edit?usp=sharing)
- Summaries:
  - Description
  - Project Requirements
  - Proposed Design
  1. Overview
  2. Modules Breakdown
  - API & Controller Breakdown 
  - Service Breakdown
  3. Tech Stack Details
  4. Service Interactions
  5. Database Schema Design
  6. Scalability and Future Enhancements

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