# 1) Getting the data - in this case, we'll be scraping data from a website

# Import Libraries
from RedditScraper import RedditScraper 
from nltk import tokenize
import yfinance as yf
import requests
import timeit
import csv
import re


# starttime = timeit.default_timer()
# print("The time difference is :", timeit.default_timer() - starttime)

# TODO: add relative imports & fix file structures
# TODO: Set up CI/CD
# TODO: Set up sqlite databasse (inside DB, keep count of number of mentions and positions)
# TODO: should also recognize tickers by company names
# TODO: start scraping user positions on stocks


class GetData:
    def __init__(self, subreddit):
        # Initialize Variables
        self.subreddit = subreddit
        self.blacklistTickers = ["YOLO", "TOS", "CEO", "CFO", "CTO", "DD", "BTFD", "WSB", "OK", "RH", "KYS", "FD", "TYS", "US", "USA", "IT", "ATH", "RIP", "BMW", "GDP", "OTM", "ATM", "ITM", "IMO", "LOL", "DOJ", "BE", "PR", "PC", "ICE", "TYS", "ISIS", "PRAY", "PT", "FBI", "SEC", "GOD", "NOT", "POS", "COD", "AYYMD", "FOMO", "TL;DR", "EDIT", "STILL", "LGMA", "WTF", "RAW", "PM", "LMAO", "LMFAO", "ROFL", "EZ", "RED", "BEZOS", "TICK", "IS", "DOW" "AM", "PM", "LPT", "GOAT", "FL", "CA", "IL", "PDFUA", "MACD", "HQ", "OP", "DJIA", "PS", "AH", "TL", "DR", "JAN", "FEB", "JUL", "AUG", "SEP", "SEPT", "OCT", "NOV", "DEC", "FDA", "IV", "ER", "IPO", "RISE" "IPA", "URL", "MILF", "BUT", "SSN", "FIFA", "USD", "CPU", "AT", "GG", "ELON", "RSI", "CCP", "EOD", "EOY"]


    # TODO: make this faster
    # TODO: recognize tickers that are misspelled, lowercase, using the company name instead of ticker
    def valtiadeTickers(self, tickers):
        valid = set()
        for ticker in tickers:
            if ticker in self.blacklistTickers:
                tickers.remove(ticker)
            else:
                # search csv file for ticker to check if it is valid
                with open('C:/Users/farha/Documents/GitHub/SelectMarket/SentimentAnalysis/Reddit/STOCKS.csv', 'rt') as csvfile:
                    my_content = csv.reader(csvfile, delimiter=',')
                    for row in my_content:
                        if ticker in row:
                            valid.add(ticker)
 
                # response = requests.get(f'http://finance.yahoo.com/quote/{ticker}')
                # if len(response.history) == 1:
                #     valid.add(ticker)

        return valid

    # TODO: sentiment analysis comment with many tickers

    # This function wil parse all tickers and related text from a submission/comment, and output it in a dictionary/csv
    def parseTickers(self, text):
        # Regex to identify stock tickers, we use a set here to avoid duplicates
        tickers = set(re.findall("(?:(?<=\A)|(?<=\s)|(?<=[$]))([A-Z]{1,5})(?=\s|$|[^a-zA-z])", text))

        # loop through tickers and verify valid ones
        tickers = self.valtiadeTickers(tickers)

        # turn set into dictionary
        tickers = dict.fromkeys(tickers, 0)
        

        if len(tickers) == 1:
            tickers = {tickers[0]: text}
        else:
            # seperate tickers based on sentences
            sentences = tokenize.sent_tokenize(text)

            # assign each ticker the sentence it was included in
            for sentence in sentences:
                for key in tickers:
                    if key in sentence:
                        tickers[key] = sentence
        print(tickers)


r = GetData("WallStreetBets")
r.parseTickers("""Thinking BABA, BIDU, BABA, TCEHY, YY, IQ have decent chance to outgrow FAANG over next 5 years. Throw in TME and HUYA for a little more 🌙 potential.""")






# def validateTicker(self, ticker):
#     try:
#         response = yf.Ticker(ticker)
#         response.info
#         return True
#     except:
#         return False

