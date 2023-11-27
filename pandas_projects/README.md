# Jupyter files for solving tasks on Pandas/NumPy theme

## Description

This project was made for lab on Big Data courses.

It's folder with few Jupyter files for population census (using CSV file with population data from 1994), house prices and so on. It's contains whole definitions to computing, graphics and others.

### Requirements

Requires Python3 to run. [(https://www.python.org/downloads/)]
Also needed such python packages:

    pandas,
    numpy,
    matplotlib,
    seaborn,
    pylab,
    sklearn,
    statsmodels

You can run program on Jupyter Notebook on your laptop or open this file on web. [https://jupyter.org/try]

## Installation

Open your command line interpreter [use command ```Ctrl+Alt+T```].
If you don't have 'pip' then install it:
```sh
python -m ensurepip
```

Install the necessary libraries.
```sh
pip install pandas
pip install numpy
pip install matplotlib
pip install seaborn
pip install pylab
pip install sklearn
pip install statsmodels
```
Install Jupyter Notebook with pip:
```sh
pip install notebook
```
You can install necessary libraries installing virtual environments and requirements.txt.
To create a virtual environment, go to your project’s directory and run venv. This will create a new virtual environment in a local folder .venv:

```sh
python3 -m venv .venv
```
Before you can start installing or using packages in your virtual environment you’ll need to activate it.

```sh
source venv/bin/activate
```
Instead of installing packages individually, pip allows you to declare all dependencies in a Requirements File. Next command install whole packages from txt file:

```sh
python3 -m pip install -r requirements.txt
```

If you want to switch projects or leave your virtual environment, deactivate the environment:

```sh
deactivate
```

## Usage

In command line interpreter start programm.
To run the notebook:
```sh
jupyter notebook
```
Open file .ipynb and activate whole cells using ```Shift+Enter```.
