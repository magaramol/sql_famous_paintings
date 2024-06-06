import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import chardet

# URL-encode the password   
password = quote_plus("Root@1234")

conn_string = f"mysql+pymysql://root:{password}@localhost/painting"

db = create_engine(conn_string)
conn = db.connect()

#files = ['artist', 'canvas_size', 'image_link', 'museum_hours', 'work','museum', 'product_size', 'subject']


files = ['ipl']



def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

for file in files:
    file_path = f'data/{file}.csv'
    encoding = detect_encoding(file_path)
    df = pd.read_csv(file_path, encoding=encoding)
    df.to_sql(file, con=conn, if_exists='replace', index=False)



"""
Update MySQL Configuration

    Open your MySQL configuration file (usually my.cnf or my.ini).
    Add the following lines under the [mysqld] section:

    ini

[mysqld]
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci

Restart your MySQL server to apply the changes.

"""