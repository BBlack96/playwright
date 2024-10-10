# Playwright Python Project

## Description
This project is a template for writing automated tests for web applications using [Playwright](https://playwright.dev/python/) in Python. 
Uses Page Object Model (POM) structure for ease of scaling and maintenance.

## Project Structure
The project is organized as follows:
- `base/` - contains base classes for pages and tests.
  - `base_page.py` - base class for all pages, containing common methods.
  - `base_test.py` - base class for all tests.
- `config/` - holds configuration files.
  - `config.py` - project settings, such as URLs for testing.
- `pages/` - contains page definitions and locators.
  - `locators/` - element locators for each page.
  - `main_page.py` - class for the main page of the application.
  - `elements_page.py` - class for the page with elements.
- `tests/` - contains test scripts.
  - `tests_main_page.py` - tests for the main page.

## Requirements
The project uses the following dependencies, listed in `requirements.txt`:
- Python 3.12 or higher
- Playwright 1.47.0
- Pytest 8.3.3
- Pytest-Playwright 0.5.2
- Other dependencies are listed in `requirements.txt`.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/BBlack96/playwright.git
2. Navigate to the project directory:
   ```bash
   cd playwright
3. Install the dependencies:
   ```bash
    pip install -r requirements.txt
4. Install browsers for Playwright:
   ```bash
   playwright install
   
## Usage

To run all tests, use the following command:
```bash
pytest
```
To run a specific test:
```bash
pytest tests/tests_main_page.py
```

## Configuration

The project uses the configuration file `config/config.py` to define environment settings, such as the application URL. 
Additionally, the `.env` file is used to store sensitive information and environment variables.