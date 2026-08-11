# Gitar context ingestion sample

This runnable Flask sample supports the Gitar context ingestion blueprint. The blueprint is the primary learning resource.

The application uses a Flask app factory and separate blueprints for its health check and order lifecycle API. The order creation, lookup, and cancellation routes contain intentional error-handling bugs, while the tests cover the happy path so readers can reproduce the blueprint's code review examples.

## Prerequisites

- Python 3.13 or later
- Flask, installed through `requirements.txt`

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --requirement requirements.txt
python -m pytest --quiet
flask --app 'app:create_app()' run
```
