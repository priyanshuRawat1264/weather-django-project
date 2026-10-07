import os
import requests
from django.shortcuts import render
from .models import SearchHistory

# Add your OpenWeatherMap API key as an environment variable named OPENWEATHER_API_KEY.
# For quick classroom testing, you may replace the placeholder below with your own key.
API_KEY = os.getenv('OPENWEATHER_API_KEY', 'your_api_key_here')
API_URL = 'https://api.openweathermap.org/data/2.5/weather'


def index(request):
    weather = None
    error = None

    if request.method == 'POST':
        city = request.POST.get('city', '').strip()

        if not city:
            error = 'Please enter a city name.'
        elif API_KEY == 'your_api_key_here':
            error = 'Please configure your OpenWeatherMap API key first.'
        else:
            try:
                response = requests.get(
                    API_URL,
                    params={
                        'q': city,
                        'appid': API_KEY,
                        'units': 'metric',
                    },
                    timeout=10,
                )
                response.raise_for_status()
                data = response.json()

                weather = {
                    'city': data.get('name', city),
                    'country': data.get('sys', {}).get('country', ''),
                    'temperature': data['main']['temp'],
                    'humidity': data['main']['humidity'],
                    'pressure': data['main']['pressure'],
                    'description': data['weather'][0]['description'].title(),
                    'icon': data['weather'][0]['icon'],
                }

                SearchHistory.objects.create(
                    city_name=weather['city'],
                    temperature=weather['temperature'],
                    humidity=weather['humidity'],
                    pressure=weather['pressure'],
                    description=weather['description'],
                    icon=weather['icon'],
                )
            except requests.HTTPError as exc:
                if exc.response is not None and exc.response.status_code == 404:
                    error = 'City not found. Please check the city name.'
                else:
                    error = 'Could not get weather data. Please try again.'
            except (requests.RequestException, KeyError, ValueError):
                error = 'Network or weather-data error. Please try again.'

    recent_searches = SearchHistory.objects.order_by('-searched_at')[:5]

    return render(
        request,
        'main/index.html',
        {
            'weather': weather,
            'error': error,
            'recent_searches': recent_searches,
        },
    )
