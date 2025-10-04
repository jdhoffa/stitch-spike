# 🪡 Stitch

[![Test DB service](https://github.com/RMI/web-api-poc/actions/workflows/db-test.yml/badge.svg?branch=main)](https://github.com/RMI/web-api-poc/actions/workflows/db-test.yml)

[![Lint API Service](https://github.com/RMI/web-api-poc/actions/workflows/api-lint.yml/badge.svg?branch=main)](https://github.com/RMI/web-api-poc/actions/workflows/api-lint.yml)
[![Test API service](https://github.com/RMI/web-api-poc/actions/workflows/api-test.yml/badge.svg?branch=main)](https://github.com/RMI/web-api-poc/actions/workflows/api-test.yml)

[![Test service integration](https://github.com/RMI/web-api-poc/actions/workflows/integration-test.yml/badge.svg?branch=main)](https://github.com/RMI/web-api-poc/actions/workflows/integration-test.yml)
[![Docker](https://github.com/RMI/web-api-poc/actions/workflows/api-docker-build-and-push.yml/badge.svg?branch=main)](https://github.com/RMI/web-api-poc/actions/workflows/api-docker-build-and-push.yml)

Stitch is a platform that integrates diverse oil & gas asset datasets, applies AI-driven enrichment with human review, and delivers curated, trustworthy data.

> **Note:** This repository represents an **early-stage spike / MVP**. It is intended to **test technical assumptions and validate architecture quickly**, not to serve as the final production implementation. Code and structure may change substantially as the design matures.

## Running the application

### Setup

1. Clone the Repo

```sh
git clone https://github.com/RMI/stitch-spike
cd stitch-spike
```

2. Create an `.env` file to store the desired API key, (internal) API port, and DB port.
```sh
cp .env.example .env
```

### Run the services with docker compose

```sh
# build the images
docker compose build

# run the containers
docker compose up --detach

# do both
docker compose up --detach --build
```

The API and API documentation will be accessible at http://localhost:8000.

### Make a request from the API

```sh
curl -X 'GET' \
  'http://localhost:8000/scenarios' \
  -H 'accept: application/json' \
  -H 'X-API-Key: abc123'
```

Defaults to the API key "abc123", but an alternate key (matching what is in your `.env` file) can be input and submitted on the page.

### Shutdown the docker container

```sh
docker compose down

# also delete the database volume when shutting down the container
docker compose down --volumes
```

## License
 This project is licensed under the [MIT License](LICENSE.txt) 
