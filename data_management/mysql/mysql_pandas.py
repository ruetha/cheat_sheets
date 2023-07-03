import pandas as pd
from sqlalchemy import create_engine

# Create the SQLAlchemy engine
engine = create_engine('mysql+mysqlconnector://root:23_SarahMySQL!91@localhost:3306/ecommerce')

# Read the query from the file
with open("./../queries/select_all_items.sql", "r") as file:
    query = file.read()

# Execute the query and retrieve results into a DataFrame
data = pd.read_sql_query(query, con=engine)

# Display the DataFrame
print(data)

# Read the query from the file
with open("./../queries/select_order_lamps.sql", "r") as file:
    query = file.read()

# Execute the query and retrieve results into a DataFrame
lamp_data = pd.read_sql_query(query, con=engine)

# Display the DataFrame
print(lamp_data)
