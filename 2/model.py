"""
SQLAlchemy example

Define some tables using the sqlalchemy declarative ORM.
Insert some data to the tables.
"""
import hashlib
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def hash(value):
    md5 = hashlib.md5()
    md5.update(value)
    return md5.hexdigest()

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String)
    passwd = Column(String)

    def __init__(self, username, email='', passwd=''):
        self.username = username
        self.email = email
        self.passwd = hash(passwd)

class Topic(Base):
    __tablename__ = "topic"
    id = Column(Integer, primary_key=True)
    description = Column(String)
    post_date = Column(DateTime, default=func.now())

    def __init__(self, description):
        self.description = description

engine = create_engine("sqlite:///topics.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
