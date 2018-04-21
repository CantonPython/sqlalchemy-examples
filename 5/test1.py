
from __future__ import print_function
import sys
from model import Session, User, Topic

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
