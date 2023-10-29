# Domain Info Service
A Flask-based service to retrieve domain-specific information.

## Table of Contents
1. [Features](#features)
2. [Dependencies](#dependencies)
3. [Setup](#setup)
4. [Usage](#usage)
    4.1. [RESTful Endpoint](#restful-endpoint)
    4.2. [WebSocket Service](#websocket-service)
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
2. Install necessary packages:
`pip install -r requirements.txt`
3. Get an API key from https://www.whoisxmlapi.com/.
4. Set the environment variable (or in the .env file) API_KEY to the API key.

## Usage
### RESTful Endpoint
Retrieve domain info:
`GET /?url=<DOMAIN_NAME>`

Replace `<DOMAIN_NAME>` with the target domain.

### WebSocket Service
1.Connect to the `/ws` endpoint.
2. Initiate a domain session with a JSON containing the `url` key.
3. Send operations using the `operation` key:
- get_info for basic details.
- get_subdomains for subdomains.
- get_asset_domains for asset domains.

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