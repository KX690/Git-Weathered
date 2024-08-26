import requests
import json_manager
import click

def verificar_clima(ciudad):

    url="https://api.openweathermap.org/data/2.5/weather?q={}&appid=ef05d644764c90ae3275ef1986021daf&units=metric".format(ciudad)

    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        data = respuesta.json()

        temperatura = data["main"]["temp"]
        velocidad = data["wind"]["speed"]
        humedad = data["main"]["humidity"]
        descripcion = data["weather"][0]["description"]

        datos_para_envio = {
            'ciudad': ciudad,
            'temperatura': f"{temperatura} Celcius",
            'velocidad': f"{velocidad} m/s",
            'humedad': humedad,
            'descripcion': descripcion,
        }
        
        json_manager.write_json(datos_para_envio)
        print(f"Datos del clima para {ciudad} guardados exitosamente.")
    else:
        print("Error al obtener datos de la API. Por favor, verifica el nombre de la ciudad o la conexión a Internet.")
