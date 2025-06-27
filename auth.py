import json
import os

ARCHIVO = "usuarios.json"

def cargar_usuarios():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r") as f:
        return json.load(f)

def guardar_usuarios(usuarios):
    with open(ARCHIVO, "w") as f:
        json.dump(usuarios, f, indent=2)

def registrar():
    usuarios = cargar_usuarios()
    nombre = input("Nombre de usuario nuevo: ")
    if any(u["nombre"] == nombre for u in usuarios):
        print("⚠️ Ese usuario ya existe.")
        return
    contraseña = input("Contraseña: ")
    usuarios.append({"nombre": nombre, "contraseña": contraseña})
    guardar_usuarios(usuarios)
    print("✅ Usuario registrado con éxito.")

def login():
    usuarios = cargar_usuarios()
    nombre = input("Usuario: ")
    contraseña = input("Contraseña: ")
    if any(u["nombre"] == nombre and u["contraseña"] == contraseña for u in usuarios):
        print("🔓 Inicio de sesión exitoso.")
    else:
        print("❌ Usuario o contraseña incorrectos.")

# Menú
print("1. Registrar")
print("2. Iniciar sesión")
opcion = input("Elegí una opción: ")

if opcion == "1":
    registrar()
elif opcion == "2":
    login()
else:
    print("Opción inválida.")
