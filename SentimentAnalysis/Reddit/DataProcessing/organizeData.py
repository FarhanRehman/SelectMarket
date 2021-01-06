# 1) Getting the data - in this case, we'll be scraping data from a website

# Import Libraries
from DataProcessing.cleanData import CleanData
from Database.db import DatabaseManager
from collections import defaultdict
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
    def __init__(self, text):
        # Initialize Variables
        self.text = text

    def valtiadeTickers(self, tickers):
        # use set to avoid duplicates   
        valid = set()
        DB = DatabaseManager()
        for ticker in tickers:
            # search DB for ticker to check if it is valid
            if DB.searchString(ticker):
                valid.add(ticker)

        return valid

    # TODO: increment mentions
    # This function wil parse all tickers and related text from a submission/comment, and output it in a dictionary/csv
    def parseTickers(self):   
        # Regex to identify stock tickers, we use a set here to avoid duplicates
        tickers = set(re.findall("(?:(?<=\A)|(?<=\s)|(?<=[$]))([A-Z]{1,5})(?=\s|$|[^a-zA-z])", self.text))

        # loop through tickers and verify valid ones
        tickers = self.valtiadeTickers(tickers)


        # TODO: check out some ways to split into sentences (should seperate by \n as well), check out nltk and regex examples
        sentences = CleanData(self.text).tokenize(self.text)

        # turn set returned from valtiadeTickers() into dictionary
        parsedDict = dict.fromkeys(sentences, tuple())

                
        # Parse text based on how many tickers are in the text
        if len(tickers) > 0:
            # assign each ticker the sentence it was included in
            for key, value in parsedDict.items():
                for ticker in tickers:
                    if ticker in key:
                        parsedDict[key] += ticker, 
            return parsedDict
        else:
            return None


