# Student Accommodation Information Project

## Description

students_accommodation is a Python CLI application to ...
This utility load data to the MySQL/PostgreSQL database ... ang display the necessary information.
#### Features

There are several options of this command application:

```--students ```, ```-sp```: Path to students file.

```--rooms ```, ```-rp```: Path to rooms file.

```--format ```, ```-f```: Choose in which format to save the information. Like: xml, json, csv, etc. Default value "json".

```--help```, ```-h``` : get the manual

## Installation
#### Requirements
Get_movies requires [Python](https://www.python.org/downloads/)  v3+ to run and MySQL/PostgreSQL on your computer.

Create a virtual environment:
```sh
$ . venv/bin/activate
```
Install the requirements:

```sh
$ pip install -r requirements.txt
```

## Usage

In command line interpreter start program.
Usage examples:

1)To get list of rooms and number of students in each of them

```sh
$python main.py -sp 'path to the file' -rp 'path to the file' -f 'json'
```

It returns:

```sh

    ...
```
