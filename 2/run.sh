#!/bin/bash
set -e
set -x

python test.py
sqlite3 topics.db .schema
sqlite3 topics.db 'select * from user'
sqlite3 topics.db 'select * from topic'
