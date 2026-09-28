from carro_general import CarroGeneral

class CarroElectrico(CarroGeneral):
    def __init__(self, modelo, color, motor, num_puertas, capacidad_pasajeros, nivel_bateria=100, año=2026):
        super().__init__(modelo, año, color, num_puertas, capacidad_pasajeros, "Eléctrico", motor)
        self.nivel_bateria = nivel_bateria

    def arranque(self):
        if self.nivel_bateria <= 0:
            return f"No se puede arrancar el carro {self.modelo} porque la batería está descargada."
        if not self.encendido:
            self.encendido = True
            return f"El carro {self.modelo} con motor eléctrico ha arrancado. (Nivel de batería: {self.nivel_bateria}%)"
        return f"El carro {self.modelo} ya está encendido. (Nivel de batería: {self.nivel_bateria}%)"