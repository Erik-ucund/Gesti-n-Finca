from granja import Granja
from gestion_cultivos import GestionCultivos
from gestion_ganado import GestionGanado
from produccion import Produccion

def menu_gestion_cultivos(granja):
    while True:
        print("\n--- Gestión de Cultivos ---")
        print("1. Agregar Cultivo")
        print("2. Editar Cultivo")
        print("3. Consultar Cultivo")
        print("4. Eliminar Cultivo")
        print("5. Listar Cultivos")
        print("6. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre del cultivo: ")
            tipo = input("Tipo de cultivo: ")
            try:
                area = float(input("Área de cultivo (hectáreas): "))
                rendimiento = float(input("Rendimiento (kg/hectárea): "))
                granja.agregar_cultivo(nombre, tipo, area, rendimiento)
            except ValueError:
                print("Por favor, ingrese valores numéricos válidos para el área y el rendimiento.")
        elif opcion == '2':
            nombre_editar = input("Nombre del cultivo a editar: ")
            nuevo_tipo = input("Nuevo tipo (dejar en blanco para no cambiar): ") or None
            nueva_area_str = input("Nueva área (hectáreas, dejar en blanco para no cambiar): ")
            nueva_area = float(nueva_area_str) if nueva_area_str else None
            nuevo_rendimiento_str = input("Nuevo rendimiento (kg/hectárea, dejar en blanco para no cambiar): ")
            nuevo_rendimiento = float(nuevo_rendimiento_str) if nuevo_rendimiento_str else None
            granja.editar_cultivo(nombre_editar, nuevo_tipo, nueva_area, nuevo_rendimiento)
        elif opcion == '3':
            nombre_consultar = input("Nombre del cultivo a consultar: ")
            cultivo = granja.consultar_cultivo(nombre_consultar)
            if cultivo:
                print(cultivo)
        elif opcion == '4':
            nombre_eliminar = input("Nombre del cultivo a eliminar: ")
            granja.eliminar_cultivo(nombre_eliminar)
        elif opcion == '5':
            granja.listar_cultivos()
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")



def menu_gestion_ganado(granja):
    while True:
        print("\n--- Gestión de Ganado ---")
        print("1. Agregar Animal")
        print("2. Editar Animal")
        print("3. Consultar Animal")
        print("4. Eliminar Animal")
        print("5. Listar Animales")
        print("6. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre del animal: ")
            especie = input("Especie del animal: ")
            raza = input("Raza del animal: ")
            try:
                edad = int(input("Edad del animal (años): "))
                peso = float(input("Peso del animal (kg): "))
                granja.agregar_animal(nombre, especie, raza, edad, peso)
            except ValueError:
                print("Por favor, ingrese valores numéricos válidos para la edad y el peso.")
        elif opcion == '2':
            nombre_editar = input("Nombre del animal a editar: ")
            nueva_especie = input("Nueva especie (dejar en blanco para no cambiar): ") or None
            nueva_raza = input("Nueva raza (dejar en blanco para no cambiar): ") or None
            nueva_edad_str = input("Nueva edad (años, dejar en blanco para no cambiar): ")
            nueva_edad = int(nueva_edad_str) if nueva_edad_str else None
            nuevo_peso_str = input("Nuevo peso (kg, dejar en blanco para no cambiar): ")
            nuevo_peso = float(nuevo_peso_str) if nuevo_peso_str else None
            granja.editar_animal(nombre_editar, nueva_especie, nueva_raza, nueva_edad, nuevo_peso)
        elif opcion == '3':
            nombre_consultar = input("Nombre del animal a consultar: ")
            animal = granja.consultar_animal(nombre_consultar)
            if animal:
                print(animal)
        elif opcion == '4':
            nombre_eliminar = input("Nombre del animal a eliminar: ")
            granja.eliminar_animal(nombre_eliminar)
        elif opcion == '5':
            granja.listar_animales()
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


def menu_principal(granja):
    while True:
        print("\n--- Gestión de La Rastrojera Rebelde ---")
        print("1. Gestión de Cultivos")
        print("2. Gestión de Ganado")
        print("5. Salir")

        opcion_principal = input("Seleccione una sección: ")

        if opcion_principal == '1':
            menu_gestion_cultivos(granja)
        elif opcion_principal == '2':
            menu_gestion_ganado(granja)
        elif opcion_principal == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    nombre_granja = "La Rastrojera Rebelde"
    granja = Granja(nombre_granja)
    menu_principal(granja)
