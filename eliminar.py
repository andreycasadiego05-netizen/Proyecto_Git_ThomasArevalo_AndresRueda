import json
def eliminar_servicio():
    nombre_borrar = input("Nombre del paquete a eliminar: ")
    
    try:
        with open("servicios.json", "r") as f:
            datos = json.load(f)
        
        nuevos_datos = [item for item in datos if item["nombre"] != nombre_borrar]
        
        if len(datos) == len(nuevos_datos):
            print("No se encontró ningún servicio con ese nombre.")
        else:
            with open("servicios.json", "w") as f:
                json.dump(nuevos_datos, f, indent=4)
            print("Servicio eliminado con éxito.")
            
    except FileNotFoundError:
        print("El archivo no existe todavía.")