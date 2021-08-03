from bs4 import BeautifulSoup
import requests
import datetime

URL = 'https://lenta.ru/rss/top7'


def find_news_lenta():
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'xml')
    posts = soup.find_all('item')
    for post in posts:
        print(post.find('title').text)
        print(post.find('link'))
        print(post.find('description').text)
        print(post.find('pubDate').text)


find_news_lenta()