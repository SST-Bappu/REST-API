from rest_framework import fields, serializers
from .models import *

class CarSpeSerializer(serializers.ModelSerializer):
    class Meta:
        model = car_spec
        fields = ['brand','model','produc_year','engine_type']

    