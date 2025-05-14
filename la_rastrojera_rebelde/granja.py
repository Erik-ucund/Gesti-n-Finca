from gestion_cultivos import GestionCultivos
from gestion_ganado import GestionGanado
from produccion import Produccion
from cultivo import Cultivo
from animal import Animal

class Granja:
    def __init__(self, nombre):
        self._nombre = nombre
        self._gestion_cultivos = GestionCultivos()
        self._gestion_ganado = GestionGanado()
        self._produccion = Produccion(self._gestion_cultivos, self._gestion_ganado)

    @property
    def nombre(self):
        return self._nombre

    def agregar_cultivo(self, nombre, tipo, area, rendimiento):
        self._gestion_cultivos.agregar_cultivo(nombre, tipo, area, rendimiento)

    def editar_cultivo(self, nombre, nuevo_tipo=None, nueva_area=None, nuevo_rendimiento=None):
        self._gestion_cultivos.editar_cultivo(nombre, nuevo_tipo, nueva_area, nuevo_rendimiento)

    def consultar_cultivo(self, nombre):
        return self._gestion_cultivos.consultar_cultivo(nombre)

    def eliminar_cultivo(self, nombre):
        self._gestion_cultivos.eliminar_cultivo(nombre)

    def listar_cultivos(self):
        self._gestion_cultivos.listar_cultivos()

    def agregar_animal(self, nombre, especie, raza, edad, peso):
        self._gestion_ganado.agregar_animal(nombre, especie, raza, edad, peso)

    def editar_animal(self, nombre, nueva_especie=None, nueva_raza=None, nueva_edad=None, nuevo_peso=None):
        self._gestion_ganado.editar_animal(nombre, nueva_especie, nueva_raza, nueva_edad, nuevo_peso)

    def consultar_animal(self, nombre):
        return self._gestion_ganado.consultar_animal(nombre)

    def eliminar_animal(self, nombre):
        self._gestion_ganado.eliminar_animal(nombre)

    def listar_animales(self):
        self._gestion_ganado.listar_animales()

    def calcular_produccion_total(self):
        return self._produccion.calcular_produccion_total_granja()

    def generar_reporte_produccion(self):
        return self._produccion.generar_reporte()