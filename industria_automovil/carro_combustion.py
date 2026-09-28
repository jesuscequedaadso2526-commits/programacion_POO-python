from carro_general import CarroGeneral

class CarroCombustion(CarroGeneral):
    def __init__(self, modelo, color, motor, num_puertas, capacidad_pasajeros, nivel_tanque=100, año=2026):
        super().__init__(modelo, año, color, num_puertas, capacidad_pasajeros, "Gasolina", motor)
        self.nivel_tanque = nivel_tanque

    def arranque(self):
        if self.nivel_tanque <= 0:
            return f"No se puede arrancar el carro {self.modelo} porque el tanque está vacío."
        return super().arranque()