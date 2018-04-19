
"""
SQLAlchemy example 2

Define a table using the sqlalchemy declarative ORM.
Create another table.
Insert some data to the tables.

"""
from __future__ import print_function
import sys

from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)

    def __init__(self, username):
        self.username = username

class Topic(Base):
    __tablename__ = "topic"
    id = Column(Integer, primary_key=True)
    description = Column(String)
    post_date = Column(DateTime, default=func.now())

    def __init__(self, description):
        self.description = description

engine = create_engine("sqlite:///example.db")
Base.metadata.create_all(engine)

#
# Example session.
#

Session = sessionmaker(bind=engine)
session = Session()

u1 = User("xyzzy")
t1 = Topic("and now for something completely different")

try:
    session.add(u1)
    session.add(t1)
    session.commit()
except Exception as e:
    print("Failed:", e)
    session.rollback()
    sys.exit(1)
