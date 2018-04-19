
"""
SQLAlchemy example 1

Define a table using the sqlalchemy declarative ORM.

"""
from __future__ import print_function
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String)


engine = create_engine("sqlite:///example.db")
Base.metadata.create_all(engine)
