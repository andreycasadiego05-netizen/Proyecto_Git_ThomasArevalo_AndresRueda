from añadir import añadir_servicio
from eliminar import eliminar_servicio
from modificar import modificar_servicio

while True:
    print("Gestion de servicios fotografico")
    print("1.agregar paquete de fotografia \n 2.Editar servicio \n 3.Eliminar servicio \n 4.Salir ") 
    opcion = int(input("elegir opcion: "))
    if opcion == 1 :
        añadir_servicio()
    elif opcion == 2:
        modificar_servicio()
    elif opcion == 3:
        eliminar_servicio()
    elif opcion == 4:
        break
