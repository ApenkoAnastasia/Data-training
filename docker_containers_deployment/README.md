# Dockerfile to build image with Ubuntu and project

## Description

Dockerfile download empty image with Ubuntu 22.04
and then set up Python, MySQL (also include MC, Git, Nano, some libraries, such as pip).
Allows to adjust the necessary layers and not to adjust unnecessary packages.

#### Features
 - -imn | --image_name: "Set your image name. Default: ubuntu_image_test"
 - -cn | --container_name: "Set your cantainer name. Default: test_container"
 - -h | --help: "Give help information"
 - -msu | --mysql_user: "Set your mysql user"
 - -msp | --mysql_password: "Set your mysql password"

## Installation
#### Requirements

Requires Docker to run.
## Usage

In CLI start program.
Usage examples:

(1) To start build image and create container:

```sh
$sh build_docker_image.sh -imn image_name -cn container_name -msu mysql_user -msp mysql_password
```

(2) To test docker container run test_docker.sh from files_for_testing folder:

```sh
$sh /test_docker.sh
```
All necessary user requirements will be installed through building an image. But if you want to create new user for MySQL go to the next steps.

(3) To configure MySQL server open /instructions/MySQL_setup.txt and follow the instructions from the file in bash.
