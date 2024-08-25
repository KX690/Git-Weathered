import json
import os

def read_json():
    if not os.path.isfile('datos.json'):
        with open('datos.json','w') as archivo:
            json.dump([],archivo)
    with open('datos.json','r') as archivo:
        datos = json.load(archivo)
    return datos

def write_json():
    pass