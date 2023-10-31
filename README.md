# data-engineering-challenge

A brief description of your Python project. This is the main heading for your project.

## Table of Contents

- [Data Engineering Challenge](#data-engineering-challenge)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
    - [Author](#author)
    - [Creation](#creation)
  - [Source Information](#source information)
  - [Architecture](#architecture)
    - [Components](#components)
    - [Load Type](#load type)
    - [Load Schedule](#load schedule)
  - [Features Covered](#features covered)
    - [Components](#components)
    - [Load Type](#load_type)
    - [Load Schedule](#load_schedule)

## Overview

This project was design for ETL purposes, the main focus is to extract data from CSV files and load into a SQL Database.

### Author

Carlos Pacheco

### Creation

Oct 30, 2023

## Source Information

Source Type: CSV

## Architecture

### Components

	*-	SQLITE3 DB: SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process.
	*-	Apache Airflow: Apache Airflow is used for the scheduling and orchestration of data pipelines or workflows.
    *-	Python Pandas: pandas is a open source data analysis and manipulation tool, built on top of the Python programming language.
    *- 	Docker: Docker is a platform designed to help developers build, share, and run container applications..

### Load Type

Incremental

### Load Schedule

Daily 00:00 hrs

## Running Process

First step will show you the following characteristics:

- Trips with similar origin, destination, and time of day should be grouped together.
- Develop a way to obtain the weekly average number of trips for an area, defined by a
bounding box (given by coordinates) or by a region.
- Use a SQL database.

To get started with this project, follow these installation requirements and steps:

- You need to have installed Docker for build and run the images that up the services and execute the code.

- Step 1:
  Clone the repository: https://github.com/carlospac202/data-engineering-challenge.git
- Step 2:
  Go to the project folder
- Step 3:
  Give permissions to the shell scripts: chmod +x shell.sh
                                         chmod +x shell_airflow.sh
- Step 4:
  Run the first shell script: ./shell.sh

To complete the project demonstration that is the workflow automation please follow these steps

- Step 1:
  Run the first shell script: ./shell_airflow.sh

