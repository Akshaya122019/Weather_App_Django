from django.shortcuts import render
import requests
from django.conf import settings


def home(request):

    city = request.GET.get("city", "Chennai")

    # Current weather API
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    # Forecast API
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={settings.API_KEY}&units=metric"
    forecast_response = requests.get(forecast_url)
    forecast_data = forecast_response.json()

    if data.get("cod") != 200:
        return render(request, "home.html", {
            "error": data.get("message")
        })

    weather_main = data["weather"][0]["main"]

    weather_data = {
        "city": city,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"],
        "weather_main": weather_main,
        "forecast": forecast_data["list"][:5]
    }

    return render(request, "home.html", weather_data)