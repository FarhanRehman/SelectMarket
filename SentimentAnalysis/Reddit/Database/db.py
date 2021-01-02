# Setup Sqlite3 database

# TODO: fetch latest csv from: https://dumbstockapi.com/stock?format=csv&countries=US, and update database

# Import Libraries
import sqlite3


# Setup connection to database
connection = sqlite3.connect('Database.db')

c = connection.cursor()

# create statistics table
c.execute("""CREATE TABLE statistics (
            comments integer,
            mentions integer,
            positions integer
            )""")


c.execute("INSERT INTO statistics VALUES ('')")

connection.commit()

# close connection
connection.close()