import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# URL-encode the password
password = quote_plus("Root@1234")

conn_string = f"mysql+pymysql://root:{password}@localhost/painting"

db = create_engine(conn_string)
conn = db.connect()



#files = ['work']

files = ['artist', 'canvas_size', 'image_link', 'museum_hours', 'museum', 'product_size', 'subject']


#  files = ['artist', 'canvas_size', 'image_link', 'museum_hours', 'museum', 'product_size', 'subject', 'work']

for file in files:
    df = pd.read_csv(f'data/{file}.csv')
    df.to_sql(file,con=conn,if_exists='replace',index=False)