import click
import json_manager
import json
import csv
import sys
from API import verificar_clima


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--ciudad", required=True, help="Ciudad donde desea saber el estado atmosférico"
)
def clima(ciudad):
    if not ciudad:
        print("Debe elegir una ciudad para poder ejecutar")
    else:
        verificar_clima(ciudad)


@cli.command()
@click.option(
    "--formato",
    default="texto",
    type=click.Choice(["texto", "json", "csv"]),
    help="Formato de salida: texto, json, o csv",
)
def datos_atm(formato):
    datos = json_manager.read_json()

    if formato == "json":
        print(json.dumps(datos, indent=4))
    elif formato == "csv":
        if datos:
            writer = csv.writer(sys.stdout)
            writer.writerow(datos[0].keys())
            for dato in datos:
                writer.writerow(dato.values())
    else:
        for dato in datos:
            for key, value in dato.items():
                print(f"{key}: {value}")
            print("----------------------------")


@cli.command()
@click.option("--ciudad", required=True, help="Ciudad cuyo dato desea borrar")
def borrar(ciudad):
    json_manager.delete_json(ciudad)


@cli.command()
@click.option("--ciudad", required=True, help="Ciudad cuyos datos desea modificar")
@click.option("--temperatura", default=None, help="Nueva temperatura para la ciudad")
@click.option(
    "--velocidad", default=None, help="Nueva velocidad del viento para la ciudad"
)
@click.option("--humedad", default=None, help="Nueva humedad para la ciudad")
@click.option(
    "--descripcion", default=None, help="Nueva descripción del clima para la ciudad"
)
def modificar(ciudad, temperatura, velocidad, humedad, descripcion):
    json_manager.update_json(ciudad, temperatura, velocidad, humedad, descripcion)


if __name__ == "__main__":
    cli()
