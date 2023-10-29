# Website Analyzer Flask App    ![Python 3.11.2](https://img.shields.io/badge/python-3.11.2-blue.svg) ![License](https://img.shields.io/badge/license-MIT-blue.svg) ![Status](https://img.shields.io/badge/status-active-brightgreen.svg)
A Flask-based service to retrieve domain-specific information.

## Table of Contents
1. [Features](#features)
2. [Dependencies](#dependencies)
3. [Setup](#setup)
4. [Usage](#usage)
    - [RESTful Endpoint](#restful-endpoint)
    - [WebSocket Service](#websocket-service)
5. [Running the Server](#running-the-server)
6. [Limitations and Caveats](#limitations-and-caveats)
7. [Testing](#testing)
8. [License](#license)

## Features
1. Query domain info via a GET request.
2. Interactive WebSocket for domain data.
3. Built-in URL validation.
4. Multi-threaded for concurrent requests.

## Dependencies
1. Python 3.11.2
2. Refer to requirements.txt for the full list of dependencies.

## Setup
1. Ensure Python is installed.
2. Create a virtual environment:
`python -m venv venv`
3. Install necessary packages in the virtual environment:
`pip install -r requirements.txt`
4. Get an API key from https://www.whoisxmlapi.com/.
5. Set the environment variable (or in the .env file) API_KEY to the API key.

## Usage
### RESTful Endpoint
Retrieve domain info:
`GET /?url=<DOMAIN_NAME>`

Replace `<DOMAIN_NAME>` with the target domain.

### WebSocket Service
1. Connect to the `/ws` endpoint.
2. Initiate a domain session with a JSON containing the `url` key.
3. Send operations using the `operation` key in the message:
    - get_info for basic details.
        ```
        {
            "operation": "get_info"
        }
        ```
    - get_subdomains for subdomains.
        ```
        {
            "operation": "get_subdomains"
        }
        ```
    - get_asset_domains for asset domains.
        ```
        {
            "operation": "get_asset_domains"
        }
        ```

## Running the Server
Launch the server with:

`python <filename>.py`
Access at http://localhost:5000/.

## Limitations and Caveats
No authentication or rate-limiting; not advisable for production usage.
Errors are JSON-formatted with the error key.

## Testing
Run the test suite with:
`python -m pytest`

## License
Open source. See the LICENSE file.
