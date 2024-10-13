# Week 3

# Completed tasks

| Task                                                                                                                                | Weight | 
|-------------------------------------------------------------------------------------------------------------------------------------|--------| 
| [Implement ConfigService and ConfigValidationController](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/22)               | 5      |      |
| [Create and test the EnvirontmentInfo class for info commands](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/21)           | 3      |      |
| [Create and test the Log class for log commands](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/19)           | 3      |      |
| [Add rerun and stop commands in CLI - skeleton version](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/18)       | 3      |      |
| [Draft MVP Design doc for Backend](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/8)                                      | 3      |    |
| [Discuss about blocker of backend design](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/10)                              | 3      |    |
| [Finish finalize backend design doc](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/26)                                       | 3      |    |




# Carry over tasks

| Task                                                                                                                                                   | Weight | Assignee          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-------------------|
| [[Parent Ticket] Create a skeleton for the Commands and Subcommands from Finalized CLI Design](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/11) | 3      | Kelvin |
| [Create and test the Validation class for configuration validation commands](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/20)                  | 2      | Kelvin |



# New tasks

| Task | Weight | Assignee |
|------|--------|----------|




# What worked this week?
- Updated the sprint meeting times and effectively conducted the meetings as scheduled.
  1. Sprint Planning: Tuesday evening after class
  2. Standup: Wednesday & Thursday 4pm, and Friday 2pm
  3. Sprint Retro: Monday 5:30pm
- Conducted multiple discussions on the advanced CI/CD backend system design. The documentation now includes the first version of a low-level, implementable design; for details, please see the "Design Updates". However, it does not yet include database schema design, Kubernetes design, future performance considerations, etc. The document has now entered the review phase.
- Completed the development and testing of Pipeline Commands, Log Commands, and Info Commands classes.
- Implemented ConfigService and ConfigValidationController.
- Defining and creating issues has become a lot easier.


# What did not work this week?
- Insufficient experience in designing backend system documentation.
- PR review takes time

# Design updates
- [Team 3 CI/CD Backend System Design](https://docs.google.com/document/d/1WmzA9xXXay2349NbBVnbmHHtN1dFnkX-mJs9rkf4Dnw/edit?usp=sharing)
- Summaries:
  - We used a client-driven approach when designing APIs. Each CLI subcommand will have its own API and unique URI. In this way there's a **one-to-one relationship between APIs and CLI subcommands**, which reduces the logic on the CLI and keeps it lightweight.
  - We designed our backend services in a way such that the **same business logic can be called by different APIs**. For example, ConfigService provides logic to validate a Config File, which can be used in both the API for pipeline run subcommand and the API for validate subcommand. The purpose is to create a loosely-coupled backend, and increase modularity and encapsulation. In this way, business logic is decoupled from the API layer, and the API doesn't need to worry about the implementation of the logic as long as it knows what service to call. This will help reducing repetitive logic in the backend, as the same logic can be invoked at different places. It also makes the backend easier to maintain and easier to extend.
  - The details in this design, e.g. the exact URI path/ request entity/ response entity/ scope and methods of each service are hand-wavy and **will be subjected to change/ update** as we haven't come up with the DB schema and don't have enough experience working with some of the dependencies e.g. Docker/ Redis. However, we believe it's more important to start implementing now and pick up on these things along the way than waiting for a confirmed 100% preparation to start. Upon implementation, we will take a deeper look at these details and make the judgement call.
  - This week we implemented the ConfigService, and the actual implementation is off from what was planned in the design document. For more details and the reasoning, please refer to the PR link:[Implement ConfigService and ConfigValidationControlle](https://github.com/CS6510-SEA-F24/t3-cicd-backend/pull/20).
  

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