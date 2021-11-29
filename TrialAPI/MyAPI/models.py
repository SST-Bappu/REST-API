from django.db import models
class car_spec(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    produc_year = models.DateField()
    engine_type = models.CharField(max_length=20)

    def __str__(self):
        return self.model
    