#
# sqlalchemy basic core examples
#

from __future__ import print_function
from model import engine, vote_table

# Example basic usage of the core engine to execute raw sql. Application code
# would normally use the ORM or sql expression language constructs.
connection = engine.connect()
result = connection.execute('select * from user_topic')
for row in result:
    print(row)
connection.close()

# Same query, but with basic sql expression language constructs make it
# more pythonic.
select = vote_table.select()
result = engine.execute(select)
for row in result:
    print(row)
