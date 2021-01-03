# TODO: average market sentiment
# TODO: SPAC Mentions
# TODO: chart with sentiment analysis compared to price action
# TODO: chart with insider trading compared to price action
# TODO: get module in for schduled tasks
# TODO: In all files specify datatype for function parameters
# TODO: error checking, catching, try/except blocks
# TODO: when a stock enters watchlist 
# 1) record its time upon entry into watchlist
# 2) depending on current stock price you can see if the price increased or decreased (represent this in percentages) 


# Import Libraries
from DataProcessing.organizeData import OrganizeData
from SentimentAnalysis import sentimentAnalysis
from DataProcessing.cleanData import CleanData
from Database.db import DatabaseManager
from RedditScraper import RedditScraper
import timeit

# Main Program

# Get comments and submissions from RedditScraper

# Time program
starttime = timeit.default_timer()

subreddit = "WallStreetBets"
Reddit = RedditScraper(subreddit)

# # Sort
# commentSort = ["top", "best", "controversial", "Q&A"]
# # Time Filter
# timeFilters = ["week", "hour", "day",]

# Daily/Weekend discussion thread
stickiedPost = Reddit.wsbDiscussion()
comments = Reddit.getComments("koiz6w", "top")

# print(comments)

for comment in comments:
    # Clean text using cleanData
    CleanedData = CleanData(comment).cleanText()
    
    # Parse cleaned data with organizedData
    OrganizedData = OrganizeData(CleanedData).parseTickers()
    print(OrganizedData)

    print("-------------------------------------------------------")

print("The time difference is :", timeit.default_timer() - starttime)
print("---------------------------------------------------------------")



# Get sentiment analysis of parsed data using sentimentAnalysis


# DATABASE COMMANDS
# D = DatabaseManager()
# D.setupDatabase()
# D.insertWatchlist("TSLA", 0.123231, 123, 123)
# D.incrementWatchlist("TSLA", "POSITIONS")
# D.updateWatchlistSentiment("TSLA", 0.232123)
# D.insertWatchlist("CHWY", 0.12321)




