import click
import json_manager
from API import verificar_clima

@click.group()
def cli():
    pass


@cli.command()
@cli.option('--ciudad', required=True, help='ciudad donde desea saber el estado admosferico')
def new(ctx, ciudad):
    if not ciudad:
        ctx.fail('Debe elegir una ciudad para poder ejecutar')
    else:
        datos = json_manager.read_json()
        
        verificar_clima(ciudad)
    
    
@cli.command()
def datos_atm():
    datos = json_manager.read_json()
    for dato in datos:
        print(dato)
    





if __name__=='__main__':
    cli()

