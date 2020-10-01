#!/usr/bin/env sh

export PYTHONPATH=.

# Run migrations
alembic upgrade head

# Create initial data in DB
python -m app.initialiser
