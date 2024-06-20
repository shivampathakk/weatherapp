from django import forms

class CityForm(forms.Form):
    city = forms.CharField(label='Enter the name of the city', max_length=100)
