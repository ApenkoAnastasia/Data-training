# Download base image ubuntu v22.04.
FROM ubuntu:22.04

# Copy files for testing our containers
COPY /files_for_testing_container/test_docker.sh ./test_docker.sh
COPY /students_accommodation ./students_accommodation

# Labels about this image.
LABEL Name="dockerproject_for_ubuntu"
LABEL Maintainer="apenkoanastasiya on DockerHub"
LABEL Version="0.0.1"
LABEL Description="Docker image with Ubuntu 22.04 and layers such as: \
Python, MySQL (also include MC, Git, Nano, some libraries, such as pip)"

# Disable Prompt During Packages Installation.
ARG DEBIAN_FRONTEND=noninteractive

# Install first layer and zip, unzip, curl from ubuntu repository.
RUN apt-get update -y && \
    apt-get install -y apt-utils && \
    apt-get upgrade -y && \
    apt-get install -y zip unzip && \
    apt-get install -y curl && \
    apt-get clean

# Install Python layer (python 3).
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    apt-get clean

# Install MySQL layer.
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y mysql-server && \
    pip3 install mysql-connector-python && \
    apt-get clean

# Arguments for creating users
ARG MySQLUser
ARG MySQLPassword

# Configure MySQL user
RUN service mysql stop && \
	usermod -d /var/lib/mysql/ mysql && \
	service mysql start && \
    service --status-all && \
    mysql -password -e "USE mysql;\
                        CREATE USER '${MySQLUser}'@'localhost' IDENTIFIED WITH caching_sha2_password BY '${MySQLPassword}';\
                        GRANT ALL PRIVILEGES ON * . * TO '${MySQLUser}'@'localhost';\
                        FLUSH PRIVILEGES;" && \
    service mysql restart

# Install layer with Git.
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y git && \
    apt-get clean

# Install MC, Nano and etc. layer.
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y mc && \
    apt-get install -y nano && \
    apt-get clean

# Set environment variables for MC.
ENV TERM=xterm
RUN export TERM=xterm

# Run testing files inside container & instalation DB
RUN /test_docker.sh && \
    service mysql restart && \
    cd /students_accommodation && \
    bash -c './orchestration/setupDB.sh'

# Set environment variables.
ENV HOME /root

# Start with bash.
ENTRYPOINT ["bash"]

# Define working directory.
WORKDIR /root
