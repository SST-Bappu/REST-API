from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated

# Create your views here.

@api_view()
@permission_classes([IsAuthenticated])
def home(request):
    print(request.query_params)
    # id = int(request.query_params['id'])
    # key = request.query_params['key']
    id = 10
    key=76576
    modified_id = id * 100
    return Response({'message':'My first touch on rest framework','mod_id':modified_id,'key':key})
