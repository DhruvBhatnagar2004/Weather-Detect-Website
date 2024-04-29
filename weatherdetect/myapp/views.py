from django.shortcuts import render
import json
import urllib.request

def index(request):
    if request.method == 'POST':
        city = request.POST.get('city', '')
        if city:
            try:
                url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=YOUR_API_KEY_HERE'.format(city)
                with urllib.request.urlopen(url) as response:
                    data = json.loads(response.read().decode('utf-8'))
                    weather_data = {
                        "country_code": str(data['sys']['country']),
                        "coordinate": str(data['coord']['lon']) + ' ' + str(data['coord']['lat']),
                        "temp": str(data['main']['temp']) + 'K',
                        "pressure": str(data['main']['pressure']),
                        "humidity": str(data['main']['humidity']),
                    }
            except urllib.error.HTTPError as e:
                error_message = "City not found. Please enter a valid city name."
                return render(request, 'index.html', {'error_message': error_message})
        else:
            error_message = "Please enter a city name."
            return render(request, 'index.html', {'error_message': error_message})
    else:
        city=''
        weather_data = {}
    return render(request, 'index.html', {'city': city, 'weather_data': weather_data})
