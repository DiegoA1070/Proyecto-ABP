import json
import os


class Producto:

    def __init__(self, nombre, precio, cantidad):

        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def to_dict(self):

        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "cantidad": self.cantidad
        }


def cargar_json(archivo):

    if not os.path.exists(archivo):

        with open(archivo, "w") as f:
            json.dump([], f)

    with open(archivo, "r") as f:
        return json.load(f)


def guardar_json(archivo, datos):

    with open(archivo, "w") as f:
        json.dump(datos, f, indent=4)