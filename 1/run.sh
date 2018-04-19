#!/bin/bash
set -e
set -x

python model.py
sqlite3 topics.db .schema
