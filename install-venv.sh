#!/bin/bash
# This script installs the CMS in a local virtual environment without
# the need for docker or any other virtualization technology. A Postgres
# SQL server is needed to run the CMS.
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install --upgrade setuptools
python3 setup.py develop
