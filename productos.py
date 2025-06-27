import json
import os

ARCHIVO = "productos.json"

def cargar_productos():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r") as f:
        return json.load(f)

def guardar_productos(productos):
    with open(ARCHIVO, "w") as f:
        json.dump(productos, f, indent=2)

def agregar_producto():
    productos = cargar_productos()
    nombre = input("Nombre del producto: ")
    descripcion = input("Descripción: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock disponible: "))

    productos.append({
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio,
        "stock": stock
    })

    guardar_productos(productos)
    print("✅ Producto agregado con éxito.")

# Ejecutar
agregar_producto()
