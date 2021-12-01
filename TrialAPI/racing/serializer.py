from rest_framework import serializers
from .models import *
import sys
best_time = sys.maxsize

class DriverSerializer(serializers.ModelSerializer):
    best_record = serializers.SerializerMethodField('_get_best_record')

    def _get_best_record(self,driver_object):
        global best_time
        round_finishing_time = getattr(driver_object,"round_finishing_time")
        if round_finishing_time<best_time:
            best_time = round_finishing_time
        return best_time
    class Meta:
        model = Driver
        fields =['id','driver_name','car_brand','round_finishing_time','best_record']