# Download base image python3 v3.10.12.
FROM python:3.10.12

# Copy project files.
COPY ./app /app
COPY ./db /db

# Labels about this image.
LABEL Name="student_accommodation_by_rooms"
LABEL Maintainer="ApenkaAnastasiya on DockerHub"
LABEL Version="0.0.1"
LABEL Description="Docker image with Python CLI app."

# Disable Prompt During Packages Installation.
ARG DEBIAN_FRONTEND=noninteractive

# Set environment variables.
ENV HOME /root

# Start with bash.
ENTRYPOINT ["bash"]

# Define working directory.
WORKDIR /app

# Install packages.
RUN apt-get update && \
    apt-get upgrade -y && \
    pip3 install --no-cache-dir -r requirements.txt && \
    apt-get clean

# Make port 8000 available to the world outside this container
EXPOSE 8000
