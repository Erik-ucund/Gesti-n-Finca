from animal import Animal

class GestionGanado:
    def __init__(self):
        self._animales = []

    def agregar_animal(self, nombre, especie, raza, edad, peso):
        nuevo_animal = Animal(nombre, especie, raza, edad, peso)
        self._animales.append(nuevo_animal)
        print(f"Animal '{nombre}' agregado.")

    def editar_animal(self, nombre, nueva_especie=None, nueva_raza=None, nueva_edad=None, nuevo_peso=None):
        for animal in self._animales:
            if animal.nombre == nombre:
                if nueva_especie:
                    animal.especie = nueva_especie
                if nueva_raza:
                    animal.raza = nueva_raza
                if nueva_edad is not None:
                    animal.edad = nueva_edad
                if nuevo_peso is not None:
                    animal.peso = nuevo_peso
                print(f"Animal '{nombre}' editado.")
                return
        print(f"No se encontró el animal '{nombre}'.")

    def consultar_animal(self, nombre):
        for animal in self._animales:
            if animal.nombre == nombre:
                return animal
        print(f"No se encontró el animal '{nombre}'.")
        return None

    def eliminar_animal(self, nombre):
        self._animales = [animal for animal in self._animales if animal.nombre != nombre]
        print(f"Animal '{nombre}' eliminado.")

    def calcular_produccion_total(self):  # Asumiendo producción total como peso total
        return sum(animal.peso for animal in self._animales)

    def listar_animales(self):
        if not self._animales:
            print("No hay animales registrados.")
            return
        print("Lista de Animales:")
        for animal in self._animales:
            print(animal)

    @property
    def animales(self):
        return self._animales