# Week 3

# Completed tasks

| Task                                                                                                                                | Weight | 
|-------------------------------------------------------------------------------------------------------------------------------------|--------| 
| [Implement ConfigService and ConfigValidationController](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/22)               | 5      |      |
| [Created Pipeline Commands, Log Commands, Info Commands Classes and Tests](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/21) | 5      |
| [Added Rerun and Stop commands in CLI (skeleton methods)](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/18)                  | 3      |
| [Draft MVP Design doc for Backend](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/8)                                      | 3      |    |
| [Discuss about blocker of backend design](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/9)                               | 1      |    |
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
- Conducted multiple discussions on the advanced CI/CD backend system design, and the documentation is now almost complete and has entered the review phase.
- Completed the development and testing of Pipeline Commands, Log Commands, and Info Commands classes.
- Implemented ConfigService and ConfigValidationController.
- Defining and creating issues has become a lot easier.


# What did not work this week?
- NA

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

# Design Document Plans vs Actual Implementation
- To help notify and explain the differences between the actual implementation and what was planned in the design document, please refer to the following example:
- [Implement ConfigService and ConfigValidationControlle](https://github.com/CS6510-SEA-F24/t3-cicd-backend/pull/20)
  1. parseConfigFile(configPath) vs parseAndValidateConfigFile(MultipartFile file):
  - Design Document: The parseConfigFile function is designed to parse configuration files in YAML or JSON formats to extract pipeline settings.
  - Actual Implementation: The parseAndValidateConfigFile method supports only uploaded YAML files and handles both parsing and validation of the pipeline configuration.
  2. validateConfigFile(config) vs Methods like validateJobScript(String jobName, Map<String, Object> jobConfig):
  - Design Document: The validateConfigFile method is intended to validate the structure and content of the configuration file.
  - Actual Implementation: There are multiple validation methods, such as validateJobScript, validateScript, and validateJobConfig, which handle different aspects of validation.
  3. overrideConfig(currentConfig, overrideParams):
  - Design Document: This function is meant to merge CLI-provided override parameters with the current configuration.
  - Actual Implementation: We did not use this method.
  4. writeConfigToFile(mergedConfig, localConfigPath):
  - Design Document: This function is designed to write the overridden configuration to a file.
- Actual Implementation: We modified this method.
-In the actual implementation, the ConfigService.java has added the following methods:
  1. processJobDependencies(): This method handles job dependencies, orders jobs within each stage, and checks for circular dependencies.
  2. loadYaml(MultipartFile file): This method loads and parses the YAML content from the uploaded file.
  3. handleConfigFile(Map<String, Object> config): This method processes the parsed YAML configuration file, separates job entries from non-job entries, validates the jobs, and processes the stages.
  4. handleJobEntry(String jobName, Map<String, Object> jobConfig, Set  jobNames)  : This method validates the job name, job configuration, and job script, then creates and stores the job.
  5. parseStages(Object value): This method parses the stages defined in the configuration, ensuring that stage names are unique.
  6. validateJobScript(String jobName, Map<String, Object> jobConfig): This method validates that the job configuration contains a "script" field.
  7. validateScript(String jobName, Object scriptObj): This method validates that the script field in the job configuration is not empty.
  8. validateJobConfig(String jobName, Object jobConfig): This method validates that the job configuration is a valid Map.
  9. handleJobStage(Object value): This method handles the stage configuration for the job, ensuring the stage is declared.
  10. handleJobScripts(Object scriptObj, List  jobScripts)  : This method handles the job script configuration, adding the script(s) to the job script list.
  

# Previous Design updates
- [Original Design doc](https://github.com/CS6510-SEA-F24/individual-proposal-for-tech-stack-and-initial-design-wp161)
- [Team 3 CI/CD Backend System Design](https://docs.google.com/document/d/1WmzA9xXXay2349NbBVnbmHHtN1dFnkX-mJs9rkf4Dnw/edit?usp=sharing)
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