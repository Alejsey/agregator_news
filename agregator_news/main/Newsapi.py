from newsapi import NewsApiClient
from bs4 import BeautifulSoup
import requests

# api token for connection  apinews.org
API_token = 'c722d3ad101244ddbe6df22a78070bcf'

URL = 'https://lenta.ru/rss/top7'
page = requests.get(URL)


news = NewsApiClient(API_token)

# /v2/top-headlines
top_headlines = news.get_top_headlines(sources='bbc-news, the-verge',
                                       language='en'
                                      )


#bs = BeautifulSoup(top_headlines, features='xml')
# /v2/everything
'''
all_articles = news.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)'''

# /v2/top-headlines/sources
# sources = news.get_sources()

data = top_headlines.get('articles')