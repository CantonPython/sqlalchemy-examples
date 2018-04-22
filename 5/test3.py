from __future__ import print_function
from model import Session, User, Topic, UsernameTaken

session = Session()

# Create a user.
try:
    user = User.create(session, "foobar")
except UsernameTaken:
    print("username is already taken")

# Get a user by id.
user = User.get_by_id(session, 1)
print(user)

# Create a new topic
user = User.get_by_id(session, 1)
topic = Topic.create(session, user, "albatross for sale")
print(topic)

# Upvote a topic
user = User.get_by_id(session, 1)
topic = Topic.get_by_id(session, 1)
topic.upvote(session, user)
print(topic)

