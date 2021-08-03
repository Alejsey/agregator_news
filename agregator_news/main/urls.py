from django.urls import path

from .views import News

app_name = 'main'
urlpatterns = [
    path('', News, name='news'),
#    path('<str:page>/', othar_page, name='other'),
#    path('login/', BBLoginView, name='login'),
#    path('profile/', profile, name='profile'),
]