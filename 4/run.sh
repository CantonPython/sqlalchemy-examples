#!/bin/bash
set -e
set -x

rm -f topics.db
python test1.py
sqlite3 topics.db .schema
sqlite3 topics.db 'select * from user'
sqlite3 topics.db 'select * from topic'
sqlite3 topics.db 'select * from user_topic'

python test2.py
