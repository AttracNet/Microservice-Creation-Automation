# Microservice Name

Version: 0.1.0

## Overview

This microservice is built using the Node.js and Express.js framework, providing a solid foundation for developing scalable and efficient web applications. It follows best practices for structuring Express.js applications and includes essential components for building a microservice.

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) installed
- [npm](https://www.npmjs.com/) (Node Package Manager) installed

### Installation

1. Create a new Microservice:

    From the Main project root, use the Python script:

```bash
python scripts/copy_expressjs_template <microservice-name>
```

```bash
cd microservices/<microservice-name>
```

```bash
npm install
```

```bash
npm run dev
```

## Docker

To containerize and run the microservice using Docker, follow these steps:

1. Build the Docker image:

    ```bash
    docker build -t <your-image-name> .
    ```

2. Run the Docker container

    ```bash
    docker run -p 3000:3000 -d <your-image-name>
    ```

3. Access the microservice at <http://localhost:3000>

For more details on Docker usage, refer to deploy/README.md.

### Makefile

The Makefile for this project provides convenient targets for common development tasks. To use these targets, make sure you have `make` installed on your system.

### Targets

1. **Update Version in README:**

    ```bash
    make update-version
    ```

    - **`update-version`:** Updates the version in the README.md file based on the version specified in version.txt.

2. **Lint Code:**

    ```bash
    make lint
    ```

    - **`lint`:** Runs ESLint to check for coding standards.

3. **Format Code:**

    ```bash
    make format
    ```

    - **`format`:** Runs Prettier to automatically format the code.

4. **Test Code:**

    ```bash
    make test
    ```

    - **`test`:** Executes unit tests using Jest.

5. **Start Dev Server:**

    ```bash
    make dev
    ```

    - **`dev`:** Starts the application in development mode using nodemon.

6. **Start Server:**

    ```bash
    make start
    ```

    - **`start`:** Starts the application in production mode.

7. **Run Scripts:**

    ```bash
    make run-scripts
    ```

    - **`run-scripts`:** Calls the `update-version` target.

### Docker-specific Targets

1. **Update Version in README:**

    ```bash
    make docker-build
    ```

    - **`docker-build`:** Builds the Docker image for the microservice.

2. **Update Version in README:**

    ```bash
    make docker-run
    ```

    - **`docker-run`:** Runs the Docker container.

3. **Update Version in README:**

    ```bash
    make docker-stop
    ```

    - **`docker-stop`:** Stops the running Docker container.

4. **Update Version in README:**

    ```bash
    make docker-clean
    ```

    - **`docker-clean`:** Removes stopped Docker containers and unused images.

5. **Update Version in README:**

    ```bash
    make docker-test
    ```

    - **`docker-test`:** Runs tests within a Docker container.

## Project Structure

- `bin/`: Contains executable scripts. Refer to [bin/README.md](bin/README.md) for details.
- `controllers/`: Handles application logic. Refer to [docs/coding-standards.md](docs/coding-standards.md) for coding standards.
- `deploy/`: Includes deployment-related files. Refer to [deploy/README.md](deploy/README.md) for deployment guidelines.
- `docs/`: Documentation files, including coding standards and deployment guide.
- `middlewares/`: Houses application middleware functions.
- `models/`: Manages data logic. Refer to [docs/project-overview.md#models](docs/project-overview.md#models) for an overview.
- `public/`: Stores static assets like stylesheets and images.
- `routes/`: Defines application routes. Refer to [docs/coding-standards.md](docs/coding-standards.md) for coding standards.
- `tests/`: Contains unit tests. Refer to [docs/coding-standards.md](docs/coding-standards.md) for testing guidelines.
- `utils/`: Holds utility functions. Refer to [utils/README.md](utils/README.md) for details.
- `views/`: Contains templates for rendering HTML views. Refer to [docs/project-overview.md#views](docs/project-overview.md#views) for an overview.

## Database Setup

This template uses SQLite as the default database. If your project requires a more robust database, consider PostgreSQL or MongoDB. Follow the instructions in [docs/project-overview.md#database](docs/project-overview.md#database) for database setup.

## Choosing Between Node/Express and Python/FastAPI Templates

Choose the Node/Express template if your project:

    Requires a lightweight and fast backend.
    Has existing JavaScript or Node.js expertise within your team.
    Prefers a larger ecosystem of available npm packages.

Consider the Python/FastAPI template if your project:

    Requires high performance.
    Benefits from type checking and asynchronous programming.
    Leverages Python or FastAPI specific libraries.

## Contributing

Feel free to contribute to this project. Follow the guidelines in [docs/coding-standards.md](docs/coding-standards.md) for code contributions.

## License

This project is licensed under the terms of the [MIT License](LICENSE.md).
