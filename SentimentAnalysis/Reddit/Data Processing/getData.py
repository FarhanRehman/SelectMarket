# 1) Getting the data - in this case, we'll be scraping data from a website

# Import Libraries
from RedditScraper import RedditScraper 
import requests
import timeit
import yfinance as yf
import time
import re

# starttime = timeit.default_timer()
# print("The time difference is :", timeit.default_timer() - starttime)


# TODO: Set up sqlite databasse (inside DB, keep count of number of mentions and positions)
# TODO: should also recognize tickers by company names


# TODO: start scraping user positions on stocks


class GetData:
    def __init__(self, subreddit):
        # Initialize Variables
        self.subreddit = subreddit
        self.blacklistTickers = ["YOLO", "TOS", "CEO", "CFO", "CTO", "DD", "BTFD", "WSB", "OK", "RH", "KYS", "FD", "TYS", "US", "USA", "IT", "ATH", "RIP", "BMW", "GDP", "OTM", "ATM", "ITM", "IMO", "LOL", "DOJ", "BE", "PR", "PC", "ICE", "TYS", "ISIS", "PRAY", "PT", "FBI", "SEC", "GOD", "NOT", "POS", "COD", "AYYMD", "FOMO", "TL;DR", "EDIT", "STILL", "LGMA", "WTF", "RAW", "PM", "LMAO", "LMFAO", "ROFL", "EZ", "RED", "BEZOS", "TICK", "IS", "DOW" "AM", "PM", "LPT", "GOAT", "FL", "CA", "IL", "PDFUA", "MACD", "HQ", "OP", "DJIA", "PS", "AH", "TL", "DR", "JAN", "FEB", "JUL", "AUG", "SEP", "SEPT", "OCT", "NOV", "DEC", "FDA", "IV", "ER", "IPO", "RISE" "IPA", "URL", "MILF", "BUT", "SSN", "FIFA", "USD", "CPU", "AT", "GG", "ELON", "RSI", "CCP", "EOD", "EOY"]

    def valtiadeTickers(self, ticker):
        response = requests.get(f'http://finance.yahoo.com/quote/{ticker}')
        
        if len(response.history) > 1:
            return False
        else:
            return True


    # TODO: make this faster
    # TODO: sentiment analysis comment with many tickers
    # TODO: function does not work with tikers in lowercase
    # This function wil parse all tickers and related text from a submission/comment, and output it in a dictionary/csv
    def parseTickers(self, text):
        # Regex to identify stock tickers
        tickers = re.findall("(?:(?<=\A)|(?<=\s)|(?<=[$]))([A-Z]{1,5})(?=\s|$|[^a-zA-z])", text)
        parsedText = {}

        # remove duplicates from list
        seen = set()
        tickers[:] = [item for item in tickers if item not in seen and not seen.add(item)]

        # loop through tickers and verify valid ones
        for ticker in tickers:
            if ticker in self.blacklistTickers:
                tickers.remove(ticker)
            elif self.valtiadeTickers(ticker) == False:
                tickers.remove(ticker)
        

        # Clean the data
        text = text.replace(",", "")
        text = text.replace(".", "")

        # Assign every ticker in text the same text
        for ticker in tickers:
            parsedText[ticker] = text


                        
        print(parsedText)


r = GetData("WallStreetBets")
r.parseTickers("""This week I’ve picked up more shares of CHWY and BABA, while also adding to my TTD position.

""")






# def validateTicker(self, ticker):
#     try:
#         response = yf.Ticker(ticker)
#         response.info
#         return True
#     except:
#         return False


# if len(tickers) == 1:
#     parsedText = {tickers[0]: text}
# else:
#     # all words to ticker
#     sentence = ""
#     for word in text.split():
#         if word.upper() in tickers:
#             print("TICKER:", word)
#             if len(sentence.split()) > 1:
#                 parsedText[ticker] = sentence
#                 print(sentence)
                
#                 sentence = ""
            
#         else:
#             sentence += f" {word}"