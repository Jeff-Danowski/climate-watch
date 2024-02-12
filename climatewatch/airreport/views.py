from django.shortcuts import render
# Import HttpResponse here
from django.views.generic import TemplateView
from .models import Sensor
from .forms import SensorForm
from django.views.generic.edit import CreateView

import folium
from folium import plugins


import ee
# ee.Authenticate()
service_account = 'jeff-danowski@jeff-danowski-climate-watch.iam.gserviceaccount.com'
credentials = ee.ServiceAccountCredentials(service_account, 'airreport/key.json')
ee.Initialize(credentials)

# Create your views here.
class HomeView(TemplateView):
    template_name = 'airreport/home.html'

    def get_context_data(self, **kwargs):
 
        figure = folium.Figure()

        m = folium.Map(
            location=[34.2085036, -77.7963709],
            zoom_start=13,
        )
        m.add_to(figure)

        for sensor in Sensor.objects.all():
          # iframe = folium.IFrame('%s <br> Location: [%s, %s] ' + 
          #                        '<br> Temp:  %s ' + 
          #                        '<br> Humidity:  %s ' + 
          #                        '<br> Air Quaility:  %s' % (sensor.ip_address, 
          #                                                    sensor.latitude,
          #                                                    sensor.longitude,
          #                                                    sensor.temp,
          #                                                    sensor.humidity,
          #                                                    sensor.airquaility
          #                                                    )
          #                       )
          iframe = folium.IFrame(sensor.ip_address + 
                                 '<br> Location: [{0}, {1}]'.format(sensor.latitude ,+sensor.longitude) + 
                                 '<br> Temp:  {0} '.format(sensor.temp) + 
                                 '<br> Humidity:  {0} '.format(sensor.humidity) + 
                                 '<br> Air Quaility:  {0} '.format(sensor.airquaility)
                                )
          
          location = sensor.latitude, sensor.longitude,
          popup = folium.Popup(iframe,
                     min_width=300,
                     max_width=300)
          
          print(sensor.airquaility)
          
          if(sensor.airquaility > 75):
              icon=folium.Icon(icon='cloud', color = 'green')
          elif(sensor.airquaility > 50):
              icon=folium.Icon(icon='cloud', color = 'orange')
          else:
              icon=folium.Icon(icon='cloud', color = 'red')

          folium.Marker(
              location = location,
              popup = popup,
              icon=icon
          ).add_to(m)
            

        # ipaddress='159.62.3.45'
        # location = 34.2024444, 
        # longitude = -77.7963709]
        # temp = 95
        # humidity = 83
        # airquaility = 34



        # folium.Marker(
        #     location=[34.2085036, -77.7963709],
        #     popup='This is my popup',
        #     icon=folium.Icon(icon='cloud')
        # ).add_to(m)

        # folium.Marker(
        #     location=[34.2085036, -77.7963709],
        #     popup='This is my popup',
        #     icon=folium.Icon(icon='cloud')
        # ).add_to(m)



        

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
            
        

        

        m.add_child(folium.LayerControl())
    
        figure.render()
        map = 55

        m = m._repr_html_()
        print('test')
        context = super().get_context_data(**kwargs)
        context["map"] = m
        context["sensors"] = Sensor.objects.all()

        return context

#forntend
#home
class CreateSensorView(TemplateView):
    template_name = 'airreport/add_sensor.html'

class CreateManualSensorView(CreateView):
    model = Sensor
    form_class = SensorForm
    template_name = 'airreport/add_manual_sensor.html'

class CreateLiveSensorView(TemplateView):
    template_name = 'airreport/add_live_sensor.html'