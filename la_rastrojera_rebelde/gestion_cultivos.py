from cultivo import Cultivo

class GestionCultivos:
    def __init__(self):
        self._cultivos = []

    def agregar_cultivo(self, nombre, tipo, area, rendimiento):
        nuevo_cultivo = Cultivo(nombre, tipo, area, rendimiento)
        self._cultivos.append(nuevo_cultivo)
        print(f"Cultivo '{nombre}' agregado.")

    def editar_cultivo(self, nombre, nuevo_tipo=None, nueva_area=None, nuevo_rendimiento=None):
        for cultivo in self._cultivos:
            if cultivo.nombre == nombre:
                if nuevo_tipo:
                    cultivo.tipo = nuevo_tipo
                if nueva_area is not None:
                    cultivo.area = nueva_area
                if nuevo_rendimiento is not None:
                    cultivo.rendimiento = nuevo_rendimiento
                print(f"Cultivo '{nombre}' editado.")
                return
        print(f"No se encontró el cultivo '{nombre}'.")

    def consultar_cultivo(self, nombre):
        for cultivo in self._cultivos:
            if cultivo.nombre == nombre:
                return cultivo
        print(f"No se encontró el cultivo '{nombre}'.")
        return None

    def eliminar_cultivo(self, nombre):
        self._cultivos = [cultivo for cultivo in self._cultivos if cultivo.nombre != nombre]
        print(f"Cultivo '{nombre}' eliminado.")

    def calcular_produccion_total(self):
        return sum(cultivo.calcular_produccion() for cultivo in self._cultivos)

    def listar_cultivos(self):
        if not self._cultivos:
            print("No hay cultivos registrados.")
            return
        print("Lista de Cultivos:")
        for cultivo in self._cultivos:
            print(cultivo)

    @property
    def cultivos(self):
        return self._cultivos