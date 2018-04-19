#!/bin/bash
set -e
set -x

python model.py
sqlite3 example.db .schema
sqlite3 example.db 'select * from user'
sqlite3 example.db 'select * from topic'
