# cs294-project

This is documentation for instructors and course staff.

## About

A new full stack web application project for CS 61A and DATA C88C designed by
Abigail Brooks-Ramirez (@abigailrb03) and Rebecca Dang (@phrdang), advised by
Profs. Lisa Yan and Michael Ball at UC Berkeley through CS 294-189 Teaching at Scale.

## Installation

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/), a cross-platform command line interface (CLI) to manage Python projects, versions, and dependencies. You can install `uv` however you wish but we recommend using the standalone installer by running one of these commands depending on your operating system:
    - MacOS or Unix:

    ```sh
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

    - Windows (run this in PowerShell):

    ```ps
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

2. Install `make`:
    - MacOS (included in Xcode, which you might already have installed):

    ```sh
    xcode-select --install
    ```

    - Windows: Follow [these instructions](https://stackoverflow.com/questions/10265742/how-to-install-make-and-gcc-on-a-mac)

## Make targets

See the `Makefile` for the `make` targets that allow you to perform various actions:

```sh
# Create starter code and .zip for students in .build/ directory
make build

# Remove the .build/ directory
make clean

# Linting and formatting
make lint       # view lint errors
make lint-fix   # fix lint errors
make format     # format code
```
