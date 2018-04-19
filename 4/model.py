
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
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy import ForeignKey, Table
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

vote_table = Table(
    "user_topic",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id")),
    Column("topic_id", Integer, ForeignKey("topic.id")),
)

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    topics = relationship("Topic", back_populates="author")
    voted = relationship("Topic", back_populates="voted", secondary=vote_table)

    def __init__(self, username):
        self.username = username

class Topic(Base):
    __tablename__ = "topic"
    id = Column(Integer, primary_key=True)
    description = Column(String)
    post_date = Column(DateTime, default=func.now())
    author_id = Column(Integer, ForeignKey("user.id"))
    author = relationship("User", back_populates="topics")
    votes = Column(Integer, default=0)
    voted = relationship("User", back_populates="voted", secondary=vote_table)

    def __init__(self, description):
        self.description = description

    def upvote(self, user):
        if user in self.voted:
            print("already voted")
        else:
            self.votes += 1
            self.voted.append(user)

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

# Have an upvote.
try:
    t1.upvote(u2)
    session.commit()
except Exception as e:
    print("Failed:", e)
    session.rollback()
    sys.exit(1)

# Only one to a customer.
try:
    t1.upvote(u2)
    session.commit()
except Exception as e:
    print("Failed:", e)
    session.rollback()
    sys.exit(1)
