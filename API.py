import requests
import json_manager
import click

def verificar_clima(ciudad):

    url="https://api.openweathermap.org/data/2.5/weather?q={}&appid=ef05d644764c90ae3275ef1986021daf&units=metric".format(ciudad)

    respuesta = requests.get(url)

    data = respuesta.json()

    temperatura = data["main"]["temp"]
    velocidad = data["wind"]["speed"]
    humedad= data["main"]["humidity"]
    descripcion = data["weather"][0]["description"]
    datos_para_envio ={
        'ciudad':ciudad,
        'temperatura': temperatura + "c",
        'velocidad': velocidad+"m/s",
        'humedad': humedad,
        'descripcion': descripcion,
    }
    json_manager.write_json(datos_para_envio)
    