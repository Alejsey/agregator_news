import json

from bs4 import BeautifulSoup
import requests
from .models import Posts
from .Newsapi import data
from .parser import URL
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agregator_news.settings')

import django
django.setup()


def api_get_news():
    for record in data:

        Posts.objects.create(title=record['title'], link=record['url'], date=record['publishedAt'], text=record['content'])


def find_news_lenta():
    list = []
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, features='xml')
    posts = soup.find_all('item')
    for post in posts:
        title = post.find('title').text
        url = post.find('link').text
        text = post.find('description').text
        date = post.find('pubDate').text
        article = {

            'title': title,
            'url': url,
            'text': text,
            'date': date

        }
        list.append(article)
    for record in list:

        Posts.objects.create(title=record['title'], link=record['url'], date=record['date'], text=record['text'])


'''
@register.inclusion_tag('Wd5PageApp/rssfeed.djhtml')
def pull_feed(feed_url, posts_to_show=5):
    try:
        feed = feedparser.parse(feed_url)
        posts = []
        for i in range(posts_to_show):
            pub_date = feed['entries'][i].updated_parsed
            published = datetime.date(pub_date[0], pub_date[1], pub_date[2] )
            posts.append({
                          'title': feed['entries'][i].title,
                          'summary': feed['entries'][i].summary,
                          'link': feed['entries'][i].link,
                          'date': published,
                          })
    except:
        pass
    return {'posts': posts}
'''

