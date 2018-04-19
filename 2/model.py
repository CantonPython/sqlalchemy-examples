
"""
SQLAlchemy example 2

Define a table using the sqlalchemy declarative ORM.
Insert some data to the table.

"""
from __future__ import print_function
import sys

from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)

    def __init__(self, username):
        self.username = username


engine = create_engine("sqlite:///example.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

u1 = User("xyzzy")

try:
    session.add(u1)
    session.commit()
except Exception as e:
    print("Failed:", e)
    session.rollback()
    sys.exit(1)
