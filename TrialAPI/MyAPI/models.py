from django.db import models
from django.db.models.fields import AutoField
class car_spec(models.Model):
    id = models.IntegerField(primary_key=True,blank=True)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    produc_year = models.DateField()
    engine_type = models.CharField(max_length=20)

    def __str__(self):
        return self.model
    