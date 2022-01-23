from rest_framework import fields, serializers
from .models import *

class CarSpeSerializer(serializers.ModelSerializer):

    mod_engine_type = serializers.SerializerMethodField('_get_modified')
    def _get_modified(self,car_object):
        engine_type = getattr(car_object,"engine_type")
        engine_type+="_Modified"
        return engine_type

    class Meta:
        model = car_spec
        fields = ['id','brand','model','produc_year','mod_engine_type']


    