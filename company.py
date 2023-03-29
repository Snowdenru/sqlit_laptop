
import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.cursor()

create_series_table_query = """
CREATE TABLE Series (
  id INT PRIMARY KEY,
  series TEXT ,
  company_id INT,
  model_id INT   
)
"""

create_company_table_query ="""
CREATE TABLE Company (
  id INT PRIMARY KEY,
  company TEXT  
)
"""

create_model_table_query="""
CREATE TABLE Model (
  id INT PRIMARY KEY,
  model TEXT,
  os_id INT,
  dedicated_id INT  
)
"""

create_os_table_query="""
CREATE TABLE OS (
  id INT PRIMARY KEY,
  OS TEXT 
)"""
create_dedicated_table_query="""
CREATE TABLE Dedicated (
  id INT PRIMARY KEY,
  dedicated TEXT 
)
"""

cursor.execute(create_series_table_query)
cursor.execute(create_company_table_query)
cursor.execute(create_os_table_query)
cursor.execute(create_dedicated_table_query)
cursor.execute(create_model_table_query)

conn.close()



