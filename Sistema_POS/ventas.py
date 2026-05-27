import tkinter as tk

from tkinter import messagebox

from clases import guardar_json

from datetime import datetime


PRODUCTOS = "productos.json"
VENTAS = "ventas.json"


def vender_producto(self):

    seleccion = self.lista.curselection()

    if not seleccion:

        messagebox.showerror(
            "Error",
            "Seleccione un producto"
        )

        return

    indice = seleccion[0]

    producto = self.productos[indice]

    if producto["cantidad"] <= 0:

        messagebox.showerror(
            "Error",
            "No hay stock"
        )

        return

    producto["cantidad"] -= 1

    self.total += producto["precio"]

    venta = {
        "producto": producto["nombre"],
        "precio": producto["precio"],
        "fecha": datetime.now().strftime("%Y-%m-%d")
    }

    self.ventas.append(venta)

    guardar_json(PRODUCTOS, self.productos)

    guardar_json(VENTAS, self.ventas)

    self.total_label.config(
        text=f"Total vendido: ${self.total}"
    )

    self.mostrar_productos()

    messagebox.showinfo(
        "Venta",
        "Venta realizada"
    )


def abrir_ventana_ventas(self):

    ventana_ventas = tk.Toplevel(self.ventana)

    ventana_ventas.title("Historial de Ventas")

    ventana_ventas.geometry("600x450")

    titulo = tk.Label(
        ventana_ventas,
        text="HISTORIAL DE VENTAS",
        font=("Arial", 18, "bold")
    )

    titulo.pack(pady=10)

    lista_ventas = tk.Listbox(
        ventana_ventas,
        width=70,
        height=18
    )

    lista_ventas.pack(pady=10)

    total_dia = 0

    fecha_hoy = datetime.now().strftime("%Y-%m-%d")

    for venta in self.ventas:

        texto = (
            f"Fecha: {venta['fecha']} | "
            f"Producto: {venta['producto']} | "
            f"Precio: ${venta['precio']}"
        )

        lista_ventas.insert(tk.END, texto)

        if venta["fecha"] == fecha_hoy:

            total_dia += venta["precio"]

    label_total = tk.Label(
        ventana_ventas,
        text=f"Total vendido hoy: ${total_dia}",
        font=("Arial", 14, "bold")
    )

    label_total.pack(pady=10)