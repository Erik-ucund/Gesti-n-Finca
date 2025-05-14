class Animal:
    def __init__(self, nombre, especie, raza, edad, peso):
        self._nombre = nombre
        self._especie = especie
        self._raza = raza
        self._edad = edad
        self._peso = peso

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def especie(self):
        return self._especie

    @especie.setter
    def especie(self, nueva_especie):
        self._especie = nueva_especie

    @property
    def raza(self):
        return self._raza

    @raza.setter
    def raza(self, nueva_raza):
        self._raza = nueva_raza

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad >= 0:
            self._edad = nueva_edad
        else:
            print("La edad no puede ser negativa.")

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, nuevo_peso):
        if nuevo_peso >= 0:
            self._peso = nuevo_peso
        else:
            print("El peso no puede ser negativo.")

    def __str__(self):
        return f"Nombre: {self._nombre}, Especie: {self._especie}, Raza: {self._raza}, Edad: {self._edad} años, Peso: {self._peso} kg"