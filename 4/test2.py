from __future__ import print_function
import sys
from model import Session, User, Topic

session = Session()

# Query by name.
print("looking for user 'xyzzy'")
u = session.query(User).filter_by(username='xyzzy').one()
print("username={0}, id={1}".format(u.username, u.id))

# Query by id.
print("looking for topic 1")
t = session.query(Topic).filter_by(id=1).one()
print("topic={0}".format(t.description))
print("voted for topic 1")
for user in t.voted:
    print(user.username)

# Get all.
for user in session.query(User).all():
    print("username={u.username}, id={u.id}".format(u=user))
    for topic in user.topics:
        print("  {t.votes} {t.description}".format(t=topic))
