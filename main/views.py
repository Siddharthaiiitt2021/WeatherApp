from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        if " " in city:
            city = city.split(" ")
            city = "%".join(city)
        print(city)
        api_key = '4bb02d0442bf5a91e4a47d7a3d592c9b'
        pos = urllib.request.urlopen('http://api.openweathermap.org/geo/1.0/direct?q='+city+'&limit=5&appid='+api_key).read()
        pos = json.loads(pos)
        print(pos)
        print(pos[0]['lat'], pos[0]['lon'])
        lat = str(pos[0]['lat'])
        lon = str(pos[0]['lon'])
        list_of_data = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?lat='+lat+'&lon='+lon+'&appid='+api_key).read()
        list_of_data = json.loads(list_of_data)
        print(list_of_data['main'])
        data = {
            'temperature': str(int(list_of_data['main']['temp'])-273) + " C",
            'feels_like': str(int(list_of_data['main']['feels_like'])-273) + " C",
            "Min_temp": str(int(list_of_data['main']['temp_min'])-273) + " C", 
            "Max_temp": str(int(list_of_data['main']['temp_max']-273)) + " C", 
            "humidity": str(list_of_data['main']['humidity']) + " %", 
        }

        print(data)
    else: 
        data = {}

    return render(request, 'main\index.html', data)