from animal_general import AnimalGeneral
from animal_acuatico import AnimalAcuatico
from animal_aereo import AnimalAereo
from animal_terrestre import AnimalTerrestre

def main():

    tiburon = AnimalAcuatico(
        nombre="Tiburón Blanco",
        edad="15 años",
        habitat="Océano abierto",
        dieta="Carnívora",
        tamano="Grande (4 metros)",
        color="Gris y blanco"
    )

    leon = AnimalTerrestre(
        nombre="León Africano",
        edad="8 años",
        habitat="Sabana",
        dieta="Carnívora",
        tamano="Grande (190 kg)",
        color="Dorado"
    )

    halcon = AnimalAereo(
        nombre="Halcón Peregrino",
        edad="3 años",
        habitat="Acantilados y zonas urbanas altas",
        dieta="Carnívora",
        tamano="Pequeño (1 kg)",
        color="Gris azulado y blanco"
    )

    print("--- ECOSISTEMA ACUÁTICO ---")
    print(tiburon.moverse())
    print(tiburon.sueno())
    print(tiburon.instintos())

    print("\n--- ECOSISTEMA TERRESTRE ---")
    print(leon.reproduccion())
    print(leon.interaccion_social())
    print(leon.descanso())

    print("\n--- ECOSISTEMA AÉREO ---")
    print(halcon.alimentarse())
    print(halcon.adaptacion())
    print(halcon.comunicacion())

if __name__ == "__main__":
    main()