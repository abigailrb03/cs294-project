# Meta

This is documentation for instructors and course staff.

## About

A new full stack web application project for CS 61A and DATA C88C designed by
Abigail Brooks-Ramirez (@abigailrb03) and Rebecca Dang (@phrdang), advised by
Profs. Lisa Yan and Michael Ball at UC Berkeley through CS 294-189 Teaching at Scale.

## Requirements

- Python 3.9+
- [Flask](https://flask.palletsprojects.com/en/stable/)

## Installation

### MacOS

1. Setup a virtual environment: `python3 -m venv .venv`
2. Activate the virtual environment: `. .venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Create the `song_metadata.csv` file by following the instructions in `project/spotify_webscrape/README.md`.
5. Initialize the database:
```sh
cd project/flask_app
flask --app __init__.py init-db
```

### Windows

1. Setup a virtual environment: `py -3 -m venv .venv`
2. Activate the virtual environment: `.venv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Create the `song_metadata.csv` file by following the instructions in `project/spotify_webscrape/README.md`.
5. Initialize the database:
```
cd project\flask_app
flask --app __init__.py init-db
```

## Running the web app locally

```sh
cd project/flask_app
flask --app __init__.py --debug run
```

Then go to [http://127.0.0.1:5000](http://127.0.0.1:5000) to view the web app!

## Running unit tests

See [README.md's "Running unit tests" section](README.md#running-unit-tests)

## Compiling starter code for students

```sh
# Make sure you are in the `project` directory
cd project

# Copy the solution code into a starter code directory
cp -R flask_app/ flask_app_starter/

# Compile solution files to starter files, for example:
python3 compile_starter.py flask_app/api.py flask_app_starter/api.py

# Make sure you are in the root directory of the repo
cd ..

# Create the starter .zip file
make archive

# Remove the zip file and start from scratch if you want
make clean
```
