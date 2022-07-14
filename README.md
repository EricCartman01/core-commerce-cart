
# Shopping Cart API

[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org) ![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg) ![FastAPI](https://img.shields.io/badge/fast_api-0.73-blue)

This project aims to provide a shopping cart api for ecommerce purposes

## Enviroments

### Development

### Homolog

## How to use?

### Docker

1. Clone this repository

2. To copy `.env.example` to `.env`, run: `make copy-envs`

3. Build docker image and run migrates: `make build`

4. Run api: `make run`

5. In your browser call: [Swagger Localhost](http://localhost:8000/api/docs)

#### Comands

Executing commands inside the container:

``` bash
make run-bash
```

Generate migration: *

``` bash
make run-migrations name=<MODULE NAME>
```

Additional dependencies: *

``` bash
make run-poetry-add name=<LIB NAME>
```

- Must be inside the container

### Locally

1. Clone this repository.
2. To initialize and install dependencies, run: `make init`
3. To apply the migrations, run: `make migrate`
4. Run: `make run-local`
5. In your browser call: [Swagger Localhost](http://localhost:8000/docs)

Note: To run locally, you must have a database service configured. Docker can be used to
quickly start this service.

Docker command example:

``` bash
docker run --name core-commerce-postgres -e POSTGRES_PASSWORD=core_commerce -e POSTGRES_USER=core_commerce -e POSTGRES_DB=core_commerce -p 5432:5432 -d postgres
```

#### Testing

To test, just run `make test`.
# core-commerce-cart
