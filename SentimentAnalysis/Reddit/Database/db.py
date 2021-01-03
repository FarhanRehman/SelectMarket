# Import Libraries
import urllib.request
import requests
import sqlite3
import pandas
import csv

class DatabaseManager:
    def __init__(self):
        # Setup connection to database
        self.connection = sqlite3.connect('Database.db')
        self.cursor = self.connection.cursor()

    def getUpdatedInfo(self):
        # URL to csv
        # url = "https://dumbstockapi.com/stock?format=csv&countries=US"

        # Get file, and write to directory
        # response = requests.get(url)
        # with open('output.csv', 'wb') as file:
        #     file.write(response.content)

        pandas.read_csv("output.csv").to_sql("STOCKS", self.connection, if_exists='replace', index=False)

        self.connection.commit()

        print("update db complete")

        return True


    def setupDatabase(self):
        # create Stocks Table
        self.cursor.execute("CREATE TABLE IF NOT EXISTS STOCKS (TICKER STRING UNIQUE, NAME STRING UNIQUE, IS_ETF STRING UNIQUE, EXCHANGE STRING)")

        # create statistics table
        self.cursor.execute("CREATE TABLE IF NOT EXISTS STATISTICS (COMMENTS INTEGER, MENTIONS INTEGER, POSITIONS INTEGER)")
        
        # commit changes
        self.connection.commit()
        
        print("setup db complete")

        # update Stocks table
        self.getUpdatedInfo()
        
        return True


    def searchString(self, string):
        # SELECT ticker From Stocks WHERE ticker={ticker}
        self.cursor.execute(f"SELECT * FROM Stocks WHERE ticker LIKE '%{string}%'")
        result = self.cursor.fetchone()
        if result:
            return True
        else:
            return False


    def __del__(self):
        self.connection.close()
        print("connection closeed")

        return True