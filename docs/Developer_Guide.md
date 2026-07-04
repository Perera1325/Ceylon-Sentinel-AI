# Developer Guide

Welcome to the Developer Guide for Ceylon Sentinel AI.

## Setup Instructions

1. Clone the repository.
2. Ensure you have Docker and Docker Compose installed.
3. Run `make up` to build and start the containers.
4. Access the backend at `http://localhost:8000/docs`
5. Access the frontend at `http://localhost:3000`

## Code Standards
- We use `black`, `isort`, and `flake8` for Python code.
- We use `ESLint` and `Prettier` for Node/React code.
- Pre-commit hooks are configured. Run `pre-commit install`.

## Running Tests
Run `make test` to execute both backend and frontend tests.
