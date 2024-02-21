# Download base image python3 v3.10.12.
FROM python:3.10

LABEL Name="python_app"
LABEL Maintainer="ApenkaAnastasiya on DockerHub"
LABEL Version="0.0.1"
LABEL Description="Docker image with Python CLI app."

COPY ./ /app

WORKDIR /app

RUN apt-get update && \
    apt-get upgrade -y && \
    pip3 install --no-cache-dir -r requirements.txt && \
    apt-get clean

ENTRYPOINT ["bash"]
