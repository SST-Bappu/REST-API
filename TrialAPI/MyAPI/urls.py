from django.urls import path
from django.conf.urls import url
from django.urls.conf import include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("cars",car_specView,basename="cars")
urlpatterns = [
    # path('home', home),
    url('home/',home),
    url('',include(router.urls))
    
]