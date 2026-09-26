from botella_plastico import BotellaPlastico
from botella_vidrio import BotellaVidrio

# **** CODIGO PRINCIPAL ****   
# 5. LLAMAR LA INSTANCIA DE LA CLASE

def main():
    botella_deportiva = BotellaPlastico(
        capacidad="750ml", 
        forma="Cilíndrica ergonómica", 
        diseno="Deportivo", 
        tapa="Chupo a presión", 
        grabados="Logotipo deportivo",
        libre_bpa=True
    )

    # Instanciando una botella de vidrio
    botella_cafe = BotellaVidrio(
        capacidad="400ml", 
        forma="Termo", 
        diseno="Elegante", 
        tapa="Rosca metálica", 
        grabados="Sin grabados",
        tipo_vidrio="borosilicato"
    )

    print("--- PRUEBA BOTELLA DE PLÁSTICO ---")
    print(botella_deportiva.contener_liquidos("Agua mineral"))
    print(botella_deportiva.transporte())
    print(botella_deportiva.reutilizacion())
    print(botella_deportiva.verificar_transparencia())

    print("\n--- PRUEBA BOTELLA DE VIDRIO ---")
    print(botella_cafe.contener_liquidos("Café expreso"))
    print(botella_cafe.cierre_hermetico())
    print(botella_cafe.compatibilidad_temperatura("caliente"))
    print(botella_cafe.facilitar_vertido())


if __name__ == "__main__":
    main()