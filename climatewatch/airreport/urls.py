from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('sensor/new', views.CreateSensorView.as_view(), name='add_sensor'),
    path('sensor/new/manual', views.CreateManualSensorView.as_view(), name='add_manual_sensor'),
    path('sensor/new/live', views.CreateLiveSensorView.as_view(success_url="../../sensor/new/live"), name='add_live_sensor'),
    path('sensor/<pk>/info', views.SensorView.as_view(), name='sensor_detail'),
]