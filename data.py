
import pandas as pd
from sqlalchemy import create_engine

mysql_engine = create_engine()

conn_string='mysql://{0}:{1}@{2}:{3}'.format(root, Root@1234, localhost, 3306)
#conn_string = 'mysql://user:admin@localhost/painting'
db = create_engine(conn_string)
conn = db.connect()