import json
def modificar_servicio():
    nombre_buscar = input("Nombre del paquete a modificar: ")
    
    try:
        with open("servicios.json", "r") as f:
            datos = json.load(f)
        
        encontrado = False
        for item in datos:
            if item["nombre"] == nombre_buscar:
                print("--- Datos actuales encontrados ---")
                print(item)
                item["precio"] = input("Nuevo precio: ")
                item["evento"] = input("Nuevo tipo de evento: ")
                item["duracion"] = input("Nuevas horas: ")
                encontrado = True
                break
        
        if encontrado:
            with open("servicios.json", "w") as f:
                json.dump(datos, f, indent=4)
            print("Servicio modificado con éxito.")
        else:
            print("No se encontró el servicio.")
            
    except FileNotFoundError:
        print("El archivo no existe.")