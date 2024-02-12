from django.db import models
from datetime import datetime

# Create your models here.
class Sensor(models.Model):
    ip_address = models.CharField(max_length = 15)
    latitude = models.FloatField(default = 0.0)
    longitude = models.FloatField(default = 0.0)
    temp = models.IntegerField(default = 0)
    humidity = models.IntegerField(default = 0)
    airquaility = models.IntegerField(default = 0)
    timestamp = models.DateTimeField(default=datetime.now())

    def get_absolute_url(self):
        return "/airreport"

    def __str__(self):
        return self.ip_address