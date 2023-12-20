# Simple-API

## Purpose
The purpose of this project is to create a simple API providing some basic CRUD endpoints.

## Setup
Prerequisites:
- Python 3

To set up the project, follow these steps:

1. Clone the repository:
    - via SSH: `git clone git@github.com:bennoheld/simple-api.git`
    - via HTTPS: `https://github.com/bennoheld/simple-api.git`
2. Navigate to the project directory: `cd simple-api`
3. Create a virtual environment: `python3 -m venv venv`
4. Activate the virtual environment:
    - For Windows: `venv\Scripts\activate`
    - For macOS/Linux: `source venv/bin/activate`
5. Install the project dependencies: `pip install -r requirements.txt`
6. Run the application: `python app.py`

## Configuration
The service can be configured using environment variables. You can modify the following variables:

- `API_HOST`: The Host URL of the API to listen to. Defaults to `0.0.0.0`
- `API_PORT`: The Host Port of the API to listen to. Defaults to `5003`

