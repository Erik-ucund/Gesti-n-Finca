from gestion_cultivos import GestionCultivos
from gestion_ganado import GestionGanado

class Produccion:
    def __init__(self, gestion_cultivos, gestion_ganado):
        self._gestion_cultivos = gestion_cultivos
        self._gestion_ganado = gestion_ganado

    def calcular_produccion_total_granja(self):
        produccion_cultivos = self._gestion_cultivos.calcular_produccion_total()
        peso_total_ganado = self._gestion_ganado.calcular_produccion_total()
        return {"produccion_cultivos_kg": produccion_cultivos, "peso_total_ganado_kg": peso_total_ganado}

    def generar_reporte(self):
        reporte = "\n--- Reporte de Producción Total de la Granja ---\n\n"
        produccion = self.calcular_produccion_total_granja()
        reporte += f"Producción Total de Cultivos: {produccion['produccion_cultivos_kg']} kg\n"
        reporte += f"Peso Total del Ganado: {produccion['peso_total_ganado_kg']} kg\n"
        return reporte