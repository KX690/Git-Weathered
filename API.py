import requests

ciudad = input()

url="https://api.openweathermap.org/data/2.5/weather?q={}&appid=ef05d644764c90ae3275ef1986021daf&units=metric".format(ciudad)

respuesta = requests.get(url)

data = respuesta.json

temperatura = data["main"]["temp"]
velocidad = data["wind"]["speed"]
humedad= data["main"]["humidity"]
descripcion = data["weather"][0]["description"]



