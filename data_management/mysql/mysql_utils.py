# Import Standard Libraries
import mysql.connector
import pandas as pd

# Create the MySQL client
mysql_client = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="23_SarahMySQL!91",
    database='ecommerce'
)

# Create Cursor
mysql_cursor = mysql_client.cursor()

# Open file
with open('./../queries/select_all_items.sql', 'r') as file:

    # Read query
    query = file.read()

# Query the Database
mysql_cursor.execute(query)

# Retrieve results
results = mysql_cursor.fetchall()

print('Read through MySQL Connector')
print(results[0])

# Query the Database through Pandas
data = pd.read_sql(query, con=mysql_client)

print('Read through Pandas')
print(data.head(1))

