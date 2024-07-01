#!/bin/bash

# DB Migration
poetry run python -m api.migrate_db

# uvicorn Server
poetry run uvicorn api.main:app --host 0.0.0.0

# for Hot Reload
# poetry run uvicorn api.main:app --host 0.0.0.0 --reload