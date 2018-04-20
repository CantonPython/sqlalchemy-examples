#!/bin/bash
set -e
set -x

python test1.py
sqlite3 topics.db .schema
sqlite3 topics.db 'select * from user'
sqlite3 topics.db 'select * from topic'

python test2.py
