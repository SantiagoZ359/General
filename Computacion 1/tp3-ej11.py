
# 11.	 Supongamos que eres el encargado de programar un sistema de gestión de tareas para un equipo de trabajo. Para ello, necesitas escribir una función que permita a los usuarios agregar tareas, eliminar tareas y ver una lista de todas las tareas pendientes.
# Para simplificar, considera que las tareas se representan como diccionarios de Python con las siguientes claves: "nombre", "descripcion", "fecha_inicio" y "fecha_limite".
# Para resolver este problema, puedes seguir los siguientes pasos:
# •	Escribir una función para agregar una tarea al sistema.
# •	Escribir una función para eliminar una tarea del sistema.
# •	Escribir una función para mostrar la lista de tareas pendientes en el sistema.
# •	Escribir una función principal que utilice las funciones anteriores para permitir al usuario interactuar con el sistema de gestión de tareas (un Menu).

def tarea(tareas, nombre, descripcion, fecha_inicio, fecha_limite):
    tarea = {
        "nombre":nombre,
        "descripcion":descripcion,
        "fecha_inicio":fecha_inicio,
        "fecha_limite":fecha_limite,
    }
    tareas.append(tarea)    
    print("tarea agregada.")

def eliminar_tarea(tareas,nombre):
    for tarea in tareas:
        if tarea["nombre"] == nombre:
            tareas.remove(tarea)
            print("tarea eliminada")
            return
    print("no se encontro la tarea")

def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas")
    else:
        for tarea in tareas:
            print(f"Nombre: {tarea['nombre']}, Descripción: {tarea['descripcion']}, Fecha de inicio: {tarea['fecha_inicio']}, Fecha límite: {tarea['fecha_limite']}")

def menu():
    tareas = []
    while True:
        print("elija una opcion")
        print("1 - Agregar tarea ")
        print("2 - Eliminar tarea ")
        print("3 - Mostrar tareas pendientes ")
        print("4 - Salir")

        opcion = int(input('Ingrese el numero que desee: '))

        if opcion == 1:
            nombre = input("Ingrese el nombre de la tarea: ")
            descripcion = input("Agregue una descripcion: ")
            fecha_inicio = input("Agregue la fecha de inicio: ")
            fecha_limite = input("Agregue la fecha limite: ")
            tarea(tareas, nombre,descripcion,fecha_inicio,fecha_limite)
        elif opcion == 2:
            nombre = input("Ingrese el nombre de la tarea a eliminar: ")
            eliminar_tarea(tareas,nombre)
        elif opcion == 3:
            mostrar_tareas(tareas)
        elif opcion == 4:
            print("exit")
            break
        else:
            print("opcion no valida")


menu()