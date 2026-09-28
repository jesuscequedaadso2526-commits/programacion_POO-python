class AnimalGeneral:
    def __init__(self, nombre, edad, habitat, dieta, tamano, color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamano = tamano
        self.color = color

        def moverse(self):
            return f"El {self.nombre} se desplaza por su entorno."

        def comunicacion(self):
            return f"El {self.nombre} emite sonidos básicos para comunicarse."

        def reproduccion(self):
            return f"El {self.nombre} busca perpetuar su especie."

        def alimentarse(self):
            return f"El {self.nombre} consume alimentos según su dieta: {self.dieta}."

        def adaptacion(self):
            return f"El {self.nombre} usa su tamaño {self.tamano} y color {self.color} para sobrevivir"

        def instintos(self):
            return f"El {self.nombre} reacciona a los estímulos de su entorno."

        def descanso(self):
            return f"El {self.nombre} necesita descansar para mantener su energía y salud."

        def sueno(self):
            return f"El {self.nombre} entra en estado de reposo profundo para recuperarse y regenerarse."

        def interaccion_social(self):
            return f"El {self.nombre} interactúa con otros individuos de su especie para establecer jerarquías y relaciones."