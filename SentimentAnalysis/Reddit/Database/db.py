# Import Libraries
import requests
import sqlite3
import pandas

class DatabaseManager:
    def __init__(self):
        # Setup connection to database
        self.connection = sqlite3.connect('Database.db')
        self.cursor = self.connection.cursor()

    def getUpdatedInfo(self):
        # URL to csv
        url = "https://dumbstockapi.com/stock?format=csv&countries=US"

        # Get file, and write to directory
        response = requests.get(url)
        with open('output.csv', 'wb') as file:
            file.write(response.content)

        pandas.read_csv("output.csv").to_sql("STOCKS", self.connection, if_exists='replace', index=False)

        self.connection.commit()

        print("Updating Database: Complete")

        return True


    def setupDatabase(self):
        # create Stocks Table
        self.cursor.execute("CREATE TABLE IF NOT EXISTS STOCKS (TICKER STRING UNIQUE, NAME STRING UNIQUE, IS_ETF STRING UNIQUE, EXCHANGE STRING)")

        # create statistics table
        self.cursor.execute("CREATE TABLE IF NOT EXISTS STATISTICS (COMMENTS INTEGER, MENTIONS INTEGER, POSITIONS INTEGER)")
        self.cursor.execute("INSERT INTO STATISTICS VALUES (0, 0, 0)")
        
        # create watchlist table
        self.cursor.execute("CREATE TABLE IF NOT EXISTS WATCHLIST (TICKER STRING UNIQUE, SENTIMENT REAL, MENTIONS INTEGER, POSITIONS INTEGER)")

        # commit changes
        self.connection.commit()
        
        print("Setting up Database: Complete")

        # update Stocks table
        self.getUpdatedInfo()
        
        return True

    def incrementStatistics(self, column, value=1):
        # UPDATE {Table} SET {Column} = {Column} + {Value} WHERE {Condition}
        self.cursor.execute(f"UPDATE STATISTICS SET {column} = {column} + {value}")
        
        self.connection.commit()

        print(f"Incremented {column} Successfully")

        return True

    def insertWatchlist(self, ticker, sentiment, mentions=0, positions=0):
        # Insert new stock into watchlist
        self.cursor.execute(f"INSERT INTO WATCHLIST (TICKER, SENTIMENT, MENTIONS, POSITIONS) VALUES ('{ticker}', {sentiment}, {mentions}, {positions});")

        # commit changes
        self.connection.commit()

        print(f"Inserted {ticker} Successfully")

        return True
    
    def incrementWatchlist(self, ticker, column):
        # Increment mentions and positions
        # UPDATE Products SET Price = Price + 50 WHERE ProductID = 1
        self.cursor.execute(f"UPDATE WATCHLIST SET {column} = {column} + 1 WHERE TICKER = '{ticker}'")
        # commit changes
        self.connection.commit()

        print(f"Incremented {column} for {ticker} Successfully")

        return True

    def updateWatchlistSentiment(self, ticker, sentiment):
        # update stocks sentient score
        self.cursor.execute(f"UPDATE WATCHLIST SET SENTIMENT = {sentiment} WHERE TICKER = '{ticker}'")
        # commit changes
        self.connection.commit()

        print(f"Updated sentiment score for {ticker} Successfully")

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