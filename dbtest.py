from django.conf import settings
from django.db import connections
from django.db.utils import OperationalError

db_conn = connections['mysql']
c = db_conn.cursor()
c.execute("select * from blog_post")
c.fetchone()
db_conn.close()

db_conn = connections['firebird']
c = db_conn.cursor()
c.execute("select * from asientos")
c.fetchone()
db_conn.close()

