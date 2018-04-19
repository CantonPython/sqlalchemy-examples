
"""
SQLAlchemy example 3

Define a table using the sqlalchemy declarative ORM.
Create another table.
Insert some data to the tables.
Create a 1-n relationship.

"""
from __future__ import print_function
import sys

from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    topics = relationship("Topic", back_populates="author")

    def __init__(self, username):
        self.username = username

class Topic(Base):
    __tablename__ = "topic"
    id = Column(Integer, primary_key=True)
    description = Column(String)
    post_date = Column(DateTime, default=func.now())
    author_id = Column(Integer, ForeignKey("user.id"))
    author = relationship("User", back_populates="topics")

    def __init__(self, description):
        self.description = description

engine = create_engine("sqlite:///example.db")
Base.metadata.create_all(engine)

#
# Example session.
#

Session = sessionmaker(bind=engine)
session = Session()

# Add a user to a topic.
t1 = Topic("and now for something completely different")
t1.author = User("xyzzy")

# Add some topics to a user.
u2 = User("plugh")
u2.topics = [
    Topic("my hovercraft is full of eels"),
    Topic("he is pining for the fjords"),
]

try:
    session.add(t1)
    session.add(u2)
    session.commit()
except Exception as e:
    print("Failed:", e)
    session.rollback()
    sys.exit(1)
