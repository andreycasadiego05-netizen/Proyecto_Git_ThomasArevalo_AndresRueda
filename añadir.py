import json
def añadir_servicio():
    nombre = input("Nombre del paquete: ")
    precio = input("Precio: ")
    evento = input("Tipo de evento: ")
    duracion = input("Horas: ")
    item = {
        "nombre": nombre,
        "precio": precio,
        "evento": evento,
        "duracion": duracion
    }
    try:
        with open("servicios.json", "r") as f:
            datos = json.load(f)
    except:
        datos = []
    datos.append(item)
    with open("servicios.json", "w") as f:
        json.dump(datos, f, indent=4)
    print("Guardado con éxito")