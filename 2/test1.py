from __future__ import print_function
import sys
from model import Session, User, Topic

session = Session()

u1 = User("xyzzy")
t1 = Topic("and now for something completely different")

try:
    session.add(u1)
    session.add(t1)
    session.commit()
except Exception as e:
    print("Failed:", e)
    session.rollback()
    sys.exit(1)
