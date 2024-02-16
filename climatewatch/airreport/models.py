from django.db import models
from datetime import datetime
from Adafruit_IO import Client

# Due to lack of GPS component, this was added to have pre populated lat lon information for sensor locations
sensor_dict = {
    "Test-Sensor" : {'lat': 0.0, 'lon': 0.0},
    "Sensor-Inside" : {'lat': 34.20279, 'lon': -77.84729}, #GTG
    "Sensor-Back-Yard" : {'lat': 34.20292, 'lon': -77.84729}, #GTG
    "Sensor-Front-Yard" : {"lat": 34.20259, 'lon': -77.84721}, #GTG
    "Sensor-South-End-Front" : {"lat": 34.186966, 'lon': -77.809460}, #GtG
    "Sensor-South-End-Back" : {"lat": 34.186788, 'lon': -77.814184}, #GtG
    "Sensor-South-End" : {"lat": 34.187941, 'lon': -77.811723}, #GtG
    "Sensor-Crystal-Pier" : {"lat": 34.192944, 'lon': -77.803737}, #GtG
    "Sensor-Mercer-Pier" : {"lat": 34.213300, 'lon': -77.786512}, #GtG
    "Sensor-North-End" : {"lat": 34.234453, 'lon': -77.775238}, #GtG
    "Sensor-River-Walk" : {"lat": 34.235298, 'lon': -77.950049}, #GtG
    "Sensor-The-Half" : {"lat": 34.241479, 'lon': -77.943595}, #GtG
    "Sensor-Downtown" : {"lat": 34.240147, 'lon': -77.946524}, #GtG
    "Sensor-Whole-Foods" : {"lat": 34.214131, 'lon': -77.901206}, #GtG
}

# Create your models here.
class Sensor(models.Model):
    name = models.CharField(max_length = 50)
    latitude = models.FloatField(default = 0.0)
    longitude = models.FloatField(default = 0.0)
    temp = models.FloatField(default = 0)
    humidity = models.FloatField(default = 0)
    airquaility1 = models.FloatField(default = 0)
    airquaility2 = models.FloatField(default = 0)
    airquaility3 = models.FloatField(default = 0)
    timestamp = models.DateTimeField(default=datetime.now())

    def get_absolute_url(self):
        return "/airreport"

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        print('******************!!!!!****************************')
        if self.name in sensor_dict:
            self.latitude = sensor_dict[self.name]['lat']
            self.longitude = sensor_dict[self.name]['lon']
            aio = Client('jiffy68s', 'aio_Shfx26EFcaM7xxfC4PIcGZtHUX2W')

            temperature_f = aio.receive('feather-esp32s2-tft13812285.ws-0x77-ambient-temp-fahrenheit')
            humidity = aio.receive('feather-esp32s2-tft13812285.ws-0x77-humidity')
            air_quality1 = aio.receive('feather-esp32s2-tft13812285.ws-0x12-pm10-std')
            air_quality2 = aio.receive('feather-esp32s2-tft13812285.ws-0x12-pm100-std')
            air_quality3 = aio.receive('feather-esp32s2-tft13812285.ws-0x12-pm25-std')
            self.temp = float(temperature_f.value)
            self.humidity = float(humidity.value)
            self.airquaility1 = float(air_quality1.value)
            self.airquaility2 = float(air_quality2.value)
            self.airquaility3 = float(air_quality3.value)
            
        self.timestamp = datetime.now()
        print(self.name)
        return super().save(*args, **kwargs)