class Cultivo:
    def __init__(self, nombre, tipo, area, rendimiento):
        self._nombre = nombre
        self._tipo = tipo
        self._area = area
        self._rendimiento = rendimiento

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, nuevo_tipo):
        self._tipo = nuevo_tipo

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, nueva_area):
        if nueva_area >= 0:
            self._area = nueva_area
        else:
            print("El área no puede ser negativa.")

    @property
    def rendimiento(self):
        return self._rendimiento

    @rendimiento.setter
    def rendimiento(self, nuevo_rendimiento):
        if nuevo_rendimiento >= 0:
            self._rendimiento = nuevo_rendimiento
        else:
            print("El rendimiento no puede ser negativo.")

    def __str__(self):
        return f"Nombre: {self._nombre}, Tipo: {self._tipo}, Área: {self._area} ha, Rendimiento: {self._rendimiento} kg/ha"

    def calcular_produccion(self):
        return self._area * self._rendimiento