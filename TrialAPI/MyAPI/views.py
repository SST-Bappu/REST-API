from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import viewsets
from .models import *
from .serializer import *
# Create your views here.

@api_view()
# @permission_classes([IsAuthenticated])
def home(request):
    print(request.query_params)
    # id = int(request.query_params['id'])
    # key = request.query_params['key']
    id = 10
    key=76576
    modified_id = id * 100
    return Response({'message':'My first touch on rest framework','mod_id':modified_id,'key':key})

class car_specView(viewsets.ModelViewSet):
    serializer_class = CarSpeSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        carSpec = car_spec.objects.all()
        return carSpec
