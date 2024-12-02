# Advent of Code Template

Advent of Code Template is a Python GitHub template designed for the
annual [Advent of Code](https://adventofcode.com/events) challenge.

Features include:

- Source code and test templates that represent one day in the challenge
- Helper function used to read each day's text file.
- Formatting and linting pre-commit checks using [Black](https://pypi.org/project/black/)
  and [Flake8](https://pypi.org/project/flake8/)

## Installation

### Create Virtual Environment (Optional)

Highly recommend creating a new virtual environment using

```sh
python -m venv /path/to/new/virtual/environment
````

and activating it with

```sh
<venv>\Scripts\Activate.ps1
```

### Install Packages

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required libraries.

```sh
pip3 install -r requirements-dev.txt
```

## Usage

1. Copy and rename template for each day
2. Rename import path in each day's test directory to match the src directory
3. Write code to calculate answer
4. Execute code to generate answer to Advent of Code challenge

## License

[MIT](https://choosealicense.com/licenses/mit/)
