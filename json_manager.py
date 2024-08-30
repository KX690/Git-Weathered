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
    with open('datos.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)
        
        
def delete_json(ciudad):
    datos = read_json()
    datos_actualizados = [dato for dato in datos if dato.get('ciudad').lower() != ciudad.lower()]
    with open('datos.json', 'w') as archivo:
        json.dump(datos_actualizados, archivo, indent=4)
    if len(datos) > len(datos_actualizados):
        print(f"Datos de la ciudad '{ciudad}' eliminados exitosamente.")
    else:
        print(f"No se encontraron datos para la ciudad '{ciudad}'.")

def update_json(ciudad, temperatura=None, velocidad=None, humedad=None, descripcion=None):
    datos = read_json()
    for dato in datos:
        if dato['ciudad'].lower() == ciudad.lower():
            if temperatura:
                dato['temperatura'] = f"{temperatura} Celcius"
            if velocidad:
                dato['velocidad'] = f"{velocidad} m/s"
            if humedad:
                dato['humedad'] = humedad
            if descripcion:
                dato['descripcion'] = descripcion
            break
    with open('datos.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)
    print(f"Datos de la ciudad '{ciudad}' actualizados exitosamente.")