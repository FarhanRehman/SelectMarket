# TODO: average market sentiment
# TODO: SPAC Mentions
# TODO: IPO meantions
# TODO: chart with sentiment analysis compared to price action
# TODO: chart with insider trading compared to price action
# TODO: get module in for schduled tasks
# TODO: In all files specify datatype for function parameters
# TODO: error checking, catching, try/except blocks
# TODO: when a stock enters watchlist 
# TODO: r/wsb METABASE stats 
# TODO: DB opens and closes on every operation, open DB when the program starts, close when it ends
# 1) record its time upon entry into watchlist
# 2) depending on current stock price you can see if the price increased or decreased (represent this in percentages) 

# TODO: set up a virtual environment
# TODO: start commiting code to SelectMarket organization

# Import Libraries
from DataProcessing.organizeData import OrganizeData
from SentimentAnalysis.sentimentAnalysis import SentimentAnalysis
from DataProcessing.cleanData import CleanData
from Database.db import DatabaseManager
from RedditScraper import RedditScraper
import timeit
import time

# Main Program
try:
    with open('Database.db') as f:
        pass
except IOError:
    # DATABASE COMMANDS
    D = DatabaseManager()
    D.setupDatabase()
    # D.insertWatchlist("TSLA", 0.123231, 123, 123)
    # D.incrementWatchlist("TSLA", "POSITIONS")
    # D.updateWatchlistSentiment("TSLA", 0.232123)
    # D.insertWatchlist("CHWY", 0.12321)


# Time program
starttime = timeit.default_timer()

# Get comments and submissions from RedditScraper
subreddit = "WallStreetBets"
Reddit = RedditScraper(subreddit)

# Daily/Weekend discussion thread
# stickiedPost = Reddit.wsbDiscussion()
# comments = Reddit.getComments("kpsy0b", "TOP")
# print(comments)

# while 1:
# comment = Reddit.streamComments()

comment = """
Yeah I like fintech, PYPL/SQ/LSPD are my holdings there, you think I'm missing anything? people heres seem excited about Paysafe? I guess you could kind of count BL/Z in ancillary way as broader Finance space.


For ads I guess social media would be the ones I have for that, FB, SNAP, PINS, TWTR. Really want to get TTD but never had cash available to grab it :(, anything besides that that you'd suggest?
"""
# Clean text using cleanData
CleanedData = CleanData(comment).cleanTextRoundOne()

# Parse cleaned data with organizedData
OrganizedData = OrganizeData(CleanedData).parseTickers()

if OrganizeData != None:
    try:
        for key, value in OrganizedData.items():
            # Get sentiment analysis of parsed data using sentimentAnalysis
            SA = SentimentAnalysis(key).analyze()
            print(f"key: {key}\nValue: {value}\nSA Score: {SA}")
    except Exception as E:
        print(E)     

# time.sleep(10)

print("-------------------------------------------------------")

print("The time difference is :", timeit.default_timer() - starttime)
print("---------------------------------------------------------------")







