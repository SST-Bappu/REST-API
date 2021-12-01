from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from .serializer import *
from .models import *
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
# Create your views here.



class DriverViewSet(viewsets.ModelViewSet):
    serializer_class = DriverSerializer
    permmission_class = [AllowAny]

    def get_queryset(self):
        drivers = Driver.objects.all()
        return drivers

