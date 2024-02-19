# Download base image python3 v3.10.12.
FROM python:3.10.12

# Copy project files.
COPY ./app /app

# Labels about this image.
LABEL Name="student_accommodation_by_rooms"
LABEL Maintainer="ApenkaAnastasiya on DockerHub"
LABEL Version="0.0.1"
LABEL Description="Docker image with Python CLI app."

# Disable Prompt During Packages Installation.
ARG DEBIAN_FRONTEND=noninteractive

# Start with bash.
ENTRYPOINT ["bash"]

# Define working directory.
WORKDIR /app

# Install packages.
RUN apt-get update && \
    apt-get upgrade -y && \
    pip3 install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000
