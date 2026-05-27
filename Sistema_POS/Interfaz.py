import tkinter as tk

from clases import cargar_json

from inventario import agregar_producto
from inventario import modificar_stock

from ventas import vender_producto
from ventas import abrir_ventana_ventas


PRODUCTOS = "productos.json"
VENTAS = "ventas.json"


class SistemaPOS:

    def __init__(self, ventana):

        self.ventana = ventana

        self.ventana.title("Sistema POS")

        self.ventana.geometry("750x600")

        self.productos = cargar_json(PRODUCTOS)

        self.ventas = cargar_json(VENTAS)

        self.total = 0


        # TITULO

        titulo = tk.Label(
            ventana,
            text="SISTEMA POS",
            font=("Arial", 22, "bold")
        )

        titulo.pack(pady=10)

        # FRAME

        frame = tk.Frame(ventana)

        frame.pack(pady=10)


        # NOMBRE

        tk.Label(
            frame,
            text="Nombre"
        ).grid(row=0, column=0)

        self.entry_nombre = tk.Entry(frame)

        self.entry_nombre.grid(row=0, column=1)


        # PRECIO

        tk.Label(
            frame,
            text="Precio"
        ).grid(row=1, column=0)

        self.entry_precio = tk.Entry(frame)

        self.entry_precio.grid(row=1, column=1)


        # CANTIDAD

        tk.Label(
            frame,
            text="Cantidad"
        ).grid(row=2, column=0)

        self.entry_cantidad = tk.Entry(frame)

        self.entry_cantidad.grid(row=2, column=1)


        # BOTONES

        btn_agregar = tk.Button(
            frame,
            text="Agregar Producto",
            width=20,
            command=lambda: agregar_producto(self)
        )

        btn_agregar.grid(row=3, column=0, pady=5)

        btn_vender = tk.Button(
            frame,
            text="Vender Producto",
            width=20,
            command=lambda: vender_producto(self)
        )

        btn_vender.grid(row=3, column=1, pady=5)

        btn_stock = tk.Button(
            frame,
            text="Modificar Stock",
            width=20,
            command=lambda: modificar_stock(self)
        )

        btn_stock.grid(row=4, column=0, pady=5)

        btn_ventas = tk.Button(
            frame,
            text="Ver Ventas",
            width=20,
            command=lambda: abrir_ventana_ventas(self)
        )

        btn_ventas.grid(row=4, column=1, pady=5)


        # LISTA PRODUCTOS

        self.lista = tk.Listbox(
            ventana,
            width=80,
            height=18
        )

        self.lista.pack(pady=20)


        # TOTAL

        self.total_label = tk.Label(
            ventana,
            text="Total vendido: $0",
            font=("Arial", 14, "bold")
        )

        self.total_label.pack()

        self.mostrar_productos()


    # MOSTRAR PRODUCTOS

    def mostrar_productos(self):

        self.lista.delete(0, tk.END)

        for producto in self.productos:

            texto = (
                f"{producto['nombre']} | "
                f"Precio: ${producto['precio']} | "
                f"Stock: {producto['cantidad']}"
            )

            self.lista.insert(tk.END, texto)