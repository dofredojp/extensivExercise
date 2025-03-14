# Python API Token Auto Fetcher Exercise

## Overview

This project is a Python-based API client that retrieves an authentication token and fetches data from an API at regular intervals. It is designed with best practices for maintainability and production readiness, including modularization, environment variable management, and logging.

## Features

- Encodes user credentials to Base64.
- Retrieves an authentication token from the API.
- Calls a second API using the token at a set interval.
- Automatically refreshes the token when expired.
- Logs errors and responses for easy debugging.
- Uses environment variables to protect sensitive information.

## Project Structure

```
/api_client_project
│── main.py              # Entry point for the application
│── config.py            # Configuration file for settings
│── utils.py             # Utility functions for API calls and encoding
│── .env                 # Environment variables (excluded from Git)
│── requirements.txt      # Dependencies list
│── .gitignore           # Git ignore rules
│── README.md            # Project documentation
```

## Setup Instructions

### 1. Install Dependencies

Ensure you have Python installed, then install dependencies:

```sh
pip install -r requirements.txt
```

### 2. Set Up and Configure Environment Variables

Create or set up a `.env` file in the root directory

### 3. Run the Project

```sh
python main.py
```

## Usage

- The script encodes the `USER_ID` to Base64 and retrieves a token.
- It then uses this token to call a second API.
- If the token expires, it fetches a new one automatically.
- The process repeats every few seconds (configurable in `config.py`).

## Logging & Debugging

The project uses Python's `logging` module to track API responses and errors. Logs are displayed in the console.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

