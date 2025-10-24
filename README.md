# cs294-project

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
mkdir instance
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
mkdir instance
flask --app __init__.py init-db
```

## Running the web app locally

```sh
cd project/flask_app
flask --app __init__.py --debug run
```

Then go to [http://127.0.0.1:5000/songs](http://127.0.0.1:5000/songs) to view the songs in the front end!
