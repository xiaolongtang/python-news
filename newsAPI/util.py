import requests
from bs4 import BeautifulSoup
import json

def get_news():
    res = requests.get("https://news.google.com/?hl=en-US&gl=US&ceid=US:en")
    soup = BeautifulSoup(res.text, "html.parser")
    newsList = []
    for item in soup.select(".NiLAwe"):
        news_title = (item.text)
        newsList.append(news_title)
    dict = {'news': newsList}
    result = json.dumps(dict)
    return result