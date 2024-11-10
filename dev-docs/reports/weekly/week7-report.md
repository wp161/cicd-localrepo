# Week 7

# Completed tasks

| Task                                                                                                                            | Weight |
| ------------------------------------------------------------------------------------------------------------------------------- | ------ |
| [[CLI] Refactor CLI options to capture new requirements](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/49)               | 2      |
| [[DockerService] Use jobs in jobOrder to create Docker containers](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/38) | 2      |

# Carry over tasks

| Task                                                                                                                                                                                                                        | Status      | Weight | Assignee        |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------ | --------------- |
| [[DB] Finalize Database Design and what we want to store](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/7)                                                                                                       | In Review   | 2      | Wenbo           |
| [Refactor Backend ConfigValidation, ConfigController, PipelineController and relevant Service](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/56)                                                                 | In Progress | 2      | Yuhan           |
| [[KubernetesService] Migrate Current Implementation of Manually Starting Docker Containers to an Implementation of Creating Multiple Containers on Kubernetes](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/50) | In Progress | 5      | ALL Team member |
| [Update CLI Design and Backend Design align with Solution Proposal for Config File Handling in the CICD Backend Validation](https://github.com/CS6510-SEA-F24/t3-cicd-cli/issues/58)                                        | In Progress | 2      | Yuhan           |

# New tasks

| Task | Weight | Assignee |
| ---- | ------ | -------- |

Currently, we do not have any new tasks. New tickets will be created following the meeting with the professor to finalize the proposal, after which we will proceed with the [[KubernetesService] Migrate Current Implementation of Manually Starting Docker Containers to an Implementation of Creating Multiple Containers on Kubernetes](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/50) split.

# What worked this week?

- Team members are working together more seamlessly, adjusting well to each other’s styles, and achieving a steady, productive rhythm.
- Team members has aligned on a common goal, and members are building mutual trust, which enhances collaboration and accountability.
- Using draft PRs on GitHub keeping the Git repository clean and organized.

# What did not work this week?

- Due to the different OS, some team members had to put in extra effort to complete the setup process.
- As the backend codebase grows, refactoring has become more complex. Refactoring code not originally written by a team member introduces additional debugging challenges, often requiring more debugging effort, such as adding detailed logging to pinpoint issues accurately. However, this process is also a great way for everyone to become more familiar with the codebase.

# Design updates

- **High-level Design Updates**:

  - [**Migration CI/CD Backend to Kubernetes**](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/50):

    Initially, our backend using springboot which is deployed using docker containers, to imporve scalability,remote execution capability, and apply our knowledge learnt form this class with kubernetes, we proposing migrating the application to kubernetes.

    The final decision hasn't been made yet, as we only have four weeks left in the semester. We will finalize it after meeting with the professor on Monday at 4 PM to get advice, prioritize components, and assess feasibility within the remaining time

  - **Kubernetes Migration Proposal**:
    [Team 3 CI/CD Kubernetes Migration Proposal - Wenbo Pan](https://docs.google.com/document/d/1SU5M4KmolEXw_lpTCaC12HCqlmNj_jYfk9j74jBfh6E/edit?usp=sharing)

- **Backend Design Updates**:
  - **[5.2.1 PostgreSQL Schema Design](https://docs.google.com/document/d/1ErWFC26lwrA9PLGpr8jBQKec97mGugHZGl6UBFeNAAM/edit?usp=sharing)**: Add backend schema design with PostgreSQL, including entity restructuring, relationship definitions between Pipeline, Stage, and Job, and adjustments to repositories and configurations.

# Previous Design updates

## Week6

- **High-level Design Updates**:
  - **[Config File Handling Solution](https://docs.google.com/document/d/1KR9USlJs-kzIUOknt-beb1QnXEubE6aH63ZUWvAiBrg/edit?tab=t.0#heading=h.73h9mfz69fxu) - Git Integration Shifted to Backend**:
    - Previously, Git actions were handled by the CLI client, including fetching the code repository and config file repository. Now, we only send the repo URL and file path to the backend to better align with current design.
- **Backend Design Updates**:
  - **Due to our team re-organization, the previous [backend design](https://docs.google.com/document/d/1WmzA9xXXay2349NbBVnbmHHtN1dFnkX-mJs9rkf4Dnw/edit?tab=t.0#heading=h.1z5btpaasnim) is deprecated from Oct 31 onwards. The backend design will be updated in our new [document](https://docs.google.com/document/d/1ErWFC26lwrA9PLGpr8jBQKec97mGugHZGl6UBFeNAAM/edit?tab=t.0#heading=h.1z5btpaasnim)**
  - **2.1.1 Run Pipeline API and pipeline controller logic updated to align with the [proposal for config file handling](https://docs.google.com/document/d/1KR9USlJs-kzIUOknt-beb1QnXEubE6aH63ZUWvAiBrg/edit?tab=t.0#heading=h.73h9mfz69fxu)**
  - **2.1.3 Config File Validation API and logic updated to align with the [proposal for config file handling](https://docs.google.com/document/d/1KR9USlJs-kzIUOknt-beb1QnXEubE6aH63ZUWvAiBrg/edit?tab=t.0#heading=h.73h9mfz69fxu)**
- **CLI Client Updated (Documentation has not been updated)**:
  - **[PR](https://github.com/CS6510-SEA-F24/t3-cicd-cli/pull/60) is awaiting review and approval**
  - **Refactored CLI client config file: Removed unnecessary parameters in the CLI configuration file.**
  - **Updated validation logic: Instead of fetching and sending the config file content in the API POST request, the CLI now sends only the repo URL, branch, and config file path, aligning with the new design where the backend handles Git fetching.**
  - **Moved all Git fetching actions to the backend, where the CLI now only passes the Git repo URL and branch.**
- **Backend DockerService- [Sidecar Approach for Code Sharing](https://github.com/CS6510-SEA-F24/t3-cicd-backend/issues/36)**
  ![JPEG image-4A76-9525-F7-0](https://github.com/user-attachments/assets/f262fa10-4ce2-40e2-9a49-f3dde2d8553a)
  - To make code accessible to job containers (main containers), we implemented a "sidecar container" approach. The sidecar container is built from a custom Docker image, which is generated dynamically each time a pipeline runs, using a Dockerfile configured as follows:
    - Base Image: A basic, public Linux image (we use `alpine:latest`)
    - Configuration Steps:
      - Install `git`
      - Run `git clone <URL> /code`, where `<URL>` is the repository URL passed as a parameter, cloning the repo into the `/code` directory.
  - Execution process
    - When a pipeline initiates, the sidecar container is started first, before the main containers.
    - During startup, its `/code` directory is mounted to a shared volume (we call it `code-volume`).
    - Once the sidecar container is running, each main container is started and similarly binds its /code directory to the shared volume.
  - The shared volume allows seamless code sharing between the sidecar and main containers, ensuring that all containers have consistent, up-to-date access to the codebase.

## Week 5

- **[Solution Proposal for Config File Handling in CI/CD Backend Validation](https://docs.google.com/document/d/1KR9USlJs-kzIUOknt-beb1QnXEubE6aH63ZUWvAiBrg/edit?usp=sharing)**
  - Summary: TBD (this ticket is still in progress, we are still deciding on the best solution)

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
