from django import forms
from .models import Sensor

class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = "__all__"

class LiveSensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ('name',)
