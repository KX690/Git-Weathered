import json
import os

def read_json():
    if not os.path.isfile('datos.json'):
        with open('datos.json','w') as archivo:
            json.dump([],archivo)
    with open('datos.json','r') as archivo:
        datos = json.load(archivo)
    return datos

def write_json(nuevo_dato):
    datos = read_json()
    datos.append(nuevo_dato)
    with open('datos.json', 'a+') as archivo:
        json.dump(datos, archivo, indent=4)