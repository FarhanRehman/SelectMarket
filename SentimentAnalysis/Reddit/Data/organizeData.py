# 1) Getting the data - in this case, we'll be scraping data from a website

# Import Libraries
from Database.DB import DatabaseManager
from cleanData import CleanData
import yfinance as yf
import timeit
import re

# starttime = timeit.default_timer()
# print("The time difference is :", timeit.default_timer() - starttime)

# TODO: make this faster
# TODO: Set up CI/CD
# TODO: should also recognize tickers by company names
# TODO: recognize tickers that are misspelled, lowercase, using the company name instead of ticker


class OrganizeData:
    def __init__(self, subreddit):
        # Initialize Variables
        pass

    def valtiadeTickers(self, tickers):
        valid = set()
        DB = DatabaseManager()
        for ticker in tickers:
            if ticker not in self.blacklistTickers:
                # is it faster to search many at a time or one by one?
                # search DB for ticker to check if it is valid
                if DB.searchString(ticker):
                    valid.add(ticker)

        return valid

    # TODO: increment mentions

    # This function wil parse all tickers and related text from a submission/comment, and output it in a dictionary/csv
    def parseTickers(self, text):
        # GET CLEANED DATA HERE
        text = CleanData(text)

        print(text)
        
        # Regex to identify stock tickers, we use a set here to avoid duplicates
        tickers = set(re.findall("(?:(?<=\A)|(?<=\s)|(?<=[$]))([A-Z]{1,5})(?=\s|$|[^a-zA-z])", text))

        # loop through tickers and verify valid ones
        tickers = self.valtiadeTickers(tickers)

        # turn set returned from valtiadeTickers() into dictionary
        tickers = dict.fromkeys(tickers, 0)
        
        # Parse text based on how many tickers are in the text
        if len(tickers) == 1:
            tickers = {tickers[0]: text}
        else:

            # TODO: check out some ways to split into sentences (should seperate by \n as well), check out nltk and regex examples
            # https://stackoverflow.com/questions/4576077/how-can-i-split-a-text-into-sentences

            # seperate tickers based on sentences
            # sentences = tokenize.sent_tokenize(text)
            # print(sentences)

            sentences = CleanData.split_into_sentences(text)
            # print(sentences)

            # TODO: if ticker appears twice it will overright previous text so find a fix for that
            # assign each ticker the sentence it was included in
            for sentence in sentences:
                for key in tickers:
                    if key in sentence:
                        tickers[key] = sentence
        return tickers


r = GetData("WallStreetBets")
asd = r.parseTickers()
print(asd)