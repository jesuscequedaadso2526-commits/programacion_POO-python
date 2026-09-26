from botella_general import BotellaGeneral

class BotellaVidrio(BotellaGeneral):
    def __init__(self, capacidad, forma, diseno, tapa, grabados, tipo_vidrio):
        super().__init__("Vidrio", capacidad, forma, diseno, tapa, grabados)
        self.tipo_vidrio = tipo_vidrio
    
    def compatibilidad_temperatura(self, temperatura):
        if temperatura.lower() in ['caliente', 'muy caliente']:
            return f"Excelente compatibilidad con bebidas calientes gracias a su vidrio de {self.tipo_vidrio}."
        return super().compatibilidad_temperatura(temperatura)