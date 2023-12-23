# Project Setup

Learn how to set up your development environment for working on the AttracNet project. This guide includes instructions for installing dependencies, configuring tools, and getting your environment ready for development.

## Microservice Creation Scripts

To streamline the process of creating new microservices, we provide utility scripts: `copy_fastapi_template.py` and `copy_expressjs_template.py`. These scripts automate the setup of a new microservice based on the FastAPI or Express.js templates respectfully. Both are used in the same way and can be used directly or via the Makefile targets.

### Usage

#### FastAPI Microservice

```bash
python3 scripts/copy_fastapi_template.py <new_microservice_name> [-f]
```

Node/Express Microservice

```bash
python3 scripts/copy_expressjs_template.py <new_microservice_name> [-f]
```

- `<new_microservice_name>`: The name for the new microservice.
- -f or --force (optional): Force copy even if the destination directory exists.

### Example

```bash
python3 scripts/copy_fastapi_template.py OsintMicro -f
```

This command creates a new microservice directory named OsintMicro inside the /microservices directory and copies the FastAPI template files into it. The -f flag allows the script to override the destination directory if it already exists.

### Help

For additional information and available options, use the help flag:

```bash
python3 scripts/copy_fastapi_template.py -h
```

This command provides a list of parameters and possible flags that can be used with the copy_fastapi_template.py. The example output of --help or -h flags is as follows:

```bash
usage: copy_fastapi_template.py [-h] [-f] new_microservice_name

Copy FastAPI template to a new microservice.

positional arguments:
  new_microservice_name  Name for the new microservice

optional arguments:
  -h, --help             show this help message and exit
  -f, --force            Force copy even if the destination directory exists
```

## Creating New Microservices via Makefile

To streamline the process of creating new microservices, we have provided Makefile targets that utilize utility scripts. These scripts copy the respective templates for FastAPI and Express.js into new microservice directories.

### FastAPI Microservices

To create a new FastAPI microservice, use the following Makefile target:

```bash
make new-fastapi-<microservice-name>
```

Replace <microservice-name> with the desired name for your FastAPI microservice. For example:

```bash
make new-fastapi-OsintMicro
```

### Express.js Microservices

Similarly, to create a new Express.js microservice, use the following Makefile target:

```bash
make new-express-<microservice-name>
```

Replace <microservice-name> with the desired name for your Express.js microservice. For example:

```bash
make new-express-AuthMicro
```

This command will create a new microservice directory named AuthMicro and copy the Express.js template files into it. The -f flag allows the script to override the destination directory if it already exists.
