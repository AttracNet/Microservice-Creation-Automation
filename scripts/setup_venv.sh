#!/bin/bash

# May consider adding this script to the python template(s) as well,
# to better automate the virtual environments and dependency installs

# Check if .venv directory exists
if [ -d ".venv" ]; then
    echo "Virtual environment (.venv) already exists. Skipping virtual environment setup."
else
    # Check if requirements.txt exists
    if [ ! -f requirements.txt ]; then
        echo "Error: requirements.txt not found in the project root directory."
        exit 1
    fi

    # Set up virtual environment
    echo "Setting up Python Virtual Environment (.venv)"
    python3 -m venv .venv

    # Activate virtual environment
    echo "Sourcing .venv/bin/activate"
    . .venv/bin/activate
fi


# Check if dependencies are already pinned in requirements.txt
if grep -q "^\S\+\=\=" requirements.txt; then
    echo "Dependencies are already pinned in requirements.txt. Skipping installation/upgrading."
else
    # Upgrade pip to the latest version
    echo "Install and upgrade pip"
    pip install --upgrade pip

    # Install or upgrade dependencies from requirements.txt
    echo "Install and upgrade dependencies from requirements.txt"
    pip install -U -r requirements.txt

    # Save dependencies to requirements.txt
    echo "Pin the dependency version numbers in the requirements.txt"
    pip freeze > requirements.txt
fi
