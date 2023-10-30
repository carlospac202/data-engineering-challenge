#!/bin/bash

# Check if the services defined in the docker-compose.yml file are running
if [[ "$(docker-compose ps -q)" ]]; then
    echo "Services are already running. Stopping and removing them..."
    docker-compose down
fi

# Build the Docker images and run the services
echo "Building and running the Docker services..."
docker-compose up -d

# Check the result
if [ $? -eq 0 ]; then
    echo "Services successfully built and started."
else
    echo "Service build and start failed."
fi