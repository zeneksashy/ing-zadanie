# ING Zadanie

## Author: Gracjan Zeniuk

[![Run Tests via Pytest](https://github.com/zeneksashy/ing-zadanie/actions/workflows/run_tests.yaml/badge.svg)](https://github.com/zeneksashy/ing-zadanie/actions/workflows/run_tests.yaml)

## Project Overview

This project contains automated browser tests for the ING website using [pytest](https://pytest.org/) and [Playwright](https://playwright.dev/python/).

## Requirements

- Python 3.13+
- [Poetry](https://python-poetry.org/) dependency management
- [pytest](https://pytest.org/) test runner
- [Playwright](https://playwright.dev/python/) webdriver

## Installation

1. **Install dependencies using Poetry:**
   ```bash
   poetry install
   ```

2. **Install Playwright browsers:**
   ```bash
   poetry run playwright install
   ```

## Running the Tests

To run all tests, use:
```bash
poetry run pytest
```

To run tests for given browser add --browser param

```bash
poetry run pytest --browser chrome
```

This will execute the test suite located in the `tests/` directory.

