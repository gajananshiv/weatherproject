from django.shortcuts import render
from django.utils import timezone
from pytz import timezone as tz
# Create your views here.
import requests

from .models import Weather

def weather_view(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = 'cdd89b67a356977146e84934e8625a93'

        url = f'http://api.openweathermap.org/data/2.5/weather?q={city},in&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            condition = data['weather'][0]['description']

            weather = Weather(city=city, condition=condition, temperature=temperature, humidity=humidity)
            weather.save()
        else:
            error_message = data['message']
            return render(request, 'testapp/error.html', {'error_message': error_message})

    weathers = Weather.objects.latest('id')
    current_time = timezone.now().astimezone(tz('Asia/Kolkata'))

    return render(request, 'testapp/weather.html', {'weathers': weathers,'current_time':current_time})
