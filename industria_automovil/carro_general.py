class CarroGeneral:
    def __init__(self, modelo, año, color, num_puertas, capacidad_pasajeros, tipo_combustible, motor):
        self.modelo = modelo
        self.año = año
        self.color = color
        self.num_puertas = num_puertas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.encendido = False
        self.velocidad = 0

    def mostrar_informacion(self):
        return f"Modelo: {self.modelo}, Año: {self.año}, Color: {self.color}, Puertas: {self.num_puertas}, Capacidad: {self.capacidad_pasajeros}, Combustible: {self.tipo_combustible}, Motor: {self.motor}"

    def  arranque(self):
        if not self.encendido:
            self.encendido = True
            return f"El carro {self.modelo} con motor {self.motor} ha arrancado. (Combustible: {self.tipo_combustible})"
        return f"El carro {self.modelo} ya está encendido. (Combustible: {self.tipo_combustible})"
    
    def apagado(self):
        if self.encendido:
            self.encendido = False
            self.velocidad = 0
            return f"El carro {self.modelo} con motor {self.motor} se ha apagado. (Combustible: {self.tipo_combustible})"
        return f"El carro {self.modelo} ya está apagado. (Combustible: {self.tipo_combustible})"

    def aceleracion_y_frenado(self, accion, cantidad=10):
        if not self.encendido:
            return f"El carro {self.modelo} no puede {accion} porque está apagado. (Combustible: {self.tipo_combustible})"
        
        if accion == "acelerar":
            self.velocidad += cantidad
            return f"El carro {self.modelo} ha acelerado a {self.velocidad} km/h. (Combustible: {self.tipo_combustible})"
        elif accion == "frenar":
            self.velocidad = max(0, self.velocidad - cantidad)
            return f"El carro {self.modelo} ha frenado a {self.velocidad} km/h. (Combustible: {self.tipo_combustible})"
        else:
            return f"Acción desconocida: {accion}. (Combustible: {self.tipo_combustible}). Use 'acelerar' o 'frenar'."
    
    def sistema_direccion(self, direccion):
        return f"El volante esta girando hacia la {direccion}."

    def climatizacion(self, estado, temperatura=22):
        if estado.lower() == "encendido":
            return f"Climatización encendida a {temperatura}°C para los {self.capacidad_pasajeros} pasajeros."
        return f"Climatización apagada."

    def tipo_seguridad(self, sistemas_activos):
        sistemas = ", " .join(sistemas_activos)
        return f"Sistemas de seguridad activos en el {self.modelo}: {sistemas}."

    def luces(self, tipo_luz, estado):
        return f"Luces {tipo_luz} están {'encendidas' if estado else 'apagadas'}."

    def sistema_ventanas(self, ventana, accion):
        return f"La ventana {ventana} está siendo {accion}. El carro tiene {self.num_puertas} puertas y capacidad para {self.capacidad_pasajeros} pasajeros."
    
    def sistema_espejos(self, espejo, posicion):
        return f"El espejo {espejo} está siendo posicionado en {posicion}."