# AttracNet Project

## Project Definition

AttracNet is a creative digital platform aimed at streamlining the job application and networking process for job seekers, especially in the technical field. The platform integrates various microservices to provide a comprehensive solution for users.

### Microservice Overview

1. **AuthMicro (Authentication Service)**
   - Handles user registration, login, and authentication.
   - Technology: Express.js (Node.js)

2. **OsintMicro (OSINT Service)**
   - Utilizes OSINT techniques to find potential employers, hiring managers, and job opportunities.
   - Technology: Python (FastAPI)

3. **NetMicro (Professional Networking Service)**
   - Facilitates user networking, connections, and interactions with potential employers.
   - Technology: FastAPI (Python)

4. **EmailMicro (Email Automation Service)**
   - Enables automated email campaigns for job seekers.
   - Technology: Express.js (Node.js)

### Project Structure

Each microservice will be part of its own GitHub repository under the organization 'AttracNet'.

```bash
github.com/AttracNet/AuthMicro
github.com/AttracNet/OsintMicro
github.com/AttracNet/NetMicro
github.com/AttracNet/EmailMicro
...
```

Each microservice follows a structured approach, but the file structure may vary depending on the technology stack.

**Python/FastAPI Microservices:**

```bash
- Dockerfile
- LICENSE.md
- Makefile
- README.md
- .gitignore
- .env
- example.env
- assets/
- bin/
- deploy/
- docs/
- requirements.txt
- scripts/
- src/
  - controllers/
    - main_controller.py
  - main.py
  - middlewares/
  - models/
    - main_model.py
  - routes/
    - main_routes.py
  - schemas/
  - utils/
- tests/
  - test_main_controller.py
- version.txt
```

**Node/Express Microservices:**

```bash
- Dockerfile
- LICENSE.md
- Makefile
- README.md
- .gitignore
- .env
- example.env
- app.js
- assets/
- bin/
  - README.md
  - docker-script.sh
  - update_version_in_readme.sh
- controllers/
  - main_controller.js
- deploy/
  - README.md
- docs/
  - coding-standards.md
  - deployment-guide.md
  - project-overview.md
- middlewares/
- models/
  - main_models.js
- package-lock.json
- package.json
- public/
- routes/
  - main_router.js
- tests/
  - main_controller.test.js
  - main_routes.test.js
- utils/
  - README.md
- version.txt
- views/
  - README.md
```

### Git Branches

- `main`: Main development branch.
- `feature/feature-name`: Feature branches for developing new features.
- `bugfix/bug-name`: Bugfix branches for addressing issues.

### Deployment and Orchestration

- Use Docker for containerization of each microservice.
- Orchestrate with Docker Compose for local development.
- Consider Kubernetes for production orchestration.

### Best Practices

1. **CI/CD:**
   - Implement continuous integration and continuous deployment pipelines for automated testing and deployment.

2. **Documentation:**
   - Maintain clear and comprehensive documentation for each microservice, including API documentation.

3. **Versioning:**
   - Follow semantic versioning for releases.

4. **Security:**
   - Implement secure coding practices, handle sensitive data securely, and regularly update dependencies.

5. **Monitoring:**
   - Integrate monitoring tools to track microservice performance.

6. **Scalability:**
   - Design microservices to be independently scalable, considering potential growth.

7. **Error Handling:**
   - Implement robust error handling mechanisms.

8. **Testing:**
   - Write unit tests and conduct thorough integration testing.

### Additional Insights

- Consider adopting Protocol Buffers for efficient data serialization.
- Start with JavaScript for Express.js services and Python for FastAPI services.
- Focus on developing the NetMicro service as the primary feature for the MVP.

## Setup Instructions

### Dependency Files

Each microservice includes dependency management files:

```bash
For Node.js services: package.json
For Python services: requirements.txt
```

### Initial Setup

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the microservice directory:

```bash
cd <microservice-directory>
```

Install dependencies:

```bash
npm install or pip install -r requirements.txt
```

Run the microservice:

```bash
npm start or python main.py
```

### Development Environment

Ensure the following:

```bash
Node.js version: >= v14.x.x
Python version: >= 3.8
```

## Directories

### `/docs`

The `/docs` directory contains project documentation, including user guides, API documentation, and any other relevant project documentation. For detailed setup instructions, refer to [Documentation](#documentation) section of this README.md.

### `/scripts`

The `/scripts` directory is designated for utility scripts or automation scripts that are not specific to any microservice but are essential for various project-related tasks. This can include setup scripts, data seeding scripts, or any other scripts relevant to your project. For more details about the available scripts, refer to [Project Setup](docs/project-setup.md).

### `/templates`

The `/templates` directory is where you store templates for microservices. The `fastapi_template` and `expressjs_template` templates can be found here. These are used to create new FastAPI ExpressJS microservices using the provided scripts. For detailed setup instructions, refer to [Project Setup](docs/project-setup.md).

  
## Potential Directories to Consider Adding to Parent Directory

### `/config`

The `/config` directory stores configuration files that are not tied to individual microservices. This may include environment-specific configurations, global settings, or any configuration files used across multiple components of your project.
[Config README](config/README.md)

### `/deploy`

The `/deploy` directory is where you can find scripts or configurations related to deployment. This might include deployment scripts, configuration files for deployment tools, or any artifacts needed for the deployment process.
[Deploy README](deploy/README.md)

### `/tests`

The `/tests` directory is suitable for storing testing-related scripts, data, or configurations that are not specific to a particular microservice. This could include common test scripts, test data sets, or any shared testing resources.
[Tests README](tests/README.md)

### `/bin`

The `/bin` directory is commonly used to store binary files or executable scripts that are shared among microservices or are part of the overall project. This might include global dependencies, scripts for managing dependencies, or any binaries needed for project-wide functionality.
[Bin README](bin/README.md)


### `/assets`

The `/assets` directory is used for storing shared assets, images, or files that are utilized across multiple microservices. This could include logos, images, or any other assets that are shared among different components of your project.
[Assets README](assets/README.md)

### Documentation

Explore detailed documentation for each aspect of the project:

- [API Documentation](docs/api-documentation.md)
- [Coding Standards](docs/coding-standards.md)
- [Contribution Guide](docs/contribution-guide.md)
- [Database Setup](docs/database-setup.md)
- [Dependencies](docs/dependencies.md)
- [Deployment Guide](docs/deployment-guide.md)
- [Monitoring Guide](docs/monitoring-guide.md)
- [Project Setup](docs/project-setup.md)
- [Security Best Practices](docs/security-best-practices.md)
- [Testing Guide](docs/testing-guide.md)
- [Versioning Guide](docs/versioning-guide.md)
- [Workflow Guide](docs/workflow-guide.md)

### Contact Information

For questions or contributions, feel free to reach out at <development@attracdev.com> or open an issue in the respective microservice repository.

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

### Acknowledgments

We express our gratitude to the open-source community and external libraries/tools that contributed to this project.
