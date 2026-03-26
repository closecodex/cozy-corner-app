# Cozy Corner App

A beginner-friendly, modular Python and Flask web application featuring a collection of cozy, funny mini-features:

- **Dog Personality Matcher**: A quirky quiz mapping you to a dog breed.
- **Cat Facts & Images**: Relaxing quotes and (currently placeholder) cat pictures.
- **Book Nook**: Search for your next read from an internal database.
- **Puzzle Time**: A slide/swap puzzle using default or uploaded images.
- **Daily Drawing Prompt**: Generates a random, cozy drawing prompt.
- **Bonus Games**: Classic Snake and Tic-Tac-Toe.

## Setup Instructions

1. Ensure you have Python 3 installed.
2. In the project root, create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
   Open your browser to `http://127.0.0.1:5000`.

## Running the Automated Tests

Automated testing is configured using `pytest` and the Flask test client. These tests verify that all routes load properly (HTTP 200) and that internal features (like Dog Matcher, Book database, etc.) function safely without external APIs.

1. Ensure test dependencies are installed:
   ```bash
   pip install pytest pytest-flask
   ```
2. Navigate to the project root directory.
3. Run the test suite:
   ```bash
   pytest tests/
   ```

*(Additional flags like `-v` (verbose) or `-s` (print output) can be useful for debugging!)*
