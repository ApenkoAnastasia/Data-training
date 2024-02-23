# Student Accommodation Information Project

## Description

Students_accommodation is a Python CLI application for obtaining information about student accommodation in dormitory rooms.

Utility allows you:
 - set up the selected database
 - fill it with data from files
 - make calculations regarding the placement of students
 - write the results to files in the required format

It also allows to run docker container with working utility.

#### Features

There are several options of this command application:

```--help```, ```-h``` : get the manual and exit

```--students_path ```, ```-sp```: Path to students file.

```--rooms_path ```, ```-rp```: Path to rooms file.

```--format ```, ```-f```: Choose in which format to save the information. Like: xml, json, csv, etc. Default value "json".

```--database ```, ```-db```: Choose database to save the information. Like: MySQL,Postgres,MongoDB, etc. Default value "MySQL".

```--list_count ```, ```-lc```: List of rooms and number of students in each of them. Choose 1 to activate option or 0 to exit without receiving such info.

```--min_avg ```: List 5 rooms where the average age of students is the smallest. Choose 1 to activate option or 0 to exit without receiving such info.

```--max_avg ```: List 5 rooms where the average age of students is the greatest. Choose 1 to activate option or 0 to exit without receiving such info.

```--list_of_mix ```, ```-lm```: List of rooms where mixed-sex students live. Choose 1 to activate option or 0 to exit without receiving such info.

```--initial_load ```, ```-il```: Choose necessary of making initial (full) load to DB. Choose 1 to start initial load or 0 to run without full loading.

## Installation
#### Requirements
Utility requires [Python](https://www.python.org/downloads/)  v3+ to run and Docker on your computer.

## Usage

In command line interpreter start program.
Usage examples:

1) To get help box:

```sh
$  python3 -m src.students_accommodation.main --help
```

2) To write data into database (default MySQL, format JSON then just write your file paths):

```sh
$  python3 -m src.students_accommodation.main -sp 'path to the file' -rp 'path to the file' --format 'xml' --database 'Postgres'
```

3) To get list of rooms and number of students in each of them::

```sh
$  python3 -m src.students_accommodation.main -sp 'path to the file' -rp 'path to the file' -lc 1
```

4) To get list of 5 rooms where the average age of students is the smallest:

```sh
$  python3 -m src.students_accommodation.main -sp 'path to the file' -rp 'path to the file' --min_avg 1
```

5) To get list of 5 rooms where the average age of students is the greatest:

```sh
$  python3 -m src.students_accommodation.main -sp 'path to the file' -rp 'path to the file' --max_avg 1
```

6) To get list of 5 rooms where the mixed-sex students live:

```sh
$  python3 -m src.students_accommodation.main -sp 'path to the file' -rp 'path to the file' -lm 1
```

You can save data in necessary format and mix different options in one launch. The following arguments are required: --students_path/-sp, --rooms_path/-rp.

The result files you can get in /output folder. Logs in /logs folder.
