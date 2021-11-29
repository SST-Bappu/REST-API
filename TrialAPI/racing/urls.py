from django.urls import path
from django.conf.urls import url,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("driver",DriverViewSet,basename="driver")

urlpatterns = [
    url('',include(router.urls))
    # url('home/',home)
    
]