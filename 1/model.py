
"""
SQLAlchemy example 1

Define a table using the sqlalchemy declarative ORM.

"""
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)


engine = create_engine("sqlite:///example.db")
Base.metadata.create_all(engine)
