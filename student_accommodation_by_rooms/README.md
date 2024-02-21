# Dockerfile to build image with Ubuntu and project

## Description

Dockerfile download empty image with Ubuntu 22.04
and then set up Python, MySQL (also include MC, Git, Nano, some libraries, such as pip).
Allows to adjust the necessary layers and not to adjust unnecessary packages.

#### Features
 - -imn | --image_name: "Set your image name. Default: stud_app_image"
 - -cn | --container_name: "Set your cantainer name. Default: stud_app_container"
 - -h | --help: "Give help information"
 - -msu | --mysql_user: "Set your mysql user. Default parameters are in /properties"
 - -msp | --mysql_password: "Set your mysql password. Default parameters are in /properties"

## Installation
#### Requirements

Requires Docker to run.
## Usage

In CLI start program.

Clone repository:
```commandline
git clone https://github.com/ApenkoAnastasia/Data-training/tree/main/students_accommodation_by_rooms
```
Change directory:
```commandline
cd students_accommodation_by_rooms
```

Create and activate a virtual environment:
```sh
$ python3 -m venv venv
$ . venv/bin/activate
```

(1) To start build project and create containers:

```sh
$ sh build_docker_image.sh -imn image_name -cn container_name -msu mysql_user -msp mysql_password
```
The container's CLI will be opened and you can launch applications inside such Ubuntu container.

[//]: # (&#40;2&#41; To test docker container run test_docker.sh from files_for_testing folder:)

[//]: # ()
[//]: # (```sh)

[//]: # ($  /test_docker.sh)

[//]: # (```)

[//]: # (To see the result of test_docker.sh go to the log file:)

[//]: # (```sh)

[//]: # ($  ls /)

[//]: # ($  cat /test_docker_log.log)

[//]: # (```)

[//]: # (Or you can go to the Docker Desktop and open that file directly.)

All necessary user requirements will be installed through building an image. But if you want to create new user for MySQL go to the next steps.

[//]: # (&#40;3&#41; To configure MySQL server open /instructions/MySQL_setup.txt and follow the instructions from the file in bash.)

(4) To run Students accommodation application in container's CLI go to folder:

```sh
$  cd ../students_accommodation/app
```
And follow the instructions in README.md in this folder.

To deactivate virtual environment:
```sh
$ deactivate
```
