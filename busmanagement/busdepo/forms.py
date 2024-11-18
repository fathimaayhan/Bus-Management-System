from django import forms
from .models import Driver,Bus

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['name']


class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['busnumber','seating_capacity','route','driver']
