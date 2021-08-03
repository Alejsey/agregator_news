import datetime

from django.shortcuts import render
from django.template.loader import get_template
from django.template import TemplateDoesNotExist
from django.http import HttpResponse, Http404
#from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .Get_news import find_news_lenta
from .models import Posts
from bs4 import BeautifulSoup
import requests

URL = 'https://lenta.ru/rss/top7'


'''
def index(req):
    return render(req, 'main/index.html')
'''
'''def othar_page(req, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=req))

class BBLoginView(LoginView):
    template_name = 'main/login.html'


@login_required
def profile(req):
    return render(req, 'main/profile.html')
'''

def News(req):
    find_news_lenta()

    news = Posts.objects.all().order_by('-id')[:7]
    return render(req, 'main/index.html', {'news': news})

