from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.main_weather, name='main_weather'),
    path('weather_five_days/', views.weather_five_days, name='weather_five_days'),
    path('error_page/', views.error_page, name='error_page'),
]
