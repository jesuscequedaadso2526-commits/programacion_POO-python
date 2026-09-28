from carro_general import CarroGeneral
from carro_electrico import CarroElectrico
from carro_combustion import CarroCombustion

def main():

    mi_sedan = CarroCombustion(
        modelo="Toyota Corolla 2026",
        color="Plata", 
        motor="2.0L 4 cilindros",
        num_puertas=4, 
        capacidad_pasajeros=5
    )

    mi_suv = CarroElectrico(
        modelo="Tesla Model Y",
        color="Blanco",
        motor="Dual Motor AWD",
        num_puertas=5,
        capacidad_pasajeros=7,
        nivel_bateria=85
    )

    print("--- Carro de Combustión ---")
    print(mi_sedan.mostrar_informacion())
    print(mi_sedan.arranque())
    print(mi_sedan.aceleracion_y_frenado("acelerar", 40))
    print(mi_sedan.sistema_direccion("izquierda"))
    print(mi_sedan.luces("Principales", True))
    print(mi_sedan.apagado())

    print("\n--- Carro Eléctrico ---")
    print(mi_suv.mostrar_informacion())
    print(mi_suv.arranque())
    print(mi_suv.climatizacion("encendido", 20))
    print(mi_suv.tipo_seguridad(["Airbags frontales y laterales", "Frenado automático de emergencia", "Control de carril"]))
    print(mi_suv.sistema_ventanas("delantera derecha", "bajando"))
    print(mi_suv.sistema_espejos("retrovisor izquierdo", "ángulo abierto"))
    print(mi_suv.aceleracion_y_frenado("acelerar", 60))
    print(mi_suv.aceleracion_y_frenado("frenar", 20))

if __name__ == "__main__":
    main()