# 2025 Challenge
- [2025 Challenge](#2025-challenge)
- [Dev environment](#dev-environment)
- [Running tests, formatting, and linting](#running-tests-formatting-and-linting)
  - [Testing](#testing)
  - [Formatting](#formatting)
  - [Linting](#linting)
- [Running the app](#running-the-app)

# Dev environment
The fastest way to get moving is to use a Github Codespace. The default dev container satisfies the requirements of this project.

This project uses UV (https://docs.astral.sh/uv/) to manage Python packages and Dependencies.  Install UV into the dev container following these [instructions](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer).

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Once UV is installed, use it to install dependencies: `uv sync`

# Running tests, formatting, and linting
## Testing
Unit tests are via *pytest*.  From the root of the repo, run `uv run pytest`.

## Formatting
Formatting uses *ruff*.  Run `uv run ruff format`.

## Linting
Linting uses *ruff*.  Run `uv run ruff check` to report errors and `uv run ruff check --fix` to fix errors.

# Running the app
This project is set up as a CLI tool using *Typer*.

To see help, run: `uv run main.py --help`
To see subcommand help, run: `uv run main.py [subcommand] --help`
To run a specific day type: `uv run main.py day1 day1.txt`