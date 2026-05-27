from tkinter import messagebox

from clase_producto import Producto
from clase_producto import guardar_json


PRODUCTOS = "productos.json"


def agregar_producto(self):

    nombre = self.entry_nombre.get()
    precio = self.entry_precio.get()
    cantidad = self.entry_cantidad.get()

    if nombre == "" or precio == "" or cantidad == "":

        messagebox.showerror(
            "Error",
            "Complete todos los campos"
        )

        return

    try:

        precio = int(precio)
        cantidad = int(cantidad)

    except:

        messagebox.showerror(
            "Error",
            "Datos inválidos"
        )

        return

    producto = Producto(
        nombre,
        precio,
        cantidad
    )

    self.productos.append(producto.to_dict())

    guardar_json(PRODUCTOS, self.productos)

    self.mostrar_productos()

    self.entry_nombre.delete(0, "end")
    self.entry_precio.delete(0, "end")
    self.entry_cantidad.delete(0, "end")

    messagebox.showinfo(
        "Éxito",
        "Producto agregado"
    )


def modificar_stock(self):

    seleccion = self.lista.curselection()

    if not seleccion:

        messagebox.showerror(
            "Error",
            "Seleccione un producto"
        )

        return

    indice = seleccion[0]

    nueva_cantidad = self.entry_cantidad.get()

    if nueva_cantidad == "":

        messagebox.showerror(
            "Error",
            "Ingrese una cantidad"
        )

        return

    try:

        nueva_cantidad = int(nueva_cantidad)

    except:

        messagebox.showerror(
            "Error",
            "Cantidad inválida"
        )

        return

    self.productos[indice]["cantidad"] = nueva_cantidad

    guardar_json(PRODUCTOS, self.productos)

    self.mostrar_productos()

    self.entry_cantidad.delete(0, "end")

    messagebox.showinfo(
        "Éxito",
        "Stock actualizado"
    )
