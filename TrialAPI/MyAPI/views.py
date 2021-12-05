from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import viewsets
from rest_framework.views import APIView
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


#Viewsets
class car_specView(viewsets.ModelViewSet):
    serializer_class = CarSpeSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        carSpec = car_spec.objects.all()
        return carSpec
    
    # def retrieve(self, request, *args, **kwargs):
    #     url_parms = kwargs
    #     print(url_parms)
    #     parmlist = url_parms['pk'].split('-')

    #     # cars = car_spec.objects.get(brand = url_parms['pk'].capitalize())
    #     cars = car_spec.objects.filter(brand = parmlist[0],model=parmlist[1])
    #     serializer = CarSpeSerializer(cars, many=True)
    #     return Response(serializer.data)

    def create(self,request,*args,**kwargs):
        car_data = request.data

        new_car = car_spec.objects.create(brand=car_data['brand'],model=car_data['model'],
        produc_year=car_data['produc_year'],engine_type=car_data['engine_type'])

        new_car.save()
        serializer = CarSpeSerializer(new_car)
        return Response(serializer.data)
    
    def destroy(self,request,*args,**kwargs):
        loggedin_user = request.user
        # if loggedin_user=='admin':
        car = self.get_object()
        car.delete()
        return Response({'message':'Object has been deleted'})
        # else:
        #     return Response({'message':'You are not allowed to perform this operation'})

#APIVIEW

class CarsAPIView(APIView):
    serializer_class = CarSpeSerializer
    
    def get_queryset(self):
        cars = car_spec.objects.all()
        return cars

    def get(self,request,*args,**kwargs):
        try:
            urlparms = request.query_params['id']
            cars = car_spec.objects.filter(brand = urlparms)
        except:
            cars = self.get_queryset()
        serializer = CarSpeSerializer(cars,many = True)
        return Response(serializer.data)
    
    def post(self,request,*args,**kwargs):
        car_data = request.data

        new_car = car_spec.objects.create(brand=car_data['brand'],model=car_data['model'],
        produc_year=car_data['produc_year'],engine_type=car_data['engine_type'])

        new_car.save()
        serializer = CarSpeSerializer(new_car)
        return Response(serializer.data)