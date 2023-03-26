#! /usr/bin/env bash

export PYTHONPATH=$PWD

# Let the DB start
python3 app/backend_pre_start.py

# Create initial data in DB
python3 app/initial_data.py