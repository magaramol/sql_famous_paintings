### ignore this file 

import os
import pandas as pd
from sqlalchemy import create_engine

# MySQL connection details
user = 'root'
password = 'password'
host = 'localhost'
database = 'painting'

# Path to CSV files
path = '/home/ams/Documents/python/vscode/SQL/sql_famous_paintings/data/'

# List of CSV files to be imported
files = ['artist', 'canvas_size', 'image_link', 'museum_hours', 'museum', 'product_size', 'subject', 'work']

# Create a connection to the MySQL database
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8mb4')

# Loop through each file and import it into the MySQL database
for file in files:
    file_path = os.path.join(path, f'{file}.csv')
    df = pd.read_csv(file_path)
    
    # Ensure the DataFrame uses UTF-8 encoding
    df.to_sql(file, con=engine, if_exists='replace', index=False, method='multi')
    
    print(f"Imported {file}.csv into the {database} database.")

print("All CSV files have been imported successfully.")