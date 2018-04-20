from __future__ import print_function
from model import Session, User, Topic

session = Session()

def query_by_name(name):
    print("query_by_name")
    user = session.query(User).filter_by(username=name).first()
    if user:
        print(user)
    else:
        print("username {0} was not found")

def query_by_id(id_):
    print("query_by_id")
    topic = session.query(Topic).filter_by(id=id_).one() # raises exc if not found
    print(topic)
    print("who voted:")
    for user in topic.voted:
        print(user.username)

def list_stuff():
    print("list_stuff")
    for user in session.query(User).all():
        print(user)
        for topic in user.topics:
            print("  ", topic)


def list_stuff_with_join():
    print("list_stuff_with_join")
    for user,topic in session.query(User,Topic).join(Topic).all():
        print(user, topic)

if __name__ == "__main__":
    query_by_name("xyzzy")
    query_by_id(1)
    list_stuff()
    list_stuff_with_join()
