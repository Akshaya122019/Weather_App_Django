from django.shortcuts import render
import requests
from django.conf import settings


def home(request):

    city = request.GET.get("city")
    lat = request.GET.get("lat")
    lon = request.GET.get("lon")

    if lat and lon:

        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={settings.API_KEY}&units=metric"

    else:

        city = city or "Chennai"

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.API_KEY}&units=metric"


    response = requests.get(url)
    data = response.json()


    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={data['name']}&appid={settings.API_KEY}&units=metric"

    forecast = requests.get(forecast_url).json()


    weather_data = {

        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"],
        "weather_main": data["weather"][0]["main"],
        "forecast": forecast["list"][:5]

    }

    return render(request, "home.html", weather_data)