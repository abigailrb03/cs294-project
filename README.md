# cs294-project

This is documentation for instructors and course staff.

## About

A new full stack web application project for CS 61A and DATA C88C designed by
Abigail Brooks-Ramirez (@abigailrb03, a.brooks [at] berkeley [dot] edu) and
Rebecca Dang (@phrdang, rdang [at] berkeley [dot] edu), advised by
Profs. Lisa Yan (yanlisa [at] berkeley [dot] edu) and Michael Ball
(ball [at] berkeley [dot] edu) at UC Berkeley through CS 294-189 Teaching at Scale.

[Google Drive materials](https://drive.google.com/drive/folders/1VEHW65rTjXktB3lfmgxmQEFzi4K95ONf?usp=sharing)

- `project.zip` is the student-facing starter code
- CS294: Student Design Doc is the student-facing design doc template for Task 1A
- Design Doc Grading Rubric is the staff-facing rubric for the design doc

> [!NOTE]
> Anyone at UC Berkeley can view the Google Drive. Email the authors if you want more permissions.

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

3. Install [pre-commit](https://pre-commit.com/) git hook scripts:

```sh
uv run pre-commit install
```

## Managing dependencies

`uv` manages all Python versions, dependencies, and virtual environments depending on which directory you are in.
There are 3 virtual environments since each involves separate dependencies:

1. Root directory
2. `src/project/`
3. `src/spotify-data/`

Prefixing commands with `uv run` will ensure that you are using the correct virtual environment.

In order to add or remove dependencies to a virtual environment, use [uv add](https://docs.astral.sh/uv/reference/cli/#uv-add) or [uv remove](https://docs.astral.sh/uv/reference/cli/#uv-remove) in the corresponding directory.

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
