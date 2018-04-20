from __future__ import print_function
import sys
from model import Session, User, Topic

session = Session()

u = session.query(User).filter_by(username='xyzzy').one()
print("username={0}, id={1}".format(u.username, u.id))

t = session.query(Topic).filter_by(id=1).one()
print("topic={0}".format(t.description))
