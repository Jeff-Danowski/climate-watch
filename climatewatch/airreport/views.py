from typing import Any
from django.shortcuts import render
from django.http import request
from django.views.generic import TemplateView, DetailView, FormView
from .models import Sensor
from .forms import SensorForm, LiveSensorForm
from django.views.generic.edit import CreateView

import pandas as pd
# import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
import plotly as plotly

import folium
from folium import plugins

import matplotlib.pyplot as plt



import ee
# ee.Authenticate()
service_account = 'jeff-danowski@jeff-danowski-climate-watch.iam.gserviceaccount.com'
credentials = ee.ServiceAccountCredentials(service_account, 'airreport/key.json')
ee.Initialize(credentials)

# Create your views here.
class HomeView(TemplateView):
    template_name = 'airreport/home.html'
    
    # aio = Client('jiffy68s', 'aio_Shfx26EFcaM7xxfC4PIcGZtHUX2W')

    # temperature_f = aio.receive('feather-esp32s2-tft13812285.ws-0x77-ambient-temp-fahrenheit')
    # humidity = aio.receive('feather-esp32s2-tft13812285.ws-0x77-humidity')
    # air_quality = aio.receive('feather-esp32s2-tft13812285.ws-0x12-pm100-std')
    # print('Received value: {0}'.format(temperature_f.value))
    # print('Received value: {0}'.format(humidity.value))
    # print('Received value: {0}'.format(air_quality.value))
    # print('Received value: {0}'.format(aio))
    # print('Received value: {0}'.format(aio.receive('feather-esp32s2-tft13812285')))

    def get_context_data(self, **kwargs):
 
        # figure = folium.Figure()

        m = folium.Map(
            location=[34.1900000, -77.840000],
            zoom_start=13
        )
        # m.add_to(figure)

        included_sensor_name = []
        latest_data_per_sensor = []
        for sensor in Sensor.objects.all().order_by('name', '-pk'):

          if(sensor.name not in included_sensor_name):
            
            latest_data_per_sensor.append(sensor)
            included_sensor_name.append(sensor.name)
            
            iframe = folium.IFrame(sensor.name + 
                                  '<br> Location: [{0}, {1}]'.format(sensor.latitude ,+sensor.longitude) + 
                                  '<br> Temp:  {0} '.format(sensor.temp) + 
                                  '<br> Humidity:  {0} '.format(sensor.humidity) + 
                                  '<br> Air Quaility:  {0} '.format(sensor.airquaility3)
                                  )
            
            location = sensor.latitude, sensor.longitude,
            popup = folium.Popup(iframe,
                      min_width=300,
                      max_width=300)
            
            print(sensor.airquaility1)
            
            if(sensor.airquaility3 < 12.0):
                icon=folium.Icon(icon='cloud', color = 'green', icon_color='green')
            elif(sensor.airquaility3 < 35.4):
                icon=folium.Icon(icon='cloud', color = 'beige', icon_color='#FFFF00')
            elif(sensor.airquaility3 < 55.4):
                icon=folium.Icon(icon='cloud', color = 'orange', icon_color='orange')
            elif(sensor.airquaility3 < 150.4):
                icon=folium.Icon(icon='cloud', color = 'red', icon_color='red')
            elif(sensor.airquaility3 < 250.4):
                icon=folium.Icon(icon='cloud', color = 'purple', icon_color='purple')
            else:
                icon=folium.Icon(icon='cloud', color = 'maroon', icon_color='maroon')

            folium.Marker(
                location = location,
                popup = popup,
                icon=icon
            ).add_to(m)
            
          m.add_child(folium.LayerControl())
    
        # dataset = ee.ImageCollection('MODIS/006/MOD13Q1').filter(ee.Filter.date('2019-07-01', '2019-11-30')).first()
        # modisndvi = dataset.select('NDVI')
        # visParams = {'min':0, 'max':3000, 'palette':['225ea8','41b6c4','a1dab4','034B48']}
        # vis_paramsNDVI = {
        #     'min': 0,
        #     'max': 9000,
        #     'palette': [ 'FE8374', 'C0E5DE', '3A837C','034B48',]}

        # map_id_dict = ee.Image(modisndvi).getMapId(vis_paramsNDVI)
        # folium.raster_layers.TileLayer(
        #             tiles = map_id_dict['tile_fetcher'].url_format,
        #             attr = 'Google Earth Engine',
        #             name = 'NDVI',
        #             overlay = True,
        #             control = True
        #             ).add_to(m)

        m = m._repr_html_()
        context = super().get_context_data(**kwargs)
        context["map"] = m
        context["sensors"] = latest_data_per_sensor

        return context

#forntend
#home
class CreateSensorView(TemplateView):
    template_name = 'airreport/add_sensor.html'

class CreateManualSensorView(CreateView):
    model = Sensor
    form_class = SensorForm
    template_name = 'airreport/add_manual_sensor.html'

class CreateLiveSensorView(CreateView):
    model = Sensor
    form_class = LiveSensorForm
    template_name = 'airreport/add_live_sensor.html'
    print('You made it there!')

    # if request.method == 'Post':
    #     print('hello')

# def process_request(request):
#     print('You made it where!')
#     if(request.method == 'Post'):
#         print('You made it here!')
#         if('new_request' in request):
#             print('even better!')


# class LiveDataRequest(request):
#     if(request.method == 'Post'):
#         if 'retrieve_data' in request:
#             print('You made it here!')

class SensorView(DetailView):
    model = Sensor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        sensor_data = Sensor.objects.get(pk=self.kwargs.get('pk'))
        all_sensor_data = Sensor.objects.filter(name=sensor_data.name)

        airquality = []
        time = []
        for data in all_sensor_data:
            airquality.append(data.airquaility3)
            time.append(time)

        # x = airquality
        # y = time

        # fig = plt.figure()
        # plt.plot(x,y)

        # imgdata = StringIO()
        # fig.savefig(imgdata, format='svg')
        # imgdata.seek(0)

        # data = imgdata.getvalue()

        # data = {
        #     'airquality' : airquality,
        #     'time' : time
        # }

        # json_data = serialize('json', data, cls=LazyEncoder)

        # plt.plot(time, airquality)
        # plt.xlabel('Time')
        # plt.ylabel('Air Quality')
        # plt.title('Air Quality Over Time')

        # fig, az = plt.subplot()
        # fig.savefig('temp_plot.png')
        
        context["sensor_data"] = all_sensor_data
        # context["plot"] = data
        return context
    # template_name = 'airreport/sensor_info.html'
    