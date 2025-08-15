# Selenium Testing Suite

This repository contains automated UI tests for [SauceDemo](https://www.saucedemo.com/) using Python, Selenium, and pytest.

## Project Structure

- `tests/` - Contains all test scripts:
  - `test_cart.py` - Tests for cart functionality
  - `test_checkout.py` - Tests for checkout flow
  - `test_login.py` - Parameterized login tests
  - `test_saucedemo.py` - End-to-end login and product checks
  - `test_sorting.py` - Product sorting tests
- `conftest.py` - Pytest fixtures (e.g., Selenium WebDriver setup)
- `assets/` - Static assets (e.g., CSS for HTML reports)
- `report.html` - Generated pytest HTML report
- `.pytest_cache/` - Pytest cache (ignored by git)
- `.gitignore` - Git ignore rules

## Requirements

- Python 3.7+
- Google Chrome browser
- [pip](https://pip.pypa.io/en/stable/)

## Setup

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
    If `requirements.txt` is missing, install manually:
    ```sh
    pip install selenium pytest webdriver-manager pytest-html
    ```

2. (Optional) Create and activate a virtual environment:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

## Running Tests

Run all tests and generate an HTML report:
```sh
pytest --html=report.html
```

## Notes

- ChromeDriver is managed automatically via `webdriver-manager`.
- Test results are saved in `report.html`.
- The `assets/` folder contains CSS for the HTML report.
- `.pytest_cache/`, `assets/`, and `report.html` are git-ignored.

---

Happy Testing!