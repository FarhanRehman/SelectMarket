# This is a sentiment analysis program that parses the tweets fetched from Twitter using Python

# Import Libraries
import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd 
import numpy as np
import re
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

# Load the dataset


