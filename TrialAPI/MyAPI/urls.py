from django.urls import path
from django.conf.urls import url
from django.urls.conf import include
from .views import *
urlpatterns = [
    # path('home', home),
    url('home/',home)
    
]