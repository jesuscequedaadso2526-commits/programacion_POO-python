from animal_general import AnimalGeneral

class AnimalAcuatico(AnimalGeneral):
    def __init__(self, nombre, edad, habitat, dieta, tamano, color):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)

    def moverse(self):
        return f"El {self.nombre} nada fluidamente a través de las corrientes de agua."

    def comunicacion(self):
        return f"El {self.nombre} genera vibraciones y ondas sonoras subacuáticas."

    def reproduccion(self):
        return f"El {self.nombre} libera huevos en el agua durante el desove."

    def alimentarse(self):
        return f"el {self.nombre} filtra el agua o caza presas marinas ({self.dieta})."

    def adaptacion(self):
        return f"El {self.nombre} usa su color {self.color} para camuflarse con el fondo o la luz de la superficie"

    def instintos(self):
        return f"El {self.nombre} detecta cambios en la presión y corrientes marinas para evitar peligros."

    def descanso(self):
        return f"El {self.nombre} se mantiene suspendido en el agua o se oculta entre corales."

    def sueno(self):
        return f"El {self.nombre} apaga la mitad de su cerebro para seguir alerta y no hundirse."

    def interaccion_socal(self):
        return f"El {self.nombre} nada en cardúmenes estructurados para defenderse."
