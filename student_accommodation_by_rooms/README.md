# Python application for getting list of students accommodation by rooms.

## Description

Application consists of 2 containers: python container with app & MySQL container with DB.
Dockerfile download images with python v.3.10, mysql v.8.0 and then set up Python, MySQL and setup all settings and requirements.

## Installation
#### Requirements

Requires Docker to run (for convenience use Docker Desktop).
## Usage

In CLI use orchestration file for building project.

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
Check the execution permissions of orchestration scripts:
```sh
$ chmod +x orchestration/build_project.sh
$ chmod +x orchestration/manual_setup_db.sh
$ chmod +x orchestration/test_app.sh
```

(1) To start build project and create containers:

```sh
$ sh build_project.sh
```
Once container's CLI will be opened you can launch application.
All necessary user requirements will be installed through building an image.

(2) To run Students accommodation application in container's CLI go to folder follow the instructions in README.md in /app folder.

To deactivate virtual environment:
```sh
$ deactivate
```
