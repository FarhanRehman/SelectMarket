# TODO: sentiment analysis on reddit comments and submissions
# TODO: recognize option/stock positions: options: ticker, strike price, expiration, entry(optional) stock: ticker, call or put, entry(optional) + bullish sentiment 
# TODO: use kaggle to prep sentiment analysis

# Import Libraries
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from textblob import TextBlob

class SentimentAnalysis:
    def __init__(self, text):
        self.text = text
    
    def analyze(self):
        # self.text = TextBlob(self.text)

        analyzer= SentimentIntensityAnalyzer()
        self.text = analyzer.polarity_scores(self.text)

        return self.text



