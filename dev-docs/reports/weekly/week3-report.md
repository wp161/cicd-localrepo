# Week 3

# Completed tasks

| Task                                                                                                                                | Weight | 
|-------------------------------------------------------------------------------------------------------------------------------------|--------| 
| [Implement ConfigService and ConfigValidationController](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/22)               | 5      |      |
| [Create and test the EnvirontmentInfo class for info commands](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/21)           | 3      |      |
| [Create and test the Log class for log commands](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/19)           | 3      |      |
| [Add rerun and stop commands in CLI - skeleton version](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/18)       | 3      |      |
| [Draft MVP Design doc for Backend](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/8)                                      | 3      |    |
| [Discuss about blocker of backend design](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/10)                              | 1      |    |
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

# Design updates
- [Team 3 CI/CD Backend System Design](https://docs.google.com/document/d/1WmzA9xXXay2349NbBVnbmHHtN1dFnkX-mJs9rkf4Dnw/edit?usp=sharing)
### Summaries:
We are designing a CI/CD system tailored for small and medium-sized companies, with the primary goal of simplifying the continuous integration and delivery process. This backend system will support operations triggered via command-line interface (CLI), including starting pipelines, stopping tasks, fetching logs, and real-time log streaming. The system will be built using Spring Boot, integrating Docker for task execution, using Redis for real-time log streaming, and PostgreSQL for persistent storage of job and pipeline data. The current design does not include Kubernetes integration but supports running jobs locally and remotely using Docker.

### Modules Modules Breakdown

#### 1.API & Controller Modules Breakdown

**API** | **Controller**
--- | ---
POST /pipeline/run | PipelineController
POST /job/rerun | JobController
POST /config/validate | ConfigValidationController
GET /logs/ | LogController
GET /history | HistoryController
GET /info/ | InfoController

##### 1.1 Pipeline
For the pipeline part, this section primarily handles operations related to the pipeline, including:

- Running the CI/CD pipeline.
- Running the CI/CD pipeline with a specified commit (optional).
- Performing a dry run of the CI/CD pipeline.
- Overriding the CI/CD configuration file.

The PipelineController is responsible for orchestrating the execution of the pipeline based on the user’s request, which includes options such as running with a specific commit, performing a dry run, and overriding configuration parameters.

##### 1.2 Job/Stage Run
This section primarily handles operations related to running a specific job, including:

- Rerunning a specific job in the pipeline with the option to override configuration values.
- Stopping a specific job or an entire stage within a running pipeline, ensuring any dependent jobs are also halted.

The JobStageController is responsible for handling job and stage-related operations such as stopping or rerunning jobs. It interacts with various services (such as DockerService and JobService) to manage the lifecycle of jobs and stages within the pipeline, allowing the user to stop running jobs or stages, or rerun them with updated configurations.

##### 1.3 Config File Validation
For the config file validation part, the system is responsible for validating the CI/CD pipeline configuration file. This validation ensures that the configuration file is correct, adheres to the expected structure, and contains all required fields for running the pipeline (such as stages, jobs, and dependencies).

The ConfigValidationController is responsible for handling the validation of CI/CD configuration files. It validates the structure, syntax, and content of the provided configuration file, ensuring that it meets the requirements for a valid CI/CD pipeline configuration.

##### 1.4 Log
This section is responsible for querying and displaying logs related to specific pipelines, stages, or jobs. The logs are stored in PostgreSQL or streamed in real-time using Redis during execution.

The LogController handles all operations related to querying logs for pipelines, stages, and jobs. It interacts with LogService to fetch logs from Redis.

##### 1.5 Run History
The run history query handles fetching the execution history related to a certain repository ID. This allows users to retrieve past pipeline run details such as status, start/end times, and overall results.

The HistoryController is responsible for handling requests to retrieve the pipeline run history for a specific repository. It interacts with the HistoryService to fetch and return the run history from the database.

##### 1.6 Info
This section includes methods for printing environment information, stage information, and job information.

### 2. Service Breakdown

- **GitService:** Responsible for interacting with Git repositories, including cloning repositories, fetching configuration files, and checking out specific branches.

- **ConfigService:** Manages and parses pipeline configuration files, providing fallback mechanisms for default configurations.

- **DockerService:** Manages Docker containers executing pipeline jobs, including starting, stopping, and monitoring container status.

- **LogService:** Handles logs related to pipeline execution, supporting real-time log streaming and persistent storage.

- **HistoryService:** Provides retrieval of pipeline execution history, supporting complex queries.

- **JobService:** Manages the status and configuration of pipeline jobs, ensuring proper job execution.

- **RedisService:** Provides common operations for interacting with the Redis database. It is mainly used for scenarios requiring high-speed access to store and read log information, temporary data, etc.

- **PostgreSQLService:** Provides common operations for interacting with the PostgreSQL database. It is mainly used for persistent data storage and querying, such as pipeline execution history and job configurations.

By designing this CI/CD system, we aim to provide a high-efficiency, scalable, and easy-to-maintain backend system that supports the smooth execution of CI/CD processes for small and medium-sized companies.
 
### Design Document Plans vs Actual Implementation
- Added a bullet point mentioning the differences between the actual implementation and what was planned in the design document. For example, the implementation of ConfigService has some differences from the design. For more details, please refer to the PR link: 
[Implement ConfigService and ConfigValidationControlle](https://github.com/CS6510-SEA-F24/t3-cicd-backend/pull/20).
  

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