# TODO: main file for running sentiment analysis on reddit comments and submissions
# TODO: run backtests on watchlists stocks:
# TODO: average market sentiment
# TODO: SPAC Mentions
# TODO: chart with sentiment analysis compared to price action
# TODO: chart with insider trading compared to price action
# TODO: use kaggle to prep sentiment analysis
# TODO: get module in for schduled tasks
# TODO: In all files specify datatype for function parameters
# TODO: error checking, catching, try/except blocks

# when a stock enters watchlist 
# 1) record its time upon entry into watchlist
# 2) depending on current stock price you can see if the price increased or decreased (represent this in percentages) 

# you can use this program for 
# # r/WSB
# r/investing
# r/SPAC



# Import Libraries
from Database.db import DatabaseManager
from Data import organizeData
from Data import cleanData
from SentimentAnalysis import sentimentAnalysis
import RedditScraper

# Main Program

# Get comments and submissions from RedditScraper
subreddit = "WallStreetBets"
Reddit = RedditScraper()


# Sort
commentSort = ["top", "best", "controversial", "Q&A"]
# Time Filter
timeFilters = ["week", "hour", "day",]

# Daily/Weekend discussion thread
stickiedPost = reddit.subreddit(SUBREDDIT).sticky()
getComments(stickiedPost, "top")
comments = getAllComments("kn2wyw")


# Top/Hot submissions of the week and day
for timeFilter in range(len(timefilter)):
    topSubmissions(reddit, timeFilter)
    hotSubmissions(reddit, timeFilter)
    newSubmissions(reddit, timeFilter)
    controversialSubmissions(reddit, timeFilter)
    risingSubmissions(reddit, timeFilter)


# Clean text using cleanData

# Parse cleaned data with organizedData

# Get sentiment analysis of parsed data using sentimentAnalysis


# DATABASE COMMANDS
# D = DatabaseManager()
# D.setupDatabase()
# D.insertWatchlist("TSLA", 0.123231, 123, 123)
# D.incrementWatchlist("TSLA", "POSITIONS")
# D.updateWatchlistSentiment("TSLA", 0.232123)
# D.insertWatchlist("CHWY", 0.12321)




