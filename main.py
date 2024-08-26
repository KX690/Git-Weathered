import click
import json_manager
from API import verificar_clima

@click.group()
def cli():
    pass


@cli.command()
@click.option('--ciudad', required=True, help='ciudad donde desea saber el estado admosferico')
def clima( ciudad):
    if not ciudad:
        print('Debe elegir una ciudad para poder ejecutar')
    else:
        datos = json_manager.read_json()
        
        verificar_clima(ciudad)
    
    
@cli.command()
def datos_atm():
    datos = json_manager.read_json()
    for dato in datos:
        print(dato)
    
    
@cli.command()
@click.option('--ciudad', required=True, help='Ciudad cuyo dato desea borrar')
def borrar(ciudad):
    json_manager.delete_json(ciudad)




if __name__=='__main__':
    cli()

