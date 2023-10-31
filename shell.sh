#!/bin/bash

# Define the image name and tag
IMAGE_NAME="data-engineering-challenge"
IMAGE_TAG="latest"

# Check if the image exists
if docker inspect "$IMAGE_NAME:$IMAGE_TAG" &> /dev/null; then
    echo "Image $IMAGE_NAME:$IMAGE_TAG exists. Deleting..."
    docker rmi "$IMAGE_NAME:$IMAGE_TAG"
else
    echo "Image $IMAGE_NAME:$IMAGE_TAG does not exist."
fi

# Build the Docker image
echo "Building the Docker image..."
docker build -t "$IMAGE_NAME:$IMAGE_TAG" .

# Check the build result
if [ $? -eq 0 ]; then
    echo "Image $IMAGE_NAME:$IMAGE_TAG successfully built."
else
    echo "Image build failed."
fi

# Run the Docker image
echo "Running the Docker image..."
docker run "$IMAGE_NAME:$IMAGE_TAG"