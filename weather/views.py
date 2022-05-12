import requests
import datetime
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import City
from .forms import CityForm

# Create your views here.
def main_weather(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=29c502e713059f0d7c0f4cc5f4fd7ec3'
    city = City.objects.get(pk=1)

    if request.GET.get('search'):
        city.city_name = request.GET.get('search').capitalize()
        city.save()

    weather_data = requests.get(url.format(city)).json()

    city_weather = {}
    if weather_data['cod'] == 200:
        city_weather = {
            'city': weather_data['name'],
            'time': datetime.datetime.now().time(),
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'].capitalize(),
            'wind_speed': weather_data['wind']['speed'],
            'humidity': weather_data['main']['humidity'],
            'icon': weather_data['weather'][0]['icon'],
        }
    else:
        return redirect('error_page')

    return render(request, "weather/weather_home.html", city_weather)


def weather_five_days(request):
    url = 'https://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid=29c502e713059f0d7c0f4cc5f4fd7ec3'

    city = City.objects.get(pk=1)

    weather_data = requests.get(url.format(city)).json()

    city_weather = {}
    if weather_data['cod'] == '200':
        date = weather_data['list'][0]['dt_txt'][0:10]
        time = weather_data['list'][0]['dt_txt'][11:19]

        weather_data_day_1 = []
        weather_data_day_2 = []
        weather_data_day_3 = []
        weather_data_day_4 = []
        weather_data_day_5 = []
        for el in weather_data['list']:
            if date[8:10] == el['dt_txt'][8:10]:
                weather_data_day_1.append({'date': el['dt_txt'][0:10],
                                           'time': el['dt_txt'][11:16],
                                           'temperature': el['main']['temp'],
                                           'description': el['weather'][0]['description'].capitalize(),
                                           'wind_speed': el['wind']['speed'], 'humidity': el['main']['humidity'],
                                           'icon': el['weather'][0]['icon'],})
            if int(date[8:10]) + 1 == int(el['dt_txt'][8:10]):
                weather_data_day_2.append({'date': el['dt_txt'][0:10],
                                           'time': el['dt_txt'][11:16],
                                           'temperature': el['main']['temp'],
                                           'description': el['weather'][0]['description'].capitalize(),
                                           'wind_speed': el['wind']['speed'], 'humidity': el['main']['humidity'],
                                           'icon': el['weather'][0]['icon'],})
            if int(date[8:10]) + 2 == int(el['dt_txt'][8:10]):
                weather_data_day_3.append({'date': el['dt_txt'][0:10],
                                           'time': el['dt_txt'][11:16],
                                           'temperature': el['main']['temp'],
                                           'description': el['weather'][0]['description'].capitalize(),
                                           'wind_speed': el['wind']['speed'], 'humidity': el['main']['humidity'],
                                           'icon': el['weather'][0]['icon'],})
            if int(date[8:10]) + 3 == int(el['dt_txt'][8:10]):
                weather_data_day_4.append({'date': el['dt_txt'][0:10],
                                           'time': el['dt_txt'][11:16],
                                           'temperature': el['main']['temp'],
                                           'description': el['weather'][0]['description'].capitalize(),
                                           'wind_speed': el['wind']['speed'], 'humidity': el['main']['humidity'],
                                           'icon': el['weather'][0]['icon'],})
            if int(date[8:10]) + 4 == int(el['dt_txt'][8:10]):
                weather_data_day_5.append({'date': el['dt_txt'][0:10],
                                           'time': el['dt_txt'][11:16],
                                           'temperature': el['main']['temp'],
                                           'description': el['weather'][0]['description'].capitalize(),
                                           'wind_speed': el['wind']['speed'], 'humidity': el['main']['humidity'],
                                           'icon': el['weather'][0]['icon'],})


        weather_data_list = []
        for el in weather_data['list']:
            weather_data_list.append({'dt': el['dt_txt'], 'temperature': el['main']['temp'], 'description': el['weather'][0]['description'], 'wind_speed': el['wind']['speed'], 'humidity': el['main']['humidity'], 'icon': el['weather'][0]['icon'],})

        city_weather = {
            'city': weather_data['city']['name'],
            'country': weather_data['city']['country'],
            'weather_data_list': weather_data_list,
            'weather_data_day_1': weather_data_day_1,
            'weather_data_day_2': weather_data_day_2,
            'weather_data_day_3': weather_data_day_3,
            'weather_data_day_4': weather_data_day_4,
            'weather_data_day_5': weather_data_day_5,
        }
    else:
        return redirect('error_page')

    return render(request, "weather/weather_five_days.html", city_weather)

def error_page(request):
    return render(request, "weather/error_page.html",)