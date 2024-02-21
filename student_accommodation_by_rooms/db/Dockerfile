FROM mysql:8.0

LABEL Name="mysql_container"
LABEL Maintainer="ApenkaAnastasiya on DockerHub"
LABEL Version="0.0.1"
LABEL Description="Docker image with MySQL."

COPY ./init.sql /docker-entrypoint-initdb.d/
