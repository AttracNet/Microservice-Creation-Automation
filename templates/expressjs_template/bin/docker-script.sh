#!/bin/bash

# Change directory to the parent directory
# cd ..

# Get the current directory name
PROJECT_NAME=$(basename "$PWD")

# Change back to the original directory
# cd -

function build {
    # Build Docker image
    docker build -t $PROJECT_NAME .
}

function run {
    # Run Docker container
    docker run -p 3000:3000 --name $PROJECT_NAME-container $PROJECT_NAME
}

function stop {
    # Stop and remove Docker container
    docker stop $PROJECT_NAME-container
    docker rm $PROJECT_NAME-container
}

function clean {
    # Clean up Docker images
    docker rmi $PROJECT_NAME
}

function test {
    # Echo the project name
    echo "Docker image name would be: '$PROJECT_NAME'"
    # Perform any additional test-related steps here
}

# Check command-line arguments
if [ "$1" == "build" ]; then
    build
elif [ "$1" == "run" ]; then
    run
elif [ "$1" == "stop" ]; then
    stop
elif [ "$1" == "clean" ]; then
    clean
elif [ "$1" == "test" ]; then
    test
else
    echo "Usage: $0 {build|run|stop|clean}"
    exit 1
fi
