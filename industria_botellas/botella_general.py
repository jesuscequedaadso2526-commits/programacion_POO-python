class BotellaGeneral:
    def __init__(self, material, capacidad, forma, diseno, tapa, grabados):
        self.capacidad = capacidad
        self.material = material
        self.forma = forma
        self.diseno = diseno
        self.tapa = tapa
        self.grabados = grabados

    def contener_liquidos(self, liquido):
        return f"La botella de {self.material} está conteniendo {liquido}."

    def facilitar_vertido(self):
        return f"Vertiendo el líquido fácilmente gracias a su forma {self.forma}."

    def cierre_hermetico(self):
        return f"Asegurando el líquido con cierre hermético usando la tapa de tipo {self.tapa}."

    def transporte(self):
        return f"Transportando cómodamente la botella de {self.capacidad}."

    def compatibilidad_temperatura(self, temperatura):
        return f"El material de {self.material} está interactuando con una bebida {temperatura}."

    def reutilizacion(self):
        return f"Reutilizando la botella con diseño {self.diseno}."

    def verificar_transparencia(self):
        return f"Verificando el nivel de transparencia del material: {self.material}."