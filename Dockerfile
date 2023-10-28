# Use the official Python image as a base image
FROM python:3.11-slim
LABEL authors="carlospac"

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the python3-pip package using apt-get
RUN apt-get update && apt-get install -y python3-pip

# Use the updated pip to install additional Python packages
RUN pip3 install pandas

# Run hello.py when the container launches
CMD ["python3", "test.py"]