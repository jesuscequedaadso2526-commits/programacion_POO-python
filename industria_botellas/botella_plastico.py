from botella_general import BotellaGeneral

class BotellaPlastico(BotellaGeneral):
    def __init__(self, capacidad, forma, diseno, tapa, grabados, libre_bpa):
        super().__init__("Plástico", capacidad, forma, diseno, tapa, grabados)
        self.libre_bpa = libre_bpa
    
    def verificar_transparencia(self):
        print("La botella de plástico es transparente y permite ver el contenido.")
        estado_bpa = "libre de BPA" if self.libre_bpa else "con precaución por BPA"
        return f"Reutilización recomendada para líquidos fríos ({estado_bpa})."