import json

ARCHIVO = "productos.json"

def cargar_productos():
    with open(ARCHIVO, "r") as f:
        return json.load(f)

def guardar_productos(productos):
    with open(ARCHIVO, "w") as f:
        json.dump(productos, f, indent=2)

def mostrar_productos(productos):
    print("\n📦 Productos disponibles:")
    for i, p in enumerate(productos):
        print(f"{i + 1}. {p['nombre']} - ${p['precio']} ({p['stock']} en stock)")

def vender_producto():
    productos = cargar_productos()
    mostrar_productos(productos)

    opcion = int(input("\nElegí el número del producto que querés comprar: ")) - 1

    if 0 <= opcion < len(productos):
        if productos[opcion]["stock"] > 0:
            productos[opcion]["stock"] -= 1
            guardar_productos(productos)
            print("✅ Compra realizada con éxito.")
        else:
            print("❌ No hay stock disponible.")
    else:
        print("❌ Opción inválida.")

# Ejecutar
vender_producto()

