# Bookstore

Bookstore APP from backend Python course from EBAC.

## Description

This is a backend application called Bookstore where an API was created with Django Rest Framework and deployed in the cloud on PythonAnywhere using CI/CD pipelines.

### Prerequisites

- Python 3.10.0 or later
- [Poetry](https://python-poetry.org/docs/#installation)
- [Docker](https://docs.docker.com/get-docker/) & [docker-compose](https://docs.docker.com/compose/install/)

## Installation

1. Clone this project:

    ```shell
    git clone https://github.com/guscassiano/bookstore.git
    ```

2. Install dependencies:

    ```shell
    cd bookstore
    poetry install
    ```

## Quickstart

1. Run local dev server:

    ```shell
    poetry run python manage.py migrate
    poetry run python manage.py runserver
    ```

2. Run docker dev server environment:

    ```shell
    docker-compose up -d --build
    docker-compose exec web python manage.py migrate
    ```

3. Run tests inside of Docker:

    ```shell
    docker-compose exec web python manage.py test
    ```

## Deployment

The project is deployed on PythonAnywhere:

- [bookstore API product](https://guscassiano.pythonanywhere.com/bookstore/v1/product/)
- [bookstore API order](https://guscassiano.pythonanywhere.com/bookstore/v1/order/)

## Contribution

Feel free to contribute to this project by creating issues or submitting pull requests.

