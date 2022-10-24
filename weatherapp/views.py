
from django.shortcuts import render
import requests, math

def index(request):
    
	data = {}
	if request.method == "POST":
     
		try:
			city_name = request.POST['city']
			url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=a0d0f86de19fd09e94086bb37c731d27"
			city_data = requests.get(url).json()
			
			data = { 
				'city': city_data['name'],
				'cod': city_data['cod'],
				'country': city_data["sys"]['country'],
				'weather': city_data['weather'][0]['description'].capitalize(),
				'wind': math.floor(city_data['wind']['speed']),
				'icon': city_data['weather'][0]['icon'],
				'temperature': math.floor(city_data['main']['temp'] - 273),
				'pressure': city_data['main']['pressure'],
				'humidity': city_data['main']['humidity'],
			}
		except:
			pass

	return render(request, 'index.html', {'city_data': data})
