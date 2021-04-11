## Introduction
### ---------------------
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.


## Project Description
### ---------------------
As a data engineer, I will be creating a Postgres database with tables designed to optimize queries on song play analysis .I will also be creating database schema and ETL pipeline for this analysis. I will need to define fact and dimention tables using star schema and build ETL pipeline to tranfer data into Postgres using python and SQLL.

### Files
### ---------------------
#### Create_tables.py
This python file is used to drop and create tables. It is recommended to run this file once before we run the **etl.py**.

#### etl.py
This python file has the etl pipeline and it ingests data into postgres after required transformations .

#### sql_queries.py
This python file contains all your sql queries, and is imported into **create_tables.py** and **etl.py** files.

### SCHEMA
### ----------------------
#### Fact Table
songplays - records in log data associated with song plays i.e. records with page NextSong
Columns: songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
#### Dimension Tables
users - users in the app
Columns:
user_id, first_name, last_name, gender, level

songs - songs in music database
Columns:
song_id, title, artist_id, year, duration

artists - artists in music database
Columns:
artist_id, name, location, latitude, longitude

time - timestamps of records in songplays broken down into specific units
Columns:
start_time, hour, day, week, month, year, weekday
