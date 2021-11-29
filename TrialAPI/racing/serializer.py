from rest_framework import serializers
from .models import *

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields =['id','driver_name','car_brand','round_finishing_time']