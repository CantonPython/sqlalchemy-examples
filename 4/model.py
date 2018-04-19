"""
SQLAlchemy example

Define some tables using the sqlalchemy declarative ORM.
Insert some data to the tables.
Create a 1-n relationship.
Create an n-n relationship.
"""
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy import ForeignKey, Table
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

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
        if user not in self.voted:
            self.votes += 1
            self.voted.append(user)

engine = create_engine("sqlite:///topics.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
