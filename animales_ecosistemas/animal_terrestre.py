from animal_general import AnimalGeneral

class AnimalTerrestre(AnimalGeneral):
    def __init__(self, nombre, edad, habitat, dieta, tamano, color):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)

    def moverse(self):
        return f"El {self.nombre} camina, corre o repta apoyando su peso sobre la tierra firme."

    def comunicacion(self):
        return f"El {self.nombre} emite sonidos vocales directos y usa posturas corporales."

    def reproduccion(self):
        return f"El {self.nombre} construye madrigueras seguras en el {self.habitat} para sus crías."

    def alimentarse(self):
        return f"El {self.nombre} recorre el terreno buscando su dieta."

    def adaptacion(self):
        return f"El {self.nombre} usa su pelaje {self.color} para regular su temperatura corporal."

    def instintos(self):
        return f"El {self.nombre} marca su territorio físico con olores y marcas."

    def descanso(self):
        return f"El {self.nombre} se recuesta sobre el suelo, hierba o rocas sombreadas."

    def sueno(self):
        return f"El {self.nombre} cierra los ojos y relaja la musculatura en un lugar resguardado."

    def interaccion_social(self):
        return f"El {self.nombre} forma manadas o rebaños estableciendo jerarquías por fuerza."