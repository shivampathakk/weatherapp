from django.shortcuts import render
import requests
from .forms import CityForm

# Create your views here.
def weather_view(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            api_key = '2312cade5ddf4dda8f264745241606'
            url = f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'
            response = requests.get(url)
            weather_data = response.json()
            temp_c = weather_data['current']['temp_c']
            context = {
                'form': form,
                'city': city,
                'temp_c': temp_c
            }
            return render(request, 'weather/weather.html', context)
    else:
        form = CityForm()
    return render(request, 'weather/weather.html', {'form': form})
