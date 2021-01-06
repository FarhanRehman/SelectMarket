# Description: News Aggregation

# Import Libraries
import requests
from bs4 import BeautifulSoup

url = "http://www.yahoo.com/news/rss"

response = requests.get(url)

soup = BeautifulSoup(response.content, features="xml")

items = soup.findAll('item')

for item in items:
    news_item = {}
    news_item['title'] = item.title.text
    news_item['description'] = item.description.text
    news_item['link'] = item.link.text
    news_item['image'] = item.content['url']
    news_item.append(news_item)