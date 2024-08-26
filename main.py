import click
import json_manager

@click.group()
def cli():
    pass


@cli.command()
@cli.option('--ciudad', required=True, help='ciudad donde desea saber el estado admosferico')
def new():
    
@cli.command()
def datos_atm():
    datos = json_manager.read_json()
    for dato in datos:
        print(dato)
    





if __name__=='__main__':
    cli()

