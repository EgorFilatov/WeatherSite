from django import forms
from django.forms import ModelForm, TextInput
from .models import City

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['city_name']
        widgets = {
            'header': forms.TextInput(attrs={'class': 'form-control'}),
            }

