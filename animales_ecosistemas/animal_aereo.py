from animal_general import AnimalGeneral

class AnimalAereo(AnimalGeneral):
    def __init__(self, nombre, edad, habitat, dieta, tamano, color):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)

    def moverse(self):
        return f"El {self.nombre} utiliza las correintes de aire térmicas para volar o planear."

    def comunicacion(self):
        return f"El {self.nombre} realiza cantos complejos que viajan largas distancias por el aire."

    def reproduccion(self):
        return f"El {self.nombre} crea nidos en lugares elevados lejos de depredadores terrestres."

    def alimentarse(self):
        return f"El {self.nombre} caza en picada desde el aire o se alimenta en pleno vuelo."

    def adaptacion(self):
        return f"El {self.nombre} mantiene un peso {self.tamano} muy ligero y huesos huecos para permitir el vuelo."

    def instintos(self):
        return f"El {self.nombre} migra estacionalmente guiado por el magnetismo terrestre."

    def descarnso(self):
        return f"El {self.nombre} se posa en ramas altas usando reflejos en sus garras para no caer."

    def sueno(self):
        return f"El {self.nombre} duerme sujeto a las alturas, ocultando la cabeza en su plumaje {self.color}."

    def interaccion_social(self):
        return f"El {self.nombre} forma bandadas sincronizadas para reducir la resistencia al viento."